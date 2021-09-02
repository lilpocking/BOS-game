import serial

ser = serial.Serial()
def open_port():
    global ser
    f = open('settings.txt', 'r')
    str1 = f.readline()
    str1 = f.readline()
    str1 = f.readline()
    str2 = f.readline()
    f.close()
    str1 = str1[:-1]
    str2 = str2[:-1]
    ser = serial.Serial(str1, int(str2), timeout = 2)
def get_value():
    global ser
    if ser.isOpen():
        val = ser.readline().decode("UTF-8")
        if val == '':
            return "Nothing"
        print(val)
        return str(val)
    else:
        ser.open()
        val = ser.readline().decode("UTF-8")
        if val == '':
            return "Nothing"
        print(val)
        return str(val)
def serclose():
    ser.close()
