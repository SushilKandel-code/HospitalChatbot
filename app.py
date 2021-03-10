#importing neccessary libraries
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

mychat_bot = ChatBot("Chatbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",
                     logic_adapters=[
                         {
                            'import_path': 'chatterbot.logic.BestMatch',
                            'default_response': 'I am sorry, but I do not understand.',
                            'maximum_similarity_threshold': 0.90
                         }
                     ]
                     )
trainer = ChatterBotCorpusTrainer(mychat_bot)
trainer.train("./data/commoncold.yml")
trainer.train("./data/doctor.yml")
trainer.train("./data/fever.yml")
trainer.train("./data/greetings.yml")
trainer.train("./data/normalchat.yml")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():

    userText = request.args.get('msg')
    return str(mychat_bot.get_response(userText))



if __name__ == '__main__':
    app.run()


