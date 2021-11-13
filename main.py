import requests
import bs4

import tkinter as tk

def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    soup = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = soup.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_=None).get_text()

        total_cases = block.find("span", class_=None).get_text()

        all_data = all_data + text + " " + total_cases + "\n"

    return all_data

def reload():
    new_data = get_covid_data()
    mainlabel['text'] = new_data

def get_country_data():
    name = search.get()
    url = "https://www.worldometers.info/coronavirus/country"+name
    html_data = get_html_data(url)
    soup = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = soup.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

    for block in info_div:
        text = block.find("h1", class_=None).get_text()

        total_cases = block.find("span", class_=None).get_text()

        all_data = all_data + text + " " + total_cases + "\n"

    mainlabel['text'] = all_data

get_covid_data()


root = tk.Tk()
root.geometry("900x700")
root.title("Covid-19 Cases Report")
f = ("arial", 18, "bold")

icon = tk.PhotoImage(file="resources/covid_banner.png")
ilabel = tk.Label(root, image=icon)
ilabel.pack()

mainlabel = tk.Label(root, text=get_covid_data(), font=f)
mainlabel.pack()

search = tk.Entry(root, width=50)
search.pack()

get_button = tk.Button(root, text="Get New Data", font=f, relief="solid", command=get_country_data)
get_button.pack()

reload_button = tk.Button(root, text="Refresh Data", font=f, relief="solid", command=reload)
reload_button.pack()

root.iconbitmap('resources/covid_icon.ico')
root.mainloop()

root.mainloop()