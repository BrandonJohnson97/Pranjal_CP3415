import requests
import tkinter as tk
from tkinter import ttk


def get_all_weather_data(city):
    """
    Helper function. Makes a request to openweathermap server.
    :param city:
    :return: Returns entire current weather for the city.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "d60e040effd14361b648c6591d82cb18"  # https://home.openweathermap.org/api_keys
    url = f'{base_url}q={city}&appid={api_key}'
    resp = requests.get(url)
    return resp.json()


def get_current_temp(city):
    """
    Grabs the temp data use kelvin to celcius formula to convert to celcius
    :param city: User input
    :return: The temperature
    """
    # return temp in Celsius
    data = get_all_weather_data(city)
    temp = data['main']['temp']
    current_temp = round(temp - 273.15)
    return (current_temp)


def get_feels_like_temp(city):
    """
    Use get weather data to grab the feels like data and subtract to convert to celcius
    :param city: User input
    :return: feels like data in celcius
    """
    # return feels like temperature in Celsius
    data = get_all_weather_data(city)
    feels_like_data = data["main"]["feels_like"]
    feels_like = round(feels_like_data - 273.15)
    return (feels_like)


def get_summary(city):
    """
    Use get weather data to get the data of the weather description
    :param city: User input
    :return: the weather description summary
    """
    # Return weather summary wasn't sure if it was Main or Description so chose Description
    data = get_all_weather_data(city)
    weather = ""
    summary = data["weather"][0]["description"]
    return (summary)


def niceness_scale():
    """
    Get the weather data to get the summary and weather ID so I can create a scale
    :return: The print statement that goes into the button clicked later on
    """
    # Grabs the city thats user inputted
    city = string_enter_city.get()
    data = get_all_weather_data(city)
    weather_id = data["weather"][0]["id"]
    summary = get_summary(city)
    # weather is a empty string to make it returnable
    # using if "" in : so it can check through the word and see if the string is inside it
    weather = ""
    if "clouds" in summary:
        weather = "Clouds? Again? 7/10"
    elif "clear" in summary:
        weather = "Wow, I can see the sky! 10/10"
    elif "rain" in summary:
        weather = "At least it isn't snow. 3/10"
    elif "snow" in summary:
        weather = "Snow? Seriously? 2/10"
    elif weather_id == 711 or 721 or 731 or 751 or 761 or 762 or 771 or 781:
        weather = "This doesn't look good, get inside! 1/10"
    elif "thunder" in summary:
        weather = "Might be a little loud. Thunders no joke. 5/10"
    elif weather_id == 741:
        weather = "I can't see very well, fog sucks! 4/10"
    elif weather_id == 701:
        weather = "A little mist isn't too bad 6/10"
    return weather


def get_wind_speed(city):
    """
    Using get weather data to get the wind speed
    :param city: User input
    :return: The windspeed in Metres per second
    """
    data = get_all_weather_data(city)
    wind_speed = data["wind"]["speed"]
    return wind_speed


def get_wind_gust(city):
    """
    Using get weather data to get the wind gust
    :param city: User input
    :return: The wind gust in Metres per second
    """
    data = get_all_weather_data(city)
    wind_gust = data["wind"]["gust"]
    return wind_gust


def get_all_weather_functions():
    """
    When the button is clicked in the GUI all of these buttons set whatever
    is returned inside each function
    :return: None
    """
    city = string_enter_city.get()
    string_temp.set(f"{get_current_temp(city)} °C")
    string_feels_like.set(f"{get_feels_like_temp(city)} °C")
    string_summary.set(get_summary(city))
    string_wind_speeds.set(f"{get_wind_speed(city)} M/Sec")
    string_wind_gust.set(f"{get_wind_gust(city)} M/Sec")



# Create root window
root = tk.Tk()
root.title("My Weather App :)")
root.geometry("300x200")

# Create main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

# Create your labels
ttk.Label(frame_home, text="Enter City:").grid(column=0, row=0)
ttk.Label(frame_home, text="Current Temp:").grid(column=0, row=2)
ttk.Label(frame_home, text="Feels Like Temp:").grid(column=0, row=3)
ttk.Label(frame_home, text="Summary:").grid(column=0, row=4)
ttk.Label(frame_home, text="Wind Speeds").grid(column=0, row=5)
ttk.Label(frame_home, text="Wind Gust").grid(column=0, row=6)
ttk.Label(frame_home, text="Niceness Score").grid(column=1, row=7)

# Create entry boxes
string_enter_city = tk.StringVar()
string_enter_city.set("")
ttk.Entry(frame_home, width=30, textvariable=string_enter_city).grid(column=1, row=0)
string_temp = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_temp).grid(column=1, row=2)
string_feels_like = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_feels_like).grid(column=1, row=3)
string_summary = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_summary).grid(column=1, row=4)
string_wind_speeds = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_wind_speeds).grid(column=1, row=5)
string_wind_gust = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_wind_gust).grid(column=1, row=6)
string_nicness_score = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_nicness_score).grid(column=1, row=8)

# Create Get Weather button
ttk.Button(frame_home, text="Get Weather", command=get_all_weather_functions).grid(column=1, row=1)

root.mainloop()
