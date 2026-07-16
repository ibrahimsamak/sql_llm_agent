import os
from langchain_community.utilities import SQLDatabase
from langchain_classic.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
QA_PORPMT  = """
Question: {question}

SQL Result:
{result}

Answer in plain English.
"""

class SQLAgent:
    def __init__(self):
        load_dotenv(override=True)
        self.db = SQLDatabase.from_uri('sqlite:///school.db')
        # self.db.run("SELECT * FROM students;")

    def answer(self, question):
        llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))
        chain = create_sql_query_chain(llm, self.db)
        sql = chain.invoke({'question': question})
        result = self.db.run(sql)
        answer = llm.invoke(QA_PORPMT.format(question=question, result=result))
        return sql, answer.content
        

