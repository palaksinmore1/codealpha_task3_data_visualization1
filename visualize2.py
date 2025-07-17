import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the dataset
df = pd.read_csv("electric_vehicle_spec_2025.csv")

# Show first few rows (optional)
print("Dataset Preview:")
print(df.head())

# ---------------------------
# 1. Top 10 EV Brands by Number of Models
# ---------------------------
top_brands = df['brand'].value_counts().head(10)
plt.figure()
sns.barplot(x=top_brands.values, y=top_brands.index, palette="viridis")
plt.title("Top 10 EV Brands by Number of Models")
plt.xlabel("Number of Models")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig("op 10 EV Brands by Number of Models.png")
plt.show()

# ---------------------------
# 2. Battery Capacity vs. Range
# ---------------------------
plt.figure()
sns.scatterplot(
    x='battery_capacity_kWh',
    y='range_km',
    hue='brand',
    data=df,
    palette='Set2',
    legend=False
)
plt.title("Battery Capacity vs. Range (km)")
plt.xlabel("Battery Capacity (kWh)")
plt.ylabel("Range (km)")
plt.tight_layout()
plt.savefig("Battery Capacity vs. Range (km).png")
plt.show()

# ---------------------------
# 3. Efficiency Distribution (Wh/km)
# ---------------------------
plt.figure()
sns.histplot(df['efficiency_wh_per_km'].dropna(), bins=20, kde=True, color="teal")
plt.title("Efficiency Distribution (Wh/km)")
plt.xlabel("Efficiency (Wh/km)")
plt.ylabel("Number of Vehicles")
plt.tight_layout()

plt.show()

# ---------------------------
# 4. Acceleration Comparison (Top 5 Brands)
# ---------------------------
top5_brands = df['brand'].value_counts().head(5).index
df_top5 = df[df['brand'].isin(top5_brands)]

plt.figure()
sns.boxplot(x='brand', y='acceleration_0_to_100_km_h', data=df_top5, palette="coolwarm")
plt.title("0–100 km/h Acceleration Time by Brand")
plt.xlabel("Brand")
plt.ylabel("Acceleration (seconds)")
plt.tight_layout()

plt.show()