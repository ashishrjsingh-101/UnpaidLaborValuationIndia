# Data Documentation for Unpaid Labor Valuation

## Overview

This directory contains all data files used in the Economic Valuation of Unpaid Labor analysis. All primary data sources are publicly available from government repositories as documented below.

## Directory Structure

```
data/
├── raw/                           # Original data source documentation
│   ├── TUS_2019_documentation.md   # Time Use Survey documentation
│   ├── wage_sources.md             # Wage data sources and methodology
│   └── financial_parameters.md     # Financial parameter sources
├── processed/                      # Cleaned and processed datasets  
│   ├── time_allocation.csv         # Processed time use data
│   ├── wage_proxies.csv            # Constructed wage proxies
│   └── financial_params.csv        # Discount rates and growth parameters
└── README_data.md                  # This file
```

## Primary Data Sources

### 1. India Time Use Survey 2019

**Source:** Ministry of Statistics and Programme Implementation (MOSPI)  
**URL:** http://mospi.nic.in/time-use-survey  
**Access:** Publicly available  
**Format:** PDF reports with aggregate statistics  
**Coverage:** All states and union territories of India  
**Sample Size:** 138,799 households  
**Collection Period:** January-December 2019  

**Usage in Study:**
- Female and male time allocation patterns (Table 2)
- Activity-specific minutes per day for unpaid work categories
- Basis for emotional labor adjustment (20% premium)

**Data Extraction Method:**
- Manual extraction from published PDF reports
- Cross-validation across multiple tables
- Annual hour calculations using 365-day conversion

### 2. Minimum Wage Database

**Source:** Labour Bureau, Government of India  
**URL:** https://labour.gov.in/minimum-wages  
**Access:** Publicly available  
**Format:** State-wise notifications and rates  
**Coverage:** All states, central government rates  
**Reference Period:** 2025 notifications  

**Usage in Study:**
- Base wage rates for different skill levels
- Skill premiums for specialized tasks (cooking, childcare)
- Regional wage variation assessment

**Processing Notes:**
- National averages computed across states
- Skill premiums added for specialized tasks
- Conservative estimates used to avoid overestimation

### 3. Financial and Economic Data

**Source:** Reserve Bank of India (RBI) / MOSPI  
**URL:** https://rbi.org.in/Scripts/AnnualPublications.aspx  
**Access:** Publicly available  
**Format:** Statistical databases and publications  
**Coverage:** National economic indicators  
**Reference Period:** 2020-2025 averages  

**Usage in Study:**
- 10-year Government Securities yields (risk-free rate)
- Consumer Price Index inflation rates
- Economic growth and wage growth trends

## Processed Data Files

### time_allocation.csv

Contains processed time use data for analysis.

**Columns:**
- `activity`: Household activity category
- `description`: Activity description
- `female_minutes_day`: Female daily minutes (TUS 2019)
- `male_minutes_day`: Male daily minutes (TUS 2019)
- `female_annual_hours`: Female annual hours (calculated)
- `male_annual_hours`: Male annual hours (calculated)
- `emotional_adjustment`: Emotional labor adjustment factor
- `adjusted_female_hours`: Female hours with emotional labor premium

**Source Processing:**
- Extracted from TUS 2019 Tables 2.1-2.5
- Converted minutes to annual hours using 365-day year
- Applied 20% emotional labor adjustment to female hours

### wage_proxies.csv

Contains wage rates for valuing different household activities.

**Columns:**
- `activity`: Household activity
- `market_equivalent`: Corresponding market service
- `wage_source`: Data source for wage rate
- `hourly_rate_inr`: Wage rate in rupees per hour
- `skill_level`: Skill categorization (basic/intermediate/specialized)
- `adjustment_factor`: Premium over minimum wage
- `notes`: Methodology notes

**Source Processing:**
- Base rates from Labour Bureau minimum wages
- Skill premiums applied based on task complexity
- Market survey data for commercial services (laundry, childcare)

### financial_params.csv

Contains financial parameters used in present value calculations.

**Columns:**
- `parameter`: Parameter name
- `value`: Numeric value
- `unit`: Units (percentage, years, etc.)
- `source`: Data source
- `calculation_method`: Derivation methodology
- `sensitivity_range`: Range for sensitivity testing

**Key Parameters:**
- `discount_rate`: 10.60% (risk-free + inflation + household risk)
- `growth_rate`: 6.00% (wage growth in organized sector)
- `time_horizon`: 55 years (average marriage duration)
- `inflation_rate`: 2.40% (2020-2025 average CPI)

## Data Quality and Limitations

### Strengths
- Nationally representative sampling (TUS 2019)
- Rigorous survey methodology with stratified sampling
- Official government data sources
- Large sample sizes ensuring statistical reliability

### Limitations
- Time diaries may underreport emotional labor and mental load
- National averages mask regional and socioeconomic variations
- Some wage proxies based on limited market data
- Seasonal variations not captured in annual averages

### Quality Assurance
- Cross-validation across multiple data sources
- Conservative estimation approaches to avoid overstatement
- Sensitivity testing for key parameters
- Validation against international benchmarks where available

## Data Processing Scripts

All data processing is automated and reproducible:

- `scripts/01_data_preparation.py`: Main data processing script
- `src/data_processing.py`: Core processing functions
- Manual extraction documented in `raw/` directory

## Data Usage Guidelines

### Attribution
When using these processed datasets, please cite:
1. Original data sources (MOSPI, Labour Bureau, RBI)
2. This replication package and methodology
3. The main research paper

### Verification
- All processing steps are documented and reproducible
- Original sources can be verified through provided URLs
- Validation scripts available in `tests/` directory

### Updates
- Data sources are checked for updates quarterly
- Processing scripts can accommodate new data releases
- Version control tracks all changes to parameters

## Contact

For questions about data processing or sources:
- **Author:** Ashish Ranjan
- **Email:** ashishrjsingh786@gmail.com
- **Repository:** https://github.com/ashishrjsingh-101/UnpaidLaborValuationIndia.git

## Last Updated

**Date:** September 2, 2025  
**Version:** 1.0  
**Next Review:** December 2025
