import json
import csv
from urllib.request import urlopen

#get list of tickers from the json file in the folder
def get_ticker_list(json_file_path):
    with open(json_file_path) as json_file:
        json_data = json.load(json_file)
        ticker_list = json_data["ticker_list"]
    return ticker_list

#get api data        
def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

#format company profile data
def format_data(company_profile):
    formatted_cp = {}
    symbol = company_profile["symbol"]
    profile_dict = company_profile["profile"]
    formatted_cp.update({"symbol" : symbol})
    formatted_cp.update(profile_dict)
    return formatted_cp

#export all comapny profiles to a csv file
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

#main
def main():
    ticker_list = get_ticker_list('ticker-list.json')
    company_profiles = []
    for ticker in ticker_list:
        url = "https://financialmodelingprep.com/api/v3/company/profile/" + ticker
        company_profile = get_jsonparsed_data(url)
        formatted_cp = format_data(company_profile)
        company_profiles.append(formatted_cp)
    export_comapny_profile(company_profiles)

#run main
main()