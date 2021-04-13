from flask import Flask
from threading import Thread
from flask import render_template
from status import check
app = Flask('')

#word=check()
@app.route('/')
def home():
  return render_template('index.html',word=check())
  
def run():
  app.run(host ='0.0.0.0', port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()
