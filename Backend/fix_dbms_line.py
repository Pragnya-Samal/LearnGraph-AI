with open('Backend/create_dbms_bank.py', 'r', encoding='utf-8') as f:
    text = f.read()

bad = '''make_q("What is a Composite Primary Key?", ["A primary key composed of two or more columns that together uniquely identify a record", "A key that combines numbers and text", "A key that references three different databases", "An encrypted primary key"], "A Composite Primary Key is formed by multiple columns to guarantee row uniqueness.", "What is a Composite Primary Key?", "A primary key composed of two or more columns that together uniquely identify a record", "Medium"),'''

good = '''make_q("What is a Composite Primary Key?", ["A primary key composed of two or more columns that together uniquely identify a record", "A key that combines numbers and text", "A key that references three different databases", "An encrypted primary key"], "A primary key composed of two or more columns that together uniquely identify a record", "A composite primary key combines multiple attributes to establish unique tuple identification.", "Medium"),'''

text = text.replace(bad, good)
with open('Backend/create_dbms_bank.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed create_dbms_bank.py line.")

