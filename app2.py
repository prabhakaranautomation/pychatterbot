# from chatterbot import ChatBot
#
# bot = ChatBot(
#     "SQLMemoryTerminal",
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         {
#             "import_path": "chatterbot.logic.BestMatch",
#             "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance"
#         },
#         {
#             'import_path' : 'chatterbot.logic.LowConfidenceAdapter',
#             'threshold' : 0.3,
#             'default_response' : "Sorry. I can not find the exact answer."
#         },
#         'chatterbot.logic.multi_adapter.MultiLogicAdapter',
#     ],
#     input_adapter="chatterbot.input.TerminalAdapter",
#     output_adapter="chatterbot.output.TerminalAdapter",
#     read_only= True
# )
#
# print("input question")
#
# while True:
#     try:
#         print("Q : ",end="")
#         bot_input = bot.get_response(None)
#
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break