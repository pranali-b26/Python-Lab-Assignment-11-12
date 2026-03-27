import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("recruitment.csv")

# a) Bar Chart
plt.bar(df['company'], df['recruits'])
plt.title("Recruitments in Companies")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.pie(df['recruits'], labels=df['company'], autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.pie(df['recruits'], labels=df['company'], autopct='%1.1f%%', shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(df['recruits'], labels=df['company'], autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# e) Compare IBM & Amdocs
companies = ['IBM', 'Amdocs']
values = df[df['company'].isin(companies)]['recruits']

plt.bar(companies, values)
plt.title("IBM vs Amdocs Recruitment")
plt.show()