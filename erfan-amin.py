import serial
import getch
serialport = serial.Serial ("/dev/ttyS0")
serialport.baudrate = 115200
while(True):
    x = getch.getch()
    if x.isupper():
        x = x.lower()
    # type your code here
    print(type(x))
    print(x)
    if x == 'w':
        command = '+100+10015+00'
    elif x == 's':
        command = '-100-10015+00'
    elif x == 'd':
        command = '+100-10015+00'
    elif x == 'a':
        command = '-100+10015+00'
    elif x == 'e':
        command = '+100+02015+00'
    elif x == 'q':
        command = '+020+10015+00'
    elif x == 'b':
        break
    else:
        command = '+000+00015+00'
    serialport.write(command.encode())
