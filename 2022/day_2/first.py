from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('input.txt', 'r')

    input = input_file.read()

    data = input.split('\n')

    dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    total = 0

    for entry in data:
        x, y = entry.split(' ')

        if x == 'A' and y == 'X':
            total += 3

        if x == 'A' and y == 'Y':
            total += 6

        if x == 'A' and y == 'Z':
            total += 0

        if x == 'B' and y == 'X':
            total += 0

        if x == 'B' and y == 'Y':
            total += 3

        if x == 'B' and y == 'Z':
            total += 6

        if x == 'C' and y == 'X':
            total += 6

        if x == 'C' and y == 'Y':
            total += 0

        if x == 'C' and y == 'Z':
            total += 3

        total += dict[y]

    input_file.close()
    return "and the total is: {}".format(total)
