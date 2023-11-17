from flask import Flask, render_template, request
import os
from properties import openai_key
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

app = Flask(__name__)

def generate_financial_advice(user_input):
    os.environ["OPENAI_API_KEY"] = openai_key

    Finance_template = '''I want you to act as an acting financial advisor for people. 
    In an easy way, explain everything deeply about the {financial_concept}.'''

    prompt = PromptTemplate(
        input_variables=['financial_concept'],
        template=Finance_template
    )
    prompt.format(financial_concept='Finance')
    llm = OpenAI(temperature=0.7)
    chain1 = LLMChain(llm=llm, prompt=prompt)
    answer = chain1.run(user_input)
    
    return answer

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        user_input = request.form['financial_concept']
        result = generate_financial_advice(user_input)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
