# SWYNEX-Data-Cleaning-Preparation

Data cleaning and preparation of the public **Titanic passenger dataset** using Python (pandas).

## Files
- `titanic_raw.csv` - original dataset
- `titanic_cleaned.csv` - cleaned dataset
- `clean_data.py` - cleaning script

## Problems found
| Issue | Details |
|---|---|
| Missing values | `Age`, `Cabin` and `Embarked` had empty values |
| Duplicate records | Checked and removed duplicate rows |
| Incorrect data types | `Pclass`, `Sex`, `Embarked` converted to category; `Age` converted to integer |
| Inconsistent values | Extra spaces removed; `Sex` made lowercase; `Embarked` made uppercase |

## Changes made
1. Dropped duplicate rows.
2. Trimmed whitespace and standardised text case.
3. Filled missing `Age` with the median, `Embarked` with the most common value, and `Cabin` with "Unknown".
4. Converted columns to proper data types.
5. Removed invalid values (age <= 0 or negative fare).

## How to run
```
pip install pandas
python clean_data.py
```
