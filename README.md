# wesm-price-prediction

### Data Sources
The project uses 4 months of WESM data (Oct 2025 – Jan 2026). Since the IEMOP website only hosts the latest 3 months, use the archived link below:

1. **Download Full Dataset:** [GDrive Link to Data](https://drive.google.com/drive/folders/1bBBfN9HHeusgjcAjRgM8dC-t4AMN0ijE?usp=sharing)
   > **NOTE:** Download the **raw_data** folder only if you want to run `01_ETL_Preprocessing.ipynb`. Otherwise, you can simply download `final_dataset_csv` and extract the csv into the root folder.

2. **(Optional) Extract** and place the CSVs into their respective folders:
   - `./raw_data/GWAP/`
   - `./raw_data/RTD_Regional/`
   - `./raw_data/Outages/`

### Directory Structure
![alt text](image.png)


### Original Data Links (Latest 3 Months only)
- [Generator Weighted Average Price (Final)](https://www.iemop.ph/market-data/generator-weighted-average-price-final/)
- [RTD Regional Summaries](https://www.iemop.ph/market-data/rtd-regional-summaries/)
- [Outage Schedules Used in RTD](https://www.iemop.ph/market-data/outage-schedules-used-in-rtd/)

### Official Resources & Documentation
- **Latest Market Data:** [IEMOP Market Data Dashboard](https://www.iemop.ph/market-data/)
- **Technical Reference:** [WESM Price Determination Methodology (PDM)](https://www.wesm.ph/downloads/download/TWFya2V0IFJlcG9ydHM=/NTYw)
- **Compliance & Rules:** [WESM Compliance Bulletin](https://www.wesm.ph/market-reports/compliance-bulletins/)