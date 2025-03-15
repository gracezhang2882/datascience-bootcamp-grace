import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

df['DayOfWeek'] = df['hour_beginning'].dt.day_name()

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
df_weekdays = df[df['DayOfWeek'].isin(weekdays)]
pedestrian_counts = df_weekdays.groupby('DayOfWeek')['Pedestrians'].sum()

order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
pedestrian_counts = pedestrian_counts.reindex(order)

plt.figure(figsize=(10, 5))
plt.plot(pedestrian_counts.index, pedestrian_counts.values, marker='o', linestyle='-')
plt.xlabel("Day of the Week")
plt.ylabel("Total Pedestrian Count")
plt.title("Pedestrian Counts for Weekdays in NYC")
plt.grid(True)
plt.show()

df_2019 = df[df['hour_beginning'].dt.year == 2019]
df_encoded = pd.get_dummies(df_2019, columns=['weather_summary'])
correlation_data = df_encoded[['Pedestrians'] + [col for col in df_encoded.columns if 'weather_summary_' in col]]
correlation_matrix = correlation_data.corr()
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.matshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)

fig.colorbar(cax)
ax.set_xticks(np.arange(len(correlation_matrix.columns)))
ax.set_yticks(np.arange(len(correlation_matrix.index)))
ax.set_xticklabels(correlation_matrix.columns, rotation=90)
ax.set_yticklabels(correlation_matrix.index)
plt.title("Correlation Matrix", pad=20)
plt.show()


time_of_day_counts = df.groupby('TimeOfDay')['Pedestrians'].sum()
order = ["Morning", "Afternoon", "Evening", "Night"]
time_of_day_counts = time_of_day_counts.reindex(order)

plt.figure(figsize=(8, 5))
plt.bar(time_of_day_counts.index, time_of_day_counts.values, color=['blue', 'orange', 'green', 'purple'])
plt.xlabel("Time of Day")
plt.ylabel("Total Pedestrian Count")
plt.title("Pedestrian Activity Patterns Throughout the Day")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()