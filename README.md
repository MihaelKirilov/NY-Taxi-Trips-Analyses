NY Taxi Trips Analyses
This project aims to analyze New York City taxi trips data, including the impact of COVID-19 on taxi usage, and to visualize insights using Google Looker Studio. The data will be processed using Mage.ai pipelines and Google Cloud Platform services, including Google Cloud Storage and BigQuery.

Data Pipeline
The data pipeline consists of the following steps:

Data Download: Mage.ai pipelines will be used to download NYC taxi trips data from the provided API.
Data Transformation: The downloaded data will be transformed to prepare it for analysis.
Data Export: The transformed data will be exported to a Google Cloud Storage bucket.
Workflow
Run the Mage.ai pipeline to download, transform, and export the data to a Google Cloud Storage bucket.
Load the exported data from the Google Cloud Storage bucket into Google BigQuery.
Connect BigQuery to DBT (Data Build Tool) for further data transformations.
Utilize DBT to transform the data according to analytical requirements.
Visualize the transformed data using Google Looker Studio.
Visualizations
Include screenshots of the following:

Data Visualization: Screenshots of visualized data insights in Google Looker Studio.
License
This project is licensed under the MIT License.
