#!flask/bin/python
from flask import Flask,jsonify,request
from chatterbot.trainers import ListTrainer # method to train the chatbot
from chatterbot import ChatBot # import the chatbot
import urllib.parse
import os
bot = ChatBot('TestBot') # create the chatbot
bot.set_trainer(ListTrainer)# set the trainer test

file_path = os.path.abspath(__file__)
files_path = os.path.join(os.path.dirname(file_path), 'files')


for root, dirs, files in os.walk(files_path, topdown=False):
    for name in files:
        print('name in files: '+os.path.join(root, name))
        chat = open(os.path.join(root, name), 'r', encoding="utf8").readlines()
        bot.train(chat)


app = Flask(__name__)

@app.route('/chatbot')
def chatbot():

    return "welcome to chatbot parent "

@app.route('/chatbot/conversations', methods=['GET'])
def get_reply():
    question = request.args.get('question')
    question=urllib.parse.unquote(question)
    response = bot.get_response(question)
    replystr='you: '+question + '<br>' + 'bot: '+str(response)
    return replystr

if __name__ == '__main__':
    app.run(debug=True)