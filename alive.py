#The web server started by this file can be pinged from third party sites to keep your repl running 24x7
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I am working dude!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
