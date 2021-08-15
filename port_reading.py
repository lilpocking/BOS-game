import serial


def get_value():
    f = open('settings.txt', 'r')
    str1 = f.readline()
    str1 = f.readline()
    str1 = f.readline()
    str2 = f.readline()
    f.close()
    str1 = str1[:-1]
    str2 = str2[:-1]
    ser = serial.Serial(str1, int(str2))
    print("heell")
    try:
        ser.isOpen()
        val = ser.readline().decode("UTF-8")
        ser.close()
        print(val)
        return str(val)
    except IOError:
        ser.close()
        ser.open()
        val = ser.readline().decode("UTF-8")
        ser.close()
        print(val)
        return str(val)

    ser.close()