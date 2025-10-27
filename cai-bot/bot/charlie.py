from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import (
    JsonFileTrainer
)  # Potentially useful for larger datasets
import os
import glob

chatbot = None


def init():
    global chatbot

    chatbot = ChatBot(
        "testBot",
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': "I'm not sure about that yet.",
                'maximum_similarity_threshold': 0.90
            }
        ],
        read_only=False
    )

    # Configure trainer with field map
    trainer = JsonFileTrainer(
        chatbot,
        field_map={
            'text': 'text',
            'in_response_to': 'in_response_to',
            'conversation': 'conversation',
            'persona': 'persona'
        }
    )

    training_path = "../training"

    json_files = glob.glob(os.path.join(training_path, "*.json"))

    if not json_files:
        print("⚠️ No JSON training files found in '../training/'.")
        return

    print(f"🧠 Found {len(json_files)} training files. Beginning training...\n")

    for file_path in json_files:
        try:
            print(f"📘 Training with: {os.path.basename(file_path)}")
            trainer.train(file_path)
            print(f"✅ Finished training on: {os.path.basename(file_path)}\n")
        except Exception as e:
            print(f"❌ Error training on {file_path}: {e}\n")

    print("🎉 All training files processed successfully!")



def get_answer(question):
    global chatbot
    if chatbot is None:
        init()
    response = chatbot.get_response(question)
    print("Confidence: ", response.confidence)
    if response.confidence < 0.5:
        return "Sorry, i cannot answer this question - please rephrase!"
    return response.text
