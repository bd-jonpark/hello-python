#!/usr/bin/env python3
"""
hello-python - Sample Python code with intentional defects for static analysis testing

This file contains common Python defects that static analysis tools can detect:
- SQL Injection
- Command Injection
- Path Traversal
- Hardcoded Credentials
- Insecure Deserialization
- Resource Leak
"""

import os
import pickle
import sqlite3
import subprocess


# SQL Injection defect
def get_user_by_name(username):
    """SQL injection vulnerability - user input directly in query"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # SQLI: User input directly concatenated into SQL query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


# Command Injection defect
def run_command(user_input):
    """Command injection vulnerability"""
    # COMMAND_INJECTION: User input passed to shell
    os.system("echo " + user_input)
    subprocess.call(user_input, shell=True)


# Path Traversal defect
def read_file(filename):
    """Path traversal vulnerability"""
    # PATH_TRAVERSAL: User input used in file path without sanitization
    base_path = "/var/data/"
    file_path = base_path + filename
    with open(file_path, 'r') as f:
        return f.read()


# Hardcoded Credentials defect
def connect_to_database():
    """Hardcoded credentials vulnerability"""
    # HARDCODED_CREDENTIALS
    db_user = "admin"
    db_password = "secret123"
    db_host = "localhost"
    connection_string = f"mysql://{db_user}:{db_password}@{db_host}/mydb"
    return connection_string


# Insecure Deserialization defect
def load_user_data(serialized_data):
    """Insecure deserialization vulnerability"""
    # INSECURE_DESERIALIZATION: Unpickling untrusted data
    return pickle.loads(serialized_data)


# Resource Leak defect
def process_file(filename):
    """Resource leak - file handle not closed"""
    # RESOURCE_LEAK: File opened but not closed
    f = open(filename, 'r')
    data = f.read()
    return data


# Null/None dereference
def get_value(data):
    """Potential None dereference"""
    result = data.get('key')
    # NULL_RETURNS: result could be None
    return result.upper()


def main():
    print("hello-python: Static Analysis Test Program")
    print("==========================================")
    print("This file contains intentional defects for testing.")
    print("Program completed successfully.")


if __name__ == "__main__":
    main()
