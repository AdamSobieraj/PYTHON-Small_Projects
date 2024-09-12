from mod_6.task_1.ConnectToDB import create_connection
from mod_6.task_1.MethodExecuteSQL import execute_sql
from mod_6.task_1.MethodAddDataSQL import add_workers, add_companies
from mod_6.task_1.MethodSelectSQL import select_all, select_where
from mod_6.task_1.MethodUpdateSQL import update
from mod_6.task_1.MethodDeleteSQL import delete_all

create_workers_sql = """
-- projects table
CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    hire_date DATE,
    job_title TEXT,
    department TEXT,
    salary REAL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES workers(id)
);
"""
create_companies_sql = """
-- zadanie table
CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    country TEXT,
    industry TEXT,
    revenue REAL,
    founded DATE,
    employees INTEGER,
    FOREIGN KEY (employees) REFERENCES workers(id)
);

"""

db_file_to_store_data = "../myDatabase.db"

def database_fun():
    # open connection
    conn = create_connection(db_file_to_store_data)

    if conn is not None:
        execute_sql(conn, create_workers_sql)
        execute_sql(conn, create_companies_sql)

    # data insert
    workers = (
        (1, 'John', 'Doe', 'john.doe@example.com', '+1234567890', '2020-01-01', 'Software Engineer', 'IT', 75000.00, 1),
        (2, 'Jane', 'Smith', 'jane.smith@example.com', '+9876543210', '2019-06-15', 'Data Scientist', 'Analytics', 90000.00, 1),
        (3, 'Michael', 'Brown', 'michael.brown@example.com', '+5551234567', '2005-03-20', 'CEO', 'Executive', 150000.00, 3),
        (4, 'Sarah', 'Johnson', 'sarah.johnson@example.com', '+4445678901', '2018-09-01', 'Marketing Manager', 'Marketing', 80000.00, 3),
        (5, 'David', 'Wilson', 'david.wilson@example.com', '+2223334444', '2015-02-14', 'Senior Developer', 'IT', 95000.00, 1)
               )

    companies = (
        (1, 'TechCorp Inc.', '1601 Willow Road', 'Menlo Park', 'California', '94025', 'United States', 'Technology', 5000000000.00, '1995-01-01', 5000),
        (2, 'GreenEarth Solutions', '123 Sustainability Drive', 'London', 'Greater London', 'SW1W 9SR', 'United Kingdom', 'Renewable Energy', 3000000000.00, '2008-06-15', 1500),
        (3, 'Healthcare Innovations', '456 Medical Center Drive', 'Boston', 'Massachusetts', '02115', 'United States', 'Healthcare Technology', 2500000000.00, '2010-03-20', 3000),
        (4, 'EcoFriendly Products', '789 Green Street', 'Toronto', 'Ontario', 'M5V 2T6', 'Canada', 'Sustainable Manufacturing', 4000000000.00, '1992-01-02', 4500),
        (5, 'Digital Solutions Inc.', '321 Tech Park Drive', 'Singapore', '', '04898', 'Singapore', 'Information Technology', 3500000000.00, '2005-07-25', 2800)
    )

    workers_id = []
    companies_id = []

    for worker in workers:
        worker_id = add_workers(conn, worker)
        workers_id.append(worker_id)

    for company in companies:
        companie_id = add_companies(conn, company)
        companies_id.append(companie_id)

    print("Added Data")
    print("---------------------------------")
    print(workers_id, companies_id)
    conn.commit()

    print("Database Content")
    print("---------------------------------")
    printAllData(conn, "companies")
    print("---------------------------------")
    printAllData(conn, "workers")

    print("Update")
    print("---------------------------------")
    print("BeforeUpdate")
    print("---------------------------------")
    attrib = {'id':'2'}
    before = select_where(conn, "companies", **attrib)
    print(before)
    print("After Update")
    print("---------------------------------")
    update(conn, "companies", 2, name="LOL")
    attrib = {'id':'2'}
    before = select_where(conn, "companies", **attrib)
    print(before)

    print("Delete")
    print("---------------------------------")
    delete_all(conn, "companies")
    delete_all(conn, "workers")

    print("---------------------------------")
    print("After cleanup")
    print("---------------------------------")

    printAllData(conn, "companies")
    printAllData(conn, "workers")

    conn.close()


def printAllData(conn, table):
    table_ontent = select_all(conn,table)
    print(table_ontent)

def cleanUp(conn, table):
    table_ontent = select_all(conn,table)
    print(table_ontent)

if __name__ == '__main__':
    database_fun()
