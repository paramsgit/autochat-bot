from flask import Flask, render_template,jsonify,request
# from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
load_dotenv()
API = os.environ['API']


# def get_data():
    
    
  
#     text='''Give only json output as given below for user input, It should have all four keys topwear,bottomwear,footwear,accesories and also should have four sub keys=catagory,subcatagory,color,tags and it must be only json no other text, Example output for input 'Generate outfit for 20 year old young woman in mumbai for diwali' is={ "topwear": {"category": "T-Shirt","subcategory": "Oversized","color":"White","tags":["Party","Stylish"]},"bottomwear": {"category": "Jeans","subcategory": "Straight","color":"Black","tags":["Straight"]},"footwear": {"category": "Shoes","subcategory": "Big","color":"Blue","tags":["Comfortable"]},"accessories": [{"category": "Watch","subcategory": "Smartwatch","color":"Black","tags":["Water Resistant"]},{"category": "Belt","subcategory": "Leather Belt","color":"brown","tags":["stylish"]}]}'''
#     openai.api_key = API
    
#     user_input = text
#     # print(user_input)
#     try:
#         response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#           messages=[
#     {
#       "role": "user",
#       "content": f"outfit for me on diwali , i am male 20 years old in Jaipur"
#     },{
#       "role": "system",
#       "content": f"{text} "
#     }
#   ],
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#         )
       
#         model_reply = response['choices'][0]['message']['content']
#         print(response,"\nresponse\n\n",model_reply)
#         # return jsonify({"response":True,"message":model_reply})
#     except Exception as e:
#         print(e)
#         error_message = f'Error: {str(e)}'
#         # return jsonify({"message":error_message,"response":False})


def get_data():
    
    
    
    
    user_input = "What is sun"
    print(user_input)
    chat_history = []
    try:
      llm = ChatOpenAI()
      
      prompt = ChatPromptTemplate(messages=[SystemMessagePromptTemplate.from_template("You are a nice chatbot having a conversation with a human."),MessagesPlaceholder(variable_name="chat_history"),HumanMessagePromptTemplate.from_template("What is sun")])
      memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
      conversation = LLMChain(llm=llm,prompt=prompt,verbose=True,memory=memory)
      print(conversation,memory)  
      conversation.predict(input="Hi there!")

        # return jsonify({"response":True,"message":"model_reply"})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        print(error_message)
        # return jsonify({"message":error_message,"response":False})


get_data()

    


