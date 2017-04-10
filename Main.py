#NAME GENERATOR

import requests
from bs4 import BeautifulSoup
import random

def name_gen(text_file_name):

    text_file = open(text_file_name, "w")

    for run in range(10):
        url = "http://www.rinkworks.com/namegen/fnames.cgi?d=1&f=0"
        html = requests.get(url).content

        soup = BeautifulSoup(html, "html.parser")
        table = soup.select_one('table.fnames_results')
        names = []

        for row in table.find_all("tr"):
            tds = row.find_all("td")
            for i in tds:
                i = str(i)
                i = i[4:-5]
                names.append(i)

        for i in names:
            text_file.write(i)
            text_file.write("\n")

    text_file.close()

def names():

    name_gen("Names.txt")
    name_gen("Surnames.txt")

    names = open("Names.txt", 'r').readlines()
    lnames = open("Surnames.txt", 'r').readlines()

    text_file = open("Names List.txt", 'w')

    for line in names:
        for line2 in lnames:
            full_name = line.rstrip() + " " + line2
            text_file.write(full_name)
    text_file.close()

names()
