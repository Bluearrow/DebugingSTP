#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def show_2D_from_file(filename=filename):
    """ Draw the position and speed (if has) with data in file
    on a chart to give a visual observation of the motion
    trail.

    :param filename: Filename containing data like: x y speed_x speed_y.
    """

    with open(filename, 'r') as f:
        lines = f.read()

    datas = [line.strip().split(" ") for line in lines.strip().split("\n")]
    length = len(datas[0])
    x = [data[0] for data in datas]
    y = [data[1] for data in datas]
    if length == 4:
        m = [data[2] for data in datas]
        n = [data[3] for data in datas]

    for i in range(len(x)):
        if length == 2:      # Only position
            delta_x = 50
            delta_y = 50.0 * (i*5 + 50) / len(x)
            #delta_x = float(x[(i+1)%len(x)])
            #delta_y = float(y[(i+1)%len(x)])
        elif length == 4:   # Position and speed
            delta_x = 50 * float(m[i])
            delta_y = 50 * float(n[i])
        plt.arrow(float(x[i]),float(y[i]), delta_x, delta_y, \
                head_width = 20, head_length = 20, fc = 'k', ec = 'k')

    plt.plot(x, y, 'b*')
    plt.plot(x, y, 'r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-3025, 3025)
    plt.ylim(-2025, 2025)
    plt.title('Motion Trail')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    filename = 'D:\Project\VS\STP\STP_Framework\log_robot_infor.txt'
    show_2D_from_file(filename)