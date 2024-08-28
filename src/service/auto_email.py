import pandas as pd
import logging
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from src.service.llm.base import BaseService
import src.service.prompt.prompt as prompts


def summary_project(client: BaseService, project_required: str) -> BaseMessage:
    logging.info("START SUMMARY")
    try:
        messages = [
            SystemMessage(prompts.SUMMARY_PROJECT_INFO),
            HumanMessage(project_required),
        ]
        summary = client.chatCompletion(message=messages)
        return summary
    except Exception as e:
        raise e
    finally:
        logging.info("END SUMMARY")


def think_solution(client: BaseService, project_summary: str) -> BaseMessage:
    logging.info("START THINK SOLUTION")
    try:
        messages = [
            SystemMessage(prompts.THINK_SOLUTION),
            HumanMessage(project_summary),
        ]
        solution = client.chatCompletion(message=messages)
        return solution
    except Exception as e:
        raise e
    finally:
        logging.info("END THINK SOLUTION")


def select_technologies(
    client: BaseService, project_info: str, solution_info: str
) -> BaseMessage:
    logging.info("START TECHNOLOGY")
    try:
        technology_csv = pd.read_csv("./data/technologies.csv")
        prompt = prompts.SELECT_TECHNOLOGY.format(
            project_info=project_info,
            solution_info=solution_info,
            technology_list_csv=technology_csv.to_string(),
        )
        messages = [SystemMessage(prompt)]
        technology = client.chatCompletion(message=messages)
        return technology
    except Exception as e:
        raise e
    finally:
        logging.info("END TECHNOLOGY")


def compose_email(
    client: BaseService, project_info: str, solution_info: str, technology_info: str
) -> BaseMessage:
    logging.info("START COMPOSE EMAIL")
    try:
        prompt = prompts.COMPOSE_EMAIL.format(
            project_info=project_info,
            solution_info=solution_info,
            technology_info=technology_info,
        )
        messages = [SystemMessage(prompt)]
        email = client.chatCompletion(message=messages)
        return email
    except Exception as e:
        raise e
    finally:
        logging.info("END COMPOSE EMAIL")
