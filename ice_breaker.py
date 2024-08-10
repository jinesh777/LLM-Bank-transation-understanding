from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from output_parser import summary_parser,Summary
from typing import Tuple
from flask import Flask, render_template, request, jsonify

def ice_break_with(information: str)-> Tuple [Summary]:
    summary_template = """
    given the information {information} about a bank statement transaction description I want you to create:
    1. identify any person 
    2. identify any organisation
    3. identify the type of transaction(imps,neft,rtgs,upi,bill payments,ach,nach)
    4. identify any location if there
    
     \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm =ChatOllama(model="llama3")
    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information": information})
    #print(jsonify(res))
    return res
#ice_break_with("BY TRANSFER IDIB000N110/Mr ABHISHEK GULABCHAND KAS YAP /XXX XX96788/abhishek.g.kashyap@ybl /UPI/318240217111/Payment fro m PhonePe")