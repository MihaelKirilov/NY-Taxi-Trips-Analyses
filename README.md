# NY Taxi Trips Analyses

This project aims to analyze New York City taxi trips data, including the impact of COVID-19 on taxi usage, and to visualize insights using Google Looker Studio. The data will be processed using Mage.ai pipelines and Google Cloud Platform services, including Google Cloud Storage and BigQuery.

## Data Pipeline

The data pipeline consists of the following steps:

1. **Data Download**: Mage.ai pipelines will be used to download NYC taxi trips data from the provided API.
2. **Data Transformation**: The downloaded data will be transformed to prepare it for analysis.
3. **Data Export**: The transformed data will be exported to a Google Cloud Storage bucket.

## Workflow

1. Run the Mage.ai pipeline to download, transform, and export the data to a Google Cloud Storage bucket.
2. Load the exported data from the Google Cloud Storage bucket into Google BigQuery.
3. Connect BigQuery to DBT (Data Build Tool) for further data transformations.
4. Utilize DBT to transform the data according to analytical requirements.
5. Visualize the transformed data using Google Looker Studio.

## Visualizations

![project-1](https://github.com/MihaelKirilov/NY-Taxi-Trips-Analyses/assets/98331411/1a0c3760-8c44-4d63-bf99-3280e8c494b5)


## License

This project is licensed under the [MIT License](LICENSE).
