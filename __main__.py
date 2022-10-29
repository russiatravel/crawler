import requests
import csv
from datetime import datetime


def collect_data():
    t_date = datetime.now().strftime('%d_%m_%Y')
    url = 'http://api.russia.travel/api/travels/frontend/v3/json/rus/travels?group=101&pagesize=50&page=1'
    response = requests.get(url, params=None)
    items = response.json()['items']
    result = []
    for item in items:
        city_name = item['region']['name']
        city_desc = item['area']['name']                
        place_name = item['title']
        place_desc = item['lid']
        result.append([city_name, city_desc, place_name, place_desc])

        
    with open(f'result_{t_date}.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Область',
                'Район',
                'Название',
                'Описание'
                
            )
        )

        writer.writerows(result)


def main():
    collect_data()
   

if __name__ == '__main__':
    main()
