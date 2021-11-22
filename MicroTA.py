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
from PIL import ImageTk, Image
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
        b1 = tk.Button(self, text="Pittsburgh", height=3, width=10, command=lambda: controller.show_frame(Pittsburgh))
        b2 = tk.Button(self, text="New York", height=3, width=10, command=lambda: controller.show_frame(NewYork))
        b3 = tk.Button(self, text="Chicago", height=3, width=10, command=lambda: controller.show_frame(Chicago))
        b1.place(rely=0.5, relx=0.2, anchor="center")
        b2.place(rely=0.5, relx=0.5, anchor="center")
        b3.place(rely=0.5, relx=0.8, anchor="center")


class Pittsburgh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image_path = 'photos/pgh.png'
        display_stock_image(self, image_path)

        # back button
        home = tk.Button(self, text="Back", height=1, width=10, command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, pady=10, padx=5)
        # title label
        label = tk.Label(self, text="Pittsburgh. Let's Plan.", font=HEADING)
        label.grid(row=1, column=5, pady=50, padx=50)

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

        # add back button and label
        display_back_button_and_title(self, controller, "Pittsburgh. Stay Awhile.", Pittsburgh)
        self.configure(background='black')

        hotel_data = get_hotel_data("Pittsburgh Hotels")
        df = pd.DataFrame(hotel_data, columns=["Hotel", "Rating", "Address"])
        frame = tk.Frame(self)
        frame.pack(fill='both', expand=True, pady=20, padx=10)
        pt = Table(frame, dataframe=df)
        pt.show()


class PittWeather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Bailey's weather microservice
        weather = get_weather("Pittsburgh")

        forecast = weather[0]
        current = weather[1]
        temp = weather[2], "F"

        # error protection, if no photo find, set background
        try:
            # background image using my image microservice API
            image = get_imageAPI(0, current)
            response = requests.get(image)
            img_data = response.content
            display_weather_image(self, img_data)
        # error handling if no image is found
        except:
            pass
        finally:
            self.configure(background='blue')

        # add back button and label
        display_back_button_and_title(self, controller, "Pittsburgh Weather", Pittsburgh)
        # display weather data
        label1 = tk.Label(self, text="Forecast:", font=HEADING)
        label1.pack(anchor='center', pady=10)
        label1 = tk.Label(self, text=forecast, font=SUBTITLE)
        label1.pack(anchor='center', pady=10)
        label2 = tk.Label(self, text="Current Conditions:", font=HEADING)
        label2.pack(anchor='center', pady=10)
        label2 = tk.Label(self, text=current, font=SUBTITLE)
        label2.pack(anchor='center', pady=10)
        label3 = tk.Label(self, text="Temperature:", font=HEADING)
        label3.pack(anchor='center', pady=10)
        label3 = tk.Label(self, text=temp, font=SUBTITLE)
        label3.pack(anchor='center', pady=10)


class NewYork(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image_path = 'photos/ny.png'
        display_stock_image(self, image_path)

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, pady=10, padx=5)

        label = tk.Label(self, text="New York. Let's Plan.", font=HEADING)
        label.grid(row=1, column=5, pady=50, padx=50)
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

        # add back button and label
        display_back_button_and_title(self, controller, "New York City. Stay Awhile.", NewYork)

        self.configure(background='black')

        hotel_data = get_hotel_data("New York City Hotels")
        df = pd.DataFrame(hotel_data, columns=["Hotel", "Rating", "Address"])
        frame = tk.Frame(self)
        frame.pack(fill='both', expand=True, pady=20, padx=10)
        pt = Table(frame, dataframe=df)
        pt.show()


class NYWeather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Bailey's weather microservice
        # weather_data = [forecast, current, temp_f]
        weather = get_weather("New York City")

        forecast = weather[0]
        current = weather[1]
        temp = weather[2], "F"
        try:
            # background image using my image microservice API
            image = get_imageAPI(0, current)
            response = requests.get(image)
            img_data = response.content
            display_weather_image(img_data)
        # error handling if no image is found
        except:
            pass
        finally:
            self.configure(background="blue")

        # add back button and label
        display_back_button_and_title(self, controller, "New York City Weather", NewYork)

        # display weather data
        label1 = tk.Label(self, text="Forecast:", font=HEADING)
        label1.pack(anchor='center', pady=10)
        label1 = tk.Label(self, text=forecast, font=SUBTITLE)
        label1.pack(anchor='center', pady=10)
        label2 = tk.Label(self, text="Current Conditions:", font=HEADING)
        label2.pack(anchor='center', pady=10)
        label2 = tk.Label(self, text=current, font=SUBTITLE)
        label2.pack(anchor='center', pady=10)
        label3 = tk.Label(self, text="Temperature:", font=HEADING)
        label3.pack(anchor='center', pady=10)
        label3 = tk.Label(self, text=temp, font=SUBTITLE)
        label3.pack(anchor='center', pady=10)


class Chicago(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image_path = 'photos/chi.png'
        display_stock_image(self, image_path)

        home = tk.Button(self, text="Back", height=1, width=10,
                         command=lambda: controller.show_frame(StartPage))
        home.grid(row=0, pady=10, padx=5)

        label = tk.Label(self, text="Chicago. Let's Plan.", font=HEADING)
        label.grid(row=1, column=5, pady=50, padx=50)

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

        # add back button and label
        display_back_button_and_title(self, controller, "Chicago. Stay Awhile.", Chicago)

        self.configure(background='black')

        hotel_data = get_hotel_data("Chicago Hotels")
        df = pd.DataFrame(hotel_data, columns=["Hotel", "Rating", "Address"])
        frame = tk.Frame(self)
        frame.pack(fill='both', expand=True, pady=20, padx=10)
        pt = Table(frame, dataframe=df)
        pt.show()


class ChiWeather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Bailey's weather microservice, must be connected to OSU server
        # weather_data = [forecast, current, temp_f]
        weather = get_weather("Chicago")
        forecast = weather[0]
        current = weather[1]
        temp = weather[2], "F"

        try:
            # background image using my image microservice API
            image = get_imageAPI(0, current)
            response = requests.get(image)
            img_data = response.content
            display_weather_image(self, img_data)

        # error handling if no image is found
        except:
            pass
        finally:
            self.configure(background="blue")

        # add back button and label
        display_back_button_and_title(self, controller, "Chicago Weather", Chicago)

        # display weather data
        label1 = tk.Label(self, text="Forecast:", font=HEADING)
        label1.pack(anchor='center', pady=10)
        label1 = tk.Label(self, text=forecast, font=SUBTITLE)
        label1.pack(anchor='center', pady=10)
        label2 = tk.Label(self, text="Current Conditions:", font=HEADING)
        label2.pack(anchor='center', pady=10)
        label2 = tk.Label(self, text=current, font=SUBTITLE)
        label2.pack(anchor='center', pady=10)
        label3 = tk.Label(self, text="Temperature:", font=HEADING)
        label3.pack(anchor='center', pady=10)
        label3 = tk.Label(self, text=temp, font=SUBTITLE)
        label3.pack(anchor='center', pady=10)


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
    """ displays back button and title label"""
    # back button
    home = tk.Button(self, text="Back", height=1, width=10,
                     command=lambda: controller.show_frame(frame_destination))
    home.pack(side=TOP, pady=5, padx=3, anchor=NW)
    # title label
    label = tk.Label(self, text=text_title, font=HEADING, bg="black", fg="white")
    label.pack(anchor='center', pady=20)


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
