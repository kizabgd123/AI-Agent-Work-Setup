import os
import logging
import time
from typing import Optional, List
import google.generativeai as genai
try:
    from mistralai import Mistral
except ImportError:
    from mistralai.client import Mistral


logger = logging.getLogger(__name__)

class UnifiedAIClient:
    """
    Unified client supporting Mistral (priority) and Gemini (with rotation fallback).
    """
    def __init__(self):
        # Initialize Mistral
        self.mistral_key = os.getenv("MISTRAL_API_KEY")
        self.mistral_client = Mistral(api_key=self.mistral_key) if self.mistral_key else None
        self.mistral_model = "mistral-large-latest"

        # Initialize Gemini Pool
        self.gemini_keys = self._load_gemini_keys()
        self.current_gemini_index = 0
        self.gemini_model_name = "gemini-pro"
        
        if not self.mistral_client and not self.gemini_keys:
            logger.error("No AI keys (Mistral or Gemini) found in environment.")

    def _load_gemini_keys(self) -> List[str]:
        keys = []
        # Check for GEMINI_KEY_1..N
        for i in range(1, 21):
            key = os.getenv(f"GEMINI_KEY_{i}")
            if key:
                keys.append(key)
        # Fallback to GEMINI_API_KEY if no numbered keys
        if not keys:
            primary = os.getenv("GEMINI_API_KEY")
            if primary:
                keys.append(primary)
        return keys

    def _configure_gemini(self):
        if not self.gemini_keys:
            return None
        current_key = self.gemini_keys[self.current_gemini_index]
        genai.configure(api_key=current_key)
        return genai.GenerativeModel(self.gemini_model_name)

    def _rotate_gemini(self) -> bool:
        if len(self.gemini_keys) <= 1:
            return False
        self.current_gemini_index = (self.current_gemini_index + 1) % len(self.gemini_keys)
        logger.warning(f"🔄 Rotating Gemini Key behind the scenes. Switching to Key #{self.current_gemini_index + 1}")
        return True

    def judge_content(self, content: str, criteria: str) -> bool:
        """
        Evaluates content using Mistral first, then falls back to Gemini rotation.
        """
        prompt = f"""
        You are an impartial Judge AI.
        
        CRITERIA:
        {criteria}
        
        CONTENT TO EVALUATE:
        {content}
        
        INSTRUCTIONS:
        Evaluate if the CONTENT meets the CRITERIA.
        If it meets ALL criteria, reply exactly with: PASSED
        If it fails ANY criteria, reply exactly with: FAILED
        Do not add any other text.
        """
        
        # 1. Attempt Mistral
        if self.mistral_client:
            try:
                logger.info("⚖️  Attempting Judge with Mistral...")
                chat_response = self.mistral_client.chat.complete(
                    model=self.mistral_model,
                    messages=[{"role": "user", "content": prompt}]
                )
                result_raw = chat_response.choices[0].message.content.strip()
                result = result_raw.upper()
                logger.info(f"Mistral Verdict: {result}")
                if "PASSED" in result: return True
                if "FAILED" in result: 
                    logger.warning(f"❌ Mistral Rejected: {result_raw}")
                    return False
                # If ambiguous, fall through to Gemini
            except Exception as e:
                logger.warning(f"⚠️  Mistral Judge Failed: {e}. Falling back to Gemini...")

        # 2. Attempt Gemini with Rotation
        if self.gemini_keys:
            max_retries = len(self.gemini_keys) * 2
            for attempt in range(max_retries):
                try:
                    model = self._configure_gemini()
                    if not model: break
                    
                    logger.info(f"⚖️  Attempting Judge with Gemini (Key #{self.current_gemini_index + 1})...")
                    response = model.generate_content(prompt)
                    result = response.text.strip().upper()
                    logger.info(f"Gemini Verdict: {result}")
                    return "PASSED" in result
                except Exception as e:
                    error_msg = str(e)
                    if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                        if self._rotate_gemini():
                            continue
                    logger.error(f"Gemini error during judge: {e}")
                    time.sleep(2)
        
        logger.error("❌ All Judge models failed.")
        return False

    def generate_content(self, prompt: str) -> str:
        """Fallback generate content method."""
        # Minimal implementation for compatibility
        if self.mistral_client:
            try:
                res = self.mistral_client.chat.complete(
                    model=self.mistral_model,
                    messages=[{"role": "user", "content": prompt}]
                )
                return res.choices[0].message.content
            except: pass
            
        model = self._configure_gemini()
        if model:
            try:
                return model.generate_content(prompt).text
            except: pass
        return ""
