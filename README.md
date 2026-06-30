 # U.S. Income Inequality Analyzer                                                                 
                                                                                                    
  **How unequal is income in America — and what would a wealth tax do about it?**                   
                                                                                                    
  **[Live Dashboard →](https://public.tableau.com/app/profile/favianesi.garcia/viz/IncomeInequality_17813089695540/IncomeInequalityDashboard)**                                                       
                                                                                                  
  ---

  ## The Policy Question

  The U.S. Gini coefficient has risen from 0.403 in 1980 to 0.498 in 2025. The top 1% now
  earns more than the entire bottom 50% combined. This project measures that trend and
  models the impact of a 1% wealth tax on incomes above $10M redistributed to the bottom 50%.

  ---

  ## Key Findings

  | Finding | Result |
  |---|---|
  | Gini Index change (1980–2025) | +0.095 |
  | Top 1% income share (2025) | 22.4% |
  | Bottom 50% income share (2025) | 14.1% |
  | Top 1% to Bottom 50% ratio | 1.59x |
  | Projected Gini after wealth tax | ~0.497 |
  | Gain for bottom 50% | +0.13 percentage points/yr |

  ---

  ## Project Structure

  income_inequality/
  ├── data/
  │   ├── income_inequality.csv        # Raw data (1980–2025)
  │   └── income_inequality_final.csv  # Processed data with wealth tax simulation
  ├── analyze.py                       # Python data pipeline
  └── README.md

  ---

  ## Methodology

  **Gini Coefficient:** Measures income inequality on a 0–1 scale. 0 = perfect equality,
  1 = perfect inequality. Source: U.S. Census Bureau / World Inequality Database.

  **Wealth Tax Model:**
  - 1% annual tax on income above $10M threshold
  - 60% of top 1% income assumed above threshold
  - Revenue redistributed equally to bottom 50%
  - Gini reduction estimated at 0.4 points per 1% redistributed

  **Note:** 2024–2025 figures are projections based on trend. Official Census data
  has a 1–2 year publication lag.

  ---

  ## Data Sources

  | Source | Data |
  |---|---|
  | U.S. Census Bureau | Gini coefficient (1980–2022) |
  | World Inequality Database | Income share by group |

  ---

  *Built for research and education. Not financial or policy advice.*
