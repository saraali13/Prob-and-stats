import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Employee Dataset
employee_data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Age": [28, 35, 42, 30, 50, 41, 29, 33, 45, 39],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["IT", "HR", "Finance", "Marketing", "Sales", "HR", "IT", "Finance", "Sales", "Marketing"],
    "Salary": [70000, 60000, 90000, 65000, 85000, 62000, 75000, 88000, 87000, 67000],
    "Experience": [3, 7, 12, 5, 15, 9, 4, 11, 14, 6],
    "Work Hours/Week": [40, 38, 45, 42, 50, 37, 39, 44, 48, 41],
    "Projects Completed": [5, 4, 6, 7, 8, 5, 6, 7, 9, 6],
    "Job Satisfaction (1-10)": [7, 8, 6, 9, 5, 7, 8, 6, 5, 8],
    "Training Hours": [20, 15, 18, 25, 12, 16, 22, 20, 14, 19],
    "Promotion Status": ["No", "Yes", "Yes", "No", "Yes", "No", "No", "Yes", "Yes", "No"]
}

df_employee = pd.DataFrame(employee_data)

print("Employee’s Performance Dataset")
print("Number of Rows and Columns: ", df_employee.shape)
summary_statistics = df_employee.describe()
print("Summary Statistics:\n", summary_statistics)
distinct_departments = df_employee["Department"].value_counts()
print("Distinct Values in the Department:\n", distinct_departments)
distinct_promotions = df_employee["Promotion Status"].value_counts()
print("Distinct Values in the Promotion State:\n", distinct_promotions)

# Handling missing values of Qualitative Data by mode and Quantitative data by mean as there are low chances of outliers to occur
df_employee["Age"] = df_employee["Age"].fillna(df_employee["Age"].mean())
df_employee["Salary"] = df_employee["Salary"].fillna(df_employee["Salary"].mean())
df_employee["Experience"] = df_employee["Experience"].fillna(df_employee["Experience"].mean())
df_employee["Gender"] = df_employee["Gender"].fillna(df_employee["Gender"].mode()[0])
df_employee["Department"] = df_employee["Department"].fillna(df_employee["Department"].mode()[0])
df_employee["Promotion Status"] = df_employee["Promotion Status"].fillna(df_employee["Promotion Status"].mode()[0])

# Visualizations
plt.figure()
plt.hist(df_employee["Salary"], color='b', edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.bar(distinct_departments.index, distinct_departments.values, color="blue", edgecolor="black")
plt.title("Employee Count per Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()

plt.figure()
sns.boxplot(x=df_employee["Experience"], orient="h")
plt.title("Experience Distribution")
plt.show()

# Heart Disease Dataset
heart_data = pd.read_csv("heart_disease.csv")

print("\n\nHeart Disease Dataset")
print("Number of Rows and Columns: ", heart_data.shape)
summary_statistics_heart = heart_data.describe()
print("Summary Statistics:\n", summary_statistics_heart)

unique_gender_count = heart_data["Gender"].value_counts()
print("Unique values in the gender:\n", unique_gender_count)
unique_smoking_count = heart_data["Smoking"].value_counts()
print("Unique values in the smokers:\n", unique_smoking_count)

# Handling missing values of Qualitative Data by mode and Quantitative data by median as there are chances of outliers to occur
heart_data["Age"] = heart_data["Age"].fillna(heart_data["Age"].median())
heart_data["Blood Pressure"] = heart_data["Blood Pressure"].fillna(heart_data["Blood Pressure"].median())
heart_data["Cholesterol Level"] = heart_data["Cholesterol Level"].fillna(heart_data["Cholesterol Level"].mode()[0])
heart_data["BMI"] = heart_data["BMI"].fillna(heart_data["BMI"].median())
heart_data["Stress Level"] = heart_data["Stress Level"].fillna(heart_data["Stress Level"].mode()[0])
heart_data["Sleep Hours"] = heart_data["Sleep Hours"].fillna(heart_data["Sleep Hours"].median())
heart_data["Gender"] = heart_data["Gender"].fillna(heart_data["Gender"].mode()[0])
heart_data["Exercise Habits"] = heart_data["Exercise Habits"].fillna(heart_data["Exercise Habits"].mode()[0])
heart_data["Smoking"] = heart_data["Smoking"].fillna(heart_data["Smoking"].mode()[0])
heart_data["Family Heart Disease"] = heart_data["Family Heart Disease"].fillna(
    heart_data["Family Heart Disease"].mode()[0])
heart_data["Diabetes"] = heart_data["Diabetes"].fillna(heart_data["Diabetes"].mode()[0])
# Visualizations
plt.figure()
plt.hist(heart_data["Age"], color='g', edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure()
Heart_disease_count = heart_data["Heart Disease Status"].value_counts()
plt.bar(Heart_disease_count.index, Heart_disease_count.values, color="red", edgecolor="black")
plt.title("Heart Disease Count")
plt.xlabel("Heart Disease Status")
plt.ylabel("Number of People")
plt.xticks(ticks=[0, 1], labels=["No Disease", "Has Disease"])
plt.show()

plt.figure()
sns.boxplot(x=heart_data["Cholesterol Level"], orient="h")
plt.title("Cholesterol Level Distribution")
plt.show()
