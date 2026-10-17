import pandas as pd
import matplotlib.pyplot as plt

# ================= DATA =================
data = [
    ['2020-03-15','Karachi',12,2,0,0],
    ['2020-04-02','Hyderabad',8,5,0,0],
    ['2020-05-05','Lahore',120,85,2,0],
    ['2020-06-08','Islamabad',210,150,3,0],
    ['2020-07-10','Karachi',340,250,5,0],
    ['2020-08-15','Sukkur',45,30,0,120],
    ['2020-09-20','Hyderabad',65,50,1,150],
    ['2020-11-12','Karachi',250,190,4,400],
    ['2021-01-05','Karachi',320,260,5,480],
    ['2021-02-10','Hyderabad',110,85,1,750],
    ['2021-03-19','Islamabad',140,110,2,450],
    ['2021-05-12','Karachi',310,250,5,900],
    ['2021-07-05','Karachi',380,310,6,850],
    ['2021-08-28','Karachi',350,280,5,950],
    ['2021-10-21','Lahore',175,140,2,1000],
    ['2021-12-14','Sukkur',80,65,1,1600],
    ['2022-01-20','Hyderabad',150,120,2,1800],
    ['2022-03-15','Islamabad',180,145,2,900],
    ['2022-05-08','Karachi',360,300,6,2000],
    ['2022-07-01','Karachi',450,380,8,1900]
]
df = pd.DataFrame(data, columns=['Date','City','New_Cases','Recovered','Deaths','Vaccinated'])

# ================= FUNCTIONS =================

def total_summary():
    print("=== TOTAL SUMMARY ===")
    print(f"Total Cases: {df['New_Cases'].sum()}")
    print(f"Total Recovered: {df['Recovered'].sum()}")
    print(f"Total Deaths: {df['Deaths'].sum()}")
    print(f"Total Vaccinated: {df['Vaccinated'].sum()}")

def city_wise():
    print("\n=== CITY WISE CASES ===")
    result = df.groupby('City')['New_Cases'].sum().sort_values(ascending=False)
    print(result)
    return result

def calculate_rates():
    print("\n=== DEATH & RECOVERY RATE ===")
    df['Death_Rate'] = (df['Deaths'] / df['New_Cases'] * 100).round(2)
    df['Recovery_Rate'] = (df['Recovered'] / df['New_Cases'] * 100).round(2)
    print(df[['City','New_Cases','Death_Rate','Recovery_Rate']])

def filter_hyderabad():
    print("\n=== HYDERABAD DATA ===")
    hyd = df[df['City'] == 'Hyderabad']
    print(hyd)
    print(f"Total Hyderabad Cases: {hyd['New_Cases'].sum()}")

def max_min():
    print("\n=== MAX / MIN ===")
    print(f"Max in 1 day: {df['New_Cases'].max()} on {df.loc[df['New_Cases'].idxmax(),'Date']}")
    print(f"Min in 1 day: {df['New_Cases'].min()}")

def plot_graphs():
    city_wise().plot(kind='bar', color='red')
    plt.title('City Wise COVID Cases - Pakistan')
    plt.ylabel('Cases')
    plt.savefig('city_cases.png')
    plt.show()

# RUN ALL
total_summary()
city_wise()
calculate_rates()
filter_hyderabad()
max_min()
plot_graphs()

# SAVE
df.to_excel('Corona_20_Pakistan.xlsx', index=False)
df.to_csv('Corona_20_Pakistan.csv', index=False)
print("\n✅ All Done & Saved!")
