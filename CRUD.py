from build_connection import BuildConnection
import re
db = BuildConnection()

class Student:

    def __init__(self):
        self.conn, self.cursor = db.make_connection()

    def register_student(self, stud_id, stud_name,year,course_id, email=None):
        try:
            query = "SELECT * FROM student WHERE stud_id = %s;"
            self.cursor.execute(query, (stud_id,))
            existing = self.cursor.fetchone()

            if existing is None:
                query = "INSERT INTO student (stud_id, stud_name, year, email, course_id) VALUES (%s, %s, %s, %s, %s);"
                self.cursor.execute(query, (stud_id, stud_name, year, email, course_id))
                self.conn.commit()
                print("Student registered successfully!")
            else:
                print("Student already registered!")
        except Exception as e:
            print("ERROR: ", e)

    def update_student(self, stud_id, update_col, new_var):
        try:
            query = "SELECT * FROM student WHERE stud_id = %s;"
            self.cursor.execute(query, (stud_id,))
            existing = self.cursor.fetchone()

            if existing:
                allowed_col = [desc[0] for desc in self.cursor.description]
                if update_col in allowed_col:
                    query = f"UPDATE student SET `{update_col}` = %s WHERE `stud_id` = %s;"
                    self.cursor.execute(query, (new_var, stud_id))
                    self.conn.commit()
                    print("Student info updated successfully!")
                else:
                    print("Column not found !!")
            else:
                print("Student not found!")
        except Exception as e:
            print("ERROR: ", e)

    def del_student(self,stud_id):
        try:
            query = "SELECT * FROM student WHERE stud_id = %s;"
            self.cursor.execute(query, (stud_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM student WHERE `stud_id` = %s;"
                self.cursor.execute(query, (stud_id,))
                self.conn.commit()
                print("Student info deleted successfully!")
            else:
                print("Student not found!")
        except Exception as e:
            print("ERROR: ", e)

    def del_student_info(self, stud_id, col_name):
        
        try:
            query = "SELECT * FROM student WHERE stud_id = %s;"
            self.cursor.execute(query, (stud_id,))
            existing = self.cursor.fetchone()

            if existing:
                allowed_col = [desc[0] for desc in self.cursor.description]
                if col_name in allowed_col:
                    query = f"UPDATE student SET `{col_name}` = NULL WHERE `stud_id` = %s;"
                    self.cursor.execute(query, (stud_id,))
                    self.conn.commit()
                    print("Student info cleared successfully!")
                else:
                    print("Column not found or restricted!!")
            else:
                print("Student not found!")
        except Exception as e:
            print("ERROR: ", e)

    def get_student_by_id(self, stud_id):
        try:
            query = "SELECT * FROM student WHERE stud_id = %s;"
            self.cursor.execute(query, (stud_id,))
            students = self.cursor.fetchall()
            for student in students:
                print(student)
        except Exception as e:
            print("ERROR: ", e)

    def get_student_by_name(self, stud_name):
        try:
            query = "SELECT * FROM student WHERE stud_name = %s;"
            self.cursor.execute(query, (stud_name,))
            students = self.cursor.fetchall()
            for student in students:
                print(student)
        except Exception as e:
            print("ERROR: ", e)

    def get_all_students(self):
        try:
            query = "SELECT * FROM student;"
            self.cursor.execute(query)
            students = self.cursor.fetchall()
            for student in students:
                print(student)
        except Exception as e:
            print("ERROR: ", e)
    

class Users:

    def __init__(self):
        self.conn, self.cursor = db.make_connection()

    def regiter_user(self, user_id, user_name, role, email = None):
        try:
            query = "SELECT * FROM users WHERE user_id = %s;"
            self.cursor.execute(query, (user_id,))
            existing = self.cursor.fetchone()

            if existing is None:
                query = "INSERT INTO users (user_id, user_name, role, email) VALUES (%s, %s, %s);"
                self.cursor.execute(query, (user_id, user_name, role, email))
                self.conn.commit()
                print("User registered successfully!")
            else:
                print("User already registered!")
        except Exception as e:
            print("ERROR: ", e)

    def get_user_by_id(self, user_id):
        try:
            query = "SELECT * FROM users WHERE user_id = %s;"
            self.cursor.execute(query, (user_id,))
            users = self.cursor.fetchall()
            for user in users:
                print(user)
        except Exception as e:
            print("ERROR: ", e)

    def get_user_by_name(self, user_name):
        try:
            query = "SELECT * FROM users WHERE user_name = %s;"
            self.cursor.execute(query, (user_name,))
            users = self.cursor.fetchall()
            for user in users:
                print(user)
        except Exception as e:
            print("ERROR: ", e)

    def get_all_users(self):
        try:
            query = "SELECT * FROM users;"
            self.cursor.execute(query)
            users = self.cursor.fetchall()
            for user in users:
                print(user)
        except Exception as e:
            print("ERROR: ", e)

    def user_by_role(self, role):
        try:
            if role not in ['module_staff', 'welfare_staff']:
                raise ValueError("Role must be either 'module_staff' or 'welfare_staff'")
            query = "SELECT * FROM users WHERE role = %s;"
            self.cursor.execute(query, (role,))
            users = self.cursor.fetchall()
            for user in users:
                print(user)
        except Exception as e:
            print("ERROR: ", e)

    def del_user(self,user_id):
        try:
            query = "SELECT * FROM users WHERE user_id = %s;"
            self.cursor.execute(query, (user_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM users WHERE `user_id` = %s;"
                self.cursor.execute(query, (user_id,))
                self.conn.commit()
                print("User info deleted successfully!")
            else:
                print("User not found!")
        except Exception as e:
            print("ERROR: ", e)

    def update_user(self, user_id, update_col, new_var):
        try:
            query = "SELECT * FROM users WHERE user_id = %s;"
            self.cursor.execute(query, (user_id,))
            existing = self.cursor.fetchone()

            if existing:
                allowed_col = [desc[0] for desc in self.cursor.description]
                if update_col in allowed_col:
                    query = f"UPDATE users SET `{update_col}` = %s WHERE `user_id` = %s;"
                    self.cursor.execute(query, (new_var, user_id))
                    self.conn.commit()
                    print("User info updated successfully!")
                else:
                    print("Column not found !!")
            else:
                print("User not found!")
        except Exception as e:
            print("ERROR: ", e)
        
    def del_user_info(self, user_id, col_name):
        
        if col_name not in ["user_name", "role", "email"]:
            raise ValueError(f"Invalid or restricted column name provided: '{col_name}'. Only allowed columns can be cleared.")        
        try:
            query = "SELECT * FROM users WHERE user_id = %s;"
            self.cursor.execute(query, (user_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = f"UPDATE users SET `{col_name}` = NULL WHERE `user_id` = %s;"
                self.cursor.execute(query, (user_id,))
                self.conn.commit()
                print("User info cleared successfully!")
            else:
                print("User not found!")
        except Exception as e:
            print("ERROR: ", e)

class Course:

    def __init__(self):
        self.conn, self.cursor = db.make_connection()

    def register_course(self, course_id, course_name):
        try:
            query = "SELECT * FROM course WHERE course_id = %s;"
            self.cursor.execute(query, (course_id,))
            existing = self.cursor.fetchone()

            if existing is None:
                query = "INSERT INTO course (course_id, course_name) VALUES (%s, %s);"
                self.cursor.execute(query, (course_id, course_name))
                self.conn.commit()
                print("Course registered successfully!")
            else:
                print("Course already registered!")
        except Exception as e:
            print("ERROR: ", e)

    def get_course_by_id(self, course_id):
        try:
            query = "SELECT * FROM course WHERE course_id = %s;"
            self.cursor.execute(query, (course_id,))
            courses = self.cursor.fetchall()
            for course in courses:
                print(course)
        except Exception as e:
            print("ERROR: ", e)
    
    def get_course_by_name(self, course_name):
        try:
            query = "SELECT * FROM course WHERE course_name = %s;"
            self.cursor.execute(query, (course_name,))
            courses = self.cursor.fetchall()
            for course in courses:
                print(course)
        except Exception as e:
            print("ERROR: ", e)

    def get_all_courses(self):
        try:
            query = "SELECT * FROM course;"
            self.cursor.execute(query)
            courses = self.cursor.fetchall()
            for course in courses:
                print(course)
        except Exception as e:
            print("ERROR: ", e)

    def del_course_by_course_id(self,course_id):
        try:
            query = "SELECT * FROM course WHERE course_id = %s;"
            self.cursor.execute(query, (course_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM course WHERE `course_id` = %s;"
                self.cursor.execute(query, (course_id,))
                self.conn.commit()
                print("Course info deleted successfully!")
            else:
                print("Course not found!")
        except Exception as e:
            print("ERROR: ", e)

    def del_course_by_course_name(self,course_name):
        try:
            query = "SELECT * FROM course WHERE course_name = %s;"
            self.cursor.execute(query, (course_name,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM course WHERE `course_name` = %s;"
                self.cursor.execute(query, (course_name,))
                self.conn.commit()
                print("Course info deleted successfully!")
            else:
                print("Course not found!")
        except Exception as e:
            print("ERROR: ", e)
        
    def update_course_name(self, course_id, new_var):
        try:
            query = "SELECT * FROM course WHERE course_id = %s;"
            self.cursor.execute(query, (course_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = "UPDATE course SET `course_name` = %s WHERE `course_id` = %s;"
                self.cursor.execute(query, (new_var, course_id))
                self.conn.commit()
                print("Course info updated successfully!")
            else:
                print("Course not found!")
        except Exception as e:
            print("ERROR: ", e)

    def update_course_id(self, course_id, new_id):
        try:
            query = "SELECT * FROM course WHERE course_id = %s;"
            self.cursor.execute(query, (course_id,))
            existing = self.cursor.fetchone()

            if existing:
                self.cursor.execute("SELECT * FROM course WHERE course_id = %s;", (new_id,))
                if self.cursor.fetchone():
                    print("New course_id already exists! Choose a different one.")
                    return
                else:
                    query = "UPDATE course SET `course_id` = %s WHERE `course_id` = %s;"
                    self.cursor.execute(query, (new_id, course_id))
                    self.conn.commit()
                    print("Course info updated successfully!")
            else:
                print("Course not found!")
        except Exception as e:
            print("ERROR: ", e)

class Module:

    def __init__(self):
        self.conn, self.cursor = db.make_connection()
    
    def register_module(self, mod_id, mod_name, course_id, year, welfare_staff_id, module_staff_id):
        try:
            query = "SELECT * FROM module WHERE mod_id = %s;"
            self.cursor.execute(query, (mod_id,))
            existing = self.cursor.fetchone()

            if existing is None:
                query = "INSERT INTO module (mod_id, mod_name, course_id, year, welfare_staff_id, module_staff_id) VALUES (%s, %s, %s, %s, %s, %s);"
                self.cursor.execute(query, (mod_id, mod_name, course_id, year, welfare_staff_id, module_staff_id))
                self.conn.commit()
                print("Module registered successfully!")
            else:
                print("Module already registered!")
        except Exception as e:
            print("ERROR: ", e) 

    def get_module_by_id(self, mod_id):
        try:
            query = "SELECT * FROM module WHERE mod_id = %s;"
            self.cursor.execute(query, (mod_id,))
            modules = self.cursor.fetchall()
            if modules is None:
                print("Module id not found!")
                return
            for module in modules:
                print(module)
        except Exception as e:
            print("ERROR: ", e)
        
    def get_module_by_name(self, mod_name):
        try:
            query = "SELECT * FROM module WHERE mod_name = %s;"
            self.cursor.execute(query, (mod_name,))
            modules = self.cursor.fetchall()
            if modules is None:
                print("Module name not found!")
                return
            for module in modules:
                print(module)
        except Exception as e:
            print("ERROR: ", e)

    def get_all_modules(self):
        try:
            query = "SELECT * FROM module;"
            self.cursor.execute(query)
            modules = self.cursor.fetchall()
            for module in modules:
                print(module)
        except Exception as e:
            print("ERROR: ", e)
    
    def del_module_by_id(self,mod_id):
        try:
            query = "SELECT * FROM module WHERE mod_id = %s;"
            self.cursor.execute(query, (mod_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM module WHERE `mod_id` = %s;"
                self.cursor.execute(query, (mod_id,))
                self.conn.commit()
                print("Module info deleted successfully!")
            else:
                print("Module not found!")
        except Exception as e:
            print("ERROR: ", e)

    def del_module_by_name(self,mod_name):
        try:
            query = "SELECT * FROM module WHERE mod_name = %s;"
            self.cursor.execute(query, (mod_name,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM module WHERE `mod_name` = %s;"
                self.cursor.execute(query, (mod_name,))
                self.conn.commit()
                print("Module info deleted successfully!")
            else:
                print("Module not found!")
        except Exception as e:
            print("ERROR: ", e)
    
    def del_module_info(self, mod_id, col_name):

        try:
            query = "SELECT * FROM module WHERE mod_id = %s;"
            self.cursor.execute(query, (mod_id,))
            existing = self.cursor.fetchone()

            if existing:
                allowed_col = [desc[0] for desc in self.cursor.description]
                if col_name in allowed_col:
                    query = f"UPDATE module SET `{col_name}` = NULL WHERE `mod_id` = %s;"
                    self.cursor.execute(query, (mod_id,))
                    self.conn.commit()
                    print("Module info cleared successfully!")
                else:
                    print("Column not found !!")
            else:
                print("Module not found!")
        except Exception as e:
            print("ERROR: ", e)

    def update_module(self, mod_id, update_col, new_var):  
        try:
            query = "SELECT * FROM module WHERE mod_id = %s;"
            self.cursor.execute(query, (mod_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = f"UPDATE module SET `{update_col}` = %s WHERE `mod_id` = %s;"
                self.cursor.execute(query, (new_var, mod_id))
                self.conn.commit()
                print("Module info updated successfully!")
            else:
                print("Module not found!")
        except Exception as e:
            print("ERROR: ", e)
    
class Deadlines:

    def __init__(self):
        self.conn, self.cursor = db.make_connection()

    def set_deadline(self, dead_id, mod_id, week_no, due_date, ass_name = None):
        try:
            query = "SELECT * FROM deadline WHERE dead_id = %s;"
            self.cursor.execute(query, (dead_id,))
            existing = self.cursor.fetchone()

            if existing is None:
                query = "INSERT INTO module (mod_id, mod_name, course_id, year, welfare_staff_id, module_staff_id) VALUES (%s, %s, %s, %s, %s, %s);"
                self.cursor.execute(query, (dead_id, mod_id, mod_id, week_no,ass_name, due_date))
                self.conn.commit()
                print("Deadline set successfully!")
            else:
                print("Deadline already set!")
        except Exception as e:
            print("ERROR: ", e)
    
    def get_deadlines(self):
        try:
            query = "SELECT * FROM deadlines;"
            self.cursor.execute(query)
            deadlines = self.cursor.fetchall()
            for deadline in deadlines:
                print(deadline)
        except Exception as e:
            print("ERROR: ", e)

    def get_deadline_by_dead_id(self,dead_id):
        try:
            query = "SELECT * FROM deadline WHERE dead_id = %s;"
            self.cursor.execute(query,(dead_id,))
            deadline = self.cursor.fetchone()
            if deadline:
                print("Deadline Found!: ", deadline)     
            else:
                print(f"Deadline Not Found for the id: {dead_id}!!")       
        except Exception as e:
            print("ERROR:",e)
    
    def get_deadline_by_mod_id(self,mod_id):
        try:
            query = "SELECT * FROM deadline WHERE mod_id = %s;"
            self.cursor.execute(query,(mod_id,))
            deadlines = self.cursor.fetchall()
            if deadlines:
                for deadline in deadlines:
                    print("Deadline Found!: ", deadline)     
            else:
                print(f"Deadline Not Found for the module id: {mod_id}!!")    
        except Exception as e:
            print("ERROR:",e)
    
    def get_deadline_by_week_no(self,week_no):
        try:
            query = "SELECT * FROM deadline WHERE week_no = %s;"
            self.cursor.execute(query,(week_no,))
            deadlines = self.cursor.fetchall()
            if deadlines:
                for deadline in deadlines:
                    print("Deadline Found!: ", deadline)     
            else:
                print(f"Deadline Not Found for the week no: {week_no}!!")    
        except Exception as e:
            print("ERROR:",e)

    def get_deadline_by_ass_name(self,ass_name):
        try:
            query = "SELECT * FROM deadline WHERE ass_name = %s;"
            self.cursor.execute(query,(ass_name,))
            deadlines = self.cursor.fetchall()
            if deadlines:
                for deadline in deadlines:
                    print("Deadline Found!: ", deadline)     
            else:
                print(f"Deadline Not Found for the assessment name: {ass_name}!!")    
        except Exception as e:
            print("ERROR:",e)

    def get_deadline_by_due_date(self, due_date):
        try:
            query = "SELECT * FROM deadline WHERE due_date = %s;"
            self.cursor.execute(query,(due_date,))
            deadlines = self.cursor.fetchall()
            if deadlines:
                for deadline in deadlines:
                    print("Deadline Found!: ", deadline)     
            else:
                print(f"Deadline Not Found for the assessment name: {due_date}!!")    
        except Exception as e:
            print("ERROR:",e)

    def del_deadline_by_dead_id(self, dead_id):
        try:
            query = "SELECT * FROM deadlines WHERE dead_id = %s;"
            self.cursor.execute(query, (dead_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM deadlines WHERE `dead_id` = %s;"
                self.cursor.execute(query, (dead_id,))
                self.conn.commit()
                print("Deadline deleted successfully!")
            else:
                print("Deadline not found!")
        except Exception as e:
            print("ERROR: ", e)
        
    def del_deadline_by_ass_name(self, ass_name):
        try:
            query = "SELECT * FROM deadlines WHERE ass_name = %s;"
            self.cursor.execute(query, (ass_name,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM deadlines WHERE `ass_name` = %s;"
                self.cursor.execute(query, (ass_name,))
                self.conn.commit()
                print("Deadline deleted successfully!")
            else:
                print("Deadline not found!")
        except Exception as e:
            print("ERROR: ", e)

    def del_deadline_by_due_date(self, due_date):
        try:
            query = "SELECT * FROM deadlines WHERE due_date = %s;"
            self.cursor.execute(query, (due_date,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM deadlines WHERE `due_date` = %s;"
                self.cursor.execute(query, (due_date,))
                self.conn.commit()
                print("Deadline deleted successfully!")
            else:
                print("Deadline not found!")
        except Exception as e:
            print("ERROR: ", e)
    
    def del_deadline_by_mod_id(self, mod_id):
        try:
            query = "SELECT * FROM deadlines WHERE mod_id = %s;"
            self.cursor.execute(query, (mod_id,))
            existing = self.cursor.fetchone()

            if existing:
                query = "DELETE FROM deadlines WHERE `mod_id` = %s;"
                self.cursor.execute(query, (mod_id,))
                self.conn.commit()
                print("Deadline deleted successfully!")
            else:
                print("Deadline not found!")
        except Exception as e:
            print("ERROR: ", e)
    
    def del_deadline_info(self, dead_id, col_name):
             
        try:
            query = "SELECT * FROM deadlines WHERE dead_id = %s;"
            self.cursor.execute(query, (dead_id,))
            existing = self.cursor.fetchone()

            if existing:
                allowed_col = [desc[0] for desc in self.cursor.description]
                if col_name in allowed_col:
                    query = f"UPDATE deadlines SET `{col_name}` = NULL WHERE `dead_id` = %s;"
                    self.cursor.execute(query, (dead_id,))
                    self.conn.commit()
                    print("Deadline info cleared successfully!")
            else:
                print("Deadline not found!")
        except Exception as e:
            print("ERROR: ", e)

    def update_deadline_by_dead_id(self, dead_id, update_col, new_var):   
        try:
            query = "SELECT * FROM deadlines WHERE dead_id = %s;"
            self.cursor.execute(query, (dead_id,))
            existing = self.cursor.fetchone()

            if existing:
                allowed_col = [desc[0] for desc in self.cursor.description]
                if update_col in allowed_col:
                    query = f"UPDATE deadlines SET `{update_col}` = %s WHERE `dead_id` = %s;"
                    self.cursor.execute(query, (new_var, dead_id))
                    self.conn.commit()
                    print("Deadline info updated successfully!")
                else:
                    print("Column not found !!")
            else:
                print("Deadline not found!")
        except Exception as e:
            print("ERROR: ", e)
    
    def update_deadline_by_mod_id(self, mod_id, update_col, new_var):   
        try:
            query = "SELECT * FROM deadlines WHERE mod_id = %s;"
            self.cursor.execute(query, (mod_id,))
            existing = self.cursor.fetchone()

            if existing:
                allowed_col = [desc[0] for desc in self.cursor.description]
                if update_col in allowed_col:
                    query = f"UPDATE deadlines SET `{update_col}` = %s WHERE `mod_id` = %s;"
                    self.cursor.execute(query, (new_var, mod_id))
                    self.conn.commit()
                    print("Deadline info updated successfully!")
                else:
                    print("Column not found !!")
            else:
                print("Deadline not found!")
        except Exception as e:
            print("ERROR: ", e)
        


    
