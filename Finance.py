import os
from properties import openai_key
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

#############################################

def Financial_Advisor():

    os.environ["OPENAI_API_KEY"] = openai_key

    Finance_template='''I want you to act as a acting financial advisor for people.
    In an easy way, explain everything deeply about the {financial_concept}.'''

    prompt= PromptTemplate(
        input_variables = ['financial_concept'],
        template = Finance_template
    )

    prompt.format(financial_concept='Finance')
    user_input = input("Enter a financial concept: ")
    llm=OpenAI(temperature=0.7)
    chain1=LLMChain(llm=llm,prompt=prompt)
    answer = chain1.run(user_input)
    print(answer)

# Call the function
Financial_Advisor()


