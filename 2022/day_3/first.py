from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('input.txt', 'r')

    input = input_file.read()

    data = input.split('\n')

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    total = 0

    for entry in data:
        length = len(entry)
        first = entry[0:length//2]
        second = entry[length//2:length]

        same_letter = []

        for letter in first:
            if second.find(letter) != -1:
                same_letter = letter
                break

        total += alphabet.index(same_letter) + 1

    input_file.close()
    return "and the total is: {}".format(total)
