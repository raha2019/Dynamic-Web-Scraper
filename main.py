import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = ""
list_of_names = [""]

# list_of_urls = [""]

def strip_Elements():
    print("this will be used in both functions")


def compare_Elements(base_url, list_of_names, div_element, element_name):
    overall_list = []
    for name in list_of_names:
        entry = []
        url = base_url + name
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html-parser")
        element = soup.find(div_element.get_text().strip())

        entry.append(element)
        overall_list.append(entry)
    df = pd.DataFrame(overall_list, columns=[element_name])
    df.to_csv("compare.csv", sep=',', index=False, encoding='utf-8')

def monitor_Elements(url, seconds_interval, div_element):
    while True:
        entry = []
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html-parser")
        element = soup.find(div_element.get_text().strip())
        print(element)
        entry.append(element)
        


        time.sleep(seconds_interval)


