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

        for idx in range(int(first[0]), int(first[1]) + 1):
            if int(second[0]) <= idx and int(second[1]) >= idx:
                total += 1
                break

    input_file.close()
    return "and the total is: {}".format(total)
