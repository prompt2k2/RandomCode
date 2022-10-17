def timedata():
    from cmath import sin
    from math import acos

# declare variables
    dt = 0.002
    pi = acos(-1)
    f1 = 8
    f2 = 10
    f3 = 40
    t = 0

    df = open('timedata.txt', 'w')  # save data to file in directory

    while t <= 5.00000:  # set limit for t

        x = 4*sin(2*pi*f1*t) + 8*sin(2*pi*f2*t) + 2*sin(2*pi*f3*t)
        # print("{:.4f}".format(t), "{:.4f}".format(x)) #4 decimal places

        df.write(str("{:.4f}".format(t)))
        df.write(str(" "))
        df.write(str("{:.4f}".format(x)))
        df.write('\n')
        t += dt

    df.close()

    return


def timedata_cos():
    from cmath import sin,cos
    from math import acos

# declare variables
    dt = 0.002
    pi = acos(-1)
    f1 = 8
    f2 = 10
    f3 = 40
    t = 0

    df = open('timedata_cos.txt', 'w')  # save data to file in directory

    while t <= 5.00000:  # set limit for t

        x = 4*sin(2*pi*f1*t) + 8*cos(2*pi*f2*t) + 2*sin(2*pi*f3*t)
        # print("{:.4f}".format(t), "{:.4f}".format(x)) #4 decimal places

        df.write(str("{:.4f}".format(t)))
        df.write(str(" "))
        df.write(str("{:.4f}".format(x)))
        df.write('\n')
        t += dt

    df.close()

    return

def main():

    timedata()
    timedata_cos()

    print("================completed=======================")


main()
