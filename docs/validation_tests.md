## validation_tests.md`

👉 Purpose: **Shows quality & testing**

```md
# Data Validation & Testing

## Validation Checks Performed

### Missing Values
- Used df.isnull().sum() to detect missing values
- Handled using removal or imputation where required

### Data Type Validation
- Ensured numeric columns were correctly typed
- Converted date columns to datetime format

### Range Checks
- Verified scores, sales, temperatures, and engagement metrics
- Removed or flagged invalid values

### Consistency Checks
- Ensured totals matched component values
- Checked logical relationships between columns

## Testing Evidence
- Re-ran analysis after cleaning
- Verified visual outputs matched expectations
- Cross-checked summary statistics

## Conclusion
All datasets passed validation checks and were suitable for analysis.
