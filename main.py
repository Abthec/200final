import serial
import time


def get_month_string(month):

    if month == 1:
        month_string = "Jan"
    elif month == 2:
        month_string = "Feb"
    elif month == 3:
        month_string = "Mar"
    elif month == 4:
        month_string = "Apr"
    elif month == 5:
        month_string = "May"
    elif month == 6:
        month_string = "Jun"
    elif month == 7:
        month_string = "Jul"
    elif month == 8:
        month_string = "Aug"
    elif month == 9:
        month_string = "Sep"
    elif month == 10:
        month_string = "Oct"
    elif month == 11:
        month_string = "Nov"
    elif month == 12:
        month_string = "Dec"

    return month_string


def create_file_name(time_struct, month_string):

    filename = str(time_struct[0]) + '-' + month_string + '-' + str(time_struct[1]) + '.' + str(time_struct[3]) + '.' + str(
        time_struct[4]) + '.' + str(time_struct[5]) + '.LapTimes' + '.txt'

    return filename


def main():

    ser = serial.Serial("COM7", baudrate=9600, timeout=1)
    time_struct = time.localtime()

    month = time_struct[2]
    month_string = get_month_string(month)

    filename = create_file_name(time_struct, month_string)

    time_file = open(filename, 'w+')

    while 1:
        arduino_data = ser.readline().decode()
        if arduino_data != '':
            if arduino_data[0] == '[':
                time_file.write(arduino_data)
                print(arduino_data)


main()

