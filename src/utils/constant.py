from src.utils.enum import LLMEnum, LLMModelEnum, ProfileEnum


LLM = [LLMEnum.OPEN_AI.value, LLMEnum.ANTHROPIC.value]
OPEN_AI_MODELS = [
    LLMModelEnum.OPEN_AI_3_5_TURBO.value,
    LLMModelEnum.OPEN_AI_4_OMNI.value,
    LLMModelEnum.OPEN_AI_4_OMNI_MINI.value,
    LLMModelEnum.OPEN_AI_4.value,
    LLMModelEnum.OPEN_AI_4_TURBO.value,
]

ANTHROPIC_MODELS = [
    LLMModelEnum.ANTHROPIC_3_OPUS.value,
    LLMModelEnum.ANTHROPIC_3_HAIKU.value,
    LLMModelEnum.ANTHROPIC_3_SONNET.value,
]

PROFILES = [
    ProfileEnum.CREATIVE.value,
    ProfileEnum.BALANCE.value,
    ProfileEnum.PRECISE.value,
]
