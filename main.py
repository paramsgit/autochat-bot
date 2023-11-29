from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

#memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    text=data.get('data')
    user_input = text
    try:
        #conversation = ConversationChain(llm=llm,memory=memory)
        #output = conversation.predict(input=user_input)
        #memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response":True,"message":get_response(user_input)})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})



def get_response(text):

    # Let's chat for 5 lines
    for step in range(5):

        chat_history_ids = None

        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens,
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # pretty print last ouput tokens from bot
        return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
if __name__ == '__main__':
    app.run()
