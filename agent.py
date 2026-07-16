import os
from dotenv import load_dotenv
from operator import itemgetter
from langchain_community.utilities import SQLDatabase
from langchain_classic.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

import helper

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
        

    def LCEL_Answer(self, question):
        answer_prompt = PromptTemplate.from_template(
         """Given the following user question, corresponding SQL query, and SQL result, answer the user question.
            Question: {question}
            SQL Query: {query}
            SQL Result: {result}
            Answer: """)
        llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY'))
        write_query= create_sql_query_chain(llm, self.db)
        execute_query = QuerySQLDataBaseTool(db=self.db)
        # chain = write_query | excute_query
        # chain.invoke({'question': question})
        answer = answer_prompt | llm | StrOutputParser()
        chain = (
                    RunnablePassthrough
                    .assign(query=write_query | RunnableLambda(helper.clean_sql) )
                    .assign(result=itemgetter("query") 
                    | execute_query)
                    .assign(answer=answer)
                )
        res = chain.invoke({'question': question})
        return res.get('query') or "", res.get('answer') or ""


# if __name__ =="__main__":
#     txt = "how many students we have?"
#     app = SQLAgent()
#     app.LCEL_Answer(txt)
