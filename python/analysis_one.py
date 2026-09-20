1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
import warnings

warnings.filterwarnings("ignore")

# Plotting configuration
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


# ============================================================
# 2. LOAD DATASET
# ============================================================

file_path = "Social_media_impact_on_life.csv"

df = pd.read_csv(file_path)


# ============================================================
# 3. INITIAL DATASET UNDERSTANDING
# ============================================================

print("=" * 70)
print("DATASET OVERVIEW")
print("=" * 70)

print("\nDataset Shape:")
print(df.shape)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])


# Display first 5 rows
print("\nFirst 5 Records:")
print(df.head())


# Display last 5 rows
print("\nLast 5 Records:")
print(df.tail())


# ============================================================
# 4. COLUMN INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("COLUMN INFORMATION")
print("=" * 70)

print(df.info())


# Column names
print("\nColumn Names:")
for column in df.columns:
    print(column)


# ============================================================
# 5. DATA TYPES
# ============================================================

print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)

print(df.dtypes)


# Count columns by data type
print("\nData Type Distribution:")
print(df.dtypes.value_counts())


# ============================================================
# 6. UNIQUE VALUES
# ============================================================

print("\n" + "=" * 70)
print("UNIQUE VALUE ANALYSIS")
print("=" * 70)

for column in df.columns:

    print(
        f"\n{column}: "
        f"{df[column].nunique()} unique values"
    )


# ============================================================
# 7. MISSING VALUE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("MISSING VALUE ANALYSIS")
print("=" * 70)

missing_values = df.isnull().sum()

missing_percentage = (
    df.isnull().sum()
    / len(df)
    * 100
)

missing_summary = pd.DataFrame({
    "Missing_Values": missing_values,
    "Missing_Percentage": missing_percentage
})

missing_summary = (
    missing_summary
    .sort_values(
        "Missing_Values",
        ascending=False
    )
)

print(missing_summary)


# Visualize missing values
missing_plot = (
    missing_summary[
        missing_summary["Missing_Values"] > 0
    ]
)

if not missing_plot.empty:

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=missing_plot.index,
        y=missing_plot["Missing_Values"]
    )

    plt.title("Missing Values by Column")
    plt.xlabel("Column")
    plt.ylabel("Number of Missing Values")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# ============================================================
# 8. DUPLICATE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("DUPLICATE ANALYSIS")
print("=" * 70)

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)


# Duplicate Student IDs
if "Student_ID" in df.columns:

    duplicate_student_ids = (
        df["Student_ID"]
        .duplicated()
        .sum()
    )

    print(
        "Duplicate Student IDs:",
        duplicate_student_ids
    )


# ============================================================
# 9. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)

print(
    df.describe()
    .round(2)
)


# Numerical columns only
numeric_columns = df.select_dtypes(
    include=np.number
).columns

print("\nNumerical Columns:")
print(list(numeric_columns))


# Categorical columns
categorical_columns = df.select_dtypes(
    include="object"
).columns

print("\nCategorical Columns:")
print(list(categorical_columns))


# ============================================================
# 10. NUMERICAL VARIABLE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("NUMERICAL VARIABLE SUMMARY")
print("=" * 70)

numerical_summary = pd.DataFrame({

    "Mean":
        df[numeric_columns].mean(),

    "Median":
        df[numeric_columns].median(),

    "Std_Dev":
        df[numeric_columns].std(),

    "Minimum":
        df[numeric_columns].min(),

    "Maximum":
        df[numeric_columns].max(),

    "Missing":
        df[numeric_columns].isnull().sum()

})

print(
    numerical_summary
    .round(2)
)


# ============================================================
# 11. CATEGORICAL VARIABLE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("CATEGORICAL VARIABLE ANALYSIS")
print("=" * 70)


# Gender
if "Gender" in df.columns:

    print("\nGender Distribution:")
    print(
        df["Gender"]
        .value_counts()
    )


# Academic level
if "Academic_Level" in df.columns:

    print("\nAcademic Level Distribution:")
    print(
        df["Academic_Level"]
        .value_counts()
    )


# Platform
if "Primary_Platform" in df.columns:

    print("\nPrimary Platform Distribution:")
    print(
        df["Primary_Platform"]
        .value_counts()
    )


# Overall impact
if "Overall_Impact" in df.columns:

    print("\nOverall Impact Distribution:")
    print(
        df["Overall_Impact"]
        .value_counts()
    )


# ============================================================
# 12. PLATFORM DISTRIBUTION
# ============================================================

if "Primary_Platform" in df.columns:

    platform_counts = (
        df["Primary_Platform"]
        .value_counts()
    )

    print("\nPlatform Distribution:")
    print(platform_counts)

    plt.figure(figsize=(10, 6))

    sns.countplot(
        data=df,
        y="Primary_Platform",
        order=platform_counts.index
    )

    plt.title(
        "Distribution of Students by Primary Social Media Platform"
    )

    plt.xlabel("Number of Students")
    plt.ylabel("Platform")

    plt.tight_layout()
    plt.show()


# ============================================================
# 13. GENDER DISTRIBUTION
# ============================================================

if "Gender" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Gender",
        order=df["Gender"].value_counts().index
    )

    plt.title("Student Distribution by Gender")

    plt.xlabel("Gender")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 14. ACADEMIC LEVEL DISTRIBUTION
# ============================================================

if "Academic_Level" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Academic_Level",
        order=df["Academic_Level"].value_counts().index
    )

    plt.title("Student Distribution by Academic Level")

    plt.xlabel("Academic Level")
    plt.ylabel("Number of Students")

    plt.xticks(rotation=15)

    plt.tight_layout()
    plt.show()


# ============================================================
# 15. OVERALL IMPACT DISTRIBUTION
# ============================================================

if "Overall_Impact" in df.columns:

    impact_counts = (
        df["Overall_Impact"]
        .value_counts()
    )

    print("\nOverall Impact:")
    print(impact_counts)

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Overall_Impact",
        order=impact_counts.index
    )

    plt.title(
        "Distribution of Overall Social Media Impact"
    )

    plt.xlabel("Overall Impact")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 16. DAILY SOCIAL MEDIA USAGE DISTRIBUTION
# ============================================================

if "Daily_Usage_Hours" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Daily_Usage_Hours"],
        bins=20,
        kde=True
    )

    plt.title(
        "Distribution of Daily Social Media Usage"
    )

    plt.xlabel("Daily Usage (Hours)")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 17. SLEEP DURATION DISTRIBUTION
# ============================================================

if "Sleep_Duration_Hours" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Sleep_Duration_Hours"],
        bins=20,
        kde=True
    )

    plt.title(
        "Distribution of Sleep Duration"
    )

    plt.xlabel("Sleep Duration (Hours)")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 18. STRESS SCORE DISTRIBUTION
# ============================================================

if "Perceived_Stress_Score" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Perceived_Stress_Score"],
        bins=20,
        kde=True
    )

    plt.title(
        "Distribution of Perceived Stress Score"
    )

    plt.xlabel("Perceived Stress Score")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 19. MENTAL HEALTH INDEX DISTRIBUTION
# ============================================================

if "Mental_Health_Index" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Mental_Health_Index"],
        bins=20,
        kde=True
    )

    plt.title(
        "Distribution of Mental Health Index"
    )

    plt.xlabel("Mental Health Index")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 20. GPA DISTRIBUTION
# ============================================================

if "Academic_Performance_GPA" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["Academic_Performance_GPA"],
        bins=20,
        kde=True
    )

    plt.title(
        "Distribution of Academic Performance GPA"
    )

    plt.xlabel("GPA")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


# ============================================================
# 21. FEATURE ENGINEERING — USAGE BANDS
# ============================================================

df["Usage_Band"] = pd.cut(

    df["Daily_Usage_Hours"],

    bins=[
        -np.inf,
        3,
        6,
        9,
        np.inf
    ],

    labels=[
        "Low (<3h)",
        "Moderate (3-6h)",
        "High (6-9h)",
        "Very High (9h+)"
    ],

    right=False
)

print("\nUsage Band Distribution:")
print(
    df["Usage_Band"]
    .value_counts()
)


# ============================================================
# 22. USAGE BAND VISUALIZATION
# ============================================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Usage_Band",
    order=[
        "Low (<3h)",
        "Moderate (3-6h)",
        "High (6-9h)",
        "Very High (9h+)"
    ]
)

plt.title(
    "Students by Daily Social Media Usage Band"
)

plt.xlabel("Usage Band")
plt.ylabel("Number of Students")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()


# ============================================================
# 23. USAGE BAND VS SLEEP
# ============================================================

usage_sleep = (
    df.groupby(
        "Usage_Band",
        observed=False
    )["Sleep_Duration_Hours"]
    .mean()
)

print("\nAverage Sleep by Usage Band:")
print(
    usage_sleep.round(2)
)


plt.figure(figsize=(10, 6))

sns.barplot(
    x=usage_sleep.index,
    y=usage_sleep.values
)

plt.title(
    "Average Sleep Duration by Social Media Usage Band"
)

plt.xlabel("Usage Band")
plt.ylabel("Average Sleep (Hours)")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()


# ============================================================
# 24. USAGE BAND VS STRESS
# ============================================================

usage_stress = (
    df.groupby(
        "Usage_Band",
        observed=False
    )["Perceived_Stress_Score"]
    .mean()
)

print("\nAverage Stress by Usage Band:")
print(
    usage_stress.round(2)
)


plt.figure(figsize=(10, 6))

sns.barplot(
    x=usage_stress.index,
    y=usage_stress.values
)

plt.title(
    "Average Stress Score by Social Media Usage Band"
)

plt.xlabel("Usage Band")
plt.ylabel("Average Stress Score")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()


# ============================================================
# 25. USAGE BAND VS MENTAL HEALTH
# ============================================================

usage_mental_health = (
    df.groupby(
        "Usage_Band",
        observed=False
    )["Mental_Health_Index"]
    .mean()
)

print("\nAverage Mental Health Index by Usage Band:")
print(
    usage_mental_health.round(2)
)


plt.figure(figsize=(10, 6))

sns.barplot(
    x=usage_mental_health.index,
    y=usage_mental_health.values
)

plt.title(
    "Average Mental Health Index by Social Media Usage Band"
)

plt.xlabel("Usage Band")
plt.ylabel("Average Mental Health Index")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()


# ============================================================
# 26. USAGE BAND VS GPA
# ============================================================

usage_gpa = (
    df.groupby(
        "Usage_Band",
        observed=False
    )["Academic_Performance_GPA"]
    .mean()
)

print("\nAverage GPA by Usage Band:")
print(
    usage_gpa.round(2)
)


plt.figure(figsize=(10, 6))

sns.barplot(
    x=usage_gpa.index,
    y=usage_gpa.values
)

plt.title(
    "Average GPA by Social Media Usage Band"
)

plt.xlabel("Usage Band")
plt.ylabel("Average GPA")

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()


# ============================================================
# 27. DAILY USAGE VS SLEEP
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Sleep_Duration_Hours",
    alpha=0.4
)

sns.regplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Sleep_Duration_Hours",
    scatter=False
)

plt.title(
    "Daily Social Media Usage vs Sleep Duration"
)

plt.xlabel("Daily Social Media Usage (Hours)")
plt.ylabel("Sleep Duration (Hours)")

plt.tight_layout()
plt.show()


# ============================================================
# 28. DAILY USAGE VS STRESS
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Perceived_Stress_Score",
    alpha=0.4
)

sns.regplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Perceived_Stress_Score",
    scatter=False
)

plt.title(
    "Daily Social Media Usage vs Perceived Stress"
)

plt.xlabel("Daily Social Media Usage (Hours)")
plt.ylabel("Perceived Stress Score")

plt.tight_layout()
plt.show()


# ============================================================
# 29. DAILY USAGE VS MENTAL HEALTH
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Mental_Health_Index",
    alpha=0.4
)

sns.regplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Mental_Health_Index",
    scatter=False
)

plt.title(
    "Daily Social Media Usage vs Mental Health Index"
)

plt.xlabel("Daily Social Media Usage (Hours)")
plt.ylabel("Mental Health Index")

plt.tight_layout()
plt.show()


# ============================================================
# 30. DAILY USAGE VS GPA
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Academic_Performance_GPA",
    alpha=0.4
)

sns.regplot(
    data=df,
    x="Daily_Usage_Hours",
    y="Academic_Performance_GPA",
    scatter=False
)

plt.title(
    "Daily Social Media Usage vs Academic GPA"
)

plt.xlabel("Daily Social Media Usage (Hours)")
plt.ylabel("Academic GPA")

plt.tight_layout()
plt.show()


# ============================================================
# 31. CORRELATION ANALYSIS
# ============================================================

correlation_columns = [

    "Age",
    "Daily_Usage_Hours",
    "Weekend_Extra_Hours",
    "Sleep_Duration_Hours",
    "Sleep_Quality_Score",
    "Perceived_Stress_Score",
    "Mental_Health_Index",
    "Academic_Performance_GPA"

]

correlation_matrix = (
    df[correlation_columns]
    .corr()
)

print("\n" + "=" * 70)
print("CORRELATION MATRIX")
print("=" * 70)

print(
    correlation_matrix
    .round(3)
)


# ============================================================
# 32. CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(12, 9))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title(
    "Correlation Heatmap of Key Variables"
)

plt.tight_layout()
plt.show()


# ============================================================
# 33. LATE-NIGHT USAGE ANALYSIS
# ============================================================

if "Late_Night_Usage" in df.columns:

    late_night_summary = (
        df.groupby("Late_Night_Usage")
        .agg(

            Students=(
                "Student_ID",
                "count"
            ),

            Avg_Usage=(
                "Daily_Usage_Hours",
                "mean"
            ),

            Avg_Sleep=(
                "Sleep_Duration_Hours",
                "mean"
            ),

            Avg_Stress=(
                "Perceived_Stress_Score",
                "mean"
            ),

            Avg_Mental_Health=(
                "Mental_Health_Index",
                "mean"
            ),

            Avg_GPA=(
                "Academic_Performance_GPA",
                "mean"
            )

        )
    )

    print("\n" + "=" * 70)
    print("LATE-NIGHT USAGE ANALYSIS")
    print("=" * 70)

    print(
        late_night_summary
        .round(2)
    )


# ============================================================
# 34. SOCIAL COMPARISON ANALYSIS
# ============================================================

if "Social_Comparison_Frequency" in df.columns:

    comparison_summary = (

        df.groupby(
            "Social_Comparison_Frequency"
        )

        .agg(

            Students=(
                "Student_ID",
                "count"
            ),

            Avg_Usage=(
                "Daily_Usage_Hours",
                "mean"
            ),

            Avg_Stress=(
                "Perceived_Stress_Score",
                "mean"
            ),

            Avg_Mental_Health=(
                "Mental_Health_Index",
                "mean"
            ),

            Avg_GPA=(
                "Academic_Performance_GPA",
                "mean"
            )

        )

    )

    print("\n" + "=" * 70)
    print("SOCIAL COMPARISON ANALYSIS")
    print("=" * 70)

    print(
        comparison_summary
        .round(2)
    )


# ============================================================
# 35. PLATFORM PERFORMANCE ANALYSIS
# ============================================================

platform_analysis = (

    df.groupby(
        "Primary_Platform"
    )

    .agg(

        Students=(
            "Student_ID",
            "count"
        ),

        Avg_Usage=(
            "Daily_Usage_Hours",
            "mean"
        ),

        Avg_Sleep=(
            "Sleep_Duration_Hours",
            "mean"
        ),

        Avg_Stress=(
            "Perceived_Stress_Score",
            "mean"
        ),

        Avg_Mental_Health=(
            "Mental_Health_Index",
            "mean"
        ),

        Avg_GPA=(
            "Academic_Performance_GPA",
            "mean"
        )

    )

    .sort_values(
        "Students",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("PLATFORM ANALYSIS")
print("=" * 70)

print(
    platform_analysis
    .round(2)
)


# ============================================================
# 36. ACADEMIC LEVEL ANALYSIS
# ============================================================

academic_analysis = (

    df.groupby(
        "Academic_Level"
    )

    .agg(

        Students=(
            "Student_ID",
            "count"
        ),

        Avg_Usage=(
            "Daily_Usage_Hours",
            "mean"
        ),

        Avg_Sleep=(
            "Sleep_Duration_Hours",
            "mean"
        ),

        Avg_Stress=(
            "Perceived_Stress_Score",
            "mean"
        ),

        Avg_Mental_Health=(
            "Mental_Health_Index",
            "mean"
        ),

        Avg_GPA=(
            "Academic_Performance_GPA",
            "mean"
        )

    )

    .sort_values(
        "Students",
        ascending=False
    )
)

print("\n" + "=" * 70)
print("ACADEMIC LEVEL ANALYSIS")
print("=" * 70)

print(
    academic_analysis
    .round(2)
)


# ============================================================
# 37. GENDER ANALYSIS
# ============================================================

gender_analysis = (

    df.groupby(
        "Gender"
    )

    .agg(

        Students=(
            "Student_ID",
            "count"
        ),

        Avg_Usage=(
            "Daily_Usage_Hours",
            "mean"
        ),

        Avg_Sleep=(
            "Sleep_Duration_Hours",
            "mean"
        ),

        Avg_Stress=(
            "Perceived_Stress_Score",
            "mean"
        ),

        Avg_Mental_Health=(
            "Mental_Health_Index",
            "mean"
        ),

        Avg_GPA=(
            "Academic_Performance_GPA",
            "mean"
        )

    )

)

print("\n" + "=" * 70)
print("GENDER ANALYSIS")
print("=" * 70)

print(
    gender_analysis
    .round(2)
)


# ============================================================
# 38. HIGH-USAGE STUDENT PROFILE
# ============================================================

high_usage_students = df[
    df["Daily_Usage_Hours"] >= 9
]

print("\n" + "=" * 70)
print("HIGH-USAGE STUDENTS")
print("=" * 70)

print(
    "Number of students:",
    len(high_usage_students)
)

print("\nAverage metrics:")

print(
    high_usage_students[
        [
            "Daily_Usage_Hours",
            "Sleep_Duration_Hours",
            "Perceived_Stress_Score",
            "Mental_Health_Index",
            "Academic_Performance_GPA"
        ]
    ]
    .mean()
    .round(2)
)


# ============================================================
# 39. HIGH-RISK PROFILE
# ============================================================

high_risk = df[
    (df["Daily_Usage_Hours"] >= 9)
    &
    (df["Sleep_Duration_Hours"] < 6)
    &
    (df["Perceived_Stress_Score"] >= 20)
]

print("\n" + "=" * 70)
print("HIGH-USAGE / LOW-SLEEP / HIGH-STRESS PROFILE")
print("=" * 70)

print(
    "Number of students:",
    len(high_risk)
)

print("\nPercentage of dataset:")

print(
    round(
        len(high_risk)
        / len(df)
        * 100,
        2
    ),
    "%"
)


# ============================================================
# 40. OVERALL IMPACT SUMMARY
# ============================================================

impact_summary = (

    df.groupby(
        "Overall_Impact"
    )

    .agg(

        Students=(
            "Student_ID",
            "count"
        ),

        Avg_Usage=(
            "Daily_Usage_Hours",
            "mean"
        ),

        Avg_Sleep=(
            "Sleep_Duration_Hours",
            "mean"
        ),

        Avg_Stress=(
            "Perceived_Stress_Score",
            "mean"
        ),

        Avg_Mental_Health=(
            "Mental_Health_Index",
            "mean"
        ),

        Avg_GPA=(
            "Academic_Performance_GPA",
            "mean"
        )

    )

)

impact_summary["Percentage"] = (
    impact_summary["Students"]
    / len(df)
    * 100
)

print("\n" + "=" * 70)
print("OVERALL IMPACT SUMMARY")
print("=" * 70)

print(
    impact_summary
    .round(2)
)


# ============================================================
# 41. BOXPLOTS — OUTLIER ANALYSIS
# ============================================================

boxplot_columns = [

    "Daily_Usage_Hours",
    "Sleep_Duration_Hours",
    "Sleep_Quality_Score",
    "Perceived_Stress_Score",
    "Mental_Health_Index",
    "Academic_Performance_GPA"

]

for column in boxplot_columns:

    plt.figure(figsize=(9, 5))

    sns.boxplot(
        y=df[column]
    )

    plt.title(
        f"Outlier Analysis — {column}"
    )

    plt.ylabel(column)

    plt.tight_layout()
    plt.show()


# ============================================================
# 42. IQR OUTLIER DETECTION
# ============================================================

print("\n" + "=" * 70)
print("OUTLIER SUMMARY")
print("=" * 70)

outlier_summary = []

for column in boxplot_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound)
        |
        (df[column] > upper_bound)
    ]

    outlier_summary.append({

        "Column": column,

        "Q1": Q1,

        "Q3": Q3,

        "IQR": IQR,

        "Lower_Bound": lower_bound,

        "Upper_Bound": upper_bound,

        "Outlier_Count": len(outliers),

        "Outlier_Percentage":
            len(outliers)
            / len(df)
            * 100

    })

outlier_summary = pd.DataFrame(
    outlier_summary
)

print(
    outlier_summary
    .round(2)
)


# ============================================================
# 43. EXECUTIVE KPI SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("EXECUTIVE KPI SUMMARY")
print("=" * 70)

print(
    f"Total Students: "
    f"{len(df):,}"
)

print(
    f"Average Daily Usage: "
    f"{df['Daily_Usage_Hours'].mean():.2f} hours"
)

print(
    f"Average Sleep Duration: "
    f"{df['Sleep_Duration_Hours'].mean():.2f} hours"
)

print(
    f"Average Sleep Quality: "
    f"{df['Sleep_Quality_Score'].mean():.2f}"
)

print(
    f"Average Stress Score: "
    f"{df['Perceived_Stress_Score'].mean():.2f}"
)

print(
    f"Average Mental Health Index: "
    f"{df['Mental_Health_Index'].mean():.2f}"
)

print(
    f"Average GPA: "
    f"{df['Academic_Performance_GPA'].mean():.2f}"
)

print(
    f"Late-Night Usage: "
    f"{df['Late_Night_Usage'].mean() * 100:.2f}%"
)


# ============================================================
# 44. EXPORT EDA OUTPUTS
# ============================================================

output_folder = "eda_outputs"

os.makedirs(
    output_folder,
    exist_ok=True
)


# Save numerical summary
numerical_summary.round(3).to_csv(
    f"{output_folder}/numerical_summary.csv"
)


# Save correlation matrix
correlation_matrix.round(3).to_csv(
    f"{output_folder}/correlation_matrix.csv"
)


# Save platform analysis
platform_analysis.round(3).to_csv(
    f"{output_folder}/platform_analysis.csv"
)


# Save academic analysis
academic_analysis.round(3).to_csv(
    f"{output_folder}/academic_level_analysis.csv"
)


# Save impact summary
impact_summary.round(3).to_csv(
    f"{output_folder}/impact_summary.csv"
)


# Save outlier analysis
outlier_summary.round(3).to_csv(
    f"{output_folder}/outlier_summary.csv"
)


print("\nEDA completed successfully.")

print(
    f"\nEDA output files saved in: "
    f"{output_folder}/"
)

# Generate visualizations with matplotlib only for maximum compatibility.
plt.rcParams.update({"figure.figsize": (9,6), "axes.grid": True})

# 1 platform distribution
s=df["Primary_Platform"].value_counts().sort_values()
fig,ax=plt.subplots(); ax.barh(s.index,s.values); ax.set_title("Students by Primary Social Media Platform")
ax.set_xlabel("Number of Students"); fig.tight_layout(); fig.savefig(os.path.join(out,"01_platform_distribution.png"),dpi=160); plt.close(fig)

# 2 usage vs GPA with simple linear trend
x=df["Daily_Usage_Hours"]; y=df["Academic_Performance_GPA"]
m=df[["Daily_Usage_Hours","Academic_Performance_GPA"]].dropna()
coef=np.polyfit(m["Daily_Usage_Hours"],m["Academic_Performance_GPA"],1)
fig,ax=plt.subplots(); ax.scatter(m["Daily_Usage_Hours"],m["Academic_Performance_GPA"],alpha=.25,s=12)
xx=np.linspace(m["Daily_Usage_Hours"].min(),m["Daily_Usage_Hours"].max(),100); ax.plot(xx,coef[0]*xx+coef[1])
ax.set_title("Daily Social Media Usage vs Academic GPA"); ax.set_xlabel("Daily Usage (hours)"); ax.set_ylabel("GPA")
fig.tight_layout(); fig.savefig(os.path.join(out,"02_usage_vs_gpa.png"),dpi=160); plt.close(fig)

# 3 usage vs sleep
m=df[["Daily_Usage_Hours","Sleep_Duration_Hours"]].dropna()
coef=np.polyfit(m["Daily_Usage_Hours"],m["Sleep_Duration_Hours"],1)
fig,ax=plt.subplots(); ax.scatter(m["Daily_Usage_Hours"],m["Sleep_Duration_Hours"],alpha=.25,s=12)
xx=np.linspace(m["Daily_Usage_Hours"].min(),m["Daily_Usage_Hours"].max(),100); ax.plot(xx,coef[0]*xx+coef[1])
ax.set_title("Daily Social Media Usage vs Sleep Duration"); ax.set_xlabel("Daily Usage (hours)"); ax.set_ylabel("Sleep Duration (hours)")
fig.tight_layout(); fig.savefig(os.path.join(out,"03_usage_vs_sleep.png"),dpi=160); plt.close(fig)

# 4 usage band mental health
bands=pd.DataFrame({"Usage_Band":pd.Categorical(df["Usage_Band"],categories=["Low (<3h)","Moderate (3-6h)","High (6-9h)","Very High (9h+)"],ordered=True),
                    "Mental_Health_Index":df["Mental_Health_Index"]}).groupby("Usage_Band",observed=False)["Mental_Health_Index"].mean()
fig,ax=plt.subplots(); ax.bar(bands.index.astype(str),bands.values); ax.set_title("Average Mental Health Index by Daily Usage Band")
ax.set_xlabel("Daily Usage Band"); ax.set_ylabel("Average Mental Health Index"); ax.tick_params(axis="x",rotation=15)
fig.tight_layout(); fig.savefig(os.path.join(out,"04_usage_band_mental_health.png"),dpi=160); plt.close(fig)

# 5 impact vs usage
impact=df.groupby("Overall_Impact")["Daily_Usage_Hours"].mean().sort_values(ascending=False)
fig,ax=plt.subplots(); ax.bar(impact.index,impact.values); ax.set_title("Average Daily Usage by Overall Impact Category")
ax.set_xlabel("Overall Impact"); ax.set_ylabel("Average Daily Usage (hours)")
fig.tight_layout(); fig.savefig(os.path.join(out,"05_impact_vs_usage.png"),dpi=160); plt.close(fig)

# 6 correlation heatmap without seaborn
cols=["Age","Daily_Usage_Hours","Weekend_Extra_Hours","Sleep_Duration_Hours","Sleep_Quality_Score",
      "Perceived_Stress_Score","Mental_Health_Index","Academic_Performance_GPA"]
corr=df[cols].corr()
fig,ax=plt.subplots(figsize=(11,8)); im=ax.imshow(corr.values,aspect="auto")
ax.set_xticks(range(len(cols))); ax.set_yticks(range(len(cols))); ax.set_xticklabels(cols,rotation=45,ha="right"); ax.set_yticklabels(cols)
for i in range(len(cols)):
    for j in range(len(cols)): ax.text(j,i,f"{corr.iloc[i,j]:.2f}",ha="center",va="center",fontsize=8)
ax.set_title("Correlation Matrix of Key Numeric Variables"); fig.colorbar(im,ax=ax,fraction=.046,pad=.04)
fig.tight_layout(); fig.savefig(os.path.join(out,"06_correlation_heatmap.png"),dpi=160); plt.close(fig)

# 7 late-night outcomes
late=df.groupby("Late_Night_Usage").agg(
    Sleep=("Sleep_Duration_Hours","mean"), Stress=("Perceived_Stress_Score","mean"),
    Mental_Health=("Mental_Health_Index","mean"), GPA=("Academic_Performance_GPA","mean")
)
fig,axes=plt.subplots(1,3,figsize=(15,5))
for ax,col,title in zip(axes,["Sleep","Stress","GPA"],["Sleep","Stress","GPA"]):
    ax.bar(["No","Yes"],late[col].reindex([False,True]).values)
    ax.set_title(title)
fig.suptitle("Outcomes by Late-Night Social Media Usage"); fig.tight_layout()
fig.savefig(os.path.join(out,"07_late_night_outcomes.png"),dpi=160); plt.close(fig)

impact_summary=df.groupby("Overall_Impact").agg(
    Students=("Student_ID","count"), Avg_Usage=("Daily_Usage_Hours","mean"),
    Avg_Sleep=("Sleep_Duration_Hours","mean"), Avg_Stress=("Perceived_Stress_Score","mean"),
    Avg_Mental_Health=("Mental_Health_Index","mean"), Avg_GPA=("Academic_Performance_GPA","mean"))
impact_summary.round(3).to_csv(os.path.join(project,"impact_summary.csv"))
corr.round(3).to_csv(os.path.join(project,"correlation_matrix.csv"))