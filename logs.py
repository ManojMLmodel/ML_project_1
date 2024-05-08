from flask import Flask
from src.logger import log

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    log.info("We are testing our logging module")
    return "Success"

if __name__=='__main__':
    app.run(debug=True) #5000