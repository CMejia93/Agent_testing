from langchain_core.prompts import ChatPromptTemplate
#from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama


from pydantic import BaseModel
from pydantic.types import StringConstraints
from typing import Annotated

# Create Query structure with pydantic so extra data can be added later
QuestionString = Annotated[
    str,
    StringConstraints(min_length=1, max_length=100, strip_whitespace=True, to_upper=True)
]

class BasicQuery(BaseModel):
    question: QuestionString


def PromptOllamaSbS(newQuery: BasicQuery):
    #define prompt template and ollama url
    remote_ollama_url = "http://38.25.74.180:11434"
    template = """Question: {question}
    Answer: Let's think step by step."""
    
    #create chain elements and invoke it
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOllama(model="llama3.2", base_url=remote_ollama_url,temeprature=0)
    chain = prompt | model
    response = chain.invoke({"question": newQuery.question})

    print(response.content)