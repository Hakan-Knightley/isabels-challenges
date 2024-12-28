import pandas as pd

# read csv files into dataframes
activity_proportions = pd.read_csv("B1_activity_proportions.csv")
print("read B1_activity_proportions.csv:")
print(activity_proportions)

activity_details = pd.read_csv("B1_activity_details.csv")
print("read B1_activity_details.csv:")
print(activity_details)

activity_costs = pd.read_csv("B1_activity_costs.csv")
print("read B1_activity_costs.csv:")
print(activity_costs)

# merge dataframes
merged_df = pd.merge(activity_proportions, activity_details, on="day_id")
print("merged activity_proportions & activity_details:")
print(merged_df)

merged_df = pd.merge(merged_df, activity_costs, on="activity_type")
print("merged with activity_costs:")
print(merged_df)

# compute total cost for each day
merged_df["total_cost"] = (
    (merged_df["X1"] * merged_df["cost1"] +
    merged_df["X2"] * merged_df["cost2"] +
    merged_df["X3"] * merged_df["cost3"]) *
    merged_df["total_time"]
)
print("computed total_cost & multiplied by total_time:")
print(merged_df)

# aggregate total costs by month
monthly_costs = merged_df.groupby("month")["total_cost"].sum().reset_index()
print("aggregated total costs by month:")
print(monthly_costs)

# save results to new csv file
monthly_costs.to_csv("B1_monthly_costs.csv", index=False)
print("saved monthly costs to B1_monthly_costs.csv")

# print month with max monthly cost
max_cost_month = monthly_costs.loc[monthly_costs["total_cost"].idxmax()]
print(f"month with max cost: {max_cost_month['month']}, total cost: {max_cost_month['total_cost']}")
