"""
Contains the services related to student
"""


def add_student(name):
    """
    Add a student to the DB
    Args:
        name (str): Name of the student

    Returns:
        None
    """
    return f"Student {name} added successfully"


def get_student(name: str):
    """
    Get the student object when the student name is supplied
    Args:
        name (str): student name

    Returns:
        Student object as a dictionary
    """
    return {"name": name}
