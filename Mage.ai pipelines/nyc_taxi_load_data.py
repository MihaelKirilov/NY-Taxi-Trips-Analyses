import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # Define the URL pattern for the data
    url_pattern = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{}/{}_tripdata_{}-{}.csv.gz'
    
    taxi_types = ['yellow', 'green']
    years = ['2019', '2020']
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    
    dfs = []
    
    # Define data types for green and yellow taxi data
    taxi_data_types = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }

    for taxi_type in taxi_types:
        for year in years:
            for month in months:
                url = url_pattern.format(taxi_type, taxi_type, year, month)
                df = pd.read_csv(url, sep=',', compression='gzip', dtype=taxi_data_types)
                dfs.append(df)

    # Concatenate dataframes into a single dataframe
    return pd.concat(dfs, ignore_index=True)



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'