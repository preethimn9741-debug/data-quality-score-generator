
# Data Quality Score Generator

## Project Description
This project calculates a **data quality score** for a CSV dataset.
It analyzes the dataset for null values, invalid dates, and negative amounts, then produces a final quality score out of 100.

The results are printed directly to the console.

---

## Files
- `quality_score.py` – Data quality scoring script
- `data.csv` – Input dataset
- `README.md` – Project documentation

---

## How the Script Works
1. Reads data from `data.csv`
2. Calculates the percentage of null values in the dataset
3. Identifies invalid dates in the `date` column
4. Calculates the percentage of negative values in the `amount` column
5. Computes a final quality score using weighted penalties
6. Prints a summary report and quality score to the console

---

## Quality Metrics Used
- **Null Values Percentage**
- **Invalid Dates Percentage**
- **Negative Amounts Percentage**

---

## Quality Score Formula
The quality score starts at 100 and applies penalties:

- Null values: 40% weight  
- Invalid dates: 30% weight  
- Negative amounts: 30% weight  

The final score is rounded and constrained to a minimum of 0.

---

## How to Run

python quality_score.py

DATA QUALITY REPORT

Total Rows: <number>
Null Values %: <value>
Invalid Dates %: <value>
Negative Amounts %: <value>

QUALITY SCORE: <score> / 100

Output

The script prints a summary similar to:

DATA QUALITY REPORT
Total Rows: <number>
Null Values %: <value>
Invalid Dates %: <value>
Negative Amounts %: <value>

QUALITY SCORE: <score> / 100



