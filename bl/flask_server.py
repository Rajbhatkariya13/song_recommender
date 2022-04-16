import sys
sys.path.insert(0, "c:/raj/major/dl")
from main1 import get_response
from flask import Flask,jsonify,request

app=Flask(__name__)


@app.route('/')
def index():
    return "welcome to the course API"

@app.route('/sendMessage',methods=['Post'])
def get_text():
    jsony=request.json
    print(jsony)
    msg=jsony['message']
    botMessage=get_response(str(msg).strip())

    print(msg)
    ls=['channa mereyaa','tu safar mera','babli badmash']
    e={'botMessage':botMessage,'mood':'happy','songs':ls}
    
    
    print(e)
    return e



if __name__=="__main__":
    app.run(host='0.0.0.0', port=5050)
    