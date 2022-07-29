import pandas as pd
import requests
import io

def get_johns_hopkins():
    
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv" 
    download = requests.get(url).content
    df_jh = pd.read_csv(io.StringIO(download.decode('utf-8')))
    df_jh.to_csv('../data/raw/COVID-19/time_series_covid19_confirmed_global.csv', index = False)

if __name__ == '__main__':
    get_johns_hopkins()