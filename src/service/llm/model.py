from src.utils.enum import ProfileEnum, LLMModelEnum

ANTHROPIC_MODEL_OPUS = {"model_name": "claude-3-opus-20240229"}
ANTHROPIC_MODEL_SONNET = {"model_name": "claude-3-sonnet-20240229"}
ANTHROPIC_MODEL_HAIKU = {"model_name": "claude-3-haiku-20240307"}

OPEN_AI_MODEL_3_5_TURBO = {"model_name": "gpt-3.5-turbo"}
OPEN_AI_MODEL_4_OMNI = {"model_name": "gpt-4o"}
OPEN_AI_MODEL_4_OMNI_MINI = {"model_name": "gpt-4o-mini"}
OPEN_AI_MODEL_4_TURBO = {"model_name": "gpt-4-turbo"}
OPEN_AI_MODEL_4 = {"model_name": "gpt-4"}


CREATIVE_PROFILE = {
    "temperature": 0.8,
    "top_p": 0.9,
    "presence_penalty": 0.1,
    "frequency_penalty": 0.1,
}

BALANCE_PROFILE = {
    "temperature": 0.5,
    "top_p": 0.85,
    "presence_penalty": 0.2,
    "frequency_penalty": 0.3,
}

PRECISE_PROFILE = {
    "temperature": 0.2,
    "top_p": 0.75,
    "presence_penalty": 0.5,
    "frequency_penalty": 0.5,
}


def get_profile(select_profile: ProfileEnum):
    if select_profile == "Creative":
        return CREATIVE_PROFILE
    if select_profile == "Balance":
        return BALANCE_PROFILE
    if select_profile == "Precise":
        return PRECISE_PROFILE


def get_model(select_model: LLMModelEnum):
    if select_model == "claude-3-opus-20240229":
        return ANTHROPIC_MODEL_OPUS
    elif select_model == "claude-3-sonnet-20240229":
        return ANTHROPIC_MODEL_SONNET
    elif select_model == "claude-3-haiku-20240307":
        return ANTHROPIC_MODEL_HAIKU
    elif select_model == "gpt-3.5-turbo":
        return OPEN_AI_MODEL_3_5_TURBO
    elif select_model == "gpt-4o":
        return OPEN_AI_MODEL_4_OMNI
    elif select_model == "gpt-4o-mini":
        return OPEN_AI_MODEL_4_OMNI_MINI
    elif select_model == "gpt-4-turbo":
        return OPEN_AI_MODEL_4_TURBO
    elif select_model == "gpt-4":
        return OPEN_AI_MODEL_4
