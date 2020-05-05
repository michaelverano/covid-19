import requests
from datetime import datetime

def main():
    time_format = datetime.today().strftime("%Y%m%d_%H-%M")
    
    url = 'https://covidtracking.com/api/v1/states/daily.csv'
    r = requests.get(url)

    file_name = "{}_daily.csv".format(time_format)

    with open(file_name, 'w') as csvfile:
        csvfile.write(r.text)

if __name__ == '__main__':
    main()

