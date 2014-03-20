# Version 1.0 was proudly created by Xinmei Wang (May).

import pyperclip

def cal(r, g, b):
    return r << 16 | g << 8 | b

def rgb(r,g,b,c):  
    c = cal(r,g,b)
    return hex(c)

print("Hello Designer. Welcome to Python \'RGB -> Hexadecimal Value Converter\'")
input_r = int(raw_input("input the integer value of R: "))
input_g = int(raw_input("input the integer value of G: "))
input_b = int(raw_input("input the integer value of B: "))

d = str(rgb(input_r, input_g, input_b, 0))


pyperclip.setcb('#'+d[2:])
clipboard_content = pyperclip.getcb()
print 'the Hexadecimal Value of inputted RGB color is in your clipboard'
print clipboard_content


