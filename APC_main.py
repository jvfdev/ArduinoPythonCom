import serial
from Tkinter import *

ser = serial.Serial('/dev/ttyACM0',9600)


window = Tk()
window.title("APC_GUI")
window.geometry('350x200')

lbl = Label(window, text="Use this tool to turn the Arduino ON or OFF", font=("arial",12,"bold"))

lbl.grid(column=0, row=0,columnspan=2)

def clicked1():
    ser.write('0')


def clicked2():
    ser.write('1')


rad1 = Radiobutton(window,text='OFF', value=1, command=clicked1)
rad2 = Radiobutton(window,text='ON', value=2, command=clicked2)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)




window.mainloop()
