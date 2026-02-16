import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect("example.db")

# Create cursor
cursor = conn.cursor()

# Run query
cursor.execute("SELECT * FROM users")

# Fetch data
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close connection
conn.close()
