import pandas as pd

files = [
    "api_data_aadhar_biometric_0_500000.csv",
    "api_data_aadhar_biometric_500000_1000000.csv",
    "api_data_aadhar_biometric_1000000_1500000.csv",
    "api_data_aadhar_biometric_1500000_1861108.csv"
]

df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

df.columns = df.columns.str.strip()

# State-wise summary
state_summary = df.groupby("state")[["bio_age_5_17", "bio_age_17_"]].sum().reset_index()

print(state_summary.head())

# Save for Power BI
state_summary.to_csv("state_biometric_summary.csv", index=False)

print("State summary file created successfully!")

# District-wise summary
district_summary = df.groupby(["state", "district"])[["bio_age_5_17", "bio_age_17_"]].sum().reset_index()

print(district_summary.head())

# Save for Power BI
district_summary.to_csv("district_biometric_summary.csv", index=False)

print("District summary file created successfully!")