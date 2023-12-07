from connection import DBConnectionHandler

def test_connection():
    with DBConnectionHandler() as conn:
        print(conn)

test_connection()