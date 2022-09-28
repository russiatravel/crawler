from urllib import response
import requests
import csv
import os
import json
from datetime import datetime
from random import uniform
import time

# proxies = {
#     'https': 'http://77.242.16.30:8080'
# }

def collect_data():
    t_date = datetime.now().strftime('%d_%m_%Y')
    data = []
    for page in range(1, 55):
        url ='http://api.russia.travel/api/travels/frontend/v3/json/rus/travels?group=101&pagesize=8&page='+str(page)
        response = requests.get(url,params=None).json()
        data.append(response)
        print(page)
        time.sleep(1)

    with open(f'info_{t_date}.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)    
    
             
    
      
def save_to_file(): 
    pass
   
def main():
    collect_data()
   
    
if __name__ == '__main__':
    main()