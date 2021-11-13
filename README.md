# Covid-19 Worldwide Cases Report

![Picture of the Covid-19 Tracker](https://i.imgur.com/VSVnRZv.png)

## Description

This project presents cases of the covid-19 pandemic organized in three categories: Total Cases, Recovered, and Deaths. 

By default, the application shows the number of cases worldwide, however, the user can type the name of any country in the search bar and then click "Get New Data" for the application to display only the stats of that specific country. 

Lastly, by clicking "Refresh Data" the application displays updated data (given that the data source has been updated). The data is scraped from the website [worldometer](https://www.worldometers.info/coronavirus/).

## How it works

It was created with Python and uses the library "requests" to extract the HTML date and "Beautiful Soup 4 (bs4)" to scrape the specific covid data that are of interest.

By locating the HTML element that contains the data, we can then move on to get the specific data that is of interest to us.

The library "tkinter" is used for the user interface and application packaging.

## What I learned

By building this project I learned how to scrape data from a website, by locating their position in the HTML document and then extracting it by taking advantage of the element's class name or ID. 

Additionally, I learned how to create a text field that acts as a search bar, presenting new data specific to the user's search parameters on command.

Concluding, I learned how to reload a window interface and present new data by incorporating a refresh button.

## Instructions

As a prerequisite, you should have already downloaded [python](https://www.python.org/downloads/).

1) Download the required libraries by running the following commands in your terminal.
```
    pip install requests
    pip install bs4
```
2) Clone the repository to your preferred directory.
3) Run the program through your terminal.
```
    python C://.../covid-tracker/main.py
```        
## Info

Thanks to [evanemran](https://github.com/evanemran) for coming up with the project!
