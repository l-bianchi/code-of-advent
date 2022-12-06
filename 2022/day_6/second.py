from flask import Flask
import sys

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('input.txt', 'r')

    data = input_file.read()

    sys.setrecursionlimit(10000)

    def find(string, letter):
        return [i for i, ltr in enumerate(string) if ltr == letter]

    def check(start, end):
        string = data[start:end]
        for letter in string:
            amount = len(find(string, letter))
            if amount > 1:
                string = check(start + 1, end + 1)

        return string

    string = check(0, 14)
    total = data.find(string) + 14

    input_file.close()
    return 'and the total is: {}'.format(total)
