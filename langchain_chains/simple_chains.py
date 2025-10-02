from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
  model="gemini-2.5-flash",
)

class SubTopic(BaseModel):
  name: str = Field(description="This is the name of Sub Topic")
  description: str = Field(description="This is the description of the sub topic")

class Topic(BaseModel):
  name: str = Field(description="This is the name of Sub Topic")
  subTopic: list["SubTopic"] = Field(description="List of Sub-Topics")

parser = StrOutputParser()
pydantic_parser = PydanticOutputParser(pydantic_object=Topic)

prompt = PromptTemplate(
  template='Give me two sub-topic and their descriptions related to {topic}\n {format_instructions}\n',
   input_variables=['topic'],
   partial_variables={'format_instructions': pydantic_parser.get_format_instructions()}
)

chain = prompt | model | pydantic_parser

chain.get_graph().print_ascii()

# result = chain.invoke({ 'topic': "Cricket"})

# print(result)
