# Plan: Fix Mistral Judge Bug & Verify Rotation

## Objective
Fix a critical bug in `src/antigravity_core/unified_client.py` where the Mistral client response is accessed before the API call is made, causing the `judge_content` method to crash. Implement a verification script to ensure the fix works and that the fallback/rotation logic is sound.

## Context
- **File**: `src/antigravity_core/unified_client.py`
- **Issue**: The variable `chat_response` is referenced without being defined in the `judge_content` method.
- **Goal**: Ensure reliable content judging with Mistral as primary and Gemini as fallback.

## Implementation Steps

### 1. Fix Bug in `unified_client.py`
- **Action**: Modify `judge_content` method.
- **Change**: Insert the missing API call to `self.mistral_client.chat.complete` before accessing `chat_response`.
- **Code Snippet**:
  ```python
  chat_response = self.mistral_client.chat.complete(
      model=self.mistral_model,
      messages=[{"role": "user", "content": prompt}]
  )
  ```

### 2. Create Verification Script (`tests/verify_rotation.py`)
- **Action**: Create a new test script.
- **Purpose**: Verify that:
    1. Mistral client is called correctly.
    2. Fallback to Gemini occurs if Mistral fails.
    3. Gemini keys rotate on 429/Resource Exhausted errors.
- **Content**: A Python script using `unittest.mock` to simulate API responses and failures.

## Verification
- **Command**: `python3 tests/verify_rotation.py`
- **Success Criteria**:
    - The script executes without errors.
    - Output confirms "Mistral Call: SUCCESS".
    - Output confirms "Fallback to Gemini: SUCCESS".
    - Output confirms "Key Rotation: SUCCESS".

## Post-Action
- Update `WORK_LOG.md` to mark `MISTRAL_ROTATION_FINAL_VERIFICATION` as complete.
