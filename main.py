import pandas as pd
import requests
from database import MongoManager
import time


def get_company_data():
    mongoManager = MongoManager('vta', 'companies')
    headers = {'User-Agent': "marvinfritz.mac@icloud.com"}
    for company in mongoManager.get_all_documents():
        cik_str = str(company['cikStr']).zfill(10)
        ticker = requests.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik_str}.json', headers=headers)
        print(ticker.json()['facts']['us-gaap']['AccruedIncomeTaxesCurrent'])
        # Restrictions by SEC https://www.sec.gov/privacy.htm#security
        # max. 10 requests per second
        time.sleep(0.2)


if __name__ == '__main__':
    get_company_data()
