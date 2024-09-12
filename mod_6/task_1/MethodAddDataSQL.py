
def add_workers(conn, project):
   """
   Create a new project into the projects table
   :param conn:
   :param project:
   :return: project id
   """
   sql = '''INSERT INTO workers (
            id, first_name, last_name, email, phone_number, hire_date, job_title, department, salary, manager_id
            ) VALUES (?,?,?,?,?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, project)
   conn.commit()
   return cur.lastrowid

def add_companies(conn, task):
   """
   Create a new task into the tasks table
   :param conn:
   :param task:
   :return: task id
   """
   sql = '''INSERT INTO companies (
            id, name, address, city, state, zip_code, country, industry, revenue, founded, employees
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   conn.commit()
   return cur.lastrowid