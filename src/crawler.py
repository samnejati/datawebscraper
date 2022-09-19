import requests 
import pandas as pd
from bs4 import BeautifulSoup # library to parse HTML documents
from typing import List


def get_wiki_table(url: str) -> pd.DataFrame:
        
    """
    Get the tables from a given Wikipedia url
    """
    try:
        response=requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            tables = soup.find_all('table',{'class':"wikitable"})
            df_list = pd.read_html(str(tables))
            
            return df_list
        

        else: 
            print(f"The status code is {response.status_code}")
            
    except Exception as e:
        print (e.message, e.arg)


def save_table (list_of_df: List[pd.DataFrame]) -> None:
    index = 1
    for df in list_of_df:
        df.to_csv(f"table{index}.csv")
        index += 1
    return

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
    list_of_df = get_wiki_table(url) 
    save_table(list_of_df)
