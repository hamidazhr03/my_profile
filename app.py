import sqlite3

# Create a connection to the database
conn = sqlite3.connect('bio.db')

# Create a cursor object
cur = conn.cursor()

# Create the table
cur.execute('''
    CREATE TABLE bio (
        id INTEGER PRIMARY KEY,
        name TEXT,
        university TEXT,
        major TEXT,
        description TEXT
    )
''')

# Insert some sample data
cur.execute("INSERT INTO bio VALUES (1, 'Hamid Azhar Abdillah', 'AMIKOM University', 'Computer Engineering', 'An engineer who loves solving problem')")

# Commit the changes
conn.commit()

# Close the connection
conn.close()