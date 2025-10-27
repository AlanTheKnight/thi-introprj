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

    @app.route("/chat")
    def chat():
        question = request.args.get("question")
        if question:
            try:
                answer = charlie.get_answer(question)
                return jsonify({"question": question, "answer": answer})
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "question parameter is missing"}), 400

    return app
