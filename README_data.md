# Economic Valuation of Unpaid Labor - Replication Package

**Repository:** unpaid-labor-valuation  
**Study:** Economic Valuation of Unpaid Labor in Indian Marriages: Complete Mathematical Framework and Transparency Volume  
**Author:** Ashish Ranjan  
**Contact:** ashishrjsingh786@gmail.com  
**Date:** September 2025  
**License:** CC BY 4.0  

## Overview

This replication package contains all computational materials required to reproduce the analyses, tables, and figures reported in "Economic Valuation of Unpaid Labor in Indian Marriages: Complete Mathematical Framework and Transparency Volume." The package follows American Economic Association data and code availability guidelines to ensure full reproducibility.

## Repository Structure

```
unpaid-labor-valuation/
├── README.md                   # This file
├── LICENSE                     # CC BY 4.0 license terms
├── CITATION                    # Citation information
├── requirements.txt            # Python dependencies
├── environment.yml             # Conda environment specification
├── .gitignore                  # Version control exclusions
├── docs/                       # Documentation and guides
│   ├── methodology-guide.md    # Detailed methodology documentation
│   ├── parameter-guide.md      # Parameter estimation guide
│   └── troubleshooting.md      # Common issues and solutions
├── data/                       # Data files and sources
│   ├── raw/                    # Original data sources (links/documentation)
│   │   ├── TUS_2019_documentation.md
│   │   ├── wage_sources.md
│   │   └── financial_parameters.md
│   ├── processed/              # Cleaned and processed data
│   │   ├── time_allocation.csv
│   │   ├── wage_proxies.csv
│   │   └── financial_params.csv
│   └── README_data.md          # Data documentation
├── src/                        # Source code
│   ├── __init__.py
│   ├── config.py               # Configuration and parameters
│   ├── data_processing.py      # Data cleaning and preparation
│   ├── valuation_models.py     # Present value calculation functions
│   ├── scenario_analysis.py    # Scenario and sensitivity analysis
│   ├── monte_carlo.py          # Stochastic simulation
│   ├── policy_analysis.py      # Policy modeling functions
│   └── utils.py                # Utility functions
├── scripts/                    # Analysis scripts
│   ├── 01_data_preparation.py  # Data processing script
│   ├── 02_baseline_analysis.py # Main analysis script
│   ├── 03_sensitivity_tests.py # Sensitivity analysis
│   ├── 04_monte_carlo_sim.py   # Monte Carlo simulations
│   ├── 05_policy_modeling.py   # Policy analysis
│   └── 06_generate_figures.py  # Figure generation
├── outputs/                    # Generated results
│   ├── tables/                 # CSV output tables
│   │   ├── baseline_results.csv
│   │   ├── sensitivity_analysis.csv
│   │   ├── monte_carlo_results.csv
│   │   └── policy_scenarios.csv
│   ├── figures/                # Generated figures (PNG/PDF)
│   │   ├── discount_sensitivity.png
│   │   ├── growth_sensitivity.png
│   │   ├── monte_carlo_dist.png
│   │   └── policy_comparison.png
│   └── logs/                   # Execution logs
│       ├── analysis_log.txt
│       └── validation_log.txt
├── tests/                      # Unit tests and validation
│   ├── __init__.py
│   ├── test_valuation_models.py
│   ├── test_scenarios.py
│   ├── test_monte_carlo.py
│   └── validation_suite.py
└── MANIFEST.txt                # Complete file listing

```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Git for version control
- Recommended: Anaconda or Miniconda for environment management

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ashishrjsingh/unpaid-labor-valuation.git
   cd unpaid-labor-valuation
   ```

2. **Create and activate environment:**

   **Option A: Using conda (recommended)**
   ```bash
   conda env create -f environment.yml
   conda activate unpaid-labor-env
   ```

   **Option B: Using pip**
   ```bash
   python -m venv unpaid-labor-env
   source unpaid-labor-env/bin/activate  # On Windows: unpaid-labor-env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python -c "import numpy, pandas, scipy, matplotlib; print('Dependencies installed successfully')"
   ```

### Replication Steps

**Step 1: Data Preparation**
```bash
python scripts/01_data_preparation.py
```
This script processes raw data sources and creates the cleaned datasets used in analysis.

**Step 2: Baseline Analysis**
```bash
python scripts/02_baseline_analysis.py
```
Reproduces all baseline present value calculations and scenario comparisons (Tables 4-6).

**Step 3: Sensitivity Analysis**
```bash
python scripts/03_sensitivity_tests.py
```
Generates discount rate and growth rate sensitivity results (Tables 5-6, Figures 1-2).

**Step 4: Monte Carlo Simulations**
```bash
python scripts/04_monte_carlo_sim.py
```
Runs 10,000-iteration stochastic simulations with random seed 20250901 (Table 7, Figure 3).

**Step 5: Policy Analysis**
```bash
python scripts/05_policy_modeling.py
```
Evaluates policy intervention scenarios and generates impact assessments.

**Step 6: Generate Figures**
```bash
python scripts/06_generate_figures.py
```
Creates all figures in publication-ready format (PNG and PDF versions).

**Complete Replication (All Steps)**
```bash
bash run_all_analysis.sh
```

### Expected Runtime

- Data preparation: 1-2 minutes
- Baseline analysis: 2-3 minutes  
- Sensitivity analysis: 3-5 minutes
- Monte Carlo simulation: 8-12 minutes (10,000 iterations)
- Policy analysis: 2-3 minutes
- Figure generation: 1-2 minutes
- **Total runtime: ~20-30 minutes**

## Key Results Files

### Tables (outputs/tables/)
- `baseline_results.csv`: Main scenario results (Table 4 in paper)
- `sensitivity_discount.csv`: Discount rate sensitivity (Table 5)  
- `sensitivity_growth.csv`: Growth rate sensitivity (Table 6)
- `monte_carlo_summary.csv`: Stochastic simulation results (Table 7)
- `policy_interventions.csv`: Policy scenario analysis

### Figures (outputs/figures/)
- `discount_sensitivity.png`: Figure 1 - Discount rate sensitivity
- `growth_sensitivity.png`: Figure 2 - Growth rate sensitivity  
- `monte_carlo_distribution.png`: Figure 3 - NPV distribution
- `policy_comparison.png`: Policy intervention comparison

## Data Sources

All data sources are publicly available:

1. **India Time Use Survey 2019**
   - Source: Ministry of Statistics and Programme Implementation (MOSPI)
   - URL: http://mospi.nic.in/time-use-survey
   - Used for: Time allocation parameters (Table 2)

2. **Minimum Wage Database**
   - Source: Labour Bureau, Government of India
   - URL: https://labour.gov.in/minimum-wages  
   - Used for: Wage proxy construction (Table 3)

3. **Consumer Price Index & Financial Data**
   - Source: Reserve Bank of India (RBI) / MOSPI
   - URL: https://rbi.org.in/Scripts/AnnualPublications.aspx
   - Used for: Discount rates and inflation adjustments

See `data/README_data.md` for detailed data documentation and processing notes.

## Computational Details

### Software Environment
- **Language:** Python 3.8+
- **Key Dependencies:** NumPy 1.21+, Pandas 1.3+, SciPy 1.7+, Matplotlib 3.4+
- **Random Seed:** 20250901 (for Monte Carlo reproducibility)
- **Platform Tested:** Linux (Ubuntu 20.04), macOS (Big Sur), Windows 10

### Mathematical Framework
- Present value calculations use numpy financial functions with precision verification
- Monte Carlo simulations employ scipy.stats for parameter sampling
- All results are validated against hand calculations for key test cases

### Validation and Testing
```bash
python -m pytest tests/ -v
```
Runs comprehensive test suite including:
- Mathematical function accuracy tests
- Parameter validation checks  
- Monte Carlo convergence tests
- Output format verification

## Troubleshooting

### Common Issues

**Issue:** Import errors for scientific libraries
**Solution:** Ensure you're using the correct Python environment with all dependencies installed

**Issue:** Monte Carlo simulation runs slowly
**Solution:** Reduce iterations in config.py for testing (restore to 10,000 for full replication)

**Issue:** Figure generation fails
**Solution:** Check matplotlib backend settings and ensure GUI libraries if needed

**Issue:** Numerical precision differences
**Solution:** Small differences (<0.1%) are expected across platforms; see validation tolerances in tests/

See `docs/troubleshooting.md` for additional solutions.

## Citation

If you use this replication package, please cite:

```bibtex
@article{ranjan2025unpaid,
  title={Economic Valuation of Unpaid Labor in Indian Marriages: Complete Mathematical Framework and Transparency Volume},
  author={Ranjan, Ashish},
  journal={Independent Research Series},
  year={2025},
  doi={[DOI will be assigned]},
  url={https://github.com/ashishrjsingh/unpaid-labor-valuation}
}
```

## License and Terms

This replication package is released under Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to:
- Share: copy and redistribute the material
- Adapt: remix, transform, and build upon the material
- Commercial use is permitted

Attribution required. See LICENSE file for complete terms.

## Contact and Support

**Author:** Ashish Ranjan  
**Email:** ashishrjsingh786@gmail.com  
**GitHub:** [@ashishrjsingh](https://github.com/ashishrjsingh)  
**Issues:** Please report issues through GitHub Issues tab

## Acknowledgments

This research uses publicly available data from:
- Ministry of Statistics and Programme Implementation (MOSPI), Government of India
- Labour Bureau, Government of India  
- Reserve Bank of India (RBI)

Special acknowledgment to the feminist economics research community whose theoretical contributions enabled this quantitative framework.

## Version History

- **v1.0** (September 2025): Initial release with complete replication materials
- **v1.1** (Planned): Updates based on peer review feedback
- **v2.0** (Planned): Extended analysis with regional stratification

---

**Last Updated:** September 2, 2025  
**Repository Status:** Active Development  
**Replication Status:** Fully Reproducible
