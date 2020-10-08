from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

BankBot = ChatBot(name = 'BankBot',
                  read_only = False,
                  logic_adapters = ["chatterbot.logic.BestMatch"],
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")

# corpus_trainer = ChatterBotCorpusTrainer(BankBot)
# corpus_trainer.train("chatterbot.corpus.english")

greet_conversation = [
    "Hello1",
    "Hi there1!",
    "How are you doing1?",
    "I'm doing great1.",
    "That is good to hear1",
    "Thank you1.",
    "You're welcome1."
]

open_timings_conversation = [
    "What time does the Bank open?",
    "The Bank opens at 9AM",
]

close_timings_conversation = [
    "What time does the Bank close?",
    "The Bank closes at 5PM",
]

# Initializing Trainer Object
trainer = ListTrainer(BankBot)

# Training BankBot
trainer.train(greet_conversation)
trainer.train(open_timings_conversation)
trainer.train(close_timings_conversation)


# Once the chatbot has been trained, it can be used by calling Chatterbot's get_response() method.
# The method takes a user string as an input and returns a response string.

# while (True):
#     user_input = input()
#     if (user_input == 'quit'):
#         break
#     response = BankBot.get_response(user_input)
#     print (response)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(BankBot.get_response(userText))

if __name__ == '__main__':
    app.run()