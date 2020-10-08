# from flask import Flask, render_template, request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer
#
# # app = Flask(__name__)
# #
# # english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# # trainer = ChatterBotCorpusTrainer(english_bot)
# # trainer.train("chatterbot.corpus.english")
#
# bot = ChatBot(
#     'Norman',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         'chatterbot.logic.MathematicalEvaluation',
#         'chatterbot.logic.TimeLogicAdapter'
#     ],
#     database_uri='sqlite:///database.sqlite3'
# )
# trainer = ListTrainer(bot)
#
# trainer.train([
#     'How are you?',
#     'I am good.',
#     'That is good to hear.',
#     'Thank you',
#     'You are welcome.',
# ])
#
# while True:
#     try:
#         bot_input = bot.get_response(input())
#         print(bot_input)
#
#     except(KeyboardInterrupt, EOFError, SystemExit):
#         break
#
# # @app.route("/")
# # def home():
# #     return render_template("index.html")
# #
# # @app.route("/get")
# # def get_bot_response():
# #     userText = request.args.get('msg')
# #     return str(english_bot.get_response(userText))
# #
# # if __name__ == '__main__':
# #     app.run()