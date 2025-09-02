#!/bin/bash
#
# Complete Replication Script for Economic Valuation of Unpaid Labor
# Executes all analysis steps in sequence
#
# Usage: bash run_all_analysis.sh
#
# Author: Ashish Ranjan
# Date: September 2025

echo "=============================================="
echo "Economic Valuation of Unpaid Labor - Complete Replication"
echo "Study: Ranjan (2025)"
echo "Started at: $(date)"
echo "=============================================="

# Check if virtual environment is activated
if [[ "$VIRTUAL_ENV" != "" ]] || [[ "$CONDA_DEFAULT_ENV" != "" ]]; then
    echo "✓ Virtual environment detected: $VIRTUAL_ENV$CONDA_DEFAULT_ENV"
else
    echo "⚠ Warning: No virtual environment detected"
    echo "  Consider activating the project environment first"
    read -p "Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create output directories if they don't exist
echo "Creating output directories..."
mkdir -p outputs/tables
mkdir -p outputs/figures
mkdir -p outputs/logs

# Set random seed for reproducibility
export PYTHONHASHSEED=20250901

# Start timing
start_time=$(date +%s)

echo ""
echo "Step 1/6: Data Preparation"
echo "----------------------------------------"
python scripts/01_data_preparation.py 2>&1 | tee outputs/logs/01_data_prep.log
if [ $? -eq 0 ]; then
    echo "✓ Data preparation completed successfully"
else
    echo "✗ Data preparation failed. Check outputs/logs/01_data_prep.log"
    exit 1
fi

echo ""
echo "Step 2/6: Baseline Analysis"
echo "----------------------------------------"
python scripts/02_baseline_analysis.py 2>&1 | tee outputs/logs/02_baseline.log
if [ $? -eq 0 ]; then
    echo "✓ Baseline analysis completed successfully"
else
    echo "✗ Baseline analysis failed. Check outputs/logs/02_baseline.log"
    exit 1
fi

echo ""
echo "Step 3/6: Sensitivity Analysis"
echo "----------------------------------------"
python scripts/03_sensitivity_tests.py 2>&1 | tee outputs/logs/03_sensitivity.log
if [ $? -eq 0 ]; then
    echo "✓ Sensitivity analysis completed successfully"
else
    echo "✗ Sensitivity analysis failed. Check outputs/logs/03_sensitivity.log"
    exit 1
fi

echo ""
echo "Step 4/6: Monte Carlo Simulations"
echo "----------------------------------------"
echo "Running 10,000 iterations (this may take 8-12 minutes)..."
python scripts/04_monte_carlo_sim.py 2>&1 | tee outputs/logs/04_monte_carlo.log
if [ $? -eq 0 ]; then
    echo "✓ Monte Carlo simulations completed successfully"
else
    echo "✗ Monte Carlo simulations failed. Check outputs/logs/04_monte_carlo.log"
    exit 1
fi

echo ""
echo "Step 5/6: Policy Analysis"
echo "----------------------------------------"
python scripts/05_policy_modeling.py 2>&1 | tee outputs/logs/05_policy.log
if [ $? -eq 0 ]; then
    echo "✓ Policy analysis completed successfully"
else
    echo "✗ Policy analysis failed. Check outputs/logs/05_policy.log"
    exit 1
fi

echo ""
echo "Step 6/6: Generate Figures"
echo "----------------------------------------"
python scripts/06_generate_figures.py 2>&1 | tee outputs/logs/06_figures.log
if [ $? -eq 0 ]; then
    echo "✓ Figure generation completed successfully"
else
    echo "✗ Figure generation failed. Check outputs/logs/06_figures.log"
    exit 1
fi

# Calculate total runtime
end_time=$(date +%s)
runtime=$((end_time-start_time))
minutes=$((runtime / 60))
seconds=$((runtime % 60))

echo ""
echo "=============================================="
echo "REPLICATION COMPLETED SUCCESSFULLY"
echo "=============================================="
echo "Total runtime: ${minutes}m ${seconds}s"
echo "Completed at: $(date)"
echo ""
echo "Generated files:"
echo "  Tables: outputs/tables/*.csv"
echo "  Figures: outputs/figures/*.png"
echo "  Logs: outputs/logs/*.log"
echo ""
echo "Key results files:"
echo "  - baseline_results.csv (Table 4 in paper)"
echo "  - sensitivity_discount.csv (Table 5)"  
echo "  - sensitivity_growth.csv (Table 6)"
echo "  - monte_carlo_summary.csv (Table 7)"
echo "  - discount_sensitivity.png (Figure 1)"
echo "  - growth_sensitivity.png (Figure 2)"
echo "  - monte_carlo_distribution.png (Figure 3)"
echo ""
echo "To verify results match paper, run:"
echo "  python tests/validation_suite.py"
echo "=============================================="
