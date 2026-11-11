// Hierarchical curriculum and subjects data

export const SUBJECTS = [
  {
    id: 'OOPS',
    name: 'OOPS',
    code: 'CS-OOP-201',
    description: 'Object-Oriented Programming Principles, Architecture, and Design Patterns',
  },
  {
    id: 'Data Structures',
    name: 'Data Structures',
    code: 'CS-DSA-102',
    description: 'Fundamental data structures, memory layouts, and algorithmic complexity',
  },
  {
    id: 'Database Systems',
    name: 'Database Systems',
    code: 'CS-DBMS-301',
    description: 'Relational model, SQL querying, normalization, transactions, and indexing',
  },
];

export const TOPICS_BY_SUBJECT = {
  'OOPS': [
    'Classes and Objects',
    'Constructors and Destructors',
    'Encapsulation and Data Hiding',
    'Inheritance Basics',
    'Multilevel and Multiple Inheritance',
    'Method Overloading',
    'Method Overriding and Dynamic Dispatch',
    'Abstraction and Interfaces',
    'Composition and Aggregation',
    'SOLID Principles and Design Patterns',
  ],
  'Data Structures': [
    'Arrays and Memory Layouts',
    'Strings and String Manipulation',
    'Singly Linked Lists',
    'Doubly and Circular Linked Lists',
    'Stacks (LIFO Operations)',
    'Queues and Deques (FIFO)',
    'Hash Tables and Hashing',
    'Binary Trees and Traversals',
    'Binary Search Trees (BST)',
    'Graphs and Graph Traversals',
  ],
  'Database Systems': [
    'Relational Model and Schemas',
    'Basic SQL Queries',
    'Aggregate Functions and GROUP BY',
    'SQL Joins and Relationships',
    'Subqueries and Nested Queries',
    'Database Integrity Constraints',
    'Database Normalization (1NF, 2NF, 3NF)',
    'Transactions and ACID Properties',
    'Database Indexing and B-Trees',
    'Concurrency Control and Locking',
  ],
};

export const MOCK_PROGRESS = {
  overall: 45,
  completedTopics: ['Classes and Objects', 'Arrays and Memory Layouts', 'Relational Model and Schemas'],
  remainingTopics: ['Inheritance Basics', 'Binary Trees and Traversals', 'Database Normalization (1NF, 2NF, 3NF)'],
  assessmentScores: [
    { topic: 'Classes and Objects', score: 85 },
    { topic: 'Arrays and Memory Layouts', score: 90 },
    { topic: 'Relational Model and Schemas', score: 75 },
  ],
};
