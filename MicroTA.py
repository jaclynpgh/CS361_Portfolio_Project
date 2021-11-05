# Author: Jaclyn Sabo
# Date: Fall 2021
# Course: CS361
# Sources: www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
# using image urls: https://python-forum.io/thread-12461.html

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from intergrateAPI import get_imageAPI
from io import BytesIO
import os
import requests



LARGE_FONT = ("Calibri", 15)
HEADING = ("Calibri", 18, 'bold')
WIDTH, HEIGHT = 456, 650

imageAPI_url = 'https://jaclynsimagescraper.herokuapp.com/'


class MicroTA(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.winfo_toplevel().title("Micro Travel Agent")
        self.geometry("455x650+700+200")
        self.resizable(0, 0)


        container = tk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor='center')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, Pittsburgh, NewYork, Chicago, PittHotels, PittRestaurants, PittMap, NYHotels,
                  NYRestaurants, NYMap, ChiHotels, ChiRestaurants, ChiMap):
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

        IMAGE_PATH = 'MTA.png'
        # Display image on a Label widget.
        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        lbl = tk.Label(self, image=img)
        lbl.img = img  # Keep a reference in case this code put is in a function.
        lbl.place(relx=0.5, rely=0.5, anchor='center')


        b1 = tk.Button(self, text="Pittsburgh", height=3, width=10, command=lambda: controller.show_frame(Pittsburgh))
        b2 = tk.Button(self, text="New York", height=3, width=10,command=lambda: controller.show_frame(NewYork))
        b3 = tk.Button(self, text="Chicago",height=3, width=10,  command=lambda: controller.show_frame(Chicago))
        b1.place(rely=0.6, relx=0.2, anchor="center")
        b2.place(rely=0.6, relx=0.5, anchor="center")
        b3.place(rely=0.6, relx=0.8, anchor="center")



class Pittsburgh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image using my image microservice API
        image = get_imageAPI(2, "Pittsburgh Skyline")
        response = requests.get(image)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((WIDTH, HEIGHT), Image.ANTIALIAS))

        # Display image on a Label widget.
        lbl = tk.Label(self, image=img)
        lbl.img = img
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, pady=10, padx=5)

        label = tk.Label(self, text="Pittsburgh.\nLet's Plan.", font=HEADING)
        label.grid(row=1, column = 1, pady=20)
        style = Style()
        b1 = Button(self, text="Hotels",  command=lambda: controller.show_frame(PittHotels))
        b2 = Button(self, text="Restaurants",  command=lambda: controller.show_frame(PittRestaurants))
        b3 = Button(self, text="Map", command=lambda: controller.show_frame(PittMap))

        b1.grid(row=2, column=0, ipady=10, ipadx=10, padx=20)
        b2.grid(row=2, column=1, ipady=10, ipadx=10, padx=20)
        b3.grid(row=2, column=2, ipady=10, ipadx=10, padx=20)




class PittRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Pittsburgh))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)


        label = tk.Label(self, text="Pittsburgh. Let's Eat.\n", font=HEADING)
        label.pack()

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(self)
        listbox.config(width=40, height=200)
        listbox.pack(fill=Y)
        file = open('restaurants.txt', 'r').readlines()
        for i in file:
            listbox.insert(END, i)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)


class PittHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Pittsburgh))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)

        label = tk.Label(self, text="Pittsburgh. Stay Awhile.\n", font=HEADING)
        label.pack(anchor='center')

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(self)
        listbox.config(width=40, height=200)
        listbox.pack(fill=Y)
        file = open('hotels.txt', 'r').readlines()
        for i in file:
            listbox.insert(END, i)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

class PittMap(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Pittsburgh))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)
        label = tk.Label(self, text="Map of Pittsburgh", font=HEADING)
        label.pack(anchor='center')

        self.image = Image.open('testPhotos/map.png')
        resized_image = self.image.resize((400, 305), Image.ANTIALIAS)
        self.python_image = ImageTk.PhotoImage(resized_image)

        ttk.Label(self, image=self.python_image).pack(fill=Y)



class NewYork(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image using my image microservice API
        image = get_imageAPI(2, "New York Skyline")
        response = requests.get(image)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((WIDTH, HEIGHT), Image.ANTIALIAS))

        # Display image on a Label widget.
        lbl = tk.Label(self, image=img)
        lbl.img = img
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, pady=10, padx=5)

        label = tk.Label(self, text="New York.\nLet's Plan.", font=HEADING)
        label.grid(row=1, column=1, pady=20)
        style = Style()
        b1 = Button(self, text="Hotels", command=lambda: controller.show_frame(NYHotels))
        b2 = Button(self, text="Restaurants", command=lambda: controller.show_frame(NYRestaurants))
        b3 = Button(self, text="Map", command=lambda: controller.show_frame(NYMap))

        b1.grid(row=2, column=0, ipady=10, ipadx=10, padx=20)
        b2.grid(row=2, column=1, ipady=10, ipadx=10, padx=20)
        b3.grid(row=2, column=2, ipady=10, ipadx=10, padx=20)

class NYRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(NewYork))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)


        label = tk.Label(self, text="New York City. Let's Eat.\n", font=HEADING)
        label.pack()

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(self)
        listbox.config(width=40, height=200)
        listbox.pack(fill=Y)
        file = open('restaurants.txt', 'r').readlines()
        for i in file:
            listbox.insert(END, i)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

class NYHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(NewYork))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)

        label = tk.Label(self, text="New York City. Stay Awhile.\n", font=HEADING)
        label.pack(anchor='center')

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(self)
        listbox.config(width=40, height=200)
        listbox.pack(fill=Y)
        file = open('hotels.txt', 'r').readlines()
        for i in file:
            listbox.insert(END, i)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

class NYMap(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(NewYork))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)
        label = tk.Label(self, text="Map of New York City", font=HEADING)
        label.pack(anchor='center')

        self.image = Image.open('testPhotos/map.png')
        resized_image = self.image.resize((400, 305), Image.ANTIALIAS)
        self.python_image = ImageTk.PhotoImage(resized_image)

        ttk.Label(self, image=self.python_image).pack(fill=Y)

class Chicago(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # background image using my image microservice API
        image = get_imageAPI(2, "Chicago City Skyline")
        response = requests.get(image)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        lbl = tk.Label(self, image=img)
        lbl.img = img
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, pady=10, padx=5)

        label = tk.Label(self, text="Chicago.\nLet's Plan.", font=HEADING)
        label.grid(row=1, column=1, pady=20)
        style = Style()
        b1 = Button(self, text="Hotels", command=lambda: controller.show_frame(ChiHotels))
        b2 = Button(self, text="Restaurants", command=lambda: controller.show_frame(ChiRestaurants))
        b3 = Button(self, text="Map", command=lambda: controller.show_frame(ChiMap))

        b1.grid(row=2, column=0, ipady=10, ipadx=10, padx=20)
        b2.grid(row=2, column=1, ipady=10, ipadx=10, padx=20)
        b3.grid(row=2, column=2, ipady=10, ipadx=10, padx=20)

class ChiRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Chicago))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)


        label = tk.Label(self, text="Chicago. Let's Eat.\n", font=HEADING)
        label.pack()

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(self)
        listbox.config(width=40, height=200)
        listbox.pack(fill=Y)
        file = open('restaurants.txt', 'r').readlines()
        for i in file:
            listbox.insert(END, i)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

class ChiHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Chicago))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)

        label = tk.Label(self, text="Chicago. Stay Awhile.\n", font=HEADING)
        label.pack(anchor='center')

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(self)
        listbox.config(width=40, height=200)
        listbox.pack(fill=Y)
        file = open('hotels.txt', 'r').readlines()
        for i in file:
            listbox.insert(END, i)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

class ChiMap(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(Chicago))
        home.pack(side=TOP, pady=5, padx=3, anchor=NW)
        label = tk.Label(self, text="Map of Chicago", font=HEADING)
        label.pack(anchor='center')

        self.image = Image.open('testPhotos/map.png')
        resized_image = self.image.resize((400, 305), Image.ANTIALIAS)
        self.python_image = ImageTk.PhotoImage(resized_image)

        ttk.Label(self, image=self.python_image).pack(fill=Y)



app = MicroTA()
app.mainloop()
