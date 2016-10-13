#!usr/bin/env python3
#-*- coding: utf-8 -*-

# Write to file with print() and write().
def write_to_file():
    filename = "log\\test_file_to_write.txt"
    with open(filename, 'w') as f:
        print('hi {} {} {}'.format(1, 1.1, 2323), file = f)
        print('{0.2f} {1.2f}'.format(1.11, 1.1111), file =f)
        f.write("hehe")


if __name__ == '__main__':
    write_to_file()