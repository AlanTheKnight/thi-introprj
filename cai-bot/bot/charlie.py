from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import (
    ChatterBotCorpusTrainer,
)  # Potentially useful for larger datasets
import os

# Initialize chatbot as None
chatbot = None


def init():
    global chatbot

    # Create a writable database path
    db_path = "/app/tmp/chatbot.db"

    chatbot = ChatBot(
        "Charlie",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri=f'sqlite:///{db_path}',
        logic_adapters=["chatterbot.logic.BestMatch"]
    )
    trainer = ListTrainer(chatbot)

    # Train with initial greetings
    trainer.train(["Hi!", "Hey there, i am Charlie!"])
    trainer.train(["Ingolstadt", "City in Bavaria, Germany."])

    # --- New part: Training from a .txt file ---
    training_path = "/app/training"  # Path to training directory
    if os.path.exists(training_path):
        files = os.listdir(training_path)

        for filename in files:
            file_path = os.path.join(training_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    answer = f.readline().strip()
                    question = f.readline().strip()
                    if answer and question:
                        print("-->", answer, question)
                        trainer.train([question, answer])
            except (IOError, OSError) as e:
                print(f"Error reading file {filename}: {e}")

    # Process the lines for training
    # This assumes your .txt file has one conversation pair per two lines,
    # or one statement per line to be used as a simple list.
    # You might need to adapt this based on the format of your .txt file.


def get_answer(question):
    global chatbot
    if chatbot is None:
        init()
    response = chatbot.get_response(question)
    if response.confidence < 0.5:
        return "Sorry, i cannot answer this question - please rephrase!"
    return response.text
