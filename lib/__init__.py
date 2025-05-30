from db.connections import get_connection

CONN = get_connection()
CURSOR = CONN.cursor()