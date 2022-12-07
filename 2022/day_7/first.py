from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('input.txt', 'r')

    input = input_file.read()

    data = input.split('\n')

    filesystem = {
        '/': {
            'dir_size': 0
        }
    }

    where_am_i = ''

    for entry in data:
        if entry[0] == '$':
            if entry[2:4] == 'cd':
                if entry[5:] == '..':
                    where_am_i = '/'.join(where_am_i.split('/')[0:-1]) or '/'
                elif entry[5:] == '/':
                    where_am_i = '/'
                else:
                    if where_am_i[-1] == '/':
                        where_am_i += entry[5:]
                    else:
                        where_am_i += '/' + entry[5:]
            elif entry[2:4] == 'ls':
                continue
        elif entry[0:3] == 'dir':
            path = where_am_i.split('/')
            open_dir = filesystem['/']
            for dir in path[1:]:
                if dir != '':
                    open_dir = open_dir[dir]
            open_dir[entry[4:]] = {'dir_size': 0}
        else:
            size, name = entry.split(' ')
            path = where_am_i.split('/')
            open_dir = filesystem['/']
            for dir in path[1:]:
                if dir != '':
                    open_dir['dir_size'] += int(size)
                    open_dir = open_dir[dir]
            open_dir[name] = int(size)
            open_dir['dir_size'] += int(size)

    def find_correct_dirs(data, max_size, total):
        for key in data.keys():
            if type(data[key]) is not int:
                size = data[key]['dir_size']
                if (size > max_size):
                    total = find_correct_dirs(data[key], max_size, total)
                else:
                    total += size
                    total = find_correct_dirs(data[key], max_size, total)

        return total

    total = find_correct_dirs(filesystem, 100000, 0)

    input_file.close()
    return 'and the total is: {}'.format(total)
