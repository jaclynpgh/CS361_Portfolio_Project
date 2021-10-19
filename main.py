# Author: Jaclyn Sabo
# Date: Fall 2021
# Course: CS361
# Sources: //www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image

LARGE_FONT = ("Calibri", 15)
HEADING = ("Calibri", 18, 'bold')

class MicroTA(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, Pittsburgh, NewYork, Chicago, PittHotels, PittRestaurants, PittMap):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        style = Style()
        heading = tk.Label(self,
            text="Discover.\nPlan.\n Personalize.\n\nYour Micro Travel Agent\n \n\nWhere to?",
            foreground="white",
            background="black",
            font=("Calibri", 20),
            width=40,
            height=30)

        heading.grid(row=0, column=0, columnspan=4, rowspan=2, sticky=tk.W + tk.E)
        style.configure('W.TButton', font=('calibri', 13), foreground='black')
        b1 = Button(self, text="Pittsburgh", style='W.TButton', command=lambda: controller.show_frame(Pittsburgh))
        b2 = Button(self, text="New York", style='W.TButton', command=lambda: controller.show_frame(NewYork))
        b3 = Button(self, text="Chicago", style='W.TButton', command=lambda: controller.show_frame(Chicago))
        b1.grid(row=1, column=0, padx=10, pady=90)
        b2.grid(row=1, column=1, padx=10, pady=90)
        b3.grid(row=1, column=2, padx=15, pady=90)



class Pittsburgh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back",height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, column=0, pady=10,padx=5)

        IMAGE_PATH = 'pgh.png'
        WIDTH, HEIGHT = 500, 700

        # Display image on a Label widget.
        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        lbl = tk.Label(self, image=img)
        lbl.img = img  # Keep a reference in case this code put is in a function.
        lbl.place(relx=0.5, rely=0.5, anchor='center')


        label = tk.Label(self, text="Pittsburgh.\n\nLet's Plan.", font=HEADING)
        label.grid(row=1, column = 2, pady=20)
        style = Style()
        style.configure('W.TButton', font=('calibri', 13), foreground='black')
        b1 = Button(self, text="Hotels", style='W.TButton', command=lambda: controller.show_frame(PittHotels))
        b2 = Button(self, text="Restaurants", style='W.TButton', command=lambda: controller.show_frame(PittRestaurants))
        b3 = Button(self, text="Map", style='W.TButton', command=lambda: controller.show_frame(PittMap))

        b1.grid(row=2, column=1, ipady=10, ipadx=10)
        b2.grid(row=2, column=2, ipady=10, ipadx=10)
        b3.grid(row=2, column=3, ipady=10, ipadx=10)



class PittRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Pittsburgh))
        home.grid(row=0, column=0, pady=10, padx=5)
        label = tk.Label(self, text="Pittsburgh.\n\n Let's Eat.\n", font=HEADING)
        label.grid(row=1, column=2)

        text = tk.Label(self)
        file = open('restaurants.txt', 'r')
        txt = file.read()
        text.config(text=txt, font=LARGE_FONT)
        text.grid(row=2, column=2)
        file.close()


class PittHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Pittsburgh))
        home.grid(row=0, column=0, pady=10, padx=5)
        label = tk.Label(self, text="Pittsburgh.\n\n Stay Awhile.\n", font=HEADING)
        label.grid(row=1, column=2)

        text = tk.Label(self)
        file = open('hotels.txt', 'r')
        txt = file.read()
        text.config(text=txt, font=LARGE_FONT)
        text.grid(row=2, column=2)
        file.close()



class NewYork(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, column=0, pady=10, padx=5)
        label = tk.Label(self, text="Page Two!!!", font=HEADING)
        label.grid(pady=10, padx=10)




class Chicago(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, column=0, pady=10, padx=5)
        label = tk.Label(self, text="Page Three!!!", font=HEADING)
        label.grid(pady=10, padx=10)




class PittMap(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Pittsburgh))
        home.grid(row=0, column=0, pady=10, padx=5)
        label = tk.Label(self, text="Map of Pittsburgh", font=HEADING)
        label.grid(row=1, column=1, pady=10, padx=10)

        self.image = Image.open('map.png')
        resized_image = self.image.resize((500, 305), Image.ANTIALIAS)
        self.python_image = ImageTk.PhotoImage(resized_image)

        ttk.Label(self, image=self.python_image).grid(columnspan=4)


app = MicroTA()
app.mainloop()
