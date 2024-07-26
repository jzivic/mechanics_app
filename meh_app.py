


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'MATER TI JEBEM!'

if __name__ == '__main__':
    app.run(debug=True)


