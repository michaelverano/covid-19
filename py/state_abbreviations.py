import requests
from bs4 import BeautifulSoup
import csv

def main():
    url = 'https://www.50states.com/abbreviations.htm'
    r = requests.get(url)

    text = BeautifulSoup(r.text, 'lxml')
    tr = text.find_all('tr')

    rows = []
    row = [rows.append(tr[num].text.split('\n')[1:-1]) for num, row in enumerate(tr)]

    with open('state_abbreviations.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in rows:
           wr.writerow(row) 

if __name__ == '__main__':
    main()
