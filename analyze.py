import pandas as pd
df = pd.read_csv("data/income_inequality.csv")
print(df)
df["gini_change"] = df["gini_index"] - df["gini_index"].iloc[0]
df["top1_to_bottom50"] = df["top1_share"] / df["bottom50_share"]
df["inequality_decade"] = (df["year"] // 10) * 10

# Wealth Tax Simulator
tax_rate = 0.01
threshold_share = 0.60
df["tax_collected"] = df["top1_share"] * threshold_share * tax_rate
df["new_bottom50"] = df["bottom50_share"] + df["tax_collected"]
df["new_top1"] = df["top1_share"] - df["tax_collected"]
df["new_gini"] = df["gini_index"] - (df["tax_collected"] * 0.4)

df.to_csv("data/income_inequality_final.csv", index=False)
print("Export complete.")