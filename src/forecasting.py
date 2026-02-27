import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_sales(df):
    revenue_df=df.groupby('date')['revenue'].sum()
    revenue_df=revenue_df.sort_values('date')
    revenue_df['day']=np.arange(len(revenue_df))
    X=revenue_df['day']
    Y=revenue_df['revenue']
    model=LinearRegression()
    model.fit(X,Y)
    future_days=np.arange(len(revenue_df),len(revenue_df)+30).reshape(-1,1)
    forecast_values=model.predict(future_days)
    
    forecast_date=pd.date_range(start=revenue_df['date'].iloc[-1]+pd.Timedelta(days=1),periods=30)
    forecast_df=pd.DataFrame({'date':forecast_date,'forecast_sales':forecast_values})
    
    return forecast_df


