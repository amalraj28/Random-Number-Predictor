from flask import Flask
import random

server = Flask(__name__)
random_number = random.randint(0, 9)


@server.route('/')
def home() -> str:
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/gT9BPNXovhAs0" width="420" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


@server.route('/<num>')
def check_num(num: int) -> str:
    num = int(num)

    if num == random_number:
        return '<h1>You win!!</h1>'
    elif num > random_number:
        return '<h1>Too high</h1>'
    else:
        return '<h1>Too low</h1>'


server.run(debug=True)
