import pandas as pd

url = "https://community.watsonanalytics.com/wp-content/uploads/2015/04/WA_fn-UseC_-Sales-Win-Loss.csv"

sales_data = pd.read_csv(url)

print(sales_data)