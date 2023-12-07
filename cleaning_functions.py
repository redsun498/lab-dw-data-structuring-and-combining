import pandas as pd

def clean_number_complaints_python(num):
    if isinstance(num, str):
        return int(num.split('/')[1])
    return 0

def remove_plural(e):
    if isinstance(e,str):
        if e.endswith('s'):
            return e[:-1]  
    return e

def clean_columns_name(df):
    df.columns = df.columns.str.lower().str.replace(' ','_')
    df.columns.values[1] = 'state'
    return df

def clean_invalid_values(df):
    dict_gender = {'Femal':'F', 'Male':'M', 'female':'F','F':'F','M':'M'}
    df['gender'].map(dict_gender,na_action='ignore').value_counts()
    state_abbrevitaion = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations')[0].iloc[11:62,[0,3]]
    state_abbrevitaion.columns = ['State','Abbr']
    state_cleaning_dict = state_abbrevitaion.set_index('Abbr').to_dict()['State']
    df['state'] = df['state'].replace(state_cleaning_dict).replace('Cali','California')
    
    df['education'] = df['education'].apply(remove_plural)
    
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%','').astype(float)
    df.rename(columns = {'customer_lifetime_value':'customer_lifetime_value_%'},inplace=True)
    df['vehicle_class'] = df['vehicle_class'].replace({'Luxury SUV':'Luxury','Luxury Car':'Luxury'})
    return df
    
def whole_pipeline(df):
    df = clean_columns_name(df)
    df = clean_invalid_values(df)
    return df
    