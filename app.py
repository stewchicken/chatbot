#!flask/bin/python
from flask import Flask,jsonify,request
from chatterbot.trainers import ListTrainer # method to train the chatbot
from chatterbot import ChatBot # import the chatbot
import  urllib3, os
bot = ChatBot('TestBot') # create the chatbot
bot.set_trainer(ListTrainer)# set the trainer test

for file in os.listdir('files'):
    chat = open('files/'+file, 'r', encoding="utf8").readlines()
    print (file)
    bot.train(chat)

app = Flask(__name__)

@app.route('/chatbot')
def chatbot():
    return "welcome to chatbot"

@app.route('/chatbot/conversations', methods=['GET'])
def get_reply():
    question = request.args.get('question')
    question=urllib3.parse.unquote(question)
    response = bot.get_response(question)
    replystr='you: '+question + '<br>' + 'bot: '+str(response)
    return replystr

if __name__ == '__main__':
    app.run(debug=True)