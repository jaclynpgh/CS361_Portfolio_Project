# Author: Jaclyn Sabo
# Date: Fall 2021
# Course: CS361
# Sources: www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
# using image urls: https://python-forum.io/thread-12461.html
# Pandas: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values

import tkinter as tk
from io import BytesIO
from tkinter import *
from tkinter.ttk import *
from pandastable import Table
import pandas as pd
import requests
from PIL import ImageTk, Image, UnidentifiedImageError
from intergrateAPI import get_imageAPI, get_yelp_info, get_weather
from hoteldata import get_hotel_data

LARGE_FONT = ("Calibri", 15)
HEADING = ("Calibri", 24, 'bold')
SUBTITLE = ("Calibri", 20, 'bold')
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
        for F in (StartPage, Pittsburgh, NewYork, Chicago, PittHotels, PittRestaurants, PittWeather, NYHotels,
                  NYRestaurants, NYWeather, ChiHotels, ChiRestaurants, ChiWeather):
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
        # display stock image created via Canva
        image_path = 'photos/MTA.png'
        display_stock_image(self, image_path)

        # Display buttons
        start_buttons(self, controller, "Pittsburgh", Pittsburgh, 0.2)
        start_buttons(self, controller, "New York", NewYork, 0.5)
        start_buttons(self, controller, "Chicago", Chicago, 0.8)


class Pittsburgh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        display_city_page(self, controller, 'photos/pgh.png', "Pittsburgh. Let's Plan.")

        # styling and frame destination for buttons
        city_button_style(self, controller, PittHotels, PittRestaurants, PittWeather)


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

        display_hotel_data(self, controller, "Pittsburgh", Pittsburgh)


class PittWeather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        display_weather_data(self, controller, "Pittsburgh", Pittsburgh)


class NewYork(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        display_city_page(self, controller, 'photos/ny.png', "New York. Let's Plan.")

        # styling and frame destination for buttons
        city_button_style(self, controller, NYHotels, NYRestaurants, NYWeather)


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

        display_hotel_data(self, controller, "New York City", NewYork)


class NYWeather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        display_weather_data(self, controller, "New York City", NewYork)


class Chicago(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        display_city_page(self, controller, 'photos/chi.png', "Chicago. Let's Plan.")
        # styling and frame destination for buttons
        city_button_style(self, controller, ChiHotels, ChiRestaurants, ChiWeather)


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

        display_hotel_data(self, controller, "Chicago", Chicago)


class ChiWeather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        display_weather_data(self, controller, "Chicago", Chicago)


def display_hotel_data(self, controller, city, frame):
    """gets hotel information for Google Places API function and displays it in a table"""

    display_back_button_and_title(self, controller, city + ". Stay Awhile.", frame)

    self.configure(background='black')

    # get hotel data from api
    hotel_data = get_hotel_data(city + " Hotels")
    df = pd.DataFrame(hotel_data, columns=["Hotel", "Rating", "Address"])
    frame = tk.Frame(self)
    frame.pack(fill='both', expand=True, pady=20, padx=10)
    pt = Table(frame, dataframe=df)
    pt.show()


def display_weather_data(self, controller, city, frame):
    """gets weather data from Bailey's microservice and displays it using labels"""

    # Bailey's weather microservice, must be connected to OSU server
    weather = get_weather(city)
    forecast = weather[0]
    current = weather[1]
    temp = weather[2], "F"

    # background image that corresponds to weather using my image microservice API
    try:
        image = get_imageAPI(0, current)
        response = requests.get(image)
        img_data = response.content
        display_weather_image(self, img_data)
    # error handling if no image available, display stock image
    except UnidentifiedImageError:
        image_path = 'photos/weather.png'
        display_stock_image(self, image_path)

    # add back button and title label
    display_back_button_and_title(self, controller, city + " Weather", frame)
    # display labels
    weather_labels(self, forecast, current, temp)


def weather_labels(self, forecast, current, temp):
    """displays weather labels"""

    # display weather data
    create_label(self, "Forecast:", HEADING)
    create_label(self, forecast, SUBTITLE)
    create_label(self, "Current Conditions:", HEADING)
    create_label(self, current, SUBTITLE)
    create_label(self, "Temperature:", HEADING)
    create_label(self, temp, SUBTITLE)


def create_label(self, text, font):
    """creates label"""
    label = tk.Label(self, text=text, font=font)
    label.pack(anchor='center', pady=10)


def display_yelp_data(self, city, state):
    """gets restaurant data from Sam's Yelp microservice and displays it in a table
    """
    restaurant_data = get_yelp_info(city, state)
    df = pd.DataFrame(restaurant_data, columns=["Restaurant", "Rating", "Cost", "Vibe"])
    frame = tk.Frame(self)
    frame.pack(fill='both', expand=True, pady=50)
    pt = Table(frame, dataframe=df)
    pt.show()


def display_stock_image(self, image_path):
    """displays stock image"""
    img = ImageTk.PhotoImage(Image.open(image_path).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
    lbl = tk.Label(self, image=img)
    lbl.img = img
    lbl.place(relx=0.5, rely=0.5, anchor='center')


def display_weather_image(self, image_data):
    """displays the current image from the image microservice"""

    img = ImageTk.PhotoImage(Image.open(BytesIO(image_data)).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
    lbl = tk.Label(self, image=img)
    lbl.img = img
    lbl.place(relx=0.5, rely=0.5, anchor='center')


def display_back_button_and_title(self, controller, text_title, frame_destination):
    """ displays back button and title label using .pack"""
    # back button
    home = tk.Button(self, text="Back", height=1, width=10,
                     command=lambda: controller.show_frame(frame_destination))
    home.pack(side=TOP, pady=5, padx=3, anchor=NW)
    # title label
    label = tk.Label(self, text=text_title, font=HEADING, bg="black", fg="white")
    label.pack(anchor='center', pady=20)


def display_city_page(self, controller, photo, title):
    image_path = photo
    display_stock_image(self, image_path)

    home = tk.Button(self, text="Back", height=1, width=10,
                     command=lambda: controller.show_frame(StartPage))
    home.grid(row=0, pady=10, padx=5)

    label = tk.Label(self, text=title, font=HEADING)
    label.grid(row=1, column=5, pady=50, padx=50)


def start_buttons(self, controller, text, frame, x_position):
    """displays start page buttons"""

    button = tk.Button(self, text=text, height=3, width=10, command=lambda: controller.show_frame(frame))
    button.place(rely=0.5, relx=x_position, anchor="center")


def city_button_style(self, controller, frame_dest1, frame_dest2, frame_dest3):
    """displays info buttons for each city"""
    b1 = Button(self, text="Hotels", command=lambda: controller.show_frame(frame_dest1))
    b2 = Button(self, text="Restaurants", command=lambda: controller.show_frame(frame_dest2))
    b3 = Button(self, text="Weather", command=lambda: controller.show_frame(frame_dest3))
    b1.grid(row=5, column=2, ipady=20, ipadx=10, padx=20, pady=20)
    b2.grid(row=5, column=5, ipady=20, ipadx=10, padx=20, pady=20)
    b3.grid(row=5, column=8, ipady=20, ipadx=10, padx=20, pady=20)


app = MicroTA()
app.mainloop()
