-- Social Media Impact on Life | PostgreSQL
DROP TABLE IF EXISTS social_media_impact;
CREATE TABLE social_media_impact (
 student_id VARCHAR(30) PRIMARY KEY, age INT, gender VARCHAR(50),
 academic_level VARCHAR(50), primary_platform VARCHAR(50),
 daily_usage_hours NUMERIC(5,2), weekend_extra_hours NUMERIC(5,2),
 device_type VARCHAR(50), sleep_duration_hours NUMERIC(5,2),
 sleep_quality_score INT, late_night_usage BOOLEAN,
 social_comparison_frequency VARCHAR(30), perceived_stress_score NUMERIC(6,2),
 mental_health_index INT, academic_performance_gpa NUMERIC(4,2),
 overall_impact VARCHAR(30)
);
-- COPY social_media_impact FROM '/path/to/Social_media_impact_on_life.csv'
-- WITH (FORMAT CSV, HEADER TRUE);

-- Data quality
SELECT COUNT(*) AS total_rows FROM social_media_impact;
SELECT COUNT(*) AS duplicate_student_ids FROM
 (SELECT student_id FROM social_media_impact GROUP BY student_id HAVING COUNT(*)>1) d;
SELECT COUNT(*) FILTER(WHERE perceived_stress_score IS NULL) AS missing_stress,
       COUNT(*) FILTER(WHERE academic_performance_gpa IS NULL) AS missing_gpa
FROM social_media_impact;

-- Executive KPIs
SELECT COUNT(*) total_students,
 ROUND(AVG(daily_usage_hours),2) avg_daily_usage_hours,
 ROUND(AVG(sleep_duration_hours),2) avg_sleep_hours,
 ROUND(AVG(perceived_stress_score),2) avg_stress,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa,
 ROUND(100*AVG(CASE WHEN late_night_usage THEN 1 ELSE 0 END),2) late_night_pct
FROM social_media_impact;

-- Platform analysis
SELECT primary_platform, COUNT(*) students,
 ROUND(AVG(daily_usage_hours),2) avg_usage,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa
FROM social_media_impact GROUP BY primary_platform ORDER BY students DESC;

-- Academic level analysis
SELECT academic_level, COUNT(*) students,
 ROUND(AVG(daily_usage_hours),2) avg_usage,
 ROUND(AVG(sleep_duration_hours),2) avg_sleep,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa
FROM social_media_impact GROUP BY academic_level ORDER BY students DESC;

-- Overall impact
SELECT overall_impact, COUNT(*) students,
 ROUND(100*COUNT(*)/SUM(COUNT(*)) OVER(),2) pct_students,
 ROUND(AVG(daily_usage_hours),2) avg_usage,
 ROUND(AVG(sleep_duration_hours),2) avg_sleep,
 ROUND(AVG(perceived_stress_score),2) avg_stress,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa
FROM social_media_impact GROUP BY overall_impact ORDER BY students DESC;

-- Usage bands
WITH x AS (
 SELECT *, CASE WHEN daily_usage_hours<3 THEN 'Low (<3h)'
 WHEN daily_usage_hours<6 THEN 'Moderate (3-6h)'
 WHEN daily_usage_hours<9 THEN 'High (6-9h)'
 ELSE 'Very High (9h+)' END usage_band
 FROM social_media_impact
)
SELECT usage_band, COUNT(*) students,
 ROUND(AVG(sleep_duration_hours),2) avg_sleep,
 ROUND(AVG(perceived_stress_score),2) avg_stress,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa
FROM x GROUP BY usage_band;

-- Late-night usage
SELECT late_night_usage, COUNT(*) students,
 ROUND(AVG(sleep_duration_hours),2) avg_sleep,
 ROUND(AVG(perceived_stress_score),2) avg_stress,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa
FROM social_media_impact GROUP BY late_night_usage;

-- Social comparison
SELECT social_comparison_frequency, COUNT(*) students,
 ROUND(AVG(perceived_stress_score),2) avg_stress,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa
FROM social_media_impact GROUP BY social_comparison_frequency;

-- Segmentation
SELECT gender, academic_level, COUNT(*) students,
 ROUND(AVG(daily_usage_hours),2) avg_usage,
 ROUND(AVG(mental_health_index),2) avg_mental_health,
 ROUND(AVG(academic_performance_gpa),2) avg_gpa
FROM social_media_impact GROUP BY gender, academic_level ORDER BY students DESC;

-- High-usage / low-sleep / high-stress profile
SELECT * FROM social_media_impact
WHERE daily_usage_hours>=9 AND sleep_duration_hours<6 AND perceived_stress_score>=20
ORDER BY perceived_stress_score DESC, daily_usage_hours DESC;

-- Correlations
SELECT ROUND(CORR(daily_usage_hours,sleep_duration_hours)::numeric,3) usage_vs_sleep,
 ROUND(CORR(daily_usage_hours,perceived_stress_score)::numeric,3) usage_vs_stress,
 ROUND(CORR(daily_usage_hours,mental_health_index)::numeric,3) usage_vs_mental_health,
 ROUND(CORR(daily_usage_hours,academic_performance_gpa)::numeric,3) usage_vs_gpa,
 ROUND(CORR(perceived_stress_score,academic_performance_gpa)::numeric,3) stress_vs_gpa
FROM social_media_impact;
