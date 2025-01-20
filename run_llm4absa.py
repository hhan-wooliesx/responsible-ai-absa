# Takes in two arguments, one for comment and another for aspect --comment, --aspect

from concurrent.futures import ThreadPoolExecutor

import vertexai
from langchain_google_vertexai import VertexAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate

from prompts import (
    PREAMBLE, SINGLEHEAD_INSTRUCTION, MULTIHEAD_INSTRUCTION, CONCAT_INSTRUCTION, ABSA_TEMPLATE
)
from constants import FAST_MODEL_TO_USE, MODEL_TO_USE, PROJECT_ID, REGION

import logging
import argparse

vertexai.init(project=PROJECT_ID, location=REGION)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--comment", help="the comment in text format", type=str)
parser.add_argument("-a", "--aspect", help="the aspect for which we want to predict the sentiment for", type=str)

args = parser.parse_args()

comment = args.comment
aspect = args.aspect

llm = VertexAI(
    model=FAST_MODEL_TO_USE,
    temperature=0.05,
    top_p=0.95,
    top_k=40,
    max_tokens=2**13,
    max_retries=1,
    stop=None,
)

prompt_template = PromptTemplate(template=ABSA_TEMPLATE, input_variables=['comment', 'aspect'])
chain = prompt_template | llm
print(chain.invoke({'comment': comment, 'aspect': aspect}))