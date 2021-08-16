import serial
f = open('settings.txt', 'r')
str1 = f.readline()
str1 = f.readline()
str1 = f.readline()
str2 = f.readline()
f.close()
str1 = str1[:-1]
str2 = str2[:-1]
ser = serial.Serial(str1, int(str2))
def get_value():
    if ser.isOpen():
        val = ser.readline().decode("UTF-8")
        print(val)
        return str(val)
    else:
        ser.open()
        val = ser.readline().decode("UTF-8")
        print(val)
        return str(val)
def serclose():
    ser.close()