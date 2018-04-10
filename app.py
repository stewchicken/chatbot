#!flask/bin/python
from flask import Flask,jsonify,request,render_template
from chatterbot.trainers import ListTrainer # method to train the chatbot
from chatterbot import ChatBot # import the chatbot
import urllib.parse
import os

bot = ChatBot('TestBot') # create the chatbot
bot.set_trainer(ListTrainer)# set the trainer test

# get current python file path
file_path = os.path.abspath(__file__)
# get directory files full path
files_path = os.path.join(os.path.dirname(file_path), 'files')

# walk through files directory to find out conversation file
for root, dirs, files in os.walk(files_path, topdown=False):
    for name in files:
        print('name in files: '+os.path.join(root, name))
        chat = open(os.path.join(root, name), 'r', encoding="utf8").readlines()
        bot.train(chat)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get', methods=['GET'])
def get_reply():
    question = request.args.get('msg')
    question=urllib.parse.unquote(question)
    response = bot.get_response(question)
    replystr=str(response)
    return replystr

if __name__ == '__main__':
    app.run(debug=True)