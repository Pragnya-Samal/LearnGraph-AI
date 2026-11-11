import os
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional

DB_PATH = Path(__file__).resolve().parent / "personalized_learning.db"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"


def get_connection():
    """Get a thread-safe connection to SQLite database with foreign keys enabled."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    """Create all tables and indexes defined in schema.sql."""
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    with get_connection() as conn:
        conn.executescript(schema_sql)
        conn.commit()

    seed_initial_data()


def seed_initial_data():
    """
    Seed 10 hierarchical topics for each subject (Easy to Hard).
    Study materials are strictly YouTube links and reference websites only (no PDFs, no raw video files).
    """
    subjects_data = [
        {
            "name": "OOPS",
            "code": "CS-OOP-201",
            "description": "Object-Oriented Programming Principles and Architecture in C++, Java, and Python",
            "topics": [
                {
                    "name": "Classes and Objects",
                    "description": "Class blueprints, object instantiation, state, behavior, memory allocation, and instance attributes",
                    "difficulty": "Beginner",
                    "display_order": 1,
                    "materials": [
                        {
                            "title": "Classes and Objects in OOP - Visual Guide",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=pTB0EiLXUC8",
                            "description": "Visual explanation of classes as blueprints and creating object instances in memory"
                        },
                        {
                            "title": "GeeksforGeeks - Classes and Objects in Java & C++",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/classes-objects-java/",
                            "description": "Comprehensive tutorial on defining classes, declaring objects, and accessing instance members"
                        }
                    ]
                },
                {
                    "name": "Constructors and Destructors",
                    "description": "Default, parameterized, copy constructors, destructor cleanup, and object lifecycle management",
                    "difficulty": "Beginner",
                    "display_order": 2,
                    "materials": [
                        {
                            "title": "Constructors and Destructors in 5 Minutes",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=1n_Z_fV5Z58",
                            "description": "Clear animated breakdown of constructor overloading, default arguments, and destructor invocation"
                        },
                        {
                            "title": "W3Schools - C++ / Java Constructors Tutorial",
                            "type": "website",
                            "url": "https://www.w3schools.com/java/java_constructors.asp",
                            "description": "Interactive web reference with syntax and examples for parameterized constructors"
                        }
                    ]
                },
                {
                    "name": "Encapsulation and Data Hiding",
                    "description": "Information hiding, access modifiers (private, protected, public), and getter/setter methods",
                    "difficulty": "Beginner",
                    "display_order": 3,
                    "materials": [
                        {
                            "title": "Encapsulation in 100 Seconds",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=0k5kP0e7Kps",
                            "description": "Fast-paced visual tutorial on data protection and restricting direct field access"
                        },
                        {
                            "title": "Baeldung - Encapsulation in OOP",
                            "type": "website",
                            "url": "https://www.baeldung.com/java-encapsulation",
                            "description": "In-depth guide on immutability, protective copying, and encapsulation contracts"
                        }
                    ]
                },
                {
                    "name": "Inheritance Basics",
                    "description": "Base classes, derived classes, single inheritance, reusability, and the IS-A relationship",
                    "difficulty": "Beginner",
                    "display_order": 4,
                    "materials": [
                        {
                            "title": "Inheritance in OOP Explained Simply",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=RMBn_O6eUoA",
                            "description": "Parent and child classes, code reuse, and hierarchical relationships visualized"
                        },
                        {
                            "title": "Oracle Official Java Tutorials: Inheritance",
                            "type": "website",
                            "url": "https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html",
                            "description": "Official documentation covering subclasses, superclass methods, and casting"
                        }
                    ]
                },
                {
                    "name": "Multilevel and Multiple Inheritance",
                    "description": "Inheritance chains, diamond problem, virtual base classes, interfaces as mixins",
                    "difficulty": "Intermediate",
                    "display_order": 5,
                    "materials": [
                        {
                            "title": "The Diamond Problem & Multiple Inheritance",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=vV95u0vXWxE",
                            "description": "Detailed video resolving ambiguities in multiple inheritance using virtual base classes"
                        },
                        {
                            "title": "GeeksforGeeks - Multiple Inheritance in C++ and Java",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/multiple-inheritance-in-c/",
                            "description": "Reference tutorial detailing why Java uses interfaces and C++ uses virtual inheritance"
                        }
                    ]
                },
                {
                    "name": "Method Overloading",
                    "description": "Compile-time polymorphism, function signatures, operator overloading, and static binding",
                    "difficulty": "Intermediate",
                    "display_order": 6,
                    "materials": [
                        {
                            "title": "Method Overloading Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=8y1_N7E06B8",
                            "description": "Explaining static polymorphism, method signature rules, and compile-time resolution"
                        },
                        {
                            "title": "W3Schools - Method Overloading Guide",
                            "type": "website",
                            "url": "https://www.w3schools.com/java/java_methods_overloading.asp",
                            "description": "Hands-on guide to changing parameter count and types with overloading"
                        }
                    ]
                },
                {
                    "name": "Method Overriding and Dynamic Dispatch",
                    "description": "Runtime dynamic polymorphism, virtual functions, vtables, override keyword, late binding",
                    "difficulty": "Intermediate",
                    "display_order": 7,
                    "materials": [
                        {
                            "title": "Polymorphism & Dynamic Method Dispatch",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=4bmS1lbfvyo",
                            "description": "YouTube video tutorial walking through runtime dispatch and vtables"
                        },
                        {
                            "title": "MDN Web Docs - Polymorphism & Overriding",
                            "type": "website",
                            "url": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance",
                            "description": "Modern developer guide to polymorphic object hierarchies and method overriding"
                        }
                    ]
                },
                {
                    "name": "Abstraction and Interfaces",
                    "description": "Pure virtual functions, abstract classes, interface contracts, and loose architectural coupling",
                    "difficulty": "Intermediate",
                    "display_order": 8,
                    "materials": [
                        {
                            "title": "Abstraction in OOP - Full Video Walkthrough",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=Ui7AX364PJE",
                            "description": "YouTube tutorial exploring how abstraction decouples high-level policy from low-level details"
                        },
                        {
                            "title": "Baeldung - Abstract Classes vs Interfaces",
                            "type": "website",
                            "url": "https://www.baeldung.com/java-interface-vs-abstract-class",
                            "description": "In-depth web comparison of abstraction contracts, abstract classes, and interface defaults"
                        }
                    ]
                },
                {
                    "name": "Composition and Aggregation",
                    "description": "HAS-A relationships, composition over inheritance, loose coupling, and object lifecycles",
                    "difficulty": "Advanced",
                    "display_order": 9,
                    "materials": [
                        {
                            "title": "Composition over Inheritance Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=wfMtDGfHWpA",
                            "description": "Explaining why composition provides greater flexibility and avoids deep inheritance trees"
                        },
                        {
                            "title": "GeeksforGeeks - Association, Composition and Aggregation",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/association-composition-aggregation-java/",
                            "description": "Clear conceptual diagrams differentiating weak aggregation from strong composition"
                        }
                    ]
                },
                {
                    "name": "SOLID Principles and Design Patterns",
                    "description": "Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion",
                    "difficulty": "Advanced",
                    "display_order": 10,
                    "materials": [
                        {
                            "title": "SOLID Principles in 8 Minutes",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=kF7rQmSRlq0",
                            "description": "Crisp animated overview of all five SOLID object-oriented architectural principles"
                        },
                        {
                            "title": "Refactoring Guru - Design Patterns & SOLID",
                            "type": "website",
                            "url": "https://refactoring.guru/design-patterns",
                            "description": "World-class visual guide to creational, structural, and behavioral OOP patterns"
                        }
                    ]
                }
            ]
        },
        {
            "name": "Data Structures",
            "code": "CS-DSA-102",
            "description": "Fundamental data structures, time and space complexity, and memory layouts",
            "topics": [
                {
                    "name": "Arrays and Memory Layouts",
                    "description": "Contiguous memory allocations, index arithmetic, multidimensional layouts, and dynamic arrays",
                    "difficulty": "Beginner",
                    "display_order": 1,
                    "materials": [
                        {
                            "title": "Arrays Data Structure in 10 Minutes",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=pmN9ExDf3yA",
                            "description": "YouTube animated tutorial on memory indexing, O(1) random access, and cache locality"
                        },
                        {
                            "title": "GeeksforGeeks - Array Data Structure Complete Roadmap",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/array-data-structure-guide/",
                            "description": "Curated reference website covering two pointers, sliding window, and prefix sums"
                        }
                    ]
                },
                {
                    "name": "Strings and String Manipulation",
                    "description": "Character encoding, string immutability, two-pointer patterns, string matching, and sliding windows",
                    "difficulty": "Beginner",
                    "display_order": 2,
                    "materials": [
                        {
                            "title": "String Algorithms & Techniques Crash Course",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=0k5kP0e7Kps",
                            "description": "Video guide on common string algorithms, palindrome checks, and memory representations"
                        },
                        {
                            "title": "W3Schools - String Data Structures",
                            "type": "website",
                            "url": "https://www.w3schools.com/dsa/dsa_algo_strings.php",
                            "description": "Interactive guide to string traversal, anagram verification, and string builder patterns"
                        }
                    ]
                },
                {
                    "name": "Singly Linked Lists",
                    "description": "Node pointers, singly linked lists, insertion, deletion, reversal, and cycle detection",
                    "difficulty": "Beginner",
                    "display_order": 3,
                    "materials": [
                        {
                            "title": "Linked Lists Crash Course",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=njTh_OwMljA",
                            "description": "YouTube step-by-step coding and diagramming of singly and doubly linked nodes"
                        },
                        {
                            "title": "Visualgo.net - Interactive Linked List Visualization",
                            "type": "website",
                            "url": "https://visualgo.net/en/list",
                            "description": "Interactive website visualization of node insertions, deletions, and traversals"
                        }
                    ]
                },
                {
                    "name": "Doubly and Circular Linked Lists",
                    "description": "Two-way pointer traversal, circular linked lists, sentinel nodes, and constant-time deque operations",
                    "difficulty": "Intermediate",
                    "display_order": 4,
                    "materials": [
                        {
                            "title": "Doubly Linked List in 7 Minutes",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=JdQeNxWCguQ",
                            "description": "Clear visual walk-through of forward/backward pointers and node manipulations"
                        },
                        {
                            "title": "GeeksforGeeks - Doubly Linked List Guide",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/doubly-linked-list/",
                            "description": "Comprehensive reference covering insertion, deletion, and circular variations"
                        }
                    ]
                },
                {
                    "name": "Stacks (LIFO Operations)",
                    "description": "LIFO mechanics, stack frames, parentheses validation, postfix evaluation, and monotonic stacks",
                    "difficulty": "Intermediate",
                    "display_order": 5,
                    "materials": [
                        {
                            "title": "Stack Data Structure Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=I5lq6sCuABE",
                            "description": "Visual explanation of push, pop, peek, and call stack frame management"
                        },
                        {
                            "title": "Programiz - Stack Data Structure Guide",
                            "type": "website",
                            "url": "https://www.programiz.com/dsa/stack",
                            "description": "Detailed illustrations and code examples of array- and list-based stack implementations"
                        }
                    ]
                },
                {
                    "name": "Queues and Deques (FIFO)",
                    "description": "FIFO queues, circular queues, priority queues, double-ended queues (deque), and BFS buffers",
                    "difficulty": "Intermediate",
                    "display_order": 6,
                    "materials": [
                        {
                            "title": "Queue Data Structure in 6 Minutes",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=D6gu-_tm9g8",
                            "description": "Animation of enqueue and dequeue operations, head/tail pointers, and circular queue wrapping"
                        },
                        {
                            "title": "GeeksforGeeks - Queue Data Structure Complete Reference",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/queue-data-structure/",
                            "description": "Tutorial covering linear, circular, double-ended, and priority queue applications"
                        }
                    ]
                },
                {
                    "name": "Hash Tables and Hashing",
                    "description": "Hash functions, load factor, collision resolution (chaining, open addressing), O(1) average lookup",
                    "difficulty": "Intermediate",
                    "display_order": 7,
                    "materials": [
                        {
                            "title": "Hash Tables and Hash Functions Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=shs0KM3wKv8",
                            "description": "Visual breakdown of hashing keys, buckets, collisions, and load factor rehashing"
                        },
                        {
                            "title": "FreeCodeCamp - How Hash Tables Work Under the Hood",
                            "type": "website",
                            "url": "https://www.freecodecamp.org/news/hash-tables/",
                            "description": "Detailed guide on collision handling, chaining vs open addressing, and complexity"
                        }
                    ]
                },
                {
                    "name": "Binary Trees and Traversals",
                    "description": "Hierarchical structures, tree terminology, depth, height, preorder, inorder, postorder, and BFS level-order",
                    "difficulty": "Advanced",
                    "display_order": 8,
                    "materials": [
                        {
                            "title": "Binary Trees & Traversals Full Guide",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=fAAZixBzIAI",
                            "description": "Comprehensive tutorial covering recursive depth-first traversals and iterative BFS"
                        },
                        {
                            "title": "Visualgo.net - Binary Tree Visualizer",
                            "type": "website",
                            "url": "https://visualgo.net/en/bst",
                            "description": "Interactive website visualization of binary tree insertion, search, and traversals"
                        }
                    ]
                },
                {
                    "name": "Binary Search Trees (BST)",
                    "description": "BST invariants, lookup, insertion, deletion cases (leaf, single child, two children), balancing intro",
                    "difficulty": "Advanced",
                    "display_order": 9,
                    "materials": [
                        {
                            "title": "Binary Search Tree Operations Visualized",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=pYT9F8_LFTM",
                            "description": "Step-by-step animations of BST search, min/max finding, and two-child deletion successor swapping"
                        },
                        {
                            "title": "GeeksforGeeks - Binary Search Tree Tutorial",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/binary-search-tree-data-structure/",
                            "description": "Comprehensive documentation on BST operations, inorder predecessor/successor, and AVL balancing"
                        }
                    ]
                },
                {
                    "name": "Graphs and Graph Traversals",
                    "description": "Adjacency matrix, adjacency list, BFS, DFS, cycle detection, topological sorting, and shortest path basics",
                    "difficulty": "Advanced",
                    "display_order": 10,
                    "materials": [
                        {
                            "title": "Graph Algorithms for Technical Interviews",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=tWVWeAqZ0WU",
                            "description": "Comprehensive walkthrough of BFS, DFS, visited sets, and connected components"
                        },
                        {
                            "title": "Khan Academy - Algorithms: Graph Representation",
                            "type": "website",
                            "url": "https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation",
                            "description": "In-depth interactive course explaining directed, undirected, and weighted graph representations"
                        }
                    ]
                }
            ]
        },
        {
            "name": "Database Systems",
            "code": "CS-DBMS-301",
            "description": "Relational algebra, SQL querying, indexing, transactions, and normalization",
            "topics": [
                {
                    "name": "Relational Model and Schemas",
                    "description": "DBMS architecture, schemas, tuples, attributes, tables, relations, and domain constraints",
                    "difficulty": "Beginner",
                    "display_order": 1,
                    "materials": [
                        {
                            "title": "Relational Database Concepts Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=NvrpuBAMddw",
                            "description": "Intuitive breakdown of relational databases, tables, rows, columns, and primary keys"
                        },
                        {
                            "title": "GeeksforGeeks - Relational Model in DBMS",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/relational-model-in-dbms/",
                            "description": "Comprehensive guide to relations, tuples, schemas, relational algebra, and domain constraints"
                        }
                    ]
                },
                {
                    "name": "Basic SQL Queries",
                    "description": "Projection, selection, filtering with operators (AND, OR, LIKE, IN), sorting records with ORDER BY",
                    "difficulty": "Beginner",
                    "display_order": 2,
                    "materials": [
                        {
                            "title": "SQL Tutorial - Full Database Course for Beginners",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
                            "description": "FreeCodeCamp YouTube comprehensive walkthrough of SQL queries and relational design"
                        },
                        {
                            "title": "W3Schools SQL Tutorial & Live Editor",
                            "type": "website",
                            "url": "https://www.w3schools.com/sql/",
                            "description": "Interactive website reference with hands-on query execution for all SQL commands"
                        }
                    ]
                },
                {
                    "name": "Aggregate Functions and GROUP BY",
                    "description": "COUNT, SUM, AVG, MIN, MAX, GROUP BY clause, HAVING filter vs WHERE clause",
                    "difficulty": "Beginner",
                    "display_order": 3,
                    "materials": [
                        {
                            "title": "SQL Aggregate Functions and GROUP BY",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=W_xZJp_C9XQ",
                            "description": "Detailed video tutorial on summarization, grouping rows, and filtering groups with HAVING"
                        },
                        {
                            "title": "PostgreSQL Tutorial - Aggregate Functions & GROUP BY",
                            "type": "website",
                            "url": "https://www.postgresqltutorial.com/postgresql-aggregate-functions/",
                            "description": "Clear technical examples demonstrating aggregate computations across grouped columns"
                        }
                    ]
                },
                {
                    "name": "SQL Joins and Relationships",
                    "description": "INNER JOIN, LEFT OUTER JOIN, RIGHT JOIN, FULL OUTER JOIN, CROSS JOIN, natural joins",
                    "difficulty": "Intermediate",
                    "display_order": 4,
                    "materials": [
                        {
                            "title": "SQL Joins Visualized & Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=9yeOJ0ZMUYw",
                            "description": "Venn diagrams and practical query animations of INNER, LEFT, RIGHT, and FULL joins"
                        },
                        {
                            "title": "W3Schools SQL Joins Guide",
                            "type": "website",
                            "url": "https://www.w3schools.com/sql/sql_join.asp",
                            "description": "Interactive tutorials with runnable examples for all relational join types"
                        }
                    ]
                },
                {
                    "name": "Subqueries and Nested Queries",
                    "description": "Scalar subqueries, correlated subqueries, EXISTS, IN, ANY, ALL, and Common Table Expressions (CTEs)",
                    "difficulty": "Intermediate",
                    "display_order": 5,
                    "materials": [
                        {
                            "title": "Subqueries in SQL - In-Depth Tutorial",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=oE_v-s_i3L8",
                            "description": "Comprehensive tutorial on writing scalar, multi-row, and correlated subqueries"
                        },
                        {
                            "title": "GeeksforGeeks - SQL Subquery Reference",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/sql-subquery/",
                            "description": "Complete breakdown of nested query execution order, EXISTS operator, and CTEs"
                        }
                    ]
                },
                {
                    "name": "Database Integrity Constraints",
                    "description": "PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK constraints, cascade update and delete rules",
                    "difficulty": "Intermediate",
                    "display_order": 6,
                    "materials": [
                        {
                            "title": "Database Constraints in SQL",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=uK1l0dF3mFE",
                            "description": "Visual explanation of referential integrity, primary keys, and foreign key cascade rules"
                        },
                        {
                            "title": "W3Schools - SQL Constraints Tutorial",
                            "type": "website",
                            "url": "https://www.w3schools.com/sql/sql_constraints.asp",
                            "description": "Reference documentation on creating, altering, and enforcing table constraints"
                        }
                    ]
                },
                {
                    "name": "Database Normalization (1NF, 2NF, 3NF)",
                    "description": "Anomalies (insertion, deletion, update), functional dependencies, 1NF, 2NF, 3NF, BCNF",
                    "difficulty": "Intermediate",
                    "display_order": 7,
                    "materials": [
                        {
                            "title": "Database Normalization - 1NF, 2NF, 3NF Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=UrYLYV7WSHM",
                            "description": "Step-by-step breakdown of functional dependencies, eliminating redundancy and anomalies"
                        },
                        {
                            "title": "GeeksforGeeks - Normalization in DBMS",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/normalization-in-dbms/",
                            "description": "Detailed examples converting unnormalized tables into 1NF, 2NF, 3NF, and BCNF"
                        }
                    ]
                },
                {
                    "name": "Transactions and ACID Properties",
                    "description": "Atomicity, Consistency, Isolation, Durability, COMMIT, ROLLBACK, savepoints, transaction states",
                    "difficulty": "Advanced",
                    "display_order": 8,
                    "materials": [
                        {
                            "title": "ACID Transactions in Databases Explained",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=pomxJOFLeNk",
                            "description": "Clear conceptual animation explaining transaction boundaries and crash-recovery durability"
                        },
                        {
                            "title": "GeeksforGeeks - ACID Properties in DBMS",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/acid-properties-in-dbms/",
                            "description": "Comprehensive guide to transaction states, log-based recovery, and consistency enforcement"
                        }
                    ]
                },
                {
                    "name": "Database Indexing and B-Trees",
                    "description": "Clustered vs non-clustered indexes, B-Tree and B+ Tree structures, index scans vs table scans",
                    "difficulty": "Advanced",
                    "display_order": 9,
                    "materials": [
                        {
                            "title": "How Database Indexes Work Under the Hood",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=clvir_ptnw8",
                            "description": "Animated walkthrough of B-Tree indexing, leaf nodes, binary search speedup, and index cost"
                        },
                        {
                            "title": "Use The Index, Luke - SQL Indexing Guide",
                            "type": "website",
                            "url": "https://use-the-index-luke.com/",
                            "description": "Gold standard developer guide for database index architecture and query optimization"
                        }
                    ]
                },
                {
                    "name": "Concurrency Control and Locking",
                    "description": "Dirty reads, non-repeatable reads, phantom reads, isolation levels, two-phase locking (2PL), deadlocks",
                    "difficulty": "Advanced",
                    "display_order": 10,
                    "materials": [
                        {
                            "title": "Concurrency Control and Database Locks",
                            "type": "youtube",
                            "url": "https://www.youtube.com/watch?v=yYl3_bS_YvM",
                            "description": "Explaining shared/exclusive locks, 2PL protocol, isolation levels, and deadlock detection"
                        },
                        {
                            "title": "GeeksforGeeks - Concurrency Control Protocols",
                            "type": "website",
                            "url": "https://www.geeksforgeeks.org/concurrency-control-protocol/",
                            "description": "In-depth guide to serializability, read committed, repeatable read, and snapshot isolation"
                        }
                    ]
                }
            ]
        }
    ]

    with get_connection() as conn:
        cursor = conn.cursor()

        # Seed default student if empty
        cursor.execute("SELECT COUNT(*) FROM student")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO student (name, email) VALUES (?, ?)",
                ("Student Learner", "student@personalizedlearning.edu")
            )

        for subj in subjects_data:
            cursor.execute(
                """
                INSERT INTO subject (name, code, description)
                VALUES (?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    code=excluded.code,
                    description=excluded.description
                """,
                (subj["name"], subj["code"], subj["description"])
            )
            cursor.execute("SELECT subject_id FROM subject WHERE name = ?", (subj["name"],))
            subject_id = cursor.fetchone()[0]

            for top in subj["topics"]:
                cursor.execute(
                    """
                    INSERT INTO topic (subject_id, name, description, difficulty, display_order)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(subject_id, name) DO UPDATE SET
                        description=excluded.description,
                        difficulty=excluded.difficulty,
                        display_order=excluded.display_order
                    """,
                    (subject_id, top["name"], top["description"], top["difficulty"], top["display_order"])
                )
                cursor.execute(
                    "SELECT topic_id FROM topic WHERE subject_id = ? AND name = ?",
                    (subject_id, top["name"])
                )
                topic_id = cursor.fetchone()[0]

                # Seed Quiz for the topic
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO quiz (topic_id, title, description, difficulty_marks)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        topic_id,
                        f"{top['name']} Knowledge Assessment",
                        f"Adaptive spaced repetition assessment evaluating conceptual understanding in {top['name']}",
                        30
                    )
                )

                # Seed Study Materials (Strictly YouTube links and Websites only)
                for mat in top.get("materials", []):
                    mat_type = mat["type"].lower()
                    if mat_type not in ("youtube", "website"):
                        continue

                    cursor.execute(
                        """
                        SELECT material_id FROM study_material
                        WHERE topic_id = ? AND url = ?
                        """,
                        (topic_id, mat["url"])
                    )
                    existing = cursor.fetchone()
                    if not existing:
                        cursor.execute(
                            """
                            INSERT INTO study_material (topic_id, title, type, url, description)
                            VALUES (?, ?, ?, ?, ?)
                            """,
                            (topic_id, mat["title"], mat_type, mat["url"], mat["description"])
                        )

        conn.commit()


# ============================================================================
# Database Helper / Query Functions
# ============================================================================

def get_all_subjects() -> List[Dict[str, Any]]:
    """Return all subjects with their nested topics and study material counts in hierarchical order."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subject ORDER BY name ASC")
        subjects = [dict(row) for row in cursor.fetchall()]

        for subj in subjects:
            cursor.execute(
                """
                SELECT t.*,
                       COUNT(DISTINCT m.material_id) as materials_count,
                       COUNT(DISTINCT q.quiz_id) as quizzes_count
                FROM topic t
                LEFT JOIN study_material m ON t.topic_id = m.topic_id
                LEFT JOIN quiz q ON t.topic_id = q.topic_id
                WHERE t.subject_id = ?
                GROUP BY t.topic_id
                ORDER BY t.display_order ASC, t.name ASC
                """,
                (subj["subject_id"],)
            )
            subj["topics"] = [dict(row) for row in cursor.fetchall()]

        return subjects


def get_subject_hierarchy(subject_name: str) -> List[Dict[str, Any]]:
    """Return all topics in a subject ordered hierarchically from easy to hard."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT t.topic_id, t.name, t.description, t.difficulty, t.display_order
            FROM topic t
            JOIN subject s ON t.subject_id = s.subject_id
            WHERE LOWER(s.name) = LOWER(?)
            ORDER BY t.display_order ASC
            """,
            (subject_name,)
        )
        return [dict(row) for row in cursor.fetchall()]


def get_next_topic_in_hierarchy(subject_name: str, current_topic_name: str) -> Optional[Dict[str, Any]]:
    """Find the next topic in the subject's hierarchical learning order."""
    topics = get_subject_hierarchy(subject_name)
    if not topics:
        return None

    current_idx = -1
    for idx, t in enumerate(topics):
        if t["name"].lower() == current_topic_name.lower() or current_topic_name.lower() in t["name"].lower():
            current_idx = idx
            break

    if current_idx != -1 and current_idx + 1 < len(topics):
        return topics[current_idx + 1]

    return None


def get_study_materials(subject_name: str, topic_name: str, material_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Get all study materials for a specific subject and topic.
    Can be filtered by type ('youtube' or 'website').
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
            SELECT m.material_id, m.title, m.type, m.url, m.description,
                   t.name as topic_name, s.name as subject_name
            FROM study_material m
            JOIN topic t ON m.topic_id = t.topic_id
            JOIN subject s ON t.subject_id = s.subject_id
            WHERE LOWER(s.name) = LOWER(?) AND (LOWER(t.name) = LOWER(?) OR LOWER(t.name) LIKE '%' || LOWER(?) || '%')
        """
        params = [subject_name, topic_name, topic_name]

        if material_type:
            query += " AND m.type = ?"
            params.append(material_type.lower())

        query += " ORDER BY m.type DESC, m.title ASC"
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]


def record_learner_progress(student_id: int, subject_name: str, topic_name: str, score: float) -> Dict[str, Any]:
    """
    Record or update a learner's topic progress and schedule next spaced revision.
    """
    with get_connection() as conn:
        cursor = conn.cursor()

        # Ensure student exists
        cursor.execute("SELECT student_id FROM student WHERE student_id = ?", (student_id,))
        if not cursor.fetchone():
            cursor.execute(
                "INSERT OR IGNORE INTO student (student_id, name, email) VALUES (?, ?, ?)",
                (student_id, f"Student {student_id}", f"student{student_id}@learning.edu")
            )

        # Find topic_id
        cursor.execute(
            """
            SELECT t.topic_id, s.subject_id
            FROM topic t
            JOIN subject s ON t.subject_id = s.subject_id
            WHERE LOWER(s.name) = LOWER(?) AND (LOWER(t.name) = LOWER(?) OR LOWER(t.name) LIKE '%' || LOWER(?) || '%')
            ORDER BY t.display_order ASC LIMIT 1
            """,
            (subject_name, topic_name, topic_name)
        )
        row = cursor.fetchone()
        if not row:
            cursor.execute("INSERT OR IGNORE INTO subject (name, code) VALUES (?, ?)", (subject_name, f"SUB-{subject_name[:4].upper()}"))
            cursor.execute("SELECT subject_id FROM subject WHERE name = ?", (subject_name,))
            s_id = cursor.fetchone()[0]
            cursor.execute("INSERT OR IGNORE INTO topic (subject_id, name) VALUES (?, ?)", (s_id, topic_name))
            cursor.execute("SELECT topic_id FROM topic WHERE subject_id = ? AND name = ?", (s_id, topic_name))
            topic_id = cursor.fetchone()[0]
        else:
            topic_id = row["topic_id"]

        # Fetch previous revision record for this student and topic
        cursor.execute(
            """
            SELECT current_interval_days
            FROM revision_record
            WHERE student_id = ? AND topic_id = ?
            ORDER BY revision_id DESC LIMIT 1
            """,
            (student_id, topic_id)
        )
        prev_row = cursor.fetchone()
        current_interval = prev_row[0] if prev_row else 0

        # Calculate next review using 1 -> 3 -> 7 -> 30 ladder with regression on fail
        from AI.SpacedRepetition.spaced_repetition_logic import calculate_next_review
        spaced_result = calculate_next_review(score=score, current_interval=current_interval)
        interval_days = spaced_result["next_review_in_days"]

        # Determine status
        if spaced_result["is_mastered"]:
            status = "Mastered"
            mastered_on = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        elif spaced_result["passed"]:
            status = "Cleared"
            mastered_on = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        else:
            status = "Needs Review"
            mastered_on = None

        # Upsert progress
        cursor.execute(
            """
            INSERT INTO learner_topic_progress (student_id, topic_id, score, status, last_reviewed, mastered_on)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, ?)
            ON CONFLICT(student_id, topic_id) DO UPDATE SET
                score = excluded.score,
                status = excluded.status,
                last_reviewed = CURRENT_TIMESTAMP,
                mastered_on = COALESCE(excluded.mastered_on, learner_topic_progress.mastered_on)
            RETURNING progress_id
            """,
            (student_id, topic_id, score, status, mastered_on)
        )
        res = cursor.fetchone()
        progress_id = res[0] if res else 1

        # Fetch quiz_id
        cursor.execute("SELECT quiz_id FROM quiz WHERE topic_id = ?", (topic_id,))
        q_row = cursor.fetchone()
        quiz_id = q_row[0] if q_row else None

        next_review = (datetime.utcnow() + timedelta(days=interval_days)).strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            """
            INSERT INTO revision_record (student_id, topic_id, quiz_id, progress_id, score, current_interval_days, last_reviewed, next_review)
            VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, ?)
            """,
            (student_id, topic_id, quiz_id, progress_id, score, interval_days, next_review)
        )

        conn.commit()

        # Find next topic in hierarchy if cleared
        next_topic = None
        if spaced_result["passed"]:
            next_topic = get_next_topic_in_hierarchy(subject_name, topic_name)

        return {
            "progress_id": progress_id,
            "student_id": student_id,
            "subject": subject_name,
            "topic": topic_name,
            "score": score,
            "status": status,
            "topic_cleared": spaced_result["passed"],
            "next_topic": next_topic,
            "current_interval_days": interval_days,
            "next_review": next_review,
            "spaced_repetition": spaced_result
        }


def get_student_progress_summary(student_id: int = 1) -> Dict[str, Any]:
    """Retrieve latest active spaced repetition schedule and progress for a student."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT p.*, t.name as topic_name, t.display_order, t.difficulty, s.name as subject_name
            FROM learner_topic_progress p
            JOIN topic t ON p.topic_id = t.topic_id
            JOIN subject s ON t.subject_id = s.subject_id
            WHERE p.student_id = ?
            ORDER BY s.name ASC, t.display_order ASC
            """,
            (student_id,)
        )
        progress_list = [dict(row) for row in cursor.fetchall()]

        # Query only the latest active revision record per topic
        cursor.execute(
            """
            SELECT r.*, t.name as topic_name, s.name as subject_name, p.status as topic_status
            FROM revision_record r
            JOIN topic t ON r.topic_id = t.topic_id
            JOIN subject s ON t.subject_id = s.subject_id
            LEFT JOIN learner_topic_progress p ON p.topic_id = t.topic_id AND p.student_id = r.student_id
            WHERE r.revision_id IN (
                SELECT MAX(revision_id)
                FROM revision_record
                WHERE student_id = ?
                GROUP BY topic_id
            )
            ORDER BY r.next_review ASC
            """,
            (student_id,)
        )
        revisions = [dict(row) for row in cursor.fetchall()]

        now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        for rev in revisions:
            target = rev.get("next_review")
            rev["is_due"] = target <= now_str if target else False
            interval = rev.get("current_interval_days", 1)
            if interval == 1:
                rev["interval_label"] = "Tomorrow (1 Day)"
                rev["ladder_step"] = 1
            elif interval == 3:
                rev["interval_label"] = "3 Days Later"
                rev["ladder_step"] = 2
            elif interval == 7:
                rev["interval_label"] = "7 Days Later"
                rev["ladder_step"] = 3
            else:
                rev["interval_label"] = "30 Days Later"
                rev["ladder_step"] = 4

        return {
            "student_id": student_id,
            "progress": progress_list,
            "upcoming_revisions": revisions
        }


# Auto-initialize database tables and seed data upon module load
init_db()
