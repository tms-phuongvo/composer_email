import os
import logging
import streamlit as st
from dotenv import load_dotenv
from src.service.llm.openai import OpenAIService
from src.service.llm.anthropic import AnthropicService
from src.service.llm.base import BaseService
from src.utils.enum import (
    LLMEnum,
    LLMModelEnum,
    ProfileEnum,
)
from src.service.llm.model import get_model, get_profile
from src.utils.constant import LLM, OPEN_AI_MODELS, ANTHROPIC_MODELS, PROFILES
from src.service.auto_email import (
    summary_project,
    think_solution,
    select_technologies,
    compose_email,
)

load_dotenv()
configuration: dict = {}
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


def generate_email():
    st.session_state.text_error = ""

    if not st.session_state.project_required:
        st.session_state.text_error = "Please enter a project required"
        return

    with st.spinner("Please wait while your email is being generated..."):
        try:
            client = create_llm()
            summary = summary_project(
                client=client, project_required=st.session_state.project_required
            )
            st.session_state.summary = summary.content
            solution = think_solution(client=client, project_summary=summary.content)
            st.session_state.solution = solution.content
            # technology = select_technologies(
            #     client=client,
            #     project_info=summary.content,
            #     solution_info=solution.content,
            # )
            # st.session_state.technology = technology.content
            mail = compose_email(
                client=client,
                project_info=summary.content,
                solution_info=solution.content,
                technology_info="",
            )
            st.session_state.mail = mail.content
        except Exception as e:
            logging.error(e.__str__())
            st.session_state.text_error = e.__str__()


def create_llm() -> BaseService:
    if st.session_state.selected_llm is None:
        raise Exception("Please select a llm")

    if st.session_state.selected_llm == "OpenAI":
        return OpenAIService(
            **configuration,
        )
    elif st.session_state.selected_llm == "Anthropic":
        return AnthropicService(
            **configuration,
        )


def reset():
    st.session_state.project_required = ""
    st.session_state.text_error = ""
    st.session_state.summary = None
    st.session_state.solution = None
    st.session_state.technology = None
    st.session_state.mail = None


def prepare():
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "project_required" not in st.session_state:
        st.session_state.project_required = ""
    if "text_error" not in st.session_state:
        st.session_state.text_error = ""
    if "summary" not in st.session_state:
        st.session_state.summary = None
    if "solution" not in st.session_state:
        st.session_state.solution = None
    if "technology" not in st.session_state:
        st.session_state.technology = None
    if "mail" not in st.session_state:
        st.session_state.mail = None

    if "selected_llm" not in st.session_state:
        st.session_state.selected_llm = LLMEnum.OPEN_AI.value
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = LLMModelEnum.OPEN_AI_3_5_TURBO.value
    if "selected_profile" not in st.session_state:
        st.session_state.selected_profile = ProfileEnum.CREATIVE.value


def build_sidebar():
    with st.sidebar:
        global configuration
        st.sidebar.title("Settings")
        st.subheader("Models and parameters")

        llm_index = model_index = profile_index = 0

        if st.session_state.selected_llm:
            llm_index = LLM.index(st.session_state.selected_llm)

        selected_llm = st.sidebar.selectbox(
            label="Choose a LLM",
            options=LLM,
            index=llm_index,
            key="selected_llm",
        )

        if selected_llm:
            models = get_model_list(selected_llm)
            if st.session_state.selected_model and models.__contains__(
                st.session_state.selected_model
            ):
                model_index = models.index(st.session_state.selected_model)
            selected_model = st.sidebar.selectbox(
                "Choose a model",
                models,
                index=model_index,
                key="selected_model",
            )

        if st.session_state.selected_profile:
            profile_index = PROFILES.index(st.session_state.selected_profile)

        selected_profile = st.sidebar.selectbox(
            "Choose a profile",
            PROFILES,
            index=profile_index,
            key="selected_profile",
        )

    api_key = get_api_key(selected_llm)

    if selected_model:
        configuration.update(get_model(selected_model))
    if selected_profile:
        configuration.update(get_profile(selected_profile))
    if api_key:
        configuration["api_key"] = api_key


def get_model_list(llm) -> list:
    if llm == LLMEnum.OPEN_AI.value:
        return OPEN_AI_MODELS
    elif llm == LLMEnum.ANTHROPIC.value:
        return ANTHROPIC_MODELS


def get_api_key(llm):
    if llm == LLMEnum.ANTHROPIC.value:
        if os.getenv("ANTHROPIC_API_KEY"):
            return os.getenv("ANTHROPIC_API_KEY")
        else:
            st.error("Please set ANTHROPIC_API_KEY environment variable")
    elif llm == LLMEnum.OPEN_AI.value:
        if os.getenv("OPEN_AI_API_KEY"):
            return os.getenv("OPEN_AI_API_KEY")
        else:
            st.error("Please set OPEN_AI_API_KEY environment variable")
    else:
        return None


def build_home():
    st.set_page_config(
        page_title="Generate Email Tool", page_icon="🤖", layout="centered"
    )
    st.write(
        """<style>
        [data-testid="column"] {
            width: calc(50% - 1rem);
            flex: 1 1 calc(50% - 1rem);
            min-width: calc(50% - 1rem);
            text-align: center;
        }
        </style>""",
        unsafe_allow_html=True,
    )

    st.title("Generate Email Tool")
    st.markdown("This mini-app generates email for **TOMOSIA SALES**")
    st.text_area(
        label="Client Required",
        placeholder="Client Required",
        key="project_required",
        height=500,
    )

    col1, col2 = st.columns(2, vertical_alignment="center")
    with col1:
        st.session_state.compose_email = st.button(
            label="Generate",
            type="primary",
            on_click=generate_email,
        )
    with col2:
        st.session_state.clearAll = st.button(
            label="Reset",
            type="secondary",
            on_click=reset,
        )

    if st.session_state.text_error:
        st.error(st.session_state.text_error)


def build_result():
    st.subheader("Result")
    st.empty()
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.summary:
            st.markdown("""---""")
            st.text_area(
                label="Summary",
                value=st.session_state.summary,
                height=500,
                disabled=True,
            )
    with col2:
        if st.session_state.solution:
            st.markdown("""---""")
            st.text_area(
                label="Solution",
                value=st.session_state.solution,
                height=500,
                disabled=True,
            )

    if st.session_state.technology:
        st.markdown("""---""")
        st.text_area(
            label="Select Technology",
            value=st.session_state.technology,
            height=300,
            disabled=True,
        )

    if st.session_state.mail:
        st.markdown("""---""")
        st.text(body="Sale Mail")
        st.markdown(body=st.session_state.mail)


if __name__ == "__main__":

    prepare()
    build_home()
    build_sidebar()
    build_result()
