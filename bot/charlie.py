from chatterbot import ChatBot
from chatterbot.trainers import JsonFileTrainer
from chatterbot.comparisons import SpacySimilarity
import os
import glob
import json

chatbot = None


def init():
    global chatbot

    chatbot = ChatBot(
        "testBot",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                # "statement_comparison_function": SpacySimilarity,
                "default_response": "Sorry, I do not understand. Please rephrase your question.",
                "maximum_similarity_threshold": 0.90,
            }
        ],
        preprocessors=["chatterbot.preprocessors.clean_whitespace"],
        response_selection_method="chatterbot.response_selection.get_most_frequent_response",
        read_only=False,
    )

    trainer = JsonFileTrainer(
        chatbot, field_map={"text": "text", "in_response_to": "in_response_to"}
    )

    training_path = "/app/training"
    json_files = glob.glob(os.path.join(training_path, "*.json"))

    if not json_files:
        print("⚠️ No JSON training files found in '/app/training/'.")
        return

    print(f"🧠 Found {len(json_files)} training files. Beginning training...\n")

    for file_path in json_files:
        try:
            print(f"📘 Training with: {os.path.basename(file_path)}")

            # Load, convert to lowercase, and train
            with open(file_path, "r") as f:
                data = json.load(f)

            # Convert all text to lowercase in the training data
            for item in data.get("conversation", []):
                if "text" in item:
                    item["text"] = item["text"]
                if "in_response_to" in item and item["in_response_to"]:
                    item["in_response_to"] = item["in_response_to"].lower()

            # Save temporary lowercase file
            temp_file = file_path + ".tmp"
            with open(temp_file, "w") as f:
                json.dump(data, f)

            trainer.train(temp_file)
            os.remove(temp_file)

            print(f"✅ Finished training on: {os.path.basename(file_path)}\n")
        except Exception as e:
            print(f"❌ Error training on {file_path}: {e}\n")

    print("🎉 All training files processed successfully!")


def get_answer(question):
    global chatbot
    if chatbot is None:
        init()

    # Convert question to lowercase before processing
    question_lower = question.lower()
    response = chatbot.get_response(question_lower)
    print("Confidence: ", response.confidence)

    return response.text
