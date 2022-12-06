from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('input.txt', 'r')

    input = input_file.read()

    data = input.split('\n')

    total = 0

    for entry in data:
        ranges = entry.split(',')
        first = ranges[0].split('-')
        second = ranges[1].split('-')

        if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
            total += 1
        elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
            total += 1

    input_file.close()
    return "and the total is: {}".format(total)
