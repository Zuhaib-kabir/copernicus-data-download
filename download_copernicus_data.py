"""
Copernicus Marine Data Downloader
---------------------------------
This script downloads Copernicus Marine datasets (e.g., OSTIA SST/Sea Ice)
year-by-year for a defined spatial and temporal range.

Author: Md. Zuhaib Kabir
"""


# 1. INSTALL REQUIREMENTS
# Run this once in terminal:

!pip -q install copernicusmarine
!pip -q install "click==8.1.7"
!pip -q install "click==8.1.8"


# 2. IMPORT LIBRARIES

import os
from getpass import getpass
from datetime import datetime
import copernicusmarine



# 3. USER INPUTS (EDIT THESE)
# Output folder
OUT_DIR = "your_provided_direction"
os.makedirs(OUT_DIR, exist_ok=True)
print("Output folder:", OUT_DIR)

# Copernicus credentials
USERNAME = "your_username"
PASSWORD = getpass("Enter Copernicus Marine password (hidden): ")

# Dataset ID (example: OSTIA)
DATASET_ID = "METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2" #this is just a sample id randomly collected from the side

# Spatial extent (replace with your study area)
MIN_LON, MAX_LON = x, y
MIN_LAT, MAX_LAT = x, y

# Time range (replace with your study time)
GLOBAL_START = datetime(yyyy, mm, dd)
GLOBAL_END   = datetime(yyyy, mm, dd)

# Variables to download
VARIABLES = ["x"]   # change based on dataset




# 4. CHECK DATASET ACCESS

print("\nChecking dataset access...")
try:
    copernicusmarine.describe(dataset_id=DATASET_ID)
    print("✅ Dataset accessible")
except Exception as e:
    print("❌ Access problem:\n", e)
    raise




# 5. Download the data year by year if you want to download more than one year (recommended). 
# You can skip the first part, but if the storage is large, it may randomly split your file.

for year in range(GLOBAL_START.year, GLOBAL_END.year + 1):

    start = datetime(year, 1, 1)
    end   = datetime(year, 12, 31)

    # Adjust first and last year
    if year == GLOBAL_START.year:
        start = GLOBAL_START
    if year == GLOBAL_END.year:
        end = GLOBAL_END

    output_file = f"copernicus_data_variavle_{year}.nc" #edit it 

    print(f"\nDownloading {year}: {start.date()} → {end.date()}")

    copernicusmarine.subset(
        dataset_id=DATASET_ID,
        username=USERNAME,
        password=PASSWORD,
        variables=VARIABLES,

        minimum_longitude=MIN_LON,
        maximum_longitude=MAX_LON,
        minimum_latitude=MIN_LAT,
        maximum_latitude=MAX_LAT,

        start_datetime=start.strftime("%Y-%m-%dT%H:%M:%S"),
        end_datetime=end.strftime("%Y-%m-%dT%H:%M:%S"),

        output_directory=OUT_DIR,
        output_filename=output_file,
        file_format="netcdf",
        overwrite=False,
    )

print("Download complete!✅")
print("Files saved in:", OUT_DIR)
