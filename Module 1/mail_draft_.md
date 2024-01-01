## Subject: Data Quality Assessment Findings

Dear [Client Name],

I hope this email finds you well. My name is Omkar Pawar, and I am part of the KPMG Data Analytics team. I am writing to share the results of our comprehensive review of the datasets provided by your company. During the data quality analysis phase, we identified several errors that require attention.

Ensuring data accuracy and reliability is crucial for generating precise analytics results. Addressing these errors will significantly enhance the overall quality of the datasets and contribute to the success of your analytics efforts.

### Sheet: CustomerDemographic (4000 X 13)

| Column Name                 | Issue Type       | Number of NaN Values | Mitigation                                               |
|-----------------------------|------------------|----------------------|----------------------------------------------------------|
| `last_name`                 | Missing Values   | 125                  | Assign a default last name or use a uniform placeholder.  |
| `DOB`                       | Missing Values   | 87                   | Impute with the mode year for consistency.                |
| `job_title`                 | Missing Values   | 506                  | Evaluate and impute using appropriate methods.            |
| `job_industry_category`     | Missing Values   | 656                  | Assess and impute based on relevant criteria.             |
| `gender`                   | Inconsistent Data  | 0                  | ensure a consistent representation (M, Male, Female, F, U)            |
| `tenure`                    | Missing Values   | 87                   | Calculate the mean of tenure values for consistency.       |

**Additional Issues:**

- `default` column contains gibberish data with no meaning. Evaluate and impute using appropriate methods or consider dropping the column for clarity.

### Sheet: CustomerAddress (3999 X 6)

| Column Name                 | Issue Type       | Number of NaN Values | Mitigation                                               |
|-----------------------------|------------------|----------------------|----------------------------------------------------------|
| `state`                     | Inconsistent     | 0                  | Use the dropdown option to gather information.             |

### Sheet: Transactions (2000 X 13)

| Column Name                 | Issue Type       | Number of NaN Values | Mitigation                                               |
|-----------------------------|------------------|----------------------|----------------------------------------------------------|
| `online_order`              | Missing Values   | 360                  | Confirm if NaN values indicate no actual purchase.        |
| `brand`                     | Missing Values   | 197                  | Evaluate and impute using appropriate methods.            |
| `product_line`              | Missing Values   | 197                  | Evaluate and impute using appropriate methods.            |
| `product_class`             | Missing Values   | 197                  | Replace `nan` with mode values for consistency.           |
| `product_size`              | Missing Values   | 197                  | Replace `nan` with mode values for consistency.           |
| `standard_cost`             | Missing Values   | 197                  | Replace `nan` with mode values for consistency.           |
| `product_first_sold_date`   | Missing Values   | 197                  | Replace `nan` with mode values for consistency.           |

### Sheet: NewCustomerList (1000 X 23)

| Column Name                 | Issue Type       | Number of NaN Values | Mitigation                                               |
|-----------------------------|------------------|----------------------|----------------------------------------------------------|
| `last_name`                 | Missing Values   | 29                   | Assign a default last name or use a uniform placeholder.  |
| `DOB`                       | Missing Values   | 17                   | Impute with the mode year for consistency.                |
| `job_title`                 | Missing Values   | 106                  | Evaluate and impute using appropriate methods.            |
| `job_industry_category`     | Missing Values   | 165                  | Assess and impute based on relevant criteria.             |

**Additional Mitigation:**
- Drop additional features with no meaning: 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19' for ease of analysis.

---------

### Recommendations:
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

For the current analysis, we have decided to replace those null values with mean and mode values. 

Thank you for your attention to this matter.

Best regards,

Omkar Pawar

KPMG Data Analytics Team
