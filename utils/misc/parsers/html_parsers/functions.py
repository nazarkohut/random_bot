"""Write useful methods for html parsers here"""
import requests
from bs4 import BeautifulSoup


def get_content(url):
    req = requests.get(url)
    content = req.text
    content = BeautifulSoup(content, 'html.parser')
    return content
