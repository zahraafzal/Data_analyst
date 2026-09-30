# Pakistan COVID-19 Data Analysis (2020)

## 📌 Project Overview
Analyzed Pakistan's COVID-19 data from March to June 2020 to identify 
regional trends, peak periods, and death rates.

## 🛠️ Tools Used
- Python (Pandas, NumPy, Matplotlib)
- Google Colab
- Excel (report output)

## 📊 Key Findings
- **Total cases:** 790,006 across 7 regions
- **Highest cases:** Punjab (325,091), Sindh (265,698)
- **Highest recoveries:** Sindh (22,047)
- **Peak day:** [your peak day]
- **National death rate:** 0.31% (⚠️ data incomplete in some regions)

## 🔍 Analysis Performed
1. Cleaned and filtered 630 rows across 7 regions
2. Aggregated cases by region using Pandas groupby
3. Built daily trend time-series
4. Calculated region-wise death rates
5. Generated formatted Excel report

## ⚠️ Data Limitations
Discharged and Expired columns were partially reported in some regions,
leading to an unrealistically low death rate. This was identified during
analysis as a data quality issue.

## 📁 Files
- `covid_analysis.ipynb` — Full analysis notebook
- `COVID_Report.xlsx` — Generated Excel report

## 🚀 How to Run
1. Open the notebook in Google Colab
2. Upload `COVID_FINAL_DATA.xlsx`
3. Run all cells
