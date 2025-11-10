import pandas as pd
import os

os.makedirs("../output", exist_ok=True)

# Step 1 – load CSV
df = pd.read_csv("sample_data.csv")


# Step 2 – clean
df.dropna(inplace=True)

# Step 3 – transform
if 'Product' in df.columns and 'Sales' in df.columns:
    agg = df.groupby("Product")["Sales"].sum().reset_index()
else:
    agg = df.copy()

# Step 4 – save output
agg.to_csv("../output/aggregated_sales.csv", index=False)

print("ETL demo complete. Output saved to output/aggregated_sales.csv")
