import pandas as pd

# 1. Load data
df = pd.read_csv("data.csv")
total_rows = len(df)

# 2. % Null values
null_count = df.isnull().sum().sum()
total_cells = df.shape[0] * df.shape[1]
null_percentage = (null_count / total_cells) * 100

# 3. % Invalid dates
df["parsed_date"] = pd.to_datetime(df["date"], errors="coerce")
invalid_dates = df["parsed_date"].isnull().sum()
invalid_date_percentage = (invalid_dates / total_rows) * 100

# 4. % Negative amounts
negative_amounts = (df["amount"] < 0).sum()
negative_amount_percentage = (negative_amounts / total_rows) * 100

# 5. Quality score calculation
score = (
    100
    - (null_percentage * 0.4)
    - (invalid_date_percentage * 0.3)
    - (negative_amount_percentage * 0.3)
)

score = max(0, round(score, 2))

# 6. Summary report
print("\n📊 DATA QUALITY REPORT")
print(f"Total Rows: {total_rows}")
print(f"Null Values %: {round(null_percentage, 2)}")
print(f"Invalid Dates %: {round(invalid_date_percentage, 2)}")
print(f"Negative Amounts %: {round(negative_amount_percentage, 2)}")
print(f"\n✅ QUALITY SCORE: {score} / 100")
