import sys
sys.path.insert(0, "Backend")
import database

conn = database.get_connection()
cursor = conn.cursor()
cursor.execute("""
    SELECT s.name AS subject_name, t.display_order, t.name AS topic_name, t.difficulty 
    FROM topic t 
    JOIN subject s ON t.subject_id = s.subject_id 
    ORDER BY s.name, t.display_order
""")
for row in cursor.fetchall():
    print(f"{row['subject_name']} | {row['display_order']} | {row['topic_name']} | {row['difficulty']}")
