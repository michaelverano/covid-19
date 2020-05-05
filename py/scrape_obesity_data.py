import requests
from bs4 import BeautifulSoup
import csv

def main():
    url = 'https://www.cdc.gov/obesity/data/prevalence-maps.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    tr = soup.find_all('tr')
    tr = tr[1:]


    rows = []
    for html_row in tr:
       cells = html_row.text.split('\n')[1:-1]
       rows.append(cells)
        
    # write to csv
    with open('all_obesity_data.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in rows:
            wr.writerow(row)
    
if __name__ == '__main__':
    main()
    
