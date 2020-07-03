from flask import Flask

app = Flask(__name__)

@app.route('/')
def your_name(num='Ruslan'):
    return(f'Your name is {num}')

# name = input("Please input Your name ")

# your_name(num='Ruslan')

if __name__ == '__main__':
    # app.run('localhost', port=5000, debug=True)
    app.run(debug=True)
    # app.run('0.0.0.0', port=80)