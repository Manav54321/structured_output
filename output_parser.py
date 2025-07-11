from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

model = ChatGroq(
    temperature=0, 
    groq_api_key='groq_api_key', 
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

prompt1 = template1.invoke({"topic": "don toliver"})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result1.content})

result2 = model.invoke(prompt2)

print(result2.content)