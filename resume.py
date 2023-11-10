from distutils import command
from tkinter import *
from tkinter import ttk

pg1 = Tk()
pg1.configure(background="blue")
pg1.title("my CV")
style = ttk.Style()
print(style.theme_names())
style.theme_use('alt')
pg1.maxsize(400, 400)
pg1.minsize(300, 250)
bu1 = ttk.Button(pg1, text = "my name")
bu1.grid(row = 2, column = 3, ipadx=114)
style.configure('bu1.TButton', background = "white", foreground = "black", font = ('atalic',10, 'bold'))
bu1.configure(style='bu1.TButton')
bu2 = ttk.Button(pg1, text = "what is the sport that i like the most")
bu2.grid(row = 3, column = 3, ipadx=40)
style.configure('bu2.TButton', background = "white", foreground = "black", font = ('atalic',10, 'bold'))
bu2.configure(style='bu2.TButton')
bu3 = ttk.Button(pg1, text = "how old am i")
bu3.grid(row = 4, column = 3, ipadx=111)
style.configure('bu3.TButton', background = "white", foreground = "black", font = ('atalic',10, 'bold'))
bu3.configure(style='bu3.TButton')
bu4 = ttk.Button(pg1, text = "which school do i go to")
bu4.grid(row = 5, column = 3, ipadx = 79)
style.configure('bu4.TButton', background = "white", foreground = "black", font = ('atalic',10, 'bold'))
bu4.configure(style='bu4.TButton')
l8 = ttk.Label(pg1, text = "BY : AISHA", background="blue", foreground="black", font = ('Arial', 20, 'bold'))
l8.grid(columnspan=6, row= 6)
bu5 = ttk.Button(pg1, text = "1")
bu5.grid(row = 7, column = 3, ipadx = 79)
style.configure('bu5.TButton', background = "blue", foreground = "blue")
bu5.configure(style='bu5.TButton')

im1 = PhotoImage(file = "WhatsApp Image 2022-10-27 at 11.03.12 AM (1).png")
im1_res = im1.subsample(4, 4)
im2 = PhotoImage(file = "basketball.png")
im2_res = im2.subsample(3, 3)
im3 = PhotoImage(file = "WhatsApp Image 2022-10-27 at 11.39.58 AM.png")
im3_res = im3.subsample(3, 3)
im4 = PhotoImage(file = "Happyface.png.png")
im4_res = im4.subsample(3, 3)

def bu1_click():
    pg2 = Toplevel(pg1)
    l1 = ttk.Label(pg2, image = im1_res)
    l1.pack()
    l2 = ttk.Label(pg2, text = "MY NAME IS AISHA ISMAIL OKASHA")
    l2.pack()
    pg2.mainloop()
bu1.config(command=bu1_click)
def bu2_click():
    pg3 = Toplevel(pg1)
    l3 = ttk.Label(pg3, image = im2_res)
    l3.pack()
    l4 = ttk.Label(pg3, text = "I LOVE BASKETBALL, IT IS MY FAVOURITE SPORT")
    l4.pack()
    pg3.mainloop()
bu2.config(command=bu2_click)
def bu3_click():
    pg4 = Toplevel(pg1)
    l5 = ttk.Label(pg4, text="I AM 16 YEARS OLD")
    l5.pack()
    pg4.mainloop()
bu3.config(command = bu3_click)

def bu4_click():
    pg5 = Toplevel(pg1)
    l6 = ttk.Label(pg5, image = im3_res)
    l6.pack()
    l7 = ttk.Label(pg5, text = "I GO TO SOROUR LANGUAGE SCHOOL")
    l7.pack()
    pg5.mainloop()
bu4.config(command =bu4_click)

bu5.config(image=im4_res)






pg1.mainloop()