import pandas as pd

df=pd.read_csv("Sales Dataset.csv",encoding="latin1")
df["Year-Month"]=pd.to_datetime(df["Year-Month"])
state_filter="Florida"
filtered_df=df[df["State"]==state_filter]

print("Filtered Sales Data:\n")
print(filtered_df)

profit_by_date=filtered_df.groupby("Year-Month")["Profit"].sum()
filtered_df.to_csv("D:\ALL FOR ONE\sapath\python\Project\Project_csv.csv",index=False)
