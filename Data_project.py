import pandas as pd

import matplotlib.pyplot as plt

# Load the datasets
df_A = pd.read_csv("screen_time_data_20250808_134948.csv")
df_B = pd.read_csv("platform_analysis_20250808_134948.csv")

print(df_A.isnull().sum())
print(df_A.describe())

# I do need to clean this CSV to get 13-19 year olds

Screentime_mean_by_app = df_B.groupby('Platform')["Avg_Hours_Per_Day"].mean()

Screentime_mean_by_app.plot(kind='bar', title='Screentime mean by app')
plt.xlabel('Platform')
plt.ylabel('Average Hours Per Day')
plt.xticks(rotation=45)
plt.xticks(size=6)
plt.tight_layout()
plt.savefig("my_custom_chart.png")
plt.show()

# Cleaning code for 13-19 year olds
Teens = df_A[(df_A['age_group'] == '13-14') | (df_A['age_group'] == '15-17') | (df_A['age_group'] == '18-19')]
Teens.to_csv('Teens&Screens_data.csv', index=False)
df_C = pd.read_csv("Teens&Screens_data.csv")

Sleep_Issues_Percentage = df_C[df_C['sleep_problems'] != 'None']['sleep_problems'].value_counts()

df_plot_sleep = Sleep_Issues_Percentage.reset_index()
df_plot_sleep.columns = ['Issue', 'Count']
df_plot_sleep.set_index('Issue').plot(kind='pie', y='Count', autopct='%1.1f%%', title='Sleep Issues within teens')
plt.xlabel('')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("sleep_issue_pie_chart.png")
plt.show()

Phone_Anxiety_Percentage = df_C[df_C['phone_anxiety'] != 'None']['phone_anxiety'].value_counts()
df_plot_anxiety = Phone_Anxiety_Percentage.reset_index()
df_plot_anxiety.columns = ['Issue', 'Count']
df_plot_anxiety.set_index('Issue').plot(kind='pie', y='Count', autopct='%1.1f%%', title='Phone Anxiety within teens')
plt.xlabel('')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("phone_anxiety_pie_chart.png")
plt.show()