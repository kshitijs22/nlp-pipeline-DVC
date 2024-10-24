import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import os

#calling test_size from params.yaml
def load_params(params_path):
    test_size=yaml.safe_load(open(params_path,'r'))['data_ingestion']['test_size']
    return test_size

def read_data(url):
    df=pd.read_csv(url)
    return df

def process_data(df):
    df.drop(columns=['tweet_id'],inplace=True)
    final_df=df[df['sentiment'].isin(['happiness','sadness'])]
    final_df['sentiment'].replace({'happiness':1,'sadness':0},inplace=True)
    return final_df

def saved_data(train_data,test_data, data_path):
    data_path = os.path.join(data_path, 'raw')
    os.makedirs(data_path, exist_ok=True)
    train_data.to_csv(os.path.join(data_path,'train.csv'))
    test_data.to_csv(os.path.join(data_path,'test.csv'))

def main():
    test_size=load_params('params.yaml')
    df=read_data('https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv')
    final_df=process_data(df)

    train_data,test_data=train_test_split(final_df,test_size=test_size,random_state=42)

    saved_data(train_data , test_data , data_path='data')

if __name__ == "__main__":
    main()