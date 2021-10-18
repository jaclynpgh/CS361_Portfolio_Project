import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


LARGE_FONT = ("Calibri", 15)


class MicroTA(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, height='350', width ='150')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        container.pack()


        self.frames = {}

        for F in (StartPage, Pittsburgh, NewYork, Chicago, PittHotels, PittRestaurants):
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
        home = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, column=0)

        label = tk.Label(self, text="Let's Plan.", font=LARGE_FONT)
        label.grid(row=1, column = 1, pady=10)
        style = Style()
        style.configure('W.TButton', font=('calibri', 13), foreground='black')
        b1 = Button(self, text="Hotels", style='W.TButton', command=lambda: controller.show_frame(PittHotels))
        b2 = Button(self, text="Restaurants", style='W.TButton', command=lambda: controller.show_frame(PittRestaurants))
        b1.grid(row=2, column=0, padx=50)
        b2.grid(row=2, column=2, padx=50)



class PittRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame(Pittsburgh))
        home.grid(row=2, column=1, pady=20)
        label = tk.Label(self, text="Pittsburgh\n Let's Eat.", font=LARGE_FONT)
        label.grid(column = 1, pady=10)

        file = open('restaurants.txt', 'r')
        txt = file.read()
        label.config(text=txt, font=LARGE_FONT)
        file.close()



class PittHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home = tk.Button(self, text="Back",
                         command=lambda: controller.show_frame(Pittsburgh))
        home.grid(row=0, column=0)
        label = tk.Label(self, text="Pittsburgh\n Stay Awhile.", font=LARGE_FONT)
        label.grid(row=1, column=2, pady=10)

        text = tk.Label(self)
        file = open('hotels.txt', 'r')
        txt = file.read()
        text.config(text=txt, font=LARGE_FONT)
        text.grid(row=2, column=1)
        file.close()

        ## OPEN IMAGE, FIGURE OUT





class NewYork(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class Chicago(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



app = MicroTA()
app.mainloop()
