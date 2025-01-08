# Bike Sharing Data Analysis

[Bike Sharing Streamlit Web App](https://bikesharing-kevinandreas.streamlit.app/)

## Overview

The dataset contains the number of bike sharing between 2011 and 2012 in the Capital bike share system with the corresponding weather and seasonal information.

## Project Structure

```
bike-sharing-data-analysis
├───dashboard
| ├───final_cleaned_data.csv
| ├───dashboard.py
| ├───function.py
| └───cycle.png
├───data
| ├───day.csv
| └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```
- `dashboard/` contains script to develop the streamlit web app and cleaned data.
- `data/` contains raw CSV data files.
- `notebook.ipynb` used for performing data wrangling and EDA
- `requirements.txt` contains dependency for deploying web app to streamlit cloud

## How to install?

1. Clone to your computer
    ```
    git clone https://github.com/kev1nandreas/bike-sharing-data-analysis
    ```
2. Go to the project directory
    ```
    cd data-analyst-dicoding
    ```
3. Install the required Python packages by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the .ipynb file using Jupyter Notebook or run streamlit locally
    ```
    streamlit run dashboard/dashboard.py
    ```

Dataset source : [Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing)