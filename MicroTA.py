# Author: Jaclyn Sabo
# Date: Fall 2021
# Course: CS361
# Sources: www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
# using image urls: https://python-forum.io/thread-12461.html
# Pandas: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values

import tkinter as tk
from io import BytesIO
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from pandastable import Table
import pandas as pd
import requests
from PIL import ImageTk, Image

from intergrateAPI import get_imageAPI, get_yelp_info

LARGE_FONT = ("Calibri", 15)
HEADING = ("Calibri", 20, 'bold')
WIDTH, HEIGHT = 850, 550


class MicroTA(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # create window frame
        self.winfo_toplevel().title("Micro Travel Agent")
        self.geometry("850x550+300+150")
        self.resizable(0, 0)

        container = tk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor='center')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # iterates through UI as user navigates
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
        # stock image created via Canva
        image_path = 'MTA.png'
        # Display image on a Label widget.
        img = ImageTk.PhotoImage(Image.open(image_path).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        lbl = tk.Label(self, image=img)
        lbl.img = img
        lbl.place(relx=0.5, rely=0.5, anchor='center')
        # Display buttons
        b1 = tk.Button(self, text="Pittsburgh", height=3, width=10, command=lambda: controller.show_frame(Pittsburgh))
        b2 = tk.Button(self, text="New York", height=3, width=10, command=lambda: controller.show_frame(NewYork))
        b3 = tk.Button(self, text="Chicago", height=3, width=10, command=lambda: controller.show_frame(Chicago))
        b1.place(rely=0.5, relx=0.2, anchor="center")
        b2.place(rely=0.5, relx=0.5, anchor="center")
        b3.place(rely=0.5, relx=0.8, anchor="center")


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

        # back button
        home = tk.Button(self, text="Back", height=1, width=10, command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, pady=10, padx=5)
        # title label
        label = tk.Label(self, text="Pittsburgh. Let's Plan.", font=HEADING)
        label.grid(row=1, column=5, pady=50, padx=50)

        # styling and frame destination for buttons
        city_button_style(self, controller, PittHotels, PittRestaurants, PittMap)


class PittRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # add back button and label
        display_back_button_and_title(self, controller, "Pittsburgh. Let's Eat.", Pittsburgh)

        self.configure(background='black')

        # display data from Sam's Yelp microservice
        display_yelp_data(self, "Pittsburgh", "PA")


class PittHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # add back button and label
        display_back_button_and_title(self, controller, "Pittsburgh. Stay Awhile.", Pittsburgh)

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

        # add back button and label
        display_back_button_and_title(self, controller, "Map of Pittsburgh", Pittsburgh)

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

        label = tk.Label(self, text="New York. Let's Plan.", font=HEADING)
        label.grid(row=1, column=5, pady=50, padx=50)
        # styling and frame destination for buttons
        city_button_style(self, controller, NYHotels, NYRestaurants, NYMap)


class NYRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background='black')

        # add back button and label
        display_back_button_and_title(self, controller, "New York City. Let's Eat.", NewYork)

        # display data from Sam's Yelp microservice
        display_yelp_data(self, "New York", "NY")


class NYHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # add back button and label
        display_back_button_and_title(self, controller, "New York City. Stay Awhile.", NewYork)

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

        # add back button and label
        display_back_button_and_title(self, controller, "Map of New York", NewYork)

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

        label = tk.Label(self, text="Chicago. Let's Plan.", font=HEADING)
        label.grid(row=1, column=5, pady=50, padx=50)

        # styling and frame destination for buttons
        city_button_style(self, controller, ChiHotels, ChiRestaurants, ChiMap)


class ChiRestaurants(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background='black')

        # add back button and label
        display_back_button_and_title(self, controller, "Chicago. Let's Eat.", Chicago)

        # display data from Sam's Yelp microservice
        display_yelp_data(self, "Chicago", "IL")


class ChiHotels(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # add back button and label
        display_back_button_and_title(self, controller, "Chicago. Stay Awhile.", Chicago)

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

        # add back button and label
        display_back_button_and_title(self, controller, "Map of Chicago", Chicago)

        self.image = Image.open('testPhotos/map.png')
        resized_image = self.image.resize((400, 305), Image.ANTIALIAS)
        self.python_image = ImageTk.PhotoImage(resized_image)

        ttk.Label(self, image=self.python_image).pack(fill=Y)


def display_yelp_data(instance, city, state):
    """gets restaurant data from Sam's Yelp microservice and displays it in a table"""
    restaurant_data = get_yelp_info(city, state)
    df = pd.DataFrame(restaurant_data, columns=["Restaurant", "Rating", "Cost", "Vibe"])
    frame = tk.Frame(instance)
    frame.pack(fill='both', expand=True, pady=50)
    pt = Table(frame, dataframe=df)
    pt.show()


def display_back_button_and_title(instance, controller, text_title, frame_destination):
    """ displays back button and title label
       :param instance: declare an instance of the class such as self
       :param controller: class controller
       :param text_title: title text to put on label
       :param frame_destination: class destination when back button is pushed"""
    # back button
    home = tk.Button(instance, text="Back", height=1, width=10,
                     command=lambda: controller.show_frame(frame_destination))
    home.pack(side=TOP, pady=5, padx=3, anchor=NW)
    # label
    label = tk.Label(instance, text=text_title, font=HEADING, bg="black", fg="white")
    label.pack(anchor='center')


def city_button_style(instance, controller, frame_dest1, framedest2, framedest3):
    b1 = Button(instance, text="Hotels", command=lambda: controller.show_frame(frame_dest1))
    b2 = Button(instance, text="Restaurants", command=lambda: controller.show_frame(framedest2))
    b3 = Button(instance, text="Map", command=lambda: controller.show_frame(framedest3))
    b1.grid(row=5, column=2, ipady=20, ipadx=10, padx=20, pady=20)
    b2.grid(row=5, column=5, ipady=20, ipadx=10, padx=20, pady=20)
    b3.grid(row=5, column=8, ipady=20, ipadx=10, padx=20, pady=20)


app = MicroTA()
app.mainloop()
