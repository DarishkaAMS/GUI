import requests
import bs4

import tkinter as tk

def get_html_data(url):
    data = requests.get(url)
    return data