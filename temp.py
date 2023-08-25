from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv
# app = Flask(__name__)
# CORS(app)

load_dotenv()
API = os.environ['API']


def get_data():
    
    
  
    text='''Give only json output as given below for user input, It should have all four keys topwear,bottomwear,footwear,accesories and also should have four sub keys=catagory,subcatagory,color,tags and it must be only json no other text, Example output for input 'Generate outfit for 20 year old young woman in mumbai for diwali' is={ "topwear": {"category": "T-Shirt","subcategory": "Oversized","color":"White","tags":["Party","Stylish"]},"bottomwear": {"category": "Jeans","subcategory": "Straight","color":"Black","tags":["Straight"]},"footwear": {"category": "Shoes","subcategory": "Big","color":"Blue","tags":["Comfortable"]},"accessories": [{"category": "Watch","subcategory": "Smartwatch","color":"Black","tags":["Water Resistant"]},{"category": "Belt","subcategory": "Leather Belt","color":"brown","tags":["stylish"]}]}'''
    openai.api_key = API
    
    user_input = text
    # print(user_input)
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
          messages=[
    {
      "role": "user",
      "content": f"outfit for me on diwali , i am male 20 years old in Jaipur"
    },{
      "role": "system",
      "content": f"{text} "
    }
  ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
       
        model_reply = response['choices'][0]['message']['content']
        print(response,"\nresponse\n\n",model_reply)
        # return jsonify({"response":True,"message":model_reply})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        # return jsonify({"message":error_message,"response":False})

get_data()

    


