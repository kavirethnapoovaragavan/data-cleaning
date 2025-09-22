
# package
import pandas as pd
import re
import phonenumbers
from phonenumbers import NumberParseException, PhoneNumberFormat


# Import dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")


# Rename column headers

df.columns

#Standardize column names (lowercase, no spaces)
df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_"))

# make more readable
rename_dict = {
    "ordernumber": "order_number",
    "quantityordered": "quantity_ordered",
    "priceeach": "price_each",
    "orderlinenumber": "order_line_number",
    "sales": "sales",
    "orderdate": "order_date",
    "status": "status",
    "qtr_id": "quarter_id",
    "month_id": "month_id",
    "year_id": "year_id",
    "productline": "product_line",
    "msrp": "msrp",
    "productcode": "product_code",
    "customername": "customer_name",
    "phone": "phone",
    "addressline1": "address_line1",
    "addressline2": "address_line2",
    "city": "city",
    "state": "state",
    "postalcode": "postal_code",
    "country": "country",
    "territory": "territory",
    "contactlastname": "contact_last_name",
    "contactfirstname": "contact_first_name",
    "dealsize": "deal_size"
}

# Apply rename
df = df.rename(columns=rename_dict)


df.columns


# Removing duplicate

#Check for duplicate rows
duplicate_rows = df.duplicated()

# Count of duplicate rows
print(f"Number of duplicate rows: {duplicate_rows.sum()}")

print("Shape of DataFrame Before Removing Duplicates: ", df.shape)

# Drop the duplicates
df = df.drop_duplicates()

# Checking the shape of the data after dropping duplicates
print("Shape of DataFrame After Removing Duplicates: ", df.shape)


#Standardize text fields
df["status"] = df["status"].str.strip().str.upper()
df["country"] = df["country"].str.strip().str.title()
df["state"] = df["state"].fillna("").str.upper()
df["city"] = df["city"].str.title()


# convert datatype year/month/quarter to integers
df["year_id"] = df["year_id"].astype(int)
df["month_id"] = df["month_id"].astype(int)
df["quarter_id"] = df["quarter_id"].astype(int)


# Convert date formats

#Convert date formats
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", dayfirst=True)
df["order_date"] = df["order_date"].dt.strftime("%d-%m-%Y")


# Convert data types
df["order_number"] = df["order_number"].astype(int)
df["quantity_ordered"] = df["quantity_ordered"].astype(int)
df["order_line_number"] = df["order_line_number"].astype(int)

df["price_each"] = df["price_each"].astype(float)
df["sales"] = df["sales"].astype(float)

df["postal_code"] = df["postal_code"].astype(str)

#Trim whitespace in names
df["customer_name"] = df["customer_name"].str.strip().str.title()
df["contact_last_name"] = df["contact_last_name"].str.strip().str.title()
df["contact_first_name"] = df["contact_first_name"].str.strip().str.title()

#Convert date formats
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", dayfirst=True)
df["order_date"] = df["order_date"].dt.strftime("%d-%m-%Y")

# Format phone number

df['phone'] = df['phone'].str.replace(r"[.\s]", "", regex=True)
df['phone'].head()

def format_phone_number(number, default_region='US'):
    try:
        number = number.replace(".", "").replace("(", "").replace(")", "").replace(" ", "")
        parsed = phonenumbers.parse(str(number), default_region)
        if phonenumbers.is_valid_number(parsed):
            return str(parsed.national_number)
        else:
            return None
    except NumberParseException:
        return None
    
df['phone'] = df['phone'].apply(format_phone_number)


# Handling missing values

df.isnull().sum()


df["address_line2"] = df["address_line2"].fillna("NA")
df["territory"] = df["territory"].fillna("NA")

df["state"]=df["state"].replace("",pd.NA)
df["state"]=df["state"].replace(pd.NA,"Unknown")

df["phone"]=df["phone"].replace("",pd.NA)
df["phone"]=df["phone"].replace(pd.NA,"Unknown")

df["postal_code"] = df["postal_code"].replace("",pd.NA)
df["postal_code"] = df["postal_code"].replace("nan",pd.NA)
df["postal_code"] = df["postal_code"].replace(pd.NA,"Unknown")

df.isnull().sum()

# Export dataset
df.to_csv("cleaned_data.csv", index=False, encoding="utf-8")

