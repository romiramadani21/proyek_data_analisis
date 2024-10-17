# Data Analysis - Dicoding Submission
[Bike Sharing Data Dashboard Streamlit App](https://bike-sharing-dicoding-ds.streamlit.app/)

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)

## Overview
This project is a data analysis and visualization project focused on The analysis of bike rental data, encompassing data wrangling, exploration, and visualization. Initial steps involve importing and cleaning the data, followed by exploratory analysis through grouping, aggregation, and correlation analysis. Visualization and explanatory analysis include plotting boxplots to compare rentals between working days and holidays, exploring the influence of weather conditions on rentals, and examining rental trends across seasons and over time. These insights aid in understanding rental patterns and inform decision-making for bike rental businesses.

## Project Structure
- `dashboard/`: This directory contains dashboard.py which is used to create dashboards of data analysis results.
- `data/`: Directory containing the raw CSV data files.
- `notebook.ipynb/`: This file is used to perform data analysis.
- `README.md`: This documentation file.

## Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/romiramadani21/proyek_data_analisis.git
```
2. Go to the project directory
```
cd proyek_data_analisis
```
3. Install the required Python packages by running:
```
pip install -r requirements.txt
```

## Usage
1. **Data Wrangling**:
- Data is imported using Pandas from two CSV files: one for daily data and one for hourly data.
- Data quality is assessed through methods like .info(), .isna(), .duplicated(), and .describe().
- Data cleaning involves dropping unnecessary columns and renaming columns for better understanding. Additionally, some numerical values are mapped to categorical labels.
- Data types are converted to appropriate types like datetime and categorical.

2. **Exploratory Data Analysis (EDA)**: 
- Grouping and aggregation operations are performed to understand patterns based on different features like month, weather condition, holiday, weekday, working day, and season.

3. **Visualization**: Run the Streamlit dashboard for interactive data exploration:

```
cd ./dashboard
streamlit run dashboard.py
```
Access the dashboard in your web browser at `https://bike-sharing-dicoding-ds.streamlit.app/`.

## Data Sources
The project uses Bike Sharing Dataset from [Belajar Analisis Data dengan Python's Final Project](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view) offered by [Dicoding](https://www.dicoding.com/).