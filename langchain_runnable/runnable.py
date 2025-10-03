from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableBranch, RunnableParallel, RunnablePassthrough, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
  model="gemini-2.5-flash",
)

parser = StrOutputParser()


# Generate project idea and it's validation
generate_project_idea_prompt = PromptTemplate(
  template="Generate a project idea based on below details: \n{project_requirements}",
  input_variables=["project_requirements"]
)

generate_project_validation_prompt = PromptTemplate(
  template="Generate a project validation criteria and with requirements based on the project_requirements: {project_requirements}",
  input_variables=["project_requirements"]
)

project_idea_chain = generate_project_idea_prompt | model | parser
validation_prompt_chain = generate_project_validation_prompt | model | parser

generate_project_idea_with_validation_criteria = RunnableParallel({
  "project_idea": project_idea_chain,
  "validation": validation_prompt_chain
})

result = generate_project_idea_with_validation_criteria.invoke({"project_requirements": "This will be a backend + generative ai project, it should reflect my experience in both fields as senior developer. This project should be end to end developed and can have a scope for monetization. The languages/framework it should include is from python ecosystem, can be fastApi based and frontend will be on next.js"})

print(f"Project Idea: {result["project_idea"]}")
print(f"Project Idea Validator: {result["validation"]}")

# Validate the project idea with re-iteration if required
# validate_project_idea = PromptTemplate(
#   template="This is the project idea: \n{project_idea}\n\nThis is the validation criteria and requirements for the idea: \n{validation}\n\n Based on the requirements rate the project idea on scale of 0 to 10",
#   input_variables=["project_idea", "validation"]
# )
#
# reiterate_the_idea_prompt = PromptTemplate(
#   template="Project idea: \n{idea} \n\nRe-iterate above project idea based on the below criteria [ It's rating was {rating} on scale of 0 to 10 for the same criteria ] : \n{validation}",
#   input_variables=["idea", "rating", "validation"]
# )
#
# reiterate_chain = RunnableParallel({
#   "project_idea": RunnablePassthrough(),
#   "rating": reiterate_the_idea_prompt | model | parser
# })
#
# validation_chain = RunnableBranch(
#   (lambda x: int(x) < 5, reiterate_chain),
#   RunnablePassthrough()
# )
