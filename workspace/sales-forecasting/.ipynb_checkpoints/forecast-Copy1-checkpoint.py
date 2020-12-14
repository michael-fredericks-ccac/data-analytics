import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import datetime

sales = pd.read_csv('sales data-set.csv')
sales['Date'] = pd.to_datetime(sales['Date'], dayfirst=True)

stores = []
depts = []
errors = []
avg_weekly_sales = []
accuracies = []
lm_used = []

stores_list = [1]
dept_list = [1]

job_count = 0
total_models = sales['Store'].nunique() * sales['Dept'].nunique()

for store in stores_list:
    for dept in dept_list:
        df = sales[(sales['Store'] == store) & (sales['Dept'] == dept)]
        df['L4W Sales'] = df['Date'].apply(lambda x: df[(df['Date'] >= pd.Timestamp(x - datetime.timedelta(weeks=5))) & 
                                                        (df['Date'] <= pd.Timestamp(x - datetime.timedelta(weeks=1)))]['Weekly_Sales'].sum())
        df['L6W Sales'] = df['Date'].apply(lambda x: df[(df['Date'] >= pd.Timestamp(x - datetime.timedelta(weeks=7))) & 
                                                        (df['Date'] <= pd.Timestamp(x - datetime.timedelta(weeks=1)))]['Weekly_Sales'].sum())
        df['L8W Sales'] = df['Date'].apply(lambda x: df[(df['Date'] >= pd.Timestamp(x - datetime.timedelta(weeks=9))) & 
                                                        (df['Date'] <= pd.Timestamp(x - datetime.timedelta(weeks=1)))]['Weekly_Sales'].sum())
        df['LY Sales'] = df['Date'].apply(lambda x: df[df['Date'] == pd.Timestamp(x - datetime.timedelta(weeks=52))]['Weekly_Sales'].sum())
        df['N4W Sales LY'] = df['Date'].apply(lambda x: df[(df['Date'] >= pd.Timestamp(x - datetime.timedelta(weeks=51))) & 
                                                           (df['Date'] <= pd.Timestamp(x - datetime.timedelta(weeks=48)))]['Weekly_Sales'].sum())
        df['N6W Sales LY'] = df['Date'].apply(lambda x: df[(df['Date'] >= pd.Timestamp(x - datetime.timedelta(weeks=51))) & 
                                                           (df['Date'] <= pd.Timestamp(x - datetime.timedelta(weeks=46)))]['Weekly_Sales'].sum())
        df['N8W Sales LY'] = df['Date'].apply(lambda x: df[(df['Date'] >= pd.Timestamp(x - datetime.timedelta(weeks=51))) & 
                                                           (df['Date'] <= pd.Timestamp(x - datetime.timedelta(weeks=44)))]['Weekly_Sales'].sum())
        train_df = df[(df['Date'] >= pd.Timestamp(datetime.date(2011, 2, 4))) & 
                      (df['Date'] <= pd.Timestamp(datetime.date(2011, 2, 4) + datetime.timedelta(weeks=71)))]
        test_df = df[df['Date'] > pd.Timestamp(datetime.date(2011, 2, 4) + datetime.timedelta(weeks=71))]
            
        try:
            X_train1 = train_df.drop(columns=['Store', 'Dept', 'Weekly_Sales', 'Date', 'L6W Sales', 'L8W Sales', 'N6W Sales LY', 'N8W Sales LY'])
            X_test1 = test_df.drop(columns=['Store', 'Dept', 'Weekly_Sales', 'Date', 'L6W Sales', 'L8W Sales', 'N6W Sales LY', 'N8W Sales LY'])
            y_train1 = train_df['Weekly_Sales']
            y_test1 = test_df['Weekly_Sales']
            lm1 = LinearRegression()
            lm1.fit(X_train1, y_train1)
            predictions1 = lm1.predict(X_test1)
            rmse1 = np.sqrt(metrics.mean_squared_error(y_test1, predictions1))
            
            X_train2 = train_df.drop(columns=['Store', 'Dept', 'Weekly_Sales', 'Date', 'L4W Sales', 'L8W Sales', 'N4W Sales LY', 'N8W Sales LY'])
            X_test2 = test_df.drop(columns=['Store', 'Dept', 'Weekly_Sales', 'Date', 'L4W Sales', 'L8W Sales', 'N4W Sales LY', 'N8W Sales LY'])
            y_train2 = train_df['Weekly_Sales']
            y_test2 = test_df['Weekly_Sales']
            lm2 = LinearRegression()
            lm2.fit(X_train2, y_train2)
            predictions2 = lm2.predict(X_test2)
            rmse2 = np.sqrt(metrics.mean_squared_error(y_test2, predictions2))
            
            X_train3 = train_df.drop(columns=['Store', 'Dept', 'Weekly_Sales', 'Date', 'L4W Sales', 'L6W Sales', 'N4W Sales LY', 'N6W Sales LY'])
            X_test3 = test_df.drop(columns=['Store', 'Dept', 'Weekly_Sales', 'Date', 'L4W Sales', 'L6W Sales', 'N4W Sales LY', 'N6W Sales LY'])
            y_train3 = train_df['Weekly_Sales']
            y_test3 = test_df['Weekly_Sales']
            lm3 = LinearRegression()
            lm3.fit(X_train3, y_train3)
            predictions3 = lm3.predict(X_test3)
            rmse3 = np.sqrt(metrics.mean_squared_error(y_test3, predictions3))
            
            rmse_list = [rmse1, rmse2, rmse3]
            
            if rmse1 == min(rmse_list):
                lm = lm1
                rmse = rmse1
                y_test = y_test1
                predictions = predictions1
                lm_used.append('lm-1')
            elif rmse2 == min(rmse_list):
                lm = lm2
                rmse = rmse2
                y_test = y_test2
                predictions = predictions2
                lm_used.append('lm-2')
            else:
                lm = lm3
                rmse = rmse3
                y_test = y_test3
                predictions = predictions3
                lm_used.append('lm-3')
                
            y_test_mean = y_test.mean()
            accuracy = 1 - (rmse / y_test_mean)
            stores.append(store)
            depts.append(dept)
            errors.append(round(rmse, 2))
            avg_weekly_sales.append(round(y_test_mean, 2))
            accuracies.append(round(accuracy, 4))
        
        except:
            stores.append(store)
            depts.append(dept)
            errors.append('error')
            avg_weekly_sales.append('error')
            accuracies.append('error')
            lm_used.append('error')
        
        line_df = test_df[['Date', 'Weekly_Sales']]
        line_df['Actual/Prediction'] = 'Actual'
        line_df1 = test_df[['Date']]
        line_df1['Weekly_Sales'] = predictions
        line_df1['Actual/Prediction'] = 'Prediction'
        line_df = pd.concat([line_df, line_df1], ignore_index=True)
        
        plt.figure(figsize=(12,8))
        sns.lineplot(x='Date', y='Weekly_Sales', data=line_df, hue='Actual/Prediction')
        plt.tight_layout()
        name = 'Store ' + str(store) + ' : Dept ' + str(dept)
        plt.savefig(name + '.png')
        
        job_count += 1
        job_status = str(round((job_count / total_models) * 100, 2)) + '% of ' + str(total_models) + ' Models Complete.' 
        print(job_status)

        

#results_dict = {
#    'Store' : stores,
#    'Department' : depts,
#    'RMSE' : errors,
#    'Actual Average Weekly Sales' : avg_weekly_sales,
#    'Accuracy' : accuracies,
#    'LM Used' : lm_used,
#}
#
#results_df = pd.DataFrame.from_dict(results_dict)
#results_df.to_csv('results.csv')