from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,openai
app = Flask(__name__)
CORS(app)
@app.route('/')








def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    return jsonify({"response":True,"message":"model_reply"})
    data = request.get_json()
    text=data.get('data')
    

    
    API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'
    
    API_KEY = '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'
    openai.api_key = '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'
    
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
