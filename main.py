from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv
app = Flask(__name__)
CORS(app)

load_dotenv()
API = os.environ['API']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    
    data = request.get_json()
    text=data.get('data')
    openai.api_key = API
    
    user_input = text
    print(user_input)
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
       
        model_reply = response['choices'][0]['text']
        print(response,model_reply)
        return jsonify({"response":True,"message":model_reply})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})

    

if __name__ == '__main__':
    app.run()
