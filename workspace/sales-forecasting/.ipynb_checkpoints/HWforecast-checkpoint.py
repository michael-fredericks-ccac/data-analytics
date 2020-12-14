import numpy as np
import pandas as pd
import datetime
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('sales data-set.csv', index_col='Date', parse_dates=True, dayfirst=True)

stores = []
depts = []
add_errors = []
add_accuracies = []
mul_errors = []
mul_accuracies = []
add_or_mul = []
data_periods = []


job_count = 0
total_models = df['Store'].nunique() * df['Dept'].nunique()

for store in df['Store'].unique():
    for dept in df['Dept'].unique():
        sd_df = df[(df['Store'] == store) & (df['Dept'] == dept)]['Weekly_Sales']
        sd_df.dropna()
        data_period = len(sd_df.index)
        
        try:
            train = sd_df.iloc[:112]
            train.index.freq = pd.infer_freq(train.index, warn=False)
            test = sd_df.iloc[112:]
            test.index.freq = pd.infer_freq(test.index, warn=False)
            
            add_fitted_model = ExponentialSmoothing(train, trend='add', seasonal='add', seasonal_periods=52).fit()
            add_test_predictions = add_fitted_model.forecast(len(test))
            
            mul_fitted_model = ExponentialSmoothing(train, trend='mul', seasonal='mul', seasonal_periods=52).fit()
            mul_test_predictions = mul_fitted_model.forecast(len(test))
            
            add_rmse = np.sqrt(mean_squared_error(test, add_test_predictions))
            mul_rmse = np.sqrt(mean_squared_error(test, mul_test_predictions))
            test_mean = test.mean()
            add_accuracy = 1 - (add_rmse / test_mean)
            mul_accuracy = 1 - (mul_rmse / test_mean)
            
            stores.append(store)
            depts.append(dept)
            add_accuracies.append(round(add_accuracy, 4))
            add_errors.append(round(add_rmse, 2))
            mul_accuracies.append(round(mul_accuracy, 4))
            mul_errors.append(round(mul_rmse, 2))
            
            if add_rmse < mul_rmse:
                add_or_mul.append('Additive')
            elif add_rmse == mul_rmse:
                add_or_mul.append('Equal')
            else:
                add_or_mul.append('Multiplicative')
            
        except:
            stores.append(store)
            depts.append(dept)
            add_accuracies.append('error') 
            add_errors.append('error')
            mul_accuracies.append('error')
            mul_errors.append('error')
            add_or_mul.append('error')
            
        data_periods.append(data_period)
        job_count += 1
        job_status = str(round((job_count / total_models) * 100, 2)) + '% of ' + str(total_models) + ' Models Complete.' 
        print(job_status)
        
results_dict = {
    'Store' : stores,
    'Department' : depts,
    'Periods Available' : data_periods,
    'Additive Model RSME' : add_errors,
    'Additive Model Accuracy' : add_accuracies,
    'Multiplicative Model RMSE' : mul_errors,
    'Mulitplicative Model Accuracy' : mul_accuracies,
    'Additive vs. Multiplicative' : add_or_mul,
    
}


results_df = pd.DataFrame.from_dict(results_dict)
results_df.to_csv('HWresults.csv')