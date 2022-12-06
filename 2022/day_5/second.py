from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('input.txt', 'r')

    input = input_file.read()

    data = input.split('\n')

    total = ''

    crates = {
        '1': 'BQC',
        '2': 'RQWZ',
        '3': 'BMRLV',
        '4': 'CZHVTW',
        '5': 'DZHBNVG',
        '6': 'HNPCJFVQ',
        '7': 'DGTRWZS',
        '8': 'CGMNBWZP',
        '9': 'NJBMWQFP'
    }

    for entry in data:
        commands = [int(s) for s in entry.split() if s.isdigit()]

        crate = crates[str(commands[1])][-commands[0]:]
        crates[str(commands[2])] += crate
        crates[str(commands[1])] = crates[str(commands[1])][:-commands[0]]

    for crate in crates.values():
        total += crate[-1]

    input_file.close()
    return 'and the total is: {}'.format(total)
