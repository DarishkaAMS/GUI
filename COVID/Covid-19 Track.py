import requests
import bs4

import tkinter as tk


def get_html_data(url):
    data = requests.get(url)
    return data


def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    print(bs)

get_covid_data()