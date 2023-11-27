## Subject: Data Quality Assessment Findings

Dear [Recipient's Name],

I hope this email finds you well. My name is Omkar Pawar, and I am part of the KPMG Data Analytics team. I am writing to share the results of our comprehensive review of the datasets provided by your company. During the data quality analysis phase, we identified several errors that require attention.

Ensuring data accuracy and reliability is crucial for generating precise analytics results. Addressing these errors will significantly enhance the overall quality of the datasets and contribute to the success of your analytics efforts.

Below are the identified errors and our recommended mitigations:

### **Sheet: CustomerDemographic (4000 X 13)**
- `last_name`: 125 NaN Values
- `DOB`: 
   1. 87 NaN Values
   2. Jephthah Bachmann - born in 1843 - age = 175??
- `job_title`: 506 NaN Values
- `job_industry_category`: 656 NaN Values
- `default`: 302 NaN Values
- `tenure`: 87 NaN Values

**Mitigations:**
- Utilize the mode year value for missing records in customers' date of birth.
- Assign a uniform last name to customers with missing values.
- Identify unknown genders based on names, addressing inconsistent data (M, Male, Female, F, U).
    
    Recommendation: Instead of allowing free text entry, implement a drop-down list for data entry to ensure uniform and meaningful variables for modeling. This helps avoid multiple representations of the same value.

- Calculate the mean of tenure values and assign the mean value to missing fields for data consistency.

### **Sheet: NewCustomerList (1000 X 23)**
- `last_name`: 29 NaN Values
- `DOB`: 17 NaN Values
- `job_title`: 106 NaN Values
- `job_industry_category`: 165 NaN Values

**Mitigation:**
- Rename columns 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19' for ease of analysis.

### **Sheet: Transactions (2000 X 13)**
- `online_order`: 360 NaN Values
- `brand`: 197 NaN Values
- `product_line`: 197 NaN Values
- `product_class`: 197 NaN Values
- `product_size`: 197 NaN Values
- `standard_cost`: 197 NaN Values
- `product_first_sold_date`: 197 NaN Values

**Mitigations:**
- Confirm if the 197 rows with NaN values indicate no actual purchase.
- Replace `nan` with mode values for `product_class` and `product_size`.

---------

### **Recommendations:**
- Ensure all tables, particularly 'Transactions' and 'Customer Address,' cover the same period to avoid discrepancies.
- Use only customer IDs from the 'Customer Master' list for model training to maintain consistency.
- Filter out records entirely if only a small number of rows have empty values, or impute based on distribution for core fields.
- For key datasets like transactions, remove records with missing fields (less than 1% of transactions, totaling less than 0.1% of revenue) from the training dataset.
- Use regular expressions to replace extended values with abbreviations for consistent representation of attributes like addresses.
- Enforce a drop-down list for user input to avoid inconsistent representations and enhance data quality.
- Convert selected records from characters to numeric and remove non-numeric characters from strings for consistent data types.
- Ensure fact tables in the database have constraints on data types to avoid difficulties in interpreting results.
- Make appropriate data transformations to ensure consistent data types for fields.
- Regularly validate and synchronize data across tables to maintain accuracy and reliability.
- Consider constraints on data types in database design for improved consistency and interpretation.
  
Note: The recommendations aim to enhance data quality, consistency, and interpretability for meaningful analytics outcomes.

Implementing these measures will significantly contribute to improving data quality and, consequently, lead to better analytics outcomes.

For current analysis we have decided to replace those null values with mean and mode values. 

Thank you for your attention to this matter.

----

Best regards,

Omkar Pawar

KPMG Data Analytics Team
