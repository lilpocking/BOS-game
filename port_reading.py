import serial
f = open('settings.txt', 'r')
str1 = f.readline()
str1 = f.readline()
str1 = f.readline()
str2 = f.readline()
f.close()
str1 = str1[:-1]
str2 = str2[:-1]
ser = serial.Serial(str1, int(str2), timeout=5)
def get_value():
    if ser.isOpen():
        try:
            val = ser.readline().decode("UTF-8")
        finally:
            return "Nothing"
        print(val)
        return str(val)
    else:
        ser.open()
        try:
            val = ser.readline().decode("UTF-8")
        finally:
            return "Nothing"
        print(val)
        return str(val)
def serclose():
    ser.close()