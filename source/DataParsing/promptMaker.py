from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

template = """
System Prompt: 
{sys_prompt}

Examples: 
{examples}

Schema to follow:
{format_instructions}

Transcript:
{context}

Output the completed JSON object and nothing else.
"""


def prompt_creator(pydantic_object):
    parser = PydanticOutputParser(pydantic_object = pydantic_object)

    prompt_template = PromptTemplate(
        input_variables=["context", "sys_prompt", "examples"],
        template = template,
        partial_variables = {"format_instructions" : parser.get_format_instructions()}

    )

    return prompt_template, parser


