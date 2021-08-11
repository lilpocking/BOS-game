import serial

def get_value():
    f = open('settings.txt', 'r')
    str = f.readline()
    str = f.readline()
    str = f.readline()
    str1 = f.readline()
    try:
        ser = serial.Serial(str[:-1], int(str1[:-1]))
        val = ser.readline().decode("UTF-8")
        ser.close()
        return val
    except:
        return "Couldn't open port"