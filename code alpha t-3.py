username = input("Enter username: ")

query = "SELECT * FROM users WHERE username = '" + username + "'"
print(query)
Secure Version
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")

query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))

print("Query executed securely")
conn.close()
Vulnerabilities Found
SQL Injection

Input Validation Missing

Error Handling Missing

Recommendations
Use parameterized queries.

Validate user input.

Implement exception handling.

Follow secure coding standards.
