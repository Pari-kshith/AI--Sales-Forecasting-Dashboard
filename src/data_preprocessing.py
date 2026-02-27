import pandas as pd

def load_and_clean(filepath):
    df=pd.read_csv(filepath)
    df=df.drop_duplicates()
    df['date']=pd.to_datetime(df['date'])
    df=df.fillna({'units_sold':0,'unit_price':0})
    df['revenue']=df['units_sold']*df['unit_price']
    
    return df
def get_business_metrices(df):
    total_revenue=df['revenue'].sum()
    total_orders=df.shape[0]
    avg_orders=total_revenue/total_orders
    revenue_region=df.groupby('region')['revenue'].sum()
    revenue_category=df.grouby('category')['revenue'].sum()
    monthly_revenue=df.groupby('monthly')['revenue'].sum()
    mom_growth=monthly_revenue.pct_change().fillna(0)

    return{
        "total_revenue":total_revenue,
        "total_orders":total_orders,
        "avg_orders":avg_orders,
        "revenue_region":revenue_region,
        "revenue_category":revenue_category,
        "monthly_revenue":monthly_revenue,
        "mom_growth":mom_growth
    }


    
