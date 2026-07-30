import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders if not exist
os.makedirs("dashboard", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Read CSV file
df = pd.read_csv("data/sales_data.csv")

# Display data
print("Sales Data:")
print(df)

# Total Sales
total_sales = df["Sales"].sum()

# Total Revenue
total_revenue = df["Revenue"].sum()

print("\nTotal Sales:", total_sales)
print("Total Revenue:", total_revenue)

# Save summary report
with open("reports/report.txt", "w") as f:
    f.write("Sales & Revenue Analysis Report\n")
    f.write("=" * 35 + "\n")
    f.write(f"Total Sales: {total_sales}\n")
    f.write(f"Total Revenue: {total_revenue}\n")

# Create Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["Product"], df["Revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("dashboard/revenue_chart.png")

print("\nProject Completed Successfully!")