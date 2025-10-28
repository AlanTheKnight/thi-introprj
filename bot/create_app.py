from flask import Flask, request, jsonify
import charlie


def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def index():
        return "Flask Server is alive!"

    @app.route("/health")
    def health():
        """Health check endpoint"""
        try:
            # Test if chatbot can be initialized
            if charlie.chatbot is None:
                charlie.init()
            return jsonify({"status": "healthy", "chatbot": "initialized"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

<<<<<<< HEAD
    @app.route("/chat")
    def chat():
        question = request.args.get("question")
=======
    @app.route("/api/chat", methods=["POST"])
    def chat():
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON body is required"}), 400
        
        question = data.get("message")
>>>>>>> f3ad263bd9a26f6c0a331d766ddd380e21b8d493
        if question:
            try:
                answer = charlie.get_answer(question)
                return jsonify({"question": question, "answer": answer})
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
<<<<<<< HEAD
            return jsonify({"error": "question parameter is missing"}), 400
=======
            return jsonify({"error": "message field is missing"}), 400
>>>>>>> f3ad263bd9a26f6c0a331d766ddd380e21b8d493

    return app
