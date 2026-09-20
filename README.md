# Social-Media-Impact-on-Life-Data-Analyst-Project

## Overview
End-to-end portfolio project using ** SQL + Python** to analyze the relationship between social-media usage, sleep, stress, mental health, and academic performance among 4,500 students.

## Dataset
- 4,500 rows
- 16 columns
- 0 duplicate rows
- 46 missing stress values
- 85 missing GPA values

## Analytical Questions
1. Which platforms are most used?
2. How does daily usage relate to sleep?
3. How does daily usage relate to GPA?
4. How does usage relate to mental health and stress?
5. How do late-night users differ?
6. How do usage bands and social-comparison frequency differ?
7. Which segments show higher-risk profiles?

## Key Findings
- Average daily usage: **5.24 hours**
- Average sleep: **6.75 hours**
- Average stress: **14.80**
- Average mental health index: **80.78**
- Average GPA: **3.43**

Observed correlations:
- Usage vs sleep: **-0.716**
- Usage vs stress: **+0.754**
- Usage vs mental health: **-0.850**
- Usage vs GPA: **-0.710**
- Stress vs GPA: **-0.651**

Overall impact groups:
- Beneficial: 3,681 students; 4.42h average usage; 7.03h sleep; 11.16 stress; 84.26 mental-health index; 3.55 GPA
- Neutral: 654 students; 8.50h usage; 5.48h sleep; 22.30 stress; 63.42 mental-health index; 3.00 GPA
- Negative: 165 students; 12.25h usage; 4.23h sleep; 31.12 stress; 47.13 mental-health index; 2.54 GPA

These are **descriptive associations within this dataset, not causal effects**.

## SQL
`sql/analysis_queries.sql` contains PostgreSQL table creation, data-quality checks, KPI queries, segmentation, usage bands, late-night analysis, high-risk profile filtering, and `CORR()` analysis.

## Python
`python/analysis.py` is the starting point for Python EDA. Generated PNGs are stored in `visualizations/`.

## Visualizations
- Platform distribution
- Usage vs GPA
- Usage vs sleep
- Usage band vs mental health
- Overall impact vs usage
- Correlation matrix
- Late-night usage outcomes

## Conclusion
The analysis shows strong descriptive relationships between social-media usage and several student outcomes. Higher usage is associated in this dataset with shorter sleep, higher perceived stress, lower mental-health-index values, and lower GPA.
