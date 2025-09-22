# data-cleaning
Cleaned and standardized orders dataset: handled missing values, removed duplicates, fixed data types, and formatted dates for analysis-ready use
# Dataset Cleaning - README

## Overview
This project involves cleaning a sample orders dataset to make it consistent, accurate, and ready for analysis. The dataset contained issues such as missing values, inconsistent formats, and mixed data types.

---

## Cleaning Steps

1. **Handling Missing Values**
   - Replaced empty strings (`""`) in columns like `address_line2`, `territory`, and `state` with `"NA"` so they are no longer counted as nulls.
   - Ensured all columns have appropriate values to avoid unexpected missing data.

2. **Standardizing Text**
   - Stripped extra spaces and standardized capitalization for text columns:
     - `status`, `product_line`, `deal_size`, `country`, `city`, `contact_first_name`, `contact_last_name`, `customer_name`.

3. **Date Formatting**
   - Converted `order_date` to `datetime` type for consistency.
   - Ensured the format is `dd-mm-yyyy`.

4. **Numeric and String Columns**
   - Converted `postal_code` and `phone` to strings to avoid mixed-type issues.
   - Ensured numeric columns (`quantity_ordered`, `price_each`, `sales`, etc.) are correctly typed.

5. **Column Names**
   - Renamed all columns to lowercase with underscores (e.g., `order_number` instead of `Order Number`) for uniformity.

6. **Removing Duplicates**
   - Checked and removed any duplicate rows to maintain data integrity.

---

## Result
- All missing values are now either valid values or `"NA"` placeholders.
- Text, numeric, and date columns are standardized.
- The dataset is ready for analysis without errors related to nulls, mixed types, or inconsistent formatting.

---

## Notes
- Use `df.isnull().sum()` to verify that there are no unexpected missing values.
- The cleaned dataset is saved as `cleaned_dataset.csv`.
