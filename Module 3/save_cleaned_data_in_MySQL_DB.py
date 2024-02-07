import mysql.connector
import pandas as pd
conn = mysql.connector.connect(host='localhost', username = 'root', password='PassWorD@6941', database='kpmg_db')

my_cursor = conn.cursor()
# -------------------------------------
def create_new_customers_table():
    table_creation_query = """
    CREATE TABLE new_customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gender VARCHAR(10),
        past_3_years_bike_related_purchases INT,
        job_title VARCHAR(255),
        job_industry_category VARCHAR(255),
        wealth_segment VARCHAR(20),
        deceased_indicator VARCHAR(1),
        owns_car VARCHAR(3),
        tenure INT,
        address VARCHAR(255),
        postcode INT,
        state VARCHAR(10),
        country VARCHAR(20),
        property_valuation INT,
        `Rank` INT,
        Value FLOAT,
        full_name VARCHAR(255),
        age INT
    )
    """
    my_cursor.execute(table_creation_query)
    # ----------------------------------------


    conn.commit()
    conn.close()
    print("successfully created new customers table")

def insert_data_to_new_customers_table():
    data = pd.read_excel('C:\Users\Omkar\Data Science Projects IMP File\KPMG-Virtual-Internship\Data\KPMG_CLEANED_New_Customers_Data.xlsx')

    # Iterate through the rows and insert data into the table
    for _, row in data.iterrows():
        query = """
        INSERT INTO your_table (gender, past_3_years_bike_related_purchases, job_title, job_industry_category, wealth_segment, deceased_indicator, owns_car, tenure, address, postcode, state, country, property_valuation, `Rank`, Value, full_name, age)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            row['gender'], row['past_3_years_bike_related_purchases'], row['job_title'],
            row['job_industry_category'], row['wealth_segment'], row['deceased_indicator'],
            row['owns_car'], row['tenure'], row['address'], row['postcode'], row['state'],
            row['country'], row['property_valuation'], row['Rank'], row['Value'],
            row['full_name'], row['age']
        )
        cursor.execute(query, values)

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()
    print("data inserted successfully")

# create_new_customers_table()
insert_data_to_new_customers_table()