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

    @app.route("/api/chat", methods=["POST"])
    def chat():
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON body is required"}), 400
        
        question = data.get("message")
        if question:
            try:
                answer = charlie.get_answer(question)
                return jsonify({"question": question, "answer": answer})
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "message field is missing"}), 400

    return app
