## Chat Bot with OpenAI API and Flask

Introducing the Flask Chat Bot powered by the OpenAI API! This innovative chat bot combines the flexibility and ease of use of Flask with the power of the OpenAI API to deliver intelligent and interactive conversations. With natural language processing capabilities, the chat bot can understand user queries and provide relevant responses in real time. Whether it's customer support, information retrieval, or just casual conversation, our chat bot is ready to engage and assist users with its advanced AI capabilities. Get ready for an immersive and dynamic chat experience like never before!


<img src="screenshot.png" alt="img_not_found">

## Prerequisites

- Python 3.9 or higher
- Flask
- Langchain
- OpenAI API
- OpenAI Python library

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/paramsgit/autochat-bot

2  Navigate to the project directory:
    
    cd autochat-bot

3 Install the required dependencies using pip:
    
    pip install -r requirements.txt

4 Set up OpenAI API:

- Create an OpenAI account and obtain an API key.
- Set the OPENAI_API_KEY environment variable with your API key 

    On Windows:
    - Use the search bar in the Start menu to find “Edit the system environment variables”.
    - Click “Environment variables”
    - Use the upper “New…” button to add a User variable
    - Create a new variable called OPENAI_API_KEY and set the value to the secret key you got from your account settings on openai.com

    For Mac or Linux:
    - Find the .bashrc, .bash_profile, or .zshrc in your home directory
    - Open the file in a text editor
    - Add a new line to the file:
    ``export OPENAI_API_KEY= [your secret key]``

5 Run the application:

    python app.py

6 Open your web browser and visit http://127.0.0.1:{port}/ to access the chat bot.



## Usage
Once the application is running, you can interact with the chat bot through the web interface. Type your messages in the input box, and the bot will respond accordingly.

## Deployment
To deploy the chat bot to a production environment, follow the deployment instructions provided by the Flask documentation. It's recommended to use a production-ready WSGI server, such as Gunicorn or uWSGI.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

    Feel free to modify and expand upon this template according to your specific project needs.


