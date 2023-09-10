import sqlite3, os

cwd = os.path.dirname(__file__)
# Create a SQLite database connection
conn = sqlite3.connect(f"{cwd}/persons.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store person records if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age TEXT NOT NULL
    )
"""
)
conn.commit()


person_details = ["id", "name", "age"]


# Function to create a new person record
def db_create_person(name: str, age: str):
    cursor.execute("INSERT INTO persons (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return (
        cursor.lastrowid,
        name,
        age,
    )  # Return the ID and details of the newly created person


# Function to read a person by name
def db_read_person(name: str):
    cursor.execute("SELECT id, name, age FROM persons WHERE name = ?", (name,))
    return cursor.fetchone()


# Function to update a person's age by name
def db_update_person_age(name: str, age: str):
    cursor.execute("UPDATE persons SET age = ? WHERE name = ?", (age, name))
    conn.commit()
    return db_read_person(name)


# Function to delete a person by name
def db_delete_person(name: str):
    cursor.execute("DELETE FROM persons WHERE name = ?", (name,))
    conn.commit()


def person_map(tup):
    return dict(zip(person_details, tup))
