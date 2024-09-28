import json
from re import search

import requests



url = 'https://static-basket-01.wbbasket.ru/vol0/data/main-menu-ru-ru-v3.json'
search_url = 'https://wildberries.ru/'
headers = {'Accept': "*/*", 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(url, headers=headers)
data = response.json()
with open('wb_catalogs_data.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'Данные сохранены в wb_catalogs_data.json')\


def get_catalogs_wb():
    data_list = []
    for d in data:
        try:
            for child in d['childs']:
                try:
                    category_name = child['name']
                    category_url = child['url']
                    data_list.append({category_name: category_url})
                except:
                    continue
                try:
                    for sub_child in child['childs']:
                        category_name = sub_child['name']
                        category_url = sub_child['url']
                        data_list.append({category_name: category_url})

                except:
                    continue
        except:
            continue
    return data_list

catalogs = get_catalogs_wb()
catalog_search = input('Введите название католога:').lower()
for search in catalogs:
    for k, v in search.items():
        if k.lower() == catalog_search:
            print(f'Категория: {k}, URL: {search_url + v}')

