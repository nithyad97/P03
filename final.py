from tkinter import *


a = int(input("Enter your value of X1: "))
b = int(input("Enter your value of Y1: "))

c = int(input("Enter your value of X2: "))
d = int(input("Enter your value of Y2: "))

g = int(input("Enter your value of X3: "))
h = int(input("Enter your value of Y3: "))

e = int(input("Enter your value of X4: "))
f = int(input("Enter your value of Y4: "))



my_window = Tk()
my_canvas = Canvas(my_window,width=400,height=400,background='white')
my_canvas.grid(row=0,column=0)
my_canvas.create_line(a,b,c+50,d,width=5)
my_canvas.create_line(c+50,d,e+50,f,width=5)
my_canvas.create_line(e+50,f,g,h,width=5)
my_canvas.create_line(g,h,a,b,width=5)
#my_window.mainloop()

my_canvas.grid(row=0,column=0)
my_canvas.create_line(a+75,b+50,c-25,d+50,width=4)
my_canvas.create_line(c-25,d+50,e-25,f-50,width=4)
my_canvas.create_line(e-25,f-50,g+75,h-50,width=4)
my_canvas.create_line(g+75,h-50,a+75,b+50,width=4)
my_window.mainloop()


