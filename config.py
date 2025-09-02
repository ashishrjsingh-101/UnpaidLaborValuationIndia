"""
Configuration and Parameters for Unpaid Labor Valuation Analysis

This module contains all parameters, constants, and configuration settings
used throughout the analysis. Centralizing these values ensures consistency
and facilitates sensitivity testing.

Author: Ashish Ranjan
Date: September 2025
"""

import os
from pathlib import Path

# =============================================================================
# PROJECT CONFIGURATION
# =============================================================================

# Project metadata
PROJECT_NAME = "Economic Valuation of Unpaid Labor"
AUTHOR = "Ashish Ranjan"
CONTACT = "ashishrjsingh786@gmail.com"
VERSION = "1.0"
DATE = "September 2025"

# Random seed for reproducibility
RANDOM_SEED = 20250901

# File paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"
LOGS_DIR = OUTPUTS_DIR / "logs"

# =============================================================================
# DATA PARAMETERS
# =============================================================================

# Time Use Survey 2019 - Time allocation (minutes per day)
TIME_ALLOCATION = {
    'food_preparation': {'female': 98, 'male': 12},
    'serving_food': {'female': 28, 'male': 3},
    'cleanup_meals': {'female': 34, 'male': 2},
    'cleaning_dwelling': {'female': 66, 'male': 8},
    'care_textiles': {'female': 30, 'male': 3},
    'gardening': {'female': 8, 'male': 4},
    'shopping': {'female': 30, 'male': 12},
    'childcare': {'female': 62, 'male': 18},
    'teaching_children': {'female': 15, 'male': 4},
    'adult_care': {'female': 35, 'male': 14},
    'other_domestic': {'female': 35, 'male': 14}
}

# Total daily unpaid work minutes
TOTAL_UNPAID_MINUTES = {
    'female': 441,
    'male': 94
}

# Emotional labor adjustment factor
EMOTIONAL_LABOR_PREMIUM = 0.20  # 20% adjustment for unmeasured mental load

# Annual hours conversion
DAYS_PER_YEAR = 365
MINUTES_PER_HOUR = 60

# =============================================================================
# WAGE PROXY PARAMETERS (₹ per hour)
# =============================================================================

WAGE_PROXIES = {
    'cooking_meal_prep': 25,      # Home cook/chef with skill premium
    'cleaning_maintenance': 20,    # Domestic worker
    'laundry_ironing': 18,        # Commercial laundry services
    'shopping': 15,               # Personal shopper (basic wage)
    'childcare': 30,              # Trained babysitter/childcare
    'adult_elderly_care': 28,     # Home healthcare aide
    'water_fuel_collection': 12,  # Manual labor
    'other_domestic_services': 15  # General domestic help
}

# =============================================================================
# FINANCIAL PARAMETERS
# =============================================================================

# Discount rate components (annual, decimal)
RISK_FREE_RATE = 0.072          # 10-year Government Securities yield
INFLATION_PREMIUM = 0.024       # Average CPI inflation 2020-2025
HOUSEHOLD_RISK_PREMIUM = 0.010  # Additional household risk

# Calculated discount rate
DISCOUNT_RATE = RISK_FREE_RATE + INFLATION_PREMIUM + HOUSEHOLD_RISK_PREMIUM  # 10.60%

# Growth rate (annual, decimal)
WAGE_GROWTH_ASI = 0.062         # ASI wage growth 2015-2024
WAGE_GROWTH_EPFO = 0.058        # EPFO payroll growth 2020-2025
CONSERVATIVE_ADJUSTMENT = -0.002 # Conservative adjustment

# Calculated growth rate
GROWTH_RATE = (WAGE_GROWTH_ASI + WAGE_GROWTH_EPFO) / 2 + CONSERVATIVE_ADJUSTMENT  # 6.00%

# Time horizon
TIME_HORIZON_YEARS = 55         # Average marriage duration

# =============================================================================
# SCENARIO PARAMETERS
# =============================================================================

# Household expense scenarios (annual ₹)
MALE_ANNUAL_EXPENSES = 945_000

# Salary scenarios (annual ₹)
FEMALE_ANNUAL_SALARY = 1_345_000
MALE_SALARY_PREMIUM = 0.35      # 35% premium for male salary
MALE_ANNUAL_SALARY = int(FEMALE_ANNUAL_SALARY * (1 + MALE_SALARY_PREMIUM))

# Transfer scenarios
SALARY_TRANSFER_RATE = 0.50     # 50% of female salary transferred to male

# Lifecycle costs (₹)
LIFECYCLE_COST_LUMP = 5_000_000  # Maternal healthcare and related costs
LIFECYCLE_DISCOUNT_YEAR = 3      # Year when lifecycle costs are incurred

# Asset transfer scenarios (₹)
ASSET_TRANSFER_MARRIAGE = 1_500_000  # Property/asset transfer at marriage

# =============================================================================
# MONTE CARLO SIMULATION PARAMETERS
# =============================================================================

# Number of iterations
MC_ITERATIONS = 10_000

# Parameter uncertainty distributions (normal distribution parameters)
MC_PARAMS = {
    'discount_rate': {
        'mean': DISCOUNT_RATE,
        'std': 0.015,
        'min': 0.05,
        'max': 0.15
    },
    'growth_rate': {
        'mean': GROWTH_RATE,
        'std': 0.012,
        'min': 0.02,
        'max': 0.10
    },
    'hours_multiplier': {
        'mean': 1.0,
        'std': 0.10,
        'min': 0.70,
        'max': 1.30
    },
    'wage_multiplier': {
        'mean': 1.0,
        'std': 0.10,
        'min': 0.80,
        'max': 1.30
    },
    'lifecycle_cost': {
        'mean': LIFECYCLE_COST_LUMP,
        'std': 0.15 * LIFECYCLE_COST_LUMP,
        'min': 0.5 * LIFECYCLE_COST_LUMP,
        'max': 1.5 * LIFECYCLE_COST_LUMP
    }
}

# Convergence criteria
MC_CONVERGENCE_TOLERANCE = 5_000  # ₹5,000 standard error tolerance

# =============================================================================
# SENSITIVITY ANALYSIS PARAMETERS
# =============================================================================

# Discount rate sensitivity range
DISCOUNT_RATE_RANGE = [0.05, 0.07, 0.08, 0.106, 0.12, 0.14]

# Growth rate sensitivity range  
GROWTH_RATE_RANGE = [0.00, 0.03, 0.06, 0.08]

# Hours variation for sensitivity (percentage changes)
HOURS_SENSITIVITY_RANGE = [-0.30, -0.20, -0.10, 0.00, 0.10, 0.20, 0.30]

# Wage variation for sensitivity (percentage changes)
WAGE_SENSITIVITY_RANGE = [-0.25, -0.15, -0.10, 0.00, 0.10, 0.15, 0.25]

# =============================================================================
# POLICY ANALYSIS PARAMETERS
# =============================================================================

# Progressive wage growth scenario
POLICY_FEMALE_GROWTH_RATE = 0.08    # 8% growth for female-dominated sectors
POLICY_MALE_GROWTH_RATE = 0.06      # 6% general economic growth
POLICY_TRANSITION_YEARS = 20        # Years of differential growth

# Care infrastructure scenario
CARE_INFRASTRUCTURE_HOUR_REDUCTION = 0.30  # 30% reduction in unpaid hours
CARE_INFRASTRUCTURE_PARTICIPATION_INCREASE = 0.40  # 40% increase in market participation

# Asset transfer scenario
POLICY_ASSET_TRANSFER = 1_500_000   # ₹1.5 million asset transfer

# =============================================================================
# OUTPUT FORMATTING PARAMETERS
# =============================================================================

# Number formatting
CURRENCY_FORMAT = "₹{:,.0f}"
PERCENTAGE_FORMAT = "{:.1%}"
DECIMAL_PLACES = 2

# Figure parameters
FIGURE_SIZE = (10, 6)
FIGURE_DPI = 300
FIGURE_FORMAT = 'png'

# Table parameters
CSV_ENCODING = 'utf-8'

# =============================================================================
# VALIDATION PARAMETERS
# =============================================================================

# Tolerance for numerical comparisons (for testing)
NUMERICAL_TOLERANCE = 1e-6

# Expected result ranges for validation
EXPECTED_RANGES = {
    'baseline_pv_unpaid': (580_000, 590_000),
    'growth_pv_unpaid': (1_450_000, 1_470_000),
    'net_pv_non_earning': (-3_350_000, -3_250_000),
    'mc_probability_female_advantage': (0.0, 0.10)
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_output_directories():
    """Create all necessary output directories."""
    directories = [
        DATA_DIR / "processed",
        OUTPUTS_DIR,
        FIGURES_DIR,
        TABLES_DIR,
        LOGS_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

def get_annual_hours(minutes_per_day):
    """Convert daily minutes to annual hours."""
    return (minutes_per_day * DAYS_PER_YEAR) / MINUTES_PER_HOUR

def apply_emotional_labor_adjustment(hours):
    """Apply emotional labor premium to hours."""
    return hours * (1 + EMOTIONAL_LABOR_PREMIUM)

def format_currency(amount):
    """Format amount as Indian currency."""
    return CURRENCY_FORMAT.format(amount)

def format_percentage(rate):
    """Format rate as percentage."""
    return PERCENTAGE_FORMAT.format(rate)

# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================

def validate_parameters():
    """Validate all parameters are within reasonable ranges."""
    assert 0 < DISCOUNT_RATE < 0.20, f"Discount rate {DISCOUNT_RATE} out of range"
    assert 0 <= GROWTH_RATE < 0.15, f"Growth rate {GROWTH_RATE} out of range"
    assert TIME_HORIZON_YEARS > 0, "Time horizon must be positive"
    assert MC_ITERATIONS >= 1000, "Monte Carlo iterations too low"
    assert 0 <= EMOTIONAL_LABOR_PREMIUM <= 0.50, "Emotional labor premium out of range"
    
    print("✓ All parameters validated successfully")

if __name__ == "__main__":
    # Run validation when script is executed directly
    validate_parameters()
    create_output_directories()
    print(f"Configuration loaded for {PROJECT_NAME} v{VERSION}")
    print(f"Author: {AUTHOR}")
    print(f"Random seed: {RANDOM_SEED}")
    print(f"Key parameters:")
    print(f"  Discount rate: {format_percentage(DISCOUNT_RATE)}")
    print(f"  Growth rate: {format_percentage(GROWTH_RATE)}")
    print(f"  Time horizon: {TIME_HORIZON_YEARS} years")
    print(f"  Monte Carlo iterations: {MC_ITERATIONS:,}")
