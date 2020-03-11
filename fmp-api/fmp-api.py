import json
import csv
from urllib.request import urlopen

def get_ticker_list(json_file_path):
    with open(json_file_path) as json_file:
        json_data = json.load(json_file)
        ticker_list = json_data["ticker_list"]
    return ticker_list
        
def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def export_comapny_profile(company_profiles):
    with open('company-profiles.csv', 'w', newline = '') as csv_file:
        sample_dict = company_profiles[0]
        fieldnames = []
        for key in sample_dict:
            fieldnames.append(key)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for cp in company_profiles:
            writer.writerow(cp)
        print("A new CSV file has been created with your requested company profiles.")

def main():
    ticker_list = get_ticker_list('ticker-list.json')
    company_profiles = []
    for ticker in ticker_list:
        url = "https://financialmodelingprep.com/api/v3/company/profile/" + ticker
        company_profile = get_jsonparsed_data(url)
        company_profiles.append(company_profile)
    export_comapny_profile(company_profiles)

main()