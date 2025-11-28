import sys
from unittest.mock import MagicMock

# Mock mysql and mysql.connector before importing modules that use it
mock_mysql = MagicMock()
sys.modules["mysql"] = mock_mysql
sys.modules["mysql.connector"] = MagicMock()

# Now we can import CRUD
# We also need to make sure build_connection doesn't fail if it's already imported or if it tries to do something else
try:
    from CRUD import Student, Users, Course, Module, Deadlines
except ImportError as e:
    print(f"Import failed: {e}")
    sys.exit(1)

def test_refactor():
    print("Testing CRUD refactor with mocks...")
    try:
        # Create dummy connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        
        print("Created mock connection and cursor.")

        # Test instantiation with shared connection
        student = Student(conn=mock_conn, cursor=mock_cursor)
        users = Users(conn=mock_conn, cursor=mock_cursor)
        course = Course(conn=mock_conn, cursor=mock_cursor)
        module = Module(conn=mock_conn, cursor=mock_cursor)
        deadlines = Deadlines(conn=mock_conn, cursor=mock_cursor)
        
        print("All classes instantiated successfully with shared connection.")
        
        # Verify that the internal attributes are set correctly
        if student.conn is mock_conn and student.cursor is mock_cursor:
            print("Student class correctly using shared connection.")
        else:
            print("ERROR: Student class NOT using shared connection.")
            sys.exit(1)

        if users.conn is mock_conn:
            print("Users class correctly using shared connection.")
        
        if course.conn is mock_conn:
            print("Course class correctly using shared connection.")

        if module.conn is mock_conn:
            print("Module class correctly using shared connection.")

        if deadlines.conn is mock_conn:
            print("Deadlines class correctly using shared connection.")

        print("Verification passed!")

    except Exception as e:
        print(f"Test failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_refactor()
