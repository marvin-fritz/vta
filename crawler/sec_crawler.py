import requests
from database import MongoManager


# Get all companies listed by the SEC and insert them  into database
# the data contains the following information:
# cik_str, ticket symbol, title
# TODO: Check if company exists
def load_ticker():
    headers = {'User-Agent': "marvinfritz.mac@icloud.com"}
    ticker = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)
    print(ticker.json().keys())
    mongoManager = MongoManager('vta', 'companies')
    for company in ticker.json().keys():
        company_document = {
            'cikStr': ticker.json()[company]['cik_str'],
            'ticker': ticker.json()[company]['ticker'],
            'title': ticker.json()[company]['title']
        }
        mongoManager.insert_document(document=company_document)
        print('inserted: ' + str(ticker.json()[company]))
