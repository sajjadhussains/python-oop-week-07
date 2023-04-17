'''My cute api'''

from flask import Flask,request

database={'shuvo':'100','nahid':'200','rifat':'300'}
app = Flask(__name__)

@app.route('/home',methods=['GET'])
def home():
    return 'Welcome to my cute API'

@app.route('/home/something',methods=['GET'])
def onno_kichu():
    return 'Tomar imagination shundor.Ayon k bad dau ekebare'

@app.route('/getdata',methods=['GET'])
def get_data():
    return database
@app.route('/adddata',methods=['GET','PUT'])
def add_data():
    key,value=list(request.args.items())[0]
    database[key]=value
    print(key,value)
    return f'{key} updated'
@app.route('/deletedata',methods=['GET','DELETE'])
def delete_data():
    key,value=list(request.args.items())[0]
    database.pop(value)
    return f'{value} deleted'

if __name__== '__main__':
    app.run()