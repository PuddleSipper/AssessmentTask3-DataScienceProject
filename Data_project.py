import pandas as pd

import matplotlib.pyplot as plt

# Load the datasets
df_A = pd.read_csv("screen_time_data_20250808_134948.csv")
df_B = pd.read_csv("platform_analysis_20250808_134948.csv")

print(df_A.isnull().sum())
print(df_A.describe())

Screentime_mean_by_app = df_B.groupby('Platform')["Avg_Hours_Per_Day"].mean()

Screentime_mean_by_app.plot(kind='bar', title='Screentime mean by app')
plt.xlabel('Platform')
plt.ylabel('Average Hours Per Day')
plt.xticks(rotation=45)
plt.xticks(size=6)
plt.tight_layout()
plt.savefig("my_custom_chart.png")
plt.show()

Sleep_Issues_Percentage = df_A[df_A['sleep_problems'] != 'None']['sleep_problems'].value_counts()

Sleep_Issues_Percentage.plot(kind='pie', autopct='%1.1f%%', title='Sleep Issues within 2000 teens')
plt.xlabel('')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("sleep_issue_pie_chart.png")
plt.show()