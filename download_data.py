#!/usr/bin/env python
"""Download Kaggle competition data."""
from kaggle.api.kaggle_api_extended import KaggleApi
import os

api = KaggleApi()
api.authenticate()

download_path = r'c:\Users\prati\Desktop\Project\F1\predict-f1-pit-stops\data\raw'
os.makedirs(download_path, exist_ok=True)

print(f'Downloading to: {download_path}')
api.competition_download_files('playground-series-s6e5', path=download_path)
print('Download complete!')

# List downloaded files
print('\nDownloaded files:')
for f in os.listdir(download_path):
    print(f'  {f}')
