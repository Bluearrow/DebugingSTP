#!usr/bin/env python3
#-*- coding: utf-8 -*-

# Write to file with print() and write().
def write_to_file():
    filename = "test_file_to_write.txt"
    with open(filename, 'w') as f:
        print('hi {} {} {}'.format(1, 1.1, 2323), file = f)
        f.write("hehe")


if __name__ == '__main__':
    write_to_file()