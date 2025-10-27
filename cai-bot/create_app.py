from flask import Flask, request
from . import charlie

def create_app():
    app = Flask(__name__)
    charlie.init()

    @app.route("/")
    def index():
        return "Flask Server is alive!"
    
    @app.route('/chat')
    def chat():
        question = request.args.get('question')
        if question:
            answer = charlie.get_answer(question)
            return answer
        else:
            return "question  parameter is missing"
    
    return app
