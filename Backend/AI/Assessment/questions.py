"""
Comprehensive Question Bank for Personalized Learning System.
Contains 10 hierarchical topics for OOPS, Data Structures, and Database Systems.
Each topic contains exactly 30 questions ordered strictly from Easy (1-10) to Medium (11-20) to Hard (21-30).
"""

from .questions_oops import oops_questions
from .questions_dsa import dsa_questions
from .questions_dbms import dbms_questions

# Construct full questions dictionary with aliases for backwards compatibility
questions = {
    "OOPS": dict(oops_questions),
    "Data Structures": dict(dsa_questions),
    "Database Systems": dict(dbms_questions),
}

# Aliases for OOPS
questions["OOPS"]["Inheritance"] = questions["OOPS"]["Inheritance Basics"]
questions["OOPS"]["Encapsulation"] = questions["OOPS"]["Encapsulation and Data Hiding"]
questions["OOPS"]["Abstraction"] = questions["OOPS"]["Abstraction and Interfaces"]
questions["OOPS"]["Polymorphism"] = questions["OOPS"]["Method Overriding and Dynamic Dispatch"]

# Aliases for Data Structures
questions["Data Structures"]["Arrays"] = questions["Data Structures"]["Arrays and Memory Layouts"]
questions["Data Structures"]["Linked Lists"] = questions["Data Structures"]["Singly Linked Lists"]

# Aliases for Database Systems
questions["Database Systems"]["SQL Basics"] = questions["Database Systems"]["Basic SQL Queries"]
