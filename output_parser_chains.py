from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

model = ChatGroq(
    temperature=0, 
    groq_api_key='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', 
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

# chain = template1 | model | template2 | model 

# print(chain.invoke({"topic": "don toliver"}).content)

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'don toliver'})

print(result)

# parser = the glue that cleans and structures model output between steps. It’s not always required for a chain to run, but critical for robust, structured workflows.
