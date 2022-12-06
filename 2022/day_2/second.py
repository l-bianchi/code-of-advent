from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('input.txt', 'r')

    input = input_file.read()

    data = input.split('\n')

    result_dict = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    z_dict = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    total = 0

    for entry in data:
        x, result = entry.split(' ')

        if x == 'A' and result == 'X':
            y = 'C'
            total += z_dict[y] + result_dict[result]

        if x == 'A' and result == 'Y':
            y = 'A'
            total += z_dict[y] + result_dict[result]

        if x == 'A' and result == 'Z':
            y = 'B'
            total += z_dict[y] + result_dict[result]

        if x == 'B' and result == 'X':
            y = 'A'
            total += z_dict[y] + result_dict[result]

        if x == 'B' and result == 'Y':
            y = 'B'
            total += z_dict[y] + result_dict[result]

        if x == 'B' and result == 'Z':
            y = 'C'
            total += z_dict[y] + result_dict[result]

        if x == 'C' and result == 'X':
            y = 'B'
            total += z_dict[y] + result_dict[result]

        if x == 'C' and result == 'Y':
            y = 'C'
            total += z_dict[y] + result_dict[result]

        if x == 'C' and result == 'Z':
            y = 'A'
            total += z_dict[y] + result_dict[result]

    input_file.close()
    return "and the total is: {}".format(total)
