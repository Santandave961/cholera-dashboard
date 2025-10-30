# cholera-dashboard
Cholera Outbreak  Project
A comprehensive data science project for analyzing global cholera outbreak patterns, trends and temporal dynamics using WHO data


Overview
This project provides in depth analysis of cholera outbreaks across multiple countries including:
- Statistical summary and regional comparisons.
- Case fatality rate (CFR) analysis
- Time series analysis with trend detection
- Outbreak wave identification.
- Interactive visualizations.


Features
Core Analytics
- Summary Statistics: Total cases, deaths, CFR and country level metrics.
- Regional Analysis: WHO region comparisons and trends.
- Mortality Analysis: High CFR countries and risk factors.
- Temporal Patterns: Week-by-week progression and moving averages.

Visualizations
- Regional distribution charts(cases and death)
- Top affected countries ranking.
- Case fatality rate analysis.
- Temporal overview with rolling averages.
- Regional temporal comparisons
- Outbreak timeline (Gantt-style)


Time Series Analysis
- Weekly case and death estimates.
- 4 week moving averages.
- Outbreak wave detection.
- Peak activity identification.
- Trend analysis (increasing/decreasing)


Project Structure
cholera-outbreak-analysis/

cholera_analysis.py          # Main analysis script
cholera_adm0_public.csv      # Dataset
requirements.txt             # Python dependencies
README.md                    # Project documentation
LICENSE                      # MIT License
.gitignore                   # Git ignore file


output/                      # Generated visualizations
regional_distribution.png
top countries.png
cfr_analysis.png
temporal_overview.png
regional_temporal.png
outbreak_timeline.png

notebooks/                  # Jupyter notebook
exploratory_analysis.ipynb


