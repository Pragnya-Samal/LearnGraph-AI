"""OOPS Question Bank - 10 Topics, 30 Questions Each (10 Easy, 10 Medium, 10 Hard)"""

oops_questions = {'Abstraction and Interfaces': [{'correct_answer': 'Hiding complex background implementation details and exposing only '
                                                   'essential features to the user',
                                 'difficulty': 'Easy',
                                 'explanation': 'Abstraction focuses on what an object does rather than how it '
                                                'achieves it internally.',
                                 'options': ['Hiding complex background implementation details and exposing only '
                                             'essential features to the user',
                                             'Creating multiple copies of an object in RAM',
                                             'Making all methods static',
                                             'Compiling code without optimization'],
                                 'question': 'What is abstraction in Object-Oriented Programming?'},
                                {'correct_answer': 'No, abstract classes cannot be directly instantiated',
                                 'difficulty': 'Easy',
                                 'explanation': 'Abstract classes serve as incomplete base templates and cannot be '
                                                'instantiated directly.',
                                 'options': ['No, abstract classes cannot be directly instantiated',
                                             'Yes, anytime like normal classes',
                                             'Yes, if it has no variables',
                                             'Only inside static methods'],
                                 'question': "Can an abstract class be directly instantiated with the 'new' operator "
                                             'in Java or C++?'},
                                {'correct_answer': 'A method declared without a body/implementation, designed to be '
                                                   'implemented by subclasses',
                                 'difficulty': 'Easy',
                                 'explanation': 'Abstract methods define a signature contract that derived concrete '
                                                'classes must fulfill.',
                                 'options': ['A method declared without a body/implementation, designed to be '
                                             'implemented by subclasses',
                                             'A method that runs on an abstract thread',
                                             'A method that returns null always',
                                             'A private method with no arguments'],
                                 'question': 'What is an abstract method?'},
                                {'correct_answer': 'A completely abstract reference type that specifies a contract of '
                                                   'method signatures that implementing classes must satisfy',
                                 'difficulty': 'Easy',
                                 'explanation': 'Interfaces specify behavioral contracts without storing instance '
                                                'state.',
                                 'options': ['A completely abstract reference type that specifies a contract of method '
                                             'signatures that implementing classes must satisfy',
                                             'A graphical user interface window',
                                             'A network socket connector',
                                             'A database connection pool'],
                                 'question': 'What is an interface in Java?'},
                                {'correct_answer': 'implements',
                                 'difficulty': 'Easy',
                                 'explanation': "In Java, a class uses the 'implements' keyword to fulfill an "
                                                'interface contract.',
                                 'options': ['implements', 'extends', 'inherits', 'uses'],
                                 'question': 'Which keyword is used by a class to implement an interface in Java?'},
                                {'correct_answer': 'A virtual function equated to zero (virtual void func() = 0;) that '
                                                   'makes the class abstract',
                                 'difficulty': 'Easy',
                                 'explanation': "In C++, '= 0' declares a pure virtual function, rendering the "
                                                'containing class abstract.',
                                 'options': ['A virtual function equated to zero (virtual void func() = 0;) that makes '
                                             'the class abstract',
                                             'A function with no variables',
                                             'A function that runs in pure assembly',
                                             'A function that cannot be overridden'],
                                 'question': 'What is a pure virtual function in C++?'},
                                {'correct_answer': 'Yes, an abstract class can contain both abstract and concrete '
                                                   'methods',
                                 'difficulty': 'Easy',
                                 'explanation': 'Abstract classes can provide shared common concrete implementations '
                                                'alongside abstract hooks.',
                                 'options': ['Yes, an abstract class can contain both abstract and concrete methods',
                                             'No, all methods in an abstract class must be abstract',
                                             'Only if the class has no fields',
                                             'Only static methods can be concrete'],
                                 'question': 'Can an abstract class have concrete (implemented) methods in Java?'},
                                {'correct_answer': 'Yes, abstract classes have constructors invoked during subclass '
                                                   'instantiation',
                                 'difficulty': 'Easy',
                                 'explanation': 'Abstract class constructors initialize base fields when derived '
                                                'objects are instantiated.',
                                 'options': ['Yes, abstract classes have constructors invoked during subclass '
                                             'instantiation',
                                             'No, abstract classes cannot have constructors',
                                             'Only default private constructors are allowed',
                                             'Only if marked static'],
                                 'question': 'Can an abstract class have a constructor in Java or C++?'},
                                {'correct_answer': 'Yes, a class can implement multiple interfaces separated by commas',
                                 'difficulty': 'Easy',
                                 'explanation': 'Java supports multiple interface inheritance: class C implements '
                                                'InterfaceA, InterfaceB.',
                                 'options': ['Yes, a class can implement multiple interfaces separated by commas',
                                             'No, only one interface per class is permitted',
                                             'Only if all interfaces have identical method names',
                                             'Only in Java EE'],
                                 'question': 'Can a class implement more than one interface in Java?'},
                                {'correct_answer': 'public abstract',
                                 'difficulty': 'Easy',
                                 'explanation': 'By default, interface methods in Java are public and abstract.',
                                 'options': ['public abstract', 'private static', 'protected final', 'synchronized'],
                                 'question': 'What modifier is implicitly applied to all methods in a traditional Java '
                                             'interface (pre-Java 8)?'},
                                {'correct_answer': 'A method with a default implementation in the interface using the '
                                                   "'default' keyword",
                                 'difficulty': 'Medium',
                                 'explanation': 'Default methods enable evolving interfaces with new capabilities '
                                                'without breaking existing implementers.',
                                 'options': ['A method with a default implementation in the interface using the '
                                             "'default' keyword",
                                             'A method that can only be called by the JVM',
                                             'A package-private method',
                                             'A method with no parameters'],
                                 'question': 'What is a default method in a Java interface (introduced in Java 8)?'},
                                {'correct_answer': 'Abstract classes can have instance state and constructors; '
                                                   'interfaces cannot have instance state (only constants/behavior)',
                                 'difficulty': 'Medium',
                                 'explanation': 'Abstract classes model identity and state hierarchies, whereas '
                                                'interfaces define pure behavioral contracts.',
                                 'options': ['Abstract classes can have instance state and constructors; interfaces '
                                             'cannot have instance state (only constants/behavior)',
                                             'Interfaces can be instantiated directly; abstract classes cannot',
                                             'Abstract classes cannot have methods',
                                             'Interfaces are stored on the hard drive'],
                                 'question': 'What is the key difference between an abstract class and an interface in '
                                             'Java?'},
                                {'correct_answer': 'An interface containing exactly one abstract method, suitable for '
                                                   'lambda expressions',
                                 'difficulty': 'Medium',
                                 'explanation': 'Functional interfaces (annotated with @FunctionalInterface) have a '
                                                'Single Abstract Method (SAM).',
                                 'options': ['An interface containing exactly one abstract method, suitable for lambda '
                                             'expressions',
                                             'An interface containing only mathematical functions',
                                             'An interface with no methods at all',
                                             'An interface that returns boolean'],
                                 'question': 'What is a functional interface in Java?'},
                                {'correct_answer': 'An interface with no methods or constants, used to indicate '
                                                   'metadata to the compiler/JVM (e.g., Serializable)',
                                 'difficulty': 'Medium',
                                 'explanation': 'Marker interfaces like Serializable or Cloneable tag classes for '
                                                'special runtime handling without adding methods.',
                                 'options': ['An interface with no methods or constants, used to indicate metadata to '
                                             'the compiler/JVM (e.g., Serializable)',
                                             'An interface that marks errors in code',
                                             'An interface used exclusively for graphic design',
                                             'A deprecated interface'],
                                 'question': 'What is a marker interface (tagging interface) in Java?'},
                                {'correct_answer': 'Yes, since Java 8, interfaces can define static utility methods '
                                                   'with implementation bodies',
                                 'difficulty': 'Medium',
                                 'explanation': 'Java 8 permitted static helper methods in interfaces, co-locating '
                                                'utility algorithms with interface types.',
                                 'options': ['Yes, since Java 8, interfaces can define static utility methods with '
                                             'implementation bodies',
                                             'No, static methods in interfaces are forbidden',
                                             'Only if marked native',
                                             'Only if the interface is private'],
                                 'question': 'Can an interface contain static methods in modern Java?'},
                                {'correct_answer': 'By defining a class with only pure virtual functions (= 0) and a '
                                                   'virtual destructor',
                                 'difficulty': 'Medium',
                                 'explanation': 'C++ has no interface keyword; pure abstract classes with only pure '
                                                'virtual functions serve as interfaces.',
                                 'options': ['By defining a class with only pure virtual functions (= 0) and a virtual '
                                             'destructor',
                                             "By using the 'interface' keyword",
                                             'By inheriting from std::interface',
                                             'By defining an empty enum'],
                                 'question': 'In C++, how is a pure interface created?'},
                                {'correct_answer': 'abc (e.g., abc.ABC and @abc.abstractmethod)',
                                 'difficulty': 'Medium',
                                 'explanation': "Python's 'abc' module provides infrastructure for defining and "
                                                'enforcing Abstract Base Classes.',
                                 'options': ['abc (e.g., abc.ABC and @abc.abstractmethod)',
                                             'abstract',
                                             'oop.interfaces',
                                             'types.abstract'],
                                 'question': 'In Python, which module from the standard library is used to define '
                                             'Abstract Base Classes?'},
                                {'correct_answer': 'The derived class itself remains abstract and cannot be '
                                                   'instantiated',
                                 'difficulty': 'Medium',
                                 'explanation': 'Subclasses that do not implement all inherited pure virtual functions '
                                                'remain abstract.',
                                 'options': ['The derived class itself remains abstract and cannot be instantiated',
                                             'A linker error occurs at build time',
                                             'The missing method is replaced with an empty function',
                                             'The program crashes upon launch'],
                                 'question': 'What happens in C++ if a derived class fails to override even one pure '
                                             'virtual function from its base class?'},
                                {'correct_answer': 'Because interfaces represent pure stateless contracts and '
                                                   'constants, not per-instance mutable state',
                                 'difficulty': 'Medium',
                                 'explanation': 'Interfaces cannot hold mutable object instance state; fields are '
                                                'compile-time constants.',
                                 'options': ['Because interfaces represent pure stateless contracts and constants, not '
                                             'per-instance mutable state',
                                             'Because interfaces cannot store strings',
                                             'To prevent inheritance from working',
                                             'Because final fields compile faster'],
                                 'question': "Why are fields in Java interfaces implicitly 'public static final'?"},
                                {'correct_answer': 'Clients should not be forced to depend on interfaces they do not '
                                                   'use (prefer small, role-specific interfaces)',
                                 'difficulty': 'Medium',
                                 'explanation': 'ISP advocates breaking fat interfaces into cohesive, focused '
                                                'interfaces tailored to specific clients.',
                                 'options': ['Clients should not be forced to depend on interfaces they do not use '
                                             '(prefer small, role-specific interfaces)',
                                             'Every interface must have at least 10 methods',
                                             'All interfaces should be combined into one mega-interface',
                                             'Interfaces must only be implemented by single classes'],
                                 'question': 'What is the Interface Segregation Principle (ISP) in relation to '
                                             'interface design?'},
                                {'correct_answer': 'It allows sharing common helper code between default methods '
                                                   'without exposing it to implementing classes or clients',
                                 'difficulty': 'Hard',
                                 'explanation': 'Private methods in interfaces allow refactoring repetitive default '
                                                'method logic safely.',
                                 'options': ['It allows sharing common helper code between default methods without '
                                             'exposing it to implementing classes or clients',
                                             'It makes the interface invisible to other packages',
                                             'It encrypts interface bytecode',
                                             'It prevents classes from implementing the interface'],
                                 'question': "How does Java 9's private interface methods feature support "
                                             'encapsulation within interfaces?'},
                                {'correct_answer': "A table attached to a class's metadata that maps interface method "
                                                   'specifications to concrete vtable offsets',
                                 'difficulty': 'Hard',
                                 'explanation': 'Because classes implement arbitrary interfaces in varying order, '
                                                'itables map interface method indices to class vtable slots.',
                                 'options': ["A table attached to a class's metadata that maps interface method "
                                             'specifications to concrete vtable offsets',
                                             'A database table storing interface names',
                                             'An array of JVM thread IDs',
                                             'A hash table of string symbols on the stack'],
                                 'question': 'What is the ITABLE (Interface Table) structure in JVM implementations '
                                             'like HotSpot?'},
                                {'correct_answer': 'Caching the last resolved interface offset at the invokeinterface '
                                                   'site, reducing dispatch to a direct check and jump',
                                 'difficulty': 'Hard',
                                 'explanation': 'Itable caching avoids linear searching of itables by remembering the '
                                                'most frequent target class and offset.',
                                 'options': ['Caching the last resolved interface offset at the invokeinterface site, '
                                             'reducing dispatch to a direct check and jump',
                                             'Translating interfaces into C macros',
                                             'Compiling interfaces into static functions',
                                             'Replacing itables with registers'],
                                 'question': 'What is the performance optimization of Quick Interface Calls (itable '
                                             'stub caching) in the HotSpot VM?'},
                                {'correct_answer': 'To guarantee that deleting an object through an interface pointer '
                                                   'invokes the derived class destructor properly',
                                 'difficulty': 'Hard',
                                 'explanation': 'Without a virtual destructor, deleting via Base* invokes only the '
                                                'base destructor, leaking derived resources.',
                                 'options': ['To guarantee that deleting an object through an interface pointer '
                                             'invokes the derived class destructor properly',
                                             'Because abstract classes cannot compile without it',
                                             'Because pure virtual destructors are mandatory',
                                             'To prevent multiple inheritance'],
                                 'question': 'In C++, why must an abstract class defining an interface ALWAYS have a '
                                             'virtual destructor?'},
                                {'correct_answer': 'Yes, pure virtual destructors MUST have an implementation body '
                                                   'because base destructors are always called during unwinding',
                                 'difficulty': 'Hard',
                                 'explanation': 'Even when pure virtual, a destructor body is required because derived '
                                                'destructors implicitly call base destructors.',
                                 'options': ['Yes, pure virtual destructors MUST have an implementation body because '
                                             'base destructors are always called during unwinding',
                                             'No, pure virtual functions can never have bodies under any circumstances',
                                             'Only if marked inline',
                                             'Only in template structs'],
                                 'question': 'Can a pure virtual destructor have an implementation in C++?'},
                                {'correct_answer': 'A base class defines the invariant skeleton of an algorithm in a '
                                                   'concrete method, deferring specific steps to abstract methods',
                                 'difficulty': 'Hard',
                                 'explanation': 'Template Method enforces overarching algorithm workflow while '
                                                'allowing subclasses to customize individual steps.',
                                 'options': ['A base class defines the invariant skeleton of an algorithm in a '
                                             'concrete method, deferring specific steps to abstract methods',
                                             'A pattern that converts classes into C++ templates',
                                             'A pattern used to generate HTML email templates',
                                             'A pattern that creates objects without constructors'],
                                 'question': 'What is the Template Method design pattern and how does it leverage '
                                             'abstract classes?'},
                                {'correct_answer': 'Structural typing matches types by having compatible member '
                                                   "signatures; nominal typing requires explicit 'implements' "
                                                   'declarations',
                                 'difficulty': 'Hard',
                                 'explanation': 'Structural systems satisfy interfaces implicitly by shape, while '
                                                'nominal systems require explicit declaration.',
                                 'options': ['Structural typing matches types by having compatible member signatures; '
                                             "nominal typing requires explicit 'implements' declarations",
                                             'Structural typing only works with structs; nominal works with classes',
                                             'Structural typing is evaluated at runtime only',
                                             'Nominal typing is untyped at compile-time'],
                                 'question': 'What is structural typing (duck typing) in TypeScript/Go vs nominal '
                                             'typing in Java regarding interfaces?'},
                                {'correct_answer': 'It allows custom class inspection to determine if a class is '
                                                   'considered a subclass of an ABC without explicit inheritance',
                                 'difficulty': 'Hard',
                                 'explanation': '__subclasshook__ enables duck-typed registration where checking '
                                                'isinstance(obj, ABC) inspects method presence.',
                                 'options': ['It allows custom class inspection to determine if a class is considered '
                                             'a subclass of an ABC without explicit inheritance',
                                             'It hooks into the operating system filesystem',
                                             'It creates bytecode patches dynamically',
                                             'It compiles Python to assembly'],
                                 'question': "How does Python's ABCMeta.__subclasshook__ enable virtual subclass "
                                             'registration?'},
                                {'correct_answer': 'A compile-time error occurs: default methods cannot override '
                                                   'methods of java.lang.Object',
                                 'difficulty': 'Hard',
                                 'explanation': "Java rules state that class implementations (like Object's concrete "
                                                'methods) always win over interface default methods.',
                                 'options': ['A compile-time error occurs: default methods cannot override methods of '
                                             'java.lang.Object',
                                             'The Object method is replaced across all classes in the JVM',
                                             "It compiles and overrides Object's implementation",
                                             'A LinkageError is thrown at runtime'],
                                 'question': 'What happens when an interface in Java redeclares a method from '
                                             'java.lang.Object (e.g. boolean equals(Object)) as a default method?'},
                                {'correct_answer': 'It decouples callers from concrete types, enabling swapping '
                                                   'implementations, dependency injection, and easier unit testing',
                                 'difficulty': 'Hard',
                                 'explanation': 'Interface-based architecture isolates consumers from changes in '
                                                'concrete implementation details.',
                                 'options': ['It decouples callers from concrete types, enabling swapping '
                                             'implementations, dependency injection, and easier unit testing',
                                             'It prevents all runtime exceptions from occurring',
                                             'It makes programs execute without using RAM',
                                             'It eliminates the need for unit testing'],
                                 'question': 'Why is programming to an interface rather than an implementation a '
                                             'cornerstone of decoupled design?'}],
 'Classes and Objects': [{'correct_answer': 'A blueprint or template for creating objects',
                          'difficulty': 'Easy',
                          'explanation': 'A class defines variables and methods that represent the state and behavior '
                                         'of an object.',
                          'options': ['A blueprint or template for creating objects',
                                      'An instance of an object stored in heap memory',
                                      'A primitive data type in memory',
                                      'A function that executes automatically'],
                          'question': 'What is a class in Object-Oriented Programming?'},
                         {'correct_answer': 'An instance of a class that holds state and behavior',
                          'difficulty': 'Easy',
                          'explanation': 'An object is a concrete instance created from a class blueprint.',
                          'options': ['An instance of a class that holds state and behavior',
                                      'A global variable accessible everywhere',
                                      'A compiler directive',
                                      'A pointer to code segment'],
                          'question': 'What is an object in OOP?'},
                         {'correct_answer': 'new',
                          'difficulty': 'Easy',
                          'explanation': "The 'new' keyword dynamically allocates memory on the heap for a new object.",
                          'options': ['new', 'create', 'alloc', 'make'],
                          'question': 'Which keyword is commonly used in languages like Java, C++, and C# to '
                                      'instantiate an object?'},
                         {'correct_answer': 'The current values of its attributes or fields',
                          'difficulty': 'Easy',
                          'explanation': "An object's state is defined by the values stored in its instance variables.",
                          'options': ['The current values of its attributes or fields',
                                      'The location of its source file',
                                      'The execution thread ID',
                                      'The return type of its methods'],
                          'question': "What does the 'state' of an object refer to?"},
                         {'correct_answer': 'The actions and methods it can perform',
                          'difficulty': 'Easy',
                          'explanation': 'Behavior represents the operations and methods available on the object.',
                          'options': ['The actions and methods it can perform',
                                      'Its memory address',
                                      'Its visibility modifier',
                                      'The time it was allocated'],
                          'question': "What does the 'behavior' of an object represent?"},
                         {'correct_answer': 'Heap memory',
                          'difficulty': 'Easy',
                          'explanation': 'Objects instantiated dynamically with new are allocated on the heap.',
                          'options': ['Heap memory',
                                      'Stack memory only',
                                      'CPU registers only',
                                      'Read-only text segment'],
                          'question': 'Where are object instances typically allocated in memory during runtime in '
                                      'languages like Java and C#?'},
                         {'correct_answer': 'A variable declared in a class that belongs to a specific object',
                          'difficulty': 'Easy',
                          'explanation': 'Each instance of a class maintains its own distinct copy of instance '
                                         'variables.',
                          'options': ['A variable declared in a class that belongs to a specific object',
                                      'A variable accessible across all classes without instantiation',
                                      'A variable defined inside a loop',
                                      'A constant that cannot change'],
                          'question': 'What is an instance variable?'},
                         {'correct_answer': 'this / self',
                          'difficulty': 'Easy',
                          'explanation': "'this' in Java/C++ or 'self' in Python refers to the current object "
                                         'instance.',
                          'options': ['this / self', 'super', 'base', 'parent'],
                          'question': 'Which keyword refers to the current invoking instance of a class?'},
                         {'correct_answer': 'A class is a blueprint; an object is a concrete instance of that '
                                            'blueprint',
                          'difficulty': 'Easy',
                          'explanation': 'A class is the abstract template, while an object is the tangible instance '
                                         'in memory.',
                          'options': ['A class is a blueprint; an object is a concrete instance of that blueprint',
                                      'A class is stored in RAM; an object is stored on disk',
                                      'A class has values; an object only has types',
                                      'There is no difference between them'],
                          'question': 'What is the fundamental difference between a class and an object?'},
                         {'correct_answer': 'Yes, each object has its own separate state',
                          'difficulty': 'Easy',
                          'explanation': 'Multiple objects can be created from one class, each maintaining independent '
                                         'state.',
                          'options': ['Yes, each object has its own separate state',
                                      'No, only one object per class is permitted',
                                      'Only if the class is declared static',
                                      'Yes, but they must share the exact same attribute values'],
                          'question': 'Can multiple independent objects be instantiated from a single class?'},
                         {'correct_answer': 'An instance method operates on specific object state, whereas a static '
                                            'method belongs to the class itself',
                          'difficulty': 'Medium',
                          'explanation': 'Static methods belong to the class namespace and do not operate on an '
                                         'individual instance.',
                          'options': ['An instance method operates on specific object state, whereas a static method '
                                      'belongs to the class itself',
                                      'An instance method runs faster than a static method',
                                      "A static method can access the 'this' reference directly",
                                      'An instance method cannot return any value'],
                          'question': 'What is the difference between an instance method and a static method?'},
                         {'correct_answer': 'The change is reflected across all instances of the class',
                          'difficulty': 'Medium',
                          'explanation': 'Static variables are shared among all instances of a class.',
                          'options': ['The change is reflected across all instances of the class',
                                      'Only that single object sees the change',
                                      'A compile-time error occurs',
                                      'A new copy of the variable is created on the stack'],
                          'question': 'What happens if you modify a static variable through one object instance?'},
                         {'correct_answer': 'It serves as the initializer/constructor when an object is created',
                          'difficulty': 'Medium',
                          'explanation': "The '__init__' method initializes newly created object instances in Python.",
                          'options': ['It serves as the initializer/constructor when an object is created',
                                      'It destroys the object from memory',
                                      'It compares two objects for equality',
                                      'It converts the object to a string'],
                          'question': "In Python, what is the role of the '__init__' method?"},
                         {'correct_answer': 'An object instantiated without assigning it to a reference variable',
                          'difficulty': 'Medium',
                          'explanation': 'Anonymous objects are used immediately upon creation without being bound to '
                                         'a named variable.',
                          'options': ['An object instantiated without assigning it to a reference variable',
                                      'An object with private methods only',
                                      'An object without a class definition',
                                      'An object stored on the GPU'],
                          'question': 'What is an anonymous object in languages like Java or C++?'},
                         {'correct_answer': 'Its instance fields, memory alignment padding, and object header overhead',
                          'difficulty': 'Medium',
                          'explanation': "An object's footprint includes its fields, alignment padding, and runtime "
                                         'metadata headers.',
                          'options': ['Its instance fields, memory alignment padding, and object header overhead',
                                      'The length of the method names',
                                      'The comments in the class definition',
                                      'The number of lines of code in the class'],
                          'question': 'What determines the memory footprint of an object in memory?'},
                         {'correct_answer': "Static methods do not have an implicit 'this' reference to any specific "
                                            'instance',
                          'difficulty': 'Medium',
                          'explanation': 'Because static methods run at the class level without an object context, '
                                         'there is no instance to read from.',
                          'options': ["Static methods do not have an implicit 'this' reference to any specific "
                                      'instance',
                                      'Static methods are stored in a different file',
                                      'Instance variables are always encrypted',
                                      'Static methods can only return void'],
                          'question': 'Why can static methods not directly access instance variables?'},
                         {'correct_answer': 'A constructor that initializes an object using another object of the same '
                                            'class',
                          'difficulty': 'Medium',
                          'explanation': 'Copy constructors create a new object by copying data members from an '
                                         'existing object.',
                          'options': ['A constructor that initializes an object using another object of the same class',
                                      'A constructor that duplicates a class bytecode',
                                      'A method that creates an exact clone on disk',
                                      'A constructor used exclusively in multi-threading'],
                          'question': 'What is a copy constructor?'},
                         {'correct_answer': 'Shallow copy duplicates reference pointers, while deep copy recursively '
                                            'duplicates referenced objects',
                          'difficulty': 'Medium',
                          'explanation': 'Shallow copy only copies top-level references, causing nested objects to be '
                                         'shared between copies.',
                          'options': ['Shallow copy duplicates reference pointers, while deep copy recursively '
                                      'duplicates referenced objects',
                                      'Shallow copy works on heap; deep copy works on stack',
                                      'Deep copy is always done by the compiler automatically',
                                      'Shallow copy creates independent copies of all nested structures'],
                          'question': 'What is the key distinction between shallow copy and deep copy of an object?'},
                         {'correct_answer': 'When a derived class object is assigned to a base class value, losing '
                                            'derived members',
                          'difficulty': 'Medium',
                          'explanation': 'Object slicing occurs when assigning a derived object by value to a base '
                                         'object, discarding derived state.',
                          'options': ['When a derived class object is assigned to a base class value, losing derived '
                                      'members',
                                      'When an object is split across two CPU cores',
                                      'When garbage collection fragments an object',
                                      'When private fields are exposed via reflection'],
                          'question': 'What is object slicing in C++?'},
                         {'correct_answer': 'It prevents the class from being extended / subclassed',
                          'difficulty': 'Medium',
                          'explanation': 'Marking a class final prevents inheritance, ensuring its implementation '
                                         'cannot be altered.',
                          'options': ['It prevents the class from being extended / subclassed',
                                      'It makes all methods static',
                                      'It forces the class to be abstract',
                                      'It allows the class to be garbage collected immediately'],
                          'question': "What is the purpose of the 'final' keyword on a class in Java?"},
                         {'correct_answer': 'When it is no longer reachable through reference traversal from any GC '
                                            'roots',
                          'difficulty': 'Hard',
                          'explanation': 'GC algorithms use reachability analysis starting from GC roots to find live '
                                         'objects.',
                          'options': ['When it is no longer reachable through reference traversal from any GC roots',
                                      'As soon as its enclosing method returns, regardless of references',
                                      'When the CPU utilization exceeds 80%',
                                      'Only when the program explicitly terminates'],
                          'question': 'In managed runtimes (e.g. JVM/CLR), when does an object become eligible for '
                                      'garbage collection?'},
                         {'correct_answer': 'It contains an invisible virtual table pointer (vptr) prepended or '
                                            'appended to its layout',
                          'difficulty': 'Hard',
                          'explanation': 'Polymorphic objects include a vptr pointing to the class vtable to support '
                                         'dynamic dispatch.',
                          'options': ['It contains an invisible virtual table pointer (vptr) prepended or appended to '
                                      'its layout',
                                      'It stores the source code of all virtual functions in the object',
                                      'It cannot contain primitive data types',
                                      'It is allocated on the stack instead of the heap'],
                          'question': 'How does dynamic memory layout of an object with virtual methods differ from a '
                                      'plain data struct in C++?'},
                         {'correct_answer': 'Independent fields located on the same CPU cache line cause invalidation '
                                            'thrashing across cores',
                          'difficulty': 'Hard',
                          'explanation': 'False sharing happens when threads modify independent variables residing on '
                                         'the same 64-byte cache line.',
                          'options': ['Independent fields located on the same CPU cache line cause invalidation '
                                      'thrashing across cores',
                                      'Objects are mistakenly shared between threads leading to memory corruption',
                                      'The compiler creates unnecessary deep copies',
                                      'Memory leaks occur in the virtual method table'],
                          'question': 'What is the performance implication of false sharing in multi-threaded object '
                                      'manipulation?'},
                         {'correct_answer': 'A technique representing 64-bit heap references as 32-bit offsets by '
                                            'shifting them by 3 bits (8-byte alignment)',
                          'difficulty': 'Hard',
                          'explanation': 'Compressed OOPs allow 32-bit pointers to address up to 32GB of heap memory '
                                         'while reducing footprint.',
                          'options': ['A technique representing 64-bit heap references as 32-bit offsets by shifting '
                                      'them by 3 bits (8-byte alignment)',
                                      'A compression algorithm like gzip applied to serialized objects',
                                      'A tool to compress Java class files on disk',
                                      'A compiler optimization that removes private fields'],
                          'question': 'What is Compressed OOPs (Ordinary Object Pointers) in the 64-bit JVM?'},
                         {'correct_answer': 'It allocates objects on the stack or scalar-replaces them if their '
                                            'reference does not escape the current method',
                          'difficulty': 'Hard',
                          'explanation': 'Escape analysis determines if an object is accessible outside the creating '
                                         'scope, enabling stack allocation.',
                          'options': ['It allocates objects on the stack or scalar-replaces them if their reference '
                                      'does not escape the current method',
                                      'It moves long-lived objects to disk swap space',
                                      'It prevents objects from calling external libraries',
                                      'It disables garbage collection for all methods'],
                          'question': 'How does Escape Analysis optimize object allocation in modern JIT compilers?'},
                         {'correct_answer': "It omits the implicit 'this' pointer from the function argument list and "
                                            'uses standard calling convention',
                          'difficulty': 'Hard',
                          'explanation': "Static member functions don't receive the hidden 'this' parameter, making "
                                         'their signatures identical to regular functions.',
                          'options': ["It omits the implicit 'this' pointer from the function argument list and uses "
                                      'standard calling convention',
                                      'It generates a polymorphic entry in the class vtable',
                                      'It makes the function executable only in kernel mode',
                                      'It changes its linkage from internal to inline'],
                          'question': "In C++, what is the consequence of declaring a member function 'static' with "
                                      'respect to name mangling and calling convention?'},
                         {'correct_answer': 'Minimizing memory consumption by sharing common fine-grained object state '
                                            'across large numbers of objects',
                          'difficulty': 'Hard',
                          'explanation': 'Flyweight separates intrinsic (shared) state from extrinsic '
                                         '(context-dependent) state to support massive object counts.',
                          'options': ['Minimizing memory consumption by sharing common fine-grained object state '
                                      'across large numbers of objects',
                                      'Preventing more than one object from being instantiated globally',
                                      'Allowing objects to dynamically change their class at runtime',
                                      'Automating deep copying of hierarchical object graphs'],
                          'question': 'What problem does the Flyweight design pattern address regarding class and '
                                      'object instances?'},
                         {'correct_answer': 'It stores Mark Word (hash code, GC age, lock state) and Klass Word '
                                            '(pointer to metadata)',
                          'difficulty': 'Hard',
                          'explanation': 'Hotspot object headers typically consist of two machine words: the Mark Word '
                                         'and the Klass Word.',
                          'options': ['It stores Mark Word (hash code, GC age, lock state) and Klass Word (pointer to '
                                      'metadata)',
                                      'It stores the source code comments and author name',
                                      'It holds the bytecode of the class methods',
                                      'It tracks network socket descriptors opened by the object'],
                          'question': 'What is the role of an Object Header in memory managed runtimes like HotSpot '
                                      'JVM?'},
                         {'correct_answer': 'Because the reference count of the mutually referencing objects never '
                                            'drops to zero',
                          'difficulty': 'Hard',
                          'explanation': 'Reference counting fails to collect isolated cyclic groups because each '
                                         "object's refcount remains >= 1.",
                          'options': ['Because the reference count of the mutually referencing objects never drops to '
                                      'zero',
                                      'Because circular references cause a stack overflow during invocation',
                                      'Because reference counters can only store prime numbers',
                                      'Because circular references trigger segmentation faults in the compiler'],
                          'question': 'Why can circular object references cause memory leaks in simple '
                                      'reference-counting garbage collectors?'},
                         {'correct_answer': 'Multiple inheritance causes duplicate copies of base subobjects; resolved '
                                            'using virtual inheritance',
                          'difficulty': 'Hard',
                          'explanation': 'Virtual inheritance ensures only a single shared instance of the common '
                                         'ancestor base class is constructed.',
                          'options': ['Multiple inheritance causes duplicate copies of base subobjects; resolved using '
                                      'virtual inheritance',
                                      'The constructor runs infinitely; resolved by making base classes static',
                                      'Memory becomes corrupted; resolved using smart pointers',
                                      'Method names collide; resolved by deleting the base class'],
                          'question': 'What is the Diamond Problem in object instantiation under multiple inheritance, '
                                      'and how is it resolved in C++?'}],
 'Composition and Aggregation': [{'correct_answer': "A strong 'has-a' relationship where the lifetime of the component "
                                                    'object depends entirely on the owner object',
                                  'difficulty': 'Easy',
                                  'explanation': 'In composition, if the parent owner is destroyed, the child '
                                                 'component is destroyed as well.',
                                  'options': ["A strong 'has-a' relationship where the lifetime of the component "
                                              'object depends entirely on the owner object',
                                              "An 'is-a' relationship created by extends",
                                              'Merging two source files into one',
                                              'Compressing objects on disk'],
                                  'question': 'What is composition in Object-Oriented Programming?'},
                                 {'correct_answer': "A weak 'has-a' relationship where the component object can exist "
                                                    'independently of the owner object',
                                  'difficulty': 'Easy',
                                  'explanation': 'In aggregation, components have their own independent lifecycle '
                                                 '(e.g. Department and Professor).',
                                  'options': ["A weak 'has-a' relationship where the component object can exist "
                                              'independently of the owner object',
                                              'A relationship where parent and child share memory addresses',
                                              'An algorithm to sum array numbers',
                                              'A mechanism for multiple inheritance'],
                                  'question': 'What is aggregation in Object-Oriented Programming?'},
                                 {'correct_answer': "A 'has-a' relationship",
                                  'difficulty': 'Easy',
                                  'explanation': 'Both composition and aggregation represent structural containment or '
                                                 "association ('has-a').",
                                  'options': ["A 'has-a' relationship",
                                              "An 'is-a' relationship",
                                              "A 'type-of' relationship",
                                              "An 'inherited-from' relationship"],
                                  'question': 'What kind of relationship is represented by both composition and '
                                              'aggregation?'},
                                 {'correct_answer': 'A filled (solid) black diamond at the owner end',
                                  'difficulty': 'Easy',
                                  'explanation': 'UML represents strong composition with a solid black diamond '
                                                 'connected to the composite class.',
                                  'options': ['A filled (solid) black diamond at the owner end',
                                              'A hollow white diamond',
                                              'A dashed arrow with open arrowhead',
                                              'A solid circle'],
                                  'question': 'In UML class diagrams, how is composition represented graphically?'},
                                 {'correct_answer': 'A hollow (empty) white diamond at the aggregate end',
                                  'difficulty': 'Easy',
                                  'explanation': 'UML represents weak aggregation with a hollow diamond.',
                                  'options': ['A hollow (empty) white diamond at the aggregate end',
                                              'A filled black diamond',
                                              'A solid line with no arrows',
                                              'A zig-zag line'],
                                  'question': 'In UML class diagrams, how is aggregation represented graphically?'},
                                 {'correct_answer': 'A Car and its Engine (if car is destroyed, its installed engine '
                                                    'is destroyed with it)',
                                  'difficulty': 'Easy',
                                  'explanation': 'Parts that cannot meaningfully outlive their owner represent '
                                                 'composition.',
                                  'options': ['A Car and its Engine (if car is destroyed, its installed engine is '
                                              'destroyed with it)',
                                              'A Library and its Student readers',
                                              'A Teacher and a School',
                                              'A Pilot and an Airline'],
                                  'question': 'Which of the following is a classic real-world example of composition?'},
                                 {'correct_answer': 'A University and a Student (student continues to exist if '
                                                    'university closes)',
                                  'difficulty': 'Easy',
                                  'explanation': 'Students exist independently of universities, demonstrating '
                                                 'aggregation.',
                                  'options': ['A University and a Student (student continues to exist if university '
                                              'closes)',
                                              'A House and its Rooms',
                                              'A Human and their Heart',
                                              'A Document and its Pages'],
                                  'question': 'Which of the following is a classic real-world example of aggregation?'},
                                 {'correct_answer': 'Designing systems by assembling reusable components rather than '
                                                    'building deep inheritance trees',
                                  'difficulty': 'Easy',
                                  'explanation': 'Composition provides greater flexibility, lower coupling, and '
                                                 'runtime dynamic behavior.',
                                  'options': ['Designing systems by assembling reusable components rather than '
                                              'building deep inheritance trees',
                                              'Never using classes in OOP',
                                              'Always writing all code in a single class',
                                              'Using global functions instead of objects'],
                                  'question': "What is the principle 'Favor Composition over Inheritance' advocating?"},
                                 {'correct_answer': 'Components are accessed through their public interfaces without '
                                                    'exposing internal base class implementation',
                                  'difficulty': 'Easy',
                                  'explanation': 'Composition treats components as black boxes, preventing the fragile '
                                                 'base class problem.',
                                  'options': ['Components are accessed through their public interfaces without '
                                              'exposing internal base class implementation',
                                              'Composition runs without compiling',
                                              'Composition eliminates all method calls',
                                              'Components share the exact same stack frame'],
                                  'question': 'How does composition provide looser coupling than class inheritance?'},
                                 {'correct_answer': 'Yes, reference fields pointing to components can be reassigned '
                                                    'dynamically during execution',
                                  'difficulty': 'Easy',
                                  'explanation': 'Unlike static inheritance hierarchies, composition allows changing '
                                                 'component delegates on the fly.',
                                  'options': ['Yes, reference fields pointing to components can be reassigned '
                                              'dynamically during execution',
                                              'No, relationships are fixed at compile time forever',
                                              'Only in assembly language',
                                              'Only if the class has no methods'],
                                  'question': 'Can component behaviors in a composite object be swapped dynamically at '
                                              'runtime?'},
                                 {'correct_answer': 'A mechanism where an object passes a task to an underlying '
                                                    'composed helper object to perform the work',
                                  'difficulty': 'Medium',
                                  'explanation': 'Delegation forwards calls to an internal component to reuse its '
                                                 'implementation cleanly.',
                                  'options': ['A mechanism where an object passes a task to an underlying composed '
                                              'helper object to perform the work',
                                              'Passing task handling to the operating system kernel',
                                              'Delegating method calls to the compiler',
                                              'Deleting an object after delegating memory'],
                                  'question': 'What is delegation in the context of composition?'},
                                 {'correct_answer': 'It encapsulates algorithms in separate strategy classes and '
                                                    'composes them into a context object that can switch strategies',
                                  'difficulty': 'Medium',
                                  'explanation': 'Strategy pattern favors composition by delegating algorithmic tasks '
                                                 'to pluggable component objects.',
                                  'options': ['It encapsulates algorithms in separate strategy classes and composes '
                                              'them into a context object that can switch strategies',
                                              'It creates strategies through deep inheritance',
                                              'It replaces classes with switch statements',
                                              'It creates static global variables'],
                                  'question': 'How does the Strategy design pattern utilize composition?'},
                                 {'correct_answer': 'By embedding component objects as direct value members (by value) '
                                                    'inside the owning class struct',
                                  'difficulty': 'Medium',
                                  'explanation': 'Direct value members are constructed with the owner and destructed '
                                                 'deterministically when the owner destructs.',
                                  'options': ['By embedding component objects as direct value members (by value) '
                                              'inside the owning class struct',
                                              'By using void* pointers to random memory',
                                              'By creating threads for each member',
                                              'By declaring all members virtual'],
                                  'question': 'In C++, how is composition typically expressed in terms of object '
                                              'lifetime and memory layout?'},
                                 {'correct_answer': 'By holding pointers (e.g. std::shared_ptr or raw pointers) or '
                                                    'references to independently allocated external objects',
                                  'difficulty': 'Medium',
                                  'explanation': 'Pointers and references allow referencing entities that exist '
                                                 'independently of the containing object.',
                                  'options': ['By holding pointers (e.g. std::shared_ptr or raw pointers) or '
                                              'references to independently allocated external objects',
                                              'By embedding value members directly',
                                              'By using static arrays only',
                                              'By placing members in ROM'],
                                  'question': 'In C++, how is aggregation typically expressed in terms of memory?'},
                                 {'correct_answer': 'It wraps a component object dynamically to augment its behavior '
                                                    'without modifying its source code or using subclassing',
                                  'difficulty': 'Medium',
                                  'explanation': 'Decorators hold a reference to an interface and wrap calls with '
                                                 'additional functionality.',
                                  'options': ['It wraps a component object dynamically to augment its behavior without '
                                              'modifying its source code or using subclassing',
                                              'It decorates source code with comments',
                                              'It replaces inheritance with multiple interfaces',
                                              'It colors GUI buttons automatically'],
                                  'question': 'What is the Decorator design pattern and how does it rely on '
                                              'composition?'},
                                 {'correct_answer': 'Boilerplate forwarding/delegation methods may be needed to expose '
                                                    'component capabilities',
                                  'difficulty': 'Medium',
                                  'explanation': 'Composed objects do not inherit public signatures automatically, '
                                                 'often requiring pass-through methods.',
                                  'options': ['Boilerplate forwarding/delegation methods may be needed to expose '
                                              'component capabilities',
                                              'Composition is 100x slower at runtime',
                                              'Composition consumes exponentially more heap memory',
                                              'Composition cannot be tested with unit tests'],
                                  'question': 'What is the primary drawback of composition compared to direct '
                                              'inheritance?'},
                                 {'correct_answer': 'Association is the general semantic relationship between classes; '
                                                    'aggregation and composition are specialized forms of association',
                                  'difficulty': 'Medium',
                                  'explanation': 'Association describes structural relationships, with aggregation '
                                                 'being weak and composition being strong ownership.',
                                  'options': ['Association is the general semantic relationship between classes; '
                                              'aggregation and composition are specialized forms of association',
                                              'Association only applies to databases',
                                              'Association is identical to inheritance',
                                              'Association applies only to primitive variables'],
                                  'question': 'What is an association in UML and how does it relate to aggregation and '
                                              'composition?'},
                                 {'correct_answer': 'Composed dependencies can be passed via interfaces and mocked or '
                                                    'stubbed easily during test setup',
                                  'difficulty': 'Medium',
                                  'explanation': 'Dependency injection of composed interfaces allows mock objects to '
                                                 'be substituted seamlessly in tests.',
                                  'options': ['Composed dependencies can be passed via interfaces and mocked or '
                                              'stubbed easily during test setup',
                                              'Composition prevents tests from throwing exceptions',
                                              'Composition compiles tests without a test runner',
                                              'Mocking is impossible with inheritance'],
                                  'question': 'Why does composition make unit testing significantly easier with '
                                              'mocking?'},
                                 {'correct_answer': 'Treating individual objects and compositions of objects uniformly '
                                                    'using a shared component interface (tree structure)',
                                  'difficulty': 'Medium',
                                  'explanation': 'Composite pattern lets clients treat leaf nodes and branches '
                                                 'uniformly through a common interface.',
                                  'options': ['Treating individual objects and compositions of objects uniformly using '
                                              'a shared component interface (tree structure)',
                                              'Compiling multiple classes into one file',
                                              'A pattern used to compress images',
                                              'A technique for creating composite keys in databases'],
                                  'question': 'What is the Composite design pattern?'},
                                 {'correct_answer': 'Dependencies are passed into the constructor at creation time, '
                                                    'establishing clean composed relationships',
                                  'difficulty': 'Medium',
                                  'explanation': 'Injecting dependencies via constructors ensures all required '
                                                 'components are provided and easily swapped.',
                                  'options': ['Dependencies are passed into the constructor at creation time, '
                                              'establishing clean composed relationships',
                                              'It uses global singletons to find dependencies',
                                              'It instantiates hardcoded classes inside the constructor',
                                              'It loads classes from external URLs'],
                                  'question': 'How does constructor dependency injection support composition?'},
                                 {'correct_answer': 'C++ embeds components contiguously in memory, yielding '
                                                    'exceptional CPU cache locality and zero pointer indirection',
                                  'difficulty': 'Hard',
                                  'explanation': 'Contiguous embedding avoids heap indirection and cache misses, '
                                                 'whereas Java objects always require pointer dereferencing.',
                                  'options': ['C++ embeds components contiguously in memory, yielding exceptional CPU '
                                              'cache locality and zero pointer indirection',
                                              'Java pointers are always faster than contiguous memory',
                                              'C++ values require extra heap allocations',
                                              'Cache locality is identical in both'],
                                  'question': 'How does composition by value in C++ affect cache locality compared to '
                                              'pointer-based composition in Java?'},
                                 {'correct_answer': 'std::unique_ptr expresses strict composition (sole ownership); '
                                                    'std::shared_ptr / weak_ptr express shared aggregation',
                                  'difficulty': 'Hard',
                                  'explanation': 'unique_ptr guarantees exclusive ownership tied to owner lifetime, '
                                                 'while shared/weak pointers represent non-exclusive associations.',
                                  'options': ['std::unique_ptr expresses strict composition (sole ownership); '
                                              'std::shared_ptr / weak_ptr express shared aggregation',
                                              'All smart pointers express inheritance',
                                              'unique_ptr is used only for primitive numbers',
                                              'weak_ptr prevents compilation'],
                                  'question': 'How does smart pointer ownership (std::unique_ptr vs std::shared_ptr vs '
                                              'std::weak_ptr) express composition vs aggregation in modern C++?'},
                                 {'correct_answer': 'A method should only talk to immediate friends (fields, '
                                                    'parameters, created objects), avoiding long chained calls '
                                                    '(a.getB().getC().doSomething())',
                                  'difficulty': 'Hard',
                                  'explanation': 'The Law of Demeter prevents tight coupling across deep object '
                                                 'traversal chains.',
                                  'options': ['A method should only talk to immediate friends (fields, parameters, '
                                              'created objects), avoiding long chained calls '
                                              '(a.getB().getC().doSomething())',
                                              'Every class must have at least three components',
                                              'Objects must know the internal state of all neighbors',
                                              'All methods must be static'],
                                  'question': "What is the 'Law of Demeter' (Principle of Least Knowledge) in relation "
                                              'to composed object graphs?'},
                                 {'correct_answer': 'It decouples an abstraction from its implementation so that both '
                                                    'can vary independently via composition',
                                  'difficulty': 'Hard',
                                  'explanation': 'Bridge uses composition to link high-level abstractions to low-level '
                                                 'implementation hierarchies without class explosion.',
                                  'options': ['It decouples an abstraction from its implementation so that both can '
                                              'vary independently via composition',
                                              'It connects C++ code to Python code',
                                              'It translates SQL queries to JSON',
                                              'It builds physical network bridges'],
                                  'question': 'What is the Bridge design pattern and how does it separate abstraction '
                                              'from implementation using composition?'},
                                 {'correct_answer': 'Mutual strong references prevent reference counts from ever '
                                                    'reaching zero, requiring weak references (std::weak_ptr / weak) '
                                                    'to break cycles',
                                  'difficulty': 'Hard',
                                  'explanation': 'Breaking reference cycles with non-owning weak references is '
                                                 'essential to prevent permanent memory leaks in ARC.',
                                  'options': ['Mutual strong references prevent reference counts from ever reaching '
                                              'zero, requiring weak references (std::weak_ptr / weak) to break cycles',
                                              'Circular references cause stack overflow during compilation',
                                              'The CPU freezes due to deadlocked instructions',
                                              'Operating system pages are marked read-only'],
                                  'question': 'How do circular dependencies in composition cause memory leaks in '
                                              'reference-counted environments (e.g. std::shared_ptr or Swift ARC)?'},
                                 {'correct_answer': 'An Aggregate Root is the sole external access gate for a cluster '
                                                    'of composed entities, ensuring all invariants are maintained '
                                                    'together',
                                  'difficulty': 'Hard',
                                  'explanation': 'Outside callers may only hold references to the Aggregate Root, '
                                                 'keeping internal composed entities shielded.',
                                  'options': ['An Aggregate Root is the sole external access gate for a cluster of '
                                              'composed entities, ensuring all invariants are maintained together',
                                              'An Aggregate Root is a database root user',
                                              'Aggregate Roots must be abstract classes',
                                              'It is an algorithm to compress domain models'],
                                  'question': 'In Domain-Driven Design (DDD), how do Aggregate Roots govern '
                                              'composition and encapsulation boundaries?'},
                                 {'correct_answer': 'Intrinsic shared state is aggregated/referenced by many objects, '
                                                    'while extrinsic state is passed in or composed',
                                  'difficulty': 'Hard',
                                  'explanation': 'Flyweight separates shared aggregated state from transient context, '
                                                 'minimizing memory footprints.',
                                  'options': ['Intrinsic shared state is aggregated/referenced by many objects, while '
                                              'extrinsic state is passed in or composed',
                                              'It creates deep inheritance trees for lightweight objects',
                                              'It flattens all objects into a single array',
                                              'It deletes all objects after 1 millisecond'],
                                  'question': "What is the Flyweight pattern's relationship with composition and "
                                              'aggregation?'},
                                 {'correct_answer': 'Value objects have no object identity and flatten directly into '
                                                    'memory layouts without heap pointer indirection',
                                  'difficulty': 'Hard',
                                  'explanation': "Valhalla's value types allow flat, contiguous memory composition "
                                                 'similar to C++ structs, eliminating pointer chasing.',
                                  'options': ['Value objects have no object identity and flatten directly into memory '
                                              'layouts without heap pointer indirection',
                                              'It removes garbage collection from the JVM',
                                              'It forces all objects to be stored in registers',
                                              'It replaces the JVM with a WebAssembly runtime'],
                                  'question': "How does Java's Project Valhalla (Value Objects / Value Types) bridge "
                                              'the performance gap between composition and primitive arrays?'},
                                 {'correct_answer': 'Call stacks become deep and repetitive traversal through multiple '
                                                    'layers causes latency and indirection overhead',
                                  'difficulty': 'Hard',
                                  'explanation': 'Deep delegation chains can accumulate CPU overhead and obscure the '
                                                 'exact origin of operations and errors.',
                                  'options': ['Call stacks become deep and repetitive traversal through multiple '
                                              'layers causes latency and indirection overhead',
                                              'The compiler crashes due to too many methods',
                                              'Garbage collection is disabled permanently',
                                              'Virtual memory is deallocated'],
                                  'question': 'What architectural hazard occurs when composite hierarchies misuse deep '
                                              'delegation without caching?'},
                                 {'correct_answer': 'Components interact through stable interfaces, allowing new '
                                                    'implementations to be introduced without touching existing code',
                                  'difficulty': 'Hard',
                                  'explanation': 'Swapping composed components satisfies open for extension, closed '
                                                 'for modification cleanly.',
                                  'options': ['Components interact through stable interfaces, allowing new '
                                              'implementations to be introduced without touching existing code',
                                              'Composition does not use CPU cycles',
                                              'Inheritance cannot use interfaces',
                                              'Composition prevents null pointers automatically'],
                                  'question': 'Why is composition fundamentally more robust against breaking changes '
                                              'than inheritance according to the Open/Closed Principle?'}],
 'Constructors and Destructors': [{'correct_answer': 'A special member method invoked automatically when an object is '
                                                     'instantiated',
                                   'difficulty': 'Easy',
                                   'explanation': 'Constructors initialize state and allocate resources upon object '
                                                  'creation.',
                                   'options': ['A special member method invoked automatically when an object is '
                                               'instantiated',
                                               'A function used to delete an object from memory',
                                               'A static method used to calculate hash codes',
                                               'A loop that constructs arrays'],
                                   'question': 'What is a constructor in OOP?'},
                                  {'correct_answer': 'It has no return type, not even void',
                                   'difficulty': 'Easy',
                                   'explanation': 'Constructors do not return any type; they construct the instance.',
                                   'options': ['It has no return type, not even void',
                                               'void',
                                               'int',
                                               'A pointer to the object'],
                                   'question': 'What is the return type of a constructor in C++ and Java?'},
                                  {'correct_answer': 'A constructor that takes no arguments',
                                   'difficulty': 'Easy',
                                   'explanation': 'A default constructor initializes an object with zero arguments or '
                                                  'default values.',
                                   'options': ['A constructor that takes no arguments',
                                               'A constructor provided by the operating system kernel',
                                               'A constructor that is always private',
                                               'A constructor that returns null'],
                                   'question': 'What is a default constructor?'},
                                  {'correct_answer': 'A constructor that accepts one or more arguments to initialize '
                                                     'fields',
                                   'difficulty': 'Easy',
                                   'explanation': 'Parameterized constructors allow passing specific initial values '
                                                  'during creation.',
                                   'options': ['A constructor that accepts one or more arguments to initialize fields',
                                               'A constructor that only takes string arguments',
                                               'A constructor that returns boolean',
                                               'A constructor used only in templates'],
                                   'question': 'What is a parameterized constructor?'},
                                  {'correct_answer': 'To release allocated resources and clean up memory when an '
                                                     'object goes out of scope',
                                   'difficulty': 'Easy',
                                   'explanation': "Destructors execute when an object's lifetime ends to free "
                                                  'resources like file handles and memory.',
                                   'options': ['To release allocated resources and clean up memory when an object goes '
                                               'out of scope',
                                               'To initialize instance variables',
                                               'To duplicate an object on the heap',
                                               'To convert an object into JSON'],
                                   'question': 'What is the role of a destructor in C++?'},
                                  {'correct_answer': 'Tilde (~)',
                                   'difficulty': 'Easy',
                                   'explanation': 'In C++, destructors are denoted by ~ClassName().',
                                   'options': ['Tilde (~)', 'Exclamation mark (!)', 'At symbol (@)', 'Hash (#)'],
                                   'question': 'Which symbol is used before a class name to define a destructor in '
                                               'C++?'},
                                  {'correct_answer': 'No, destructors cannot take any arguments',
                                   'difficulty': 'Easy',
                                   'explanation': 'Destructors cannot accept parameters or be overloaded.',
                                   'options': ['No, destructors cannot take any arguments',
                                               'Yes, up to 2 arguments',
                                               'Yes, any number of arguments',
                                               'Only if it is declared virtual'],
                                   'question': 'Can a destructor take arguments in C++?'},
                                  {'correct_answer': 'Exactly one',
                                   'difficulty': 'Easy',
                                   'explanation': 'Because destructors cannot take parameters, there can only ever be '
                                                  'one destructor per class.',
                                   'options': ['Exactly one', 'Up to two', 'Any number based on overloading', 'Zero'],
                                   'question': 'How many destructors can a class have in C++?'},
                                  {'correct_answer': 'The compiler automatically generates a default no-argument '
                                                     'constructor',
                                   'difficulty': 'Easy',
                                   'explanation': 'Compilers synthesize a public default parameterless constructor if '
                                                  'no constructor is explicitly provided.',
                                   'options': ['The compiler automatically generates a default no-argument constructor',
                                               'A compilation error occurs',
                                               'The program crashes at runtime',
                                               'The class cannot be instantiated'],
                                   'question': 'What happens if no constructor is defined by the programmer in Java or '
                                               'C++?'},
                                  {'correct_answer': 'Automatically when the enclosing scope is exited',
                                   'difficulty': 'Easy',
                                   'explanation': 'Stack-allocated objects are deterministically destroyed upon '
                                                  'exiting their lexical scope.',
                                   'options': ['Automatically when the enclosing scope is exited',
                                               'Only when free() is explicitly called',
                                               'When the entire program finishes',
                                               'Destructors are never called for stack objects'],
                                   'question': 'When an object is created on the stack in C++, when is its destructor '
                                               'called?'},
                                  {'correct_answer': 'The practice of calling one constructor from another constructor '
                                                     'within the same or parent class',
                                   'difficulty': 'Medium',
                                   'explanation': 'Constructor chaining uses this(...) or super(...) to reuse '
                                                  'initialization logic.',
                                   'options': ['The practice of calling one constructor from another constructor '
                                               'within the same or parent class',
                                               'Chaining method calls using dot notation',
                                               'Creating an array of constructors',
                                               'Invoking destructors in a loop'],
                                   'question': 'What is constructor chaining?'},
                                  {'correct_answer': 'this()',
                                   'difficulty': 'Medium',
                                   'explanation': 'this() delegates initialization to an overloaded constructor in the '
                                                  'same class.',
                                   'options': ['this()', 'super()', 'self()', 'base()'],
                                   'question': 'Which keyword is used in Java to call another constructor in the same '
                                               'class?'},
                                  {'correct_answer': 'this() or super() invocation',
                                   'difficulty': 'Medium',
                                   'explanation': 'Java enforces that explicit constructor delegation calls (this() or '
                                                  'super()) must be the first statement.',
                                   'options': ['this() or super() invocation',
                                               'return statement',
                                               'Variable declaration',
                                               'System.out.println()'],
                                   'question': 'In Java, which statement must be the very first line inside a '
                                               'constructor body?'},
                                  {'correct_answer': 'The compiler no longer generates the default no-argument '
                                                     'constructor',
                                   'difficulty': 'Medium',
                                   'explanation': 'Defining any explicit constructor suppresses automatic generation '
                                                  'of the default constructor.',
                                   'options': ['The compiler no longer generates the default no-argument constructor',
                                               'The compiler replaces your parameterized constructor',
                                               'The default constructor remains and becomes private',
                                               'A runtime error is triggered'],
                                   'question': 'What happens to the compiler-provided default constructor once you '
                                               'define any parameterized constructor?'},
                                  {'correct_answer': 'An idiom where resource lifetime is tied to object lifetime via '
                                                     'constructors and destructors',
                                   'difficulty': 'Medium',
                                   'explanation': 'RAII guarantees resource acquisition in constructor and release in '
                                                  'destructor.',
                                   'options': ['An idiom where resource lifetime is tied to object lifetime via '
                                               'constructors and destructors',
                                               'A garbage collection algorithm',
                                               'A design pattern for singleton objects',
                                               'A compiler flag to enable multithreading'],
                                   'question': 'What is RAII (Resource Acquisition Is Initialization) in C++?'},
                                  {'correct_answer': 'To ensure derived class destructors are properly invoked when '
                                                     'deleting via a base pointer',
                                   'difficulty': 'Medium',
                                   'explanation': 'Deleting a derived object through a base pointer with a non-virtual '
                                                  'destructor causes undefined behavior and resource leaks.',
                                   'options': ['To ensure derived class destructors are properly invoked when deleting '
                                               'via a base pointer',
                                               'To speed up constructor execution',
                                               'To allow destructors to take arguments',
                                               'To prevent the class from being inherited'],
                                   'question': 'Why should base class destructors almost always be declared virtual in '
                                               'C++?'},
                                  {'correct_answer': 'Base class constructors run first, followed by derived class '
                                                     'constructors',
                                   'difficulty': 'Medium',
                                   'explanation': 'The foundation (base subobject) must be fully constructed before '
                                                  'derived extensions can be initialized.',
                                   'options': ['Base class constructors run first, followed by derived class '
                                               'constructors',
                                               'Derived class constructors run first, followed by base',
                                               'Constructors run in arbitrary order',
                                               'Only the derived class constructor runs'],
                                   'question': 'What is the order of constructor execution in a derived class '
                                               'hierarchy?'},
                                  {'correct_answer': 'Derived class destructor runs first, followed by base class '
                                                     'destructor',
                                   'difficulty': 'Medium',
                                   'explanation': 'Destruction mirrors construction in exact reverse order (LIFO).',
                                   'options': ['Derived class destructor runs first, followed by base class destructor',
                                               'Base class destructor runs first, followed by derived',
                                               'Destructors run concurrently on separate threads',
                                               'Only the base class destructor runs'],
                                   'question': 'What is the order of destructor execution in a derived class '
                                               'hierarchy?'},
                                  {'correct_answer': 'To prevent direct instantiation, common in Singleton and '
                                                     'utility/factory classes',
                                   'difficulty': 'Medium',
                                   'explanation': 'Private constructors prevent external callers from instantiating '
                                                  'the class directly.',
                                   'options': ['To prevent direct instantiation, common in Singleton and '
                                               'utility/factory classes',
                                               'To allow only the OS to create instances',
                                               'To speed up compilation times',
                                               'To make all methods public automatically'],
                                   'question': 'What is a private constructor used for?'},
                                  {'correct_answer': "'__new__' is the static method that creates and returns the "
                                                     "instance, while '__init__' initializes it",
                                   'difficulty': 'Medium',
                                   'explanation': "'__new__' allocates and returns the raw object instance, which is "
                                                  "then passed to '__init__' for setup.",
                                   'options': ["'__new__' is the static method that creates and returns the instance, "
                                               "while '__init__' initializes it",
                                               "'__init__' creates the memory and '__new__' destroys it",
                                               "'__new__' is only called for subclasses of int",
                                               'There is no difference between them'],
                                   'question': "In Python, what is the key difference between '__new__' and "
                                               "'__init__'?"},
                                  {'correct_answer': 'The destructor for that object will NOT be called, causing '
                                                     'resource leaks if raw pointers are used',
                                   'difficulty': 'Hard',
                                   'explanation': 'In C++, an object is only considered created once its constructor '
                                                  "finishes; failing constructors never trigger the object's "
                                                  'destructor.',
                                   'options': ['The destructor for that object will NOT be called, causing resource '
                                               'leaks if raw pointers are used',
                                               'The program instantly crashes with SIGSEGV',
                                               'The compiler deletes the class definition',
                                               'The exception is silently swallowed'],
                                   'question': 'What is the danger of throwing an exception from inside a C++ '
                                               'constructor?'},
                                  {'correct_answer': 'If another exception is already unwinding the stack, throwing '
                                                     'from a destructor causes std::terminate()',
                                   'difficulty': 'Hard',
                                   'explanation': 'Two active exceptions during stack unwinding cannot be handled '
                                                  'simultaneously, causing immediate program termination.',
                                   'options': ['If another exception is already unwinding the stack, throwing from a '
                                               'destructor causes std::terminate()',
                                               'It causes compiler syntax errors',
                                               'Destructors cannot contain try/catch blocks',
                                               'It turns the class into a virtual class'],
                                   'question': 'Why is throwing an exception from inside a C++ destructor strongly '
                                               'discouraged (or noexcept by default)?'},
                                  {'correct_answer': 'Dynamic dispatch resolves only to the base class implementation, '
                                                     'not the derived override',
                                   'difficulty': 'Hard',
                                   'explanation': 'During base construction, the derived object has not yet been '
                                                  'initialized; C++ intentionally restricts vtable dispatch to base.',
                                   'options': ['Dynamic dispatch resolves only to the base class implementation, not '
                                               'the derived override',
                                               'The derived class implementation executes normally',
                                               'A PureVirtualMethodCalled exception is always thrown',
                                               'The call is dispatched to the operating system'],
                                   'question': 'What happens when a virtual function is called from inside a base '
                                               'class constructor in C++?'},
                                  {'correct_answer': 'A constructor that invokes another constructor of the same class '
                                                     'in its member initializer list',
                                   'difficulty': 'Hard',
                                   'explanation': 'Delegating constructors avoid redundant code by calling peer '
                                                  'constructors within the class initialization list.',
                                   'options': ['A constructor that invokes another constructor of the same class in '
                                               'its member initializer list',
                                               'A constructor that passes work to another thread',
                                               'A constructor that delegates memory to the garbage collector',
                                               'A constructor that takes a function pointer'],
                                   'question': 'What is a delegating constructor in C++11?'},
                                  {'correct_answer': 'If you define destructor, copy constructor, or copy assignment, '
                                                     'you should also define move constructor and move assignment',
                                   'difficulty': 'Hard',
                                   'explanation': 'Resource-managing classes in C++11 must handle copy and move '
                                                  'semantics alongside destruction.',
                                   'options': ['If you define destructor, copy constructor, or copy assignment, you '
                                               'should also define move constructor and move assignment',
                                               'A class cannot have more than five constructors',
                                               'A class must inherit from at most five interfaces',
                                               'An object can live on at most five threads'],
                                   'question': "What is the 'Rule of Five' in modern C++?"},
                                  {'correct_answer': 'They MUST be initialized using the constructor member '
                                                     'initializer list, not in the constructor body',
                                   'difficulty': 'Hard',
                                   'explanation': 'Const and reference members cannot be assigned; they must be bound '
                                                  'at point of initialization.',
                                   'options': ['They MUST be initialized using the constructor member initializer '
                                               'list, not in the constructor body',
                                               'They are initialized to zero automatically',
                                               'They can be reassigned in the constructor body',
                                               'They can only be initialized by static methods'],
                                   'question': 'What happens to const or reference member variables regarding '
                                               'constructors in C++?'},
                                  {'correct_answer': 'Unpredictable execution timing, performance overhead, '
                                                     'resurrection vulnerabilities, and deadlock risks',
                                   'difficulty': 'Hard',
                                   'explanation': 'Finalizers suffer from severe flaws: promptness is not guaranteed, '
                                                  'and uncaught exceptions are ignored.',
                                   'options': ['Unpredictable execution timing, performance overhead, resurrection '
                                               'vulnerabilities, and deadlock risks',
                                               'It was replaced by C++ delete',
                                               'It could only delete static variables',
                                               'It was incompatible with 64-bit processors'],
                                   'question': 'Why is finalize() deprecated in Java (since Java 9) and removed in '
                                               'recent versions?'},
                                  {'correct_answer': "When an unreferenced object reassigns 'this' to an active "
                                                     'reference inside finalize(), surviving GC',
                                   'difficulty': 'Hard',
                                   'explanation': 'Inside finalize(), the object can re-attach itself to a GC root, '
                                                  'resurrecting itself and defying collection.',
                                   'options': ["When an unreferenced object reassigns 'this' to an active reference "
                                               'inside finalize(), surviving GC',
                                               'Rebooting the JVM to recover deleted objects',
                                               'Loading class files from disk after crash',
                                               'Converting a dead thread into a live worker'],
                                   'question': "What is 'Object Resurrection' in Java finalization?"},
                                  {'correct_answer': "A constructor marked 'explicit' to prevent implicit type "
                                                     'conversions and copy-initialization',
                                   'difficulty': 'Hard',
                                   'explanation': 'The explicit specifier forbids the compiler from using '
                                                  'single-argument constructors for implicit conversions.',
                                   'options': ["A constructor marked 'explicit' to prevent implicit type conversions "
                                               'and copy-initialization',
                                               'A constructor written in assembly',
                                               'A constructor that cannot be overloaded',
                                               'A constructor that runs only in debug mode'],
                                   'question': 'What is an explicit constructor in C++?'},
                                  {'correct_answer': 'Destructors are invoked for already fully constructed subobjects '
                                                     'before the exception propagates',
                                   'difficulty': 'Hard',
                                   'explanation': 'C++ guarantees unwinding and destructor invocation for any members '
                                                  'whose constructors successfully finished prior to the failure.',
                                   'options': ['Destructors are invoked for already fully constructed subobjects '
                                               'before the exception propagates',
                                               'The entire heap is cleared',
                                               'The enclosing object is created anyway with null values',
                                               'A compilation warning is issued'],
                                   'question': "In C++, if a member object's constructor throws during enclosing "
                                               'object construction, what happens?'}],
 'Encapsulation and Data Hiding': [{'correct_answer': 'Bundling data and methods into a single unit while restricting '
                                                      'direct external access',
                                    'difficulty': 'Easy',
                                    'explanation': 'Encapsulation wraps state and operations together, hiding internal '
                                                   'implementation details.',
                                    'options': ['Bundling data and methods into a single unit while restricting direct '
                                                'external access',
                                                'Allowing all variables to be globally modified',
                                                'Converting source code into binary machine code',
                                                'Running code across multiple threads'],
                                    'question': 'What is encapsulation in Object-Oriented Programming?'},
                                   {'correct_answer': 'private',
                                    'difficulty': 'Easy',
                                    'explanation': 'Private members can only be accessed by code within the same class '
                                                   'definition.',
                                    'options': ['private', 'public', 'protected', 'default / package-private'],
                                    'question': 'Which access modifier restricts member visibility exclusively to the '
                                                'declaring class?'},
                                   {'correct_answer': 'public',
                                    'difficulty': 'Easy',
                                    'explanation': 'Public members have unrestricted visibility across the entire '
                                                   'application.',
                                    'options': ['public', 'private', 'protected', 'internal'],
                                    'question': 'Which access modifier allows members to be accessed from any class in '
                                                'any package?'},
                                   {'correct_answer': 'protected',
                                    'difficulty': 'Easy',
                                    'explanation': 'Protected members are accessible by derived classes and within the '
                                                   'same package.',
                                    'options': ['protected', 'private', 'final', 'transient'],
                                    'question': 'Which access modifier permits access within the declaring class, its '
                                                'subclasses, and same package?'},
                                   {'correct_answer': 'Providing controlled read and write access to private fields '
                                                      'with optional validation',
                                    'difficulty': 'Easy',
                                    'explanation': 'Getters and setters mediate field access, allowing invariants and '
                                                   'validation logic to be enforced.',
                                    'options': ['Providing controlled read and write access to private fields with '
                                                'optional validation',
                                                'Constructing database tables',
                                                'Running unit tests automatically',
                                                'Speeding up disk I/O'],
                                    'question': 'What are getter and setter methods used for?'},
                                   {'correct_answer': 'Shielding the internal state of an object from direct '
                                                      'unauthorized modification by outside code',
                                    'difficulty': 'Easy',
                                    'explanation': 'Data hiding ensures that external clients cannot directly alter '
                                                   'private member variables.',
                                    'options': ['Shielding the internal state of an object from direct unauthorized '
                                                'modification by outside code',
                                                'Hiding password files on disk',
                                                'Encrypting memory using AES',
                                                'Hiding method names from the debugger'],
                                    'question': "What is 'data hiding' in OOP?"},
                                   {'correct_answer': 'Internal implementation can be modified without breaking '
                                                      'external code relying on the public API',
                                    'difficulty': 'Easy',
                                    'explanation': 'Encapsulation creates a stable public contract while keeping '
                                                   'implementation details flexible.',
                                    'options': ['Internal implementation can be modified without breaking external '
                                                'code relying on the public API',
                                                'It eliminates the need for unit testing',
                                                'It prevents compile errors from occurring',
                                                'It makes applications consume zero RAM'],
                                    'question': 'How does encapsulation improve software maintainability?'},
                                   {'correct_answer': 'Prefixing with two leading underscores (e.g., __variable)',
                                    'difficulty': 'Easy',
                                    'explanation': 'Python uses double underscores for private attributes, triggering '
                                                   'name mangling.',
                                    'options': ['Prefixing with two leading underscores (e.g., __variable)',
                                                "Adding 'private' before the variable name",
                                                'Capitalizing all letters',
                                                'Placing an @ symbol at the beginning'],
                                    'question': 'In Python, how is a private attribute conventionally indicated by '
                                                'name?'},
                                   {'correct_answer': 'No, private fields are inaccessible outside the declaring class '
                                                      'without reflection',
                                    'difficulty': 'Easy',
                                    'explanation': 'Java compiler enforces that private members cannot be accessed '
                                                   'directly by other classes.',
                                    'options': ['No, private fields are inaccessible outside the declaring class '
                                                'without reflection',
                                                'Yes, anytime by using the dot operator',
                                                'Yes, if the calling class is in the same file',
                                                'Only on Tuesdays'],
                                    'question': 'Can external code directly access private fields of an object in '
                                                'standard Java?'},
                                   {'correct_answer': 'A class whose object state cannot be modified after '
                                                      'instantiation',
                                    'difficulty': 'Easy',
                                    'explanation': 'Immutable objects have fixed state throughout their lifetime, '
                                                   'offering strong thread safety.',
                                    'options': ['A class whose object state cannot be modified after instantiation',
                                                'A class that cannot be compiled',
                                                'A class with no methods',
                                                'A class stored in read-only ROM'],
                                    'question': 'What is an immutable class?'},
                                   {'correct_answer': 'Transforming __var to _ClassName__var to prevent accidental '
                                                      'overwriting in subclasses',
                                    'difficulty': 'Medium',
                                    'explanation': 'Python mangles double-underscore attributes with the class name to '
                                                   'avoid naming collisions.',
                                    'options': ['Transforming __var to _ClassName__var to prevent accidental '
                                                'overwriting in subclasses',
                                                'Compressing variable names to save memory',
                                                'Encrypting string literals',
                                                'Translating code into bytecode'],
                                    'question': 'What is name mangling in Python?'},
                                   {'correct_answer': 'Setters and constructors validate incoming data and reject '
                                                      'invalid states',
                                    'difficulty': 'Medium',
                                    'explanation': 'Encapsulated methods act as gatekeepers ensuring objects never '
                                                   'enter an invalid state.',
                                    'options': ['Setters and constructors validate incoming data and reject invalid '
                                                'states',
                                                'The OS checks invariants during page faults',
                                                'By making all fields public',
                                                'By running an invariant thread every second'],
                                    'question': 'How does encapsulation enforce class invariants?'},
                                   {'correct_answer': 'Package-private is accessible only within the package; '
                                                      'protected is also accessible in subclasses outside the package',
                                    'difficulty': 'Medium',
                                    'explanation': 'Protected extends package visibility to derived classes regardless '
                                                   'of package location.',
                                    'options': ['Package-private is accessible only within the package; protected is '
                                                'also accessible in subclasses outside the package',
                                                'Package-private is public everywhere; protected is private',
                                                'Protected cannot be accessed in subclasses',
                                                'They are identical in every way'],
                                    'question': 'What is the difference between default (package-private) and '
                                                'protected access in Java?'},
                                   {'correct_answer': 'Callers can modify the private object state externally, '
                                                      'violating encapsulation',
                                    'difficulty': 'Medium',
                                    'explanation': 'Exposing mutable references allows callers to bypass validation '
                                                   'and corrupt object state.',
                                    'options': ['Callers can modify the private object state externally, violating '
                                                'encapsulation',
                                                'It causes immediate NullPointerException',
                                                'It doubles garbage collection pauses',
                                                'It prevents garbage collection of the enclosing class'],
                                    'question': 'Why is returning a direct reference to a mutable private field '
                                                'considered bad practice?'},
                                   {'correct_answer': 'Return an unmodifiable view or a defensive copy of the '
                                                      'collection',
                                    'difficulty': 'Medium',
                                    'explanation': 'Defensive copying or wrapping in Collections.unmodifiableList '
                                                   'prevents external tampering.',
                                    'options': ['Return an unmodifiable view or a defensive copy of the collection',
                                                'Make the collection public',
                                                'Cast the collection to an array',
                                                'Return null'],
                                    'question': 'How do you safely return a mutable collection from an encapsulated '
                                                'getter?'},
                                   {'correct_answer': "By declaring the function as a 'friend' inside the class",
                                    'difficulty': 'Medium',
                                    'explanation': "The 'friend' keyword explicitly grants non-member functions or "
                                                   'other classes access to private members.',
                                    'options': ["By declaring the function as a 'friend' inside the class",
                                                'By casting the pointer to void*',
                                                'By placing the function in the same namespace',
                                                'Private members can never be accessed by non-members'],
                                    'question': 'In C++, how can a non-member function access the private members of a '
                                                'class?'},
                                   {'correct_answer': 'It weakens encapsulation by exposing private internals to '
                                                      'external entities',
                                    'difficulty': 'Medium',
                                    'explanation': 'Friendship couples external code tightly to private '
                                                   'representation, undermining modularity.',
                                    'options': ['It weakens encapsulation by exposing private internals to external '
                                                'entities',
                                                'It increases binary executable size by 50%',
                                                'It breaks inheritance vtables',
                                                'It slows down CPU clock speed'],
                                    'question': "What is the disadvantage of excessive use of 'friend' in C++?"},
                                   {'correct_answer': 'They provide getter/setter syntax while allowing backing fields '
                                                      'to remain private and validated',
                                    'difficulty': 'Medium',
                                    'explanation': 'Properties look like field access externally while running '
                                                   'validation logic internally.',
                                    'options': ['They provide getter/setter syntax while allowing backing fields to '
                                                'remain private and validated',
                                                'They compile into raw SQL queries',
                                                'They eliminate all memory allocations',
                                                'They convert variables into global constants'],
                                    'question': 'How do properties in C# or Python (@property) support encapsulation?'},
                                   {'correct_answer': 'Creating copies of mutable input parameters and return values '
                                                      'to isolate internal state',
                                    'difficulty': 'Medium',
                                    'explanation': 'Defensive copying ensures external modifications to passed objects '
                                                   'do not affect internal state.',
                                    'options': ['Creating copies of mutable input parameters and return values to '
                                                'isolate internal state',
                                                'Backing up classes to an external hard drive',
                                                'Encrypting data packets across the network',
                                                'Duplicating stack frames during recursion'],
                                    'question': 'What is defensive copying?'},
                                   {'correct_answer': 'Public fields allow uncontrolled modification, preventing '
                                                      'invariant checking and breaking ABI compatibility on change',
                                    'difficulty': 'Medium',
                                    'explanation': 'Direct field exposure tightly couples clients to internal '
                                                   'representation and destroys data integrity.',
                                    'options': ['Public fields allow uncontrolled modification, preventing invariant '
                                                'checking and breaking ABI compatibility on change',
                                                'Public fields cause linker errors',
                                                'Public fields cannot store numbers',
                                                'Public fields require double the memory'],
                                    'question': 'Why should instance fields almost never be declared public in '
                                                'production code?'},
                                   {'correct_answer': 'Using Java Reflection with setAccessible(true) or Unsafe, '
                                                      'unless blocked by Java 9+ Modules',
                                    'difficulty': 'Hard',
                                    'explanation': 'Reflection allows runtime introspection and can bypass access '
                                                   'checks unless strong encapsulation is enforced.',
                                    'options': ['Using Java Reflection with setAccessible(true) or Unsafe, unless '
                                                'blocked by Java 9+ Modules',
                                                'Using regular dot syntax in a separate thread',
                                                'By changing file permissions on disk',
                                                'By running the JVM with 32-bit flags'],
                                    'question': 'How can private fields in Java be accessed despite compiler '
                                                'encapsulation rules?'},
                                   {'correct_answer': 'Packages are not exported by default, preventing deep '
                                                      'reflective access to non-public types',
                                    'difficulty': 'Hard',
                                    'explanation': 'The JPMS (Java Platform Module System) prevents unauthorized '
                                                   'reflective access to unexported packages.',
                                    'options': ['Packages are not exported by default, preventing deep reflective '
                                                'access to non-public types',
                                                'All private variables are encrypted with RSA',
                                                'The JVM runs inside an isolated sandbox per class',
                                                'Reflection was removed entirely from Java'],
                                    'question': 'What mechanism in Java 9+ Module System enforces strong encapsulation '
                                                'across packages?'},
                                   {'correct_answer': 'Yes, access specifiers affect callability, not virtual table '
                                                      'overriding',
                                    'difficulty': 'Hard',
                                    'explanation': 'Overriding depends on vtable matching, whereas access checks occur '
                                                   'at the call site.',
                                    'options': ['Yes, access specifiers affect callability, not virtual table '
                                                'overriding',
                                                'No, derived classes cannot see private base functions to override '
                                                'them',
                                                'Only if the derived class is declared friend',
                                                'Only in template classes'],
                                    'question': 'In C++, can private virtual functions be overridden by derived '
                                                'classes?'},
                                   {'correct_answer': 'Public non-virtual methods wrap private or protected virtual '
                                                      'methods to control workflow invariants',
                                    'difficulty': 'Hard',
                                    'explanation': 'NVI ensures base class pre- and post-conditions are always '
                                                   'enforced before and after polymorphic calls.',
                                    'options': ['Public non-virtual methods wrap private or protected virtual methods '
                                                'to control workflow invariants',
                                                'Making all virtual functions static',
                                                'Removing all interfaces from the codebase',
                                                'Using virtual base classes exclusively'],
                                    'question': 'What is the Non-Virtual Interface (NVI) idiom in C++ and how does it '
                                                'advance encapsulation?'},
                                   {'correct_answer': 'Moving private data and methods to an opaque pointer '
                                                      'implementation class, hiding headers and decoupling ABI',
                                    'difficulty': 'Hard',
                                    'explanation': 'PIMPL eliminates private details from public headers, minimizing '
                                                   'compilation dependencies and stabilizing ABI.',
                                    'options': ['Moving private data and methods to an opaque pointer implementation '
                                                'class, hiding headers and decoupling ABI',
                                                'A tool to measure pointer arithmetic speed',
                                                'A design pattern for multi-process communication',
                                                'Using smart pointers for all variables'],
                                    'question': 'What is the PIMPL (Pointer to Implementation) idiom in C++ and its '
                                                'primary benefit for encapsulation?'},
                                   {'correct_answer': 'Inner and outer classes share a NestHost attribute defined in '
                                                      'JVM bytecode (JEP 181)',
                                    'difficulty': 'Hard',
                                    'explanation': 'Nest-Based Access Control allows nested classes in the same '
                                                   "compilation unit to access each other's private members.",
                                    'options': ['Inner and outer classes share a NestHost attribute defined in JVM '
                                                'bytecode (JEP 181)',
                                                'Inner classes run on the kernel thread',
                                                'Inner classes are always public in bytecode',
                                                'Inner class fields are copied into the outer class'],
                                    'question': 'In Java, why can an outer class access the private members of its '
                                                'nested inner class?'},
                                   {'correct_answer': 'A subclass overrides finalize() to capture a partially '
                                                      'initialized invalid object when constructor throws',
                                    'difficulty': 'Hard',
                                    'explanation': 'If a constructor throws a security exception, an overridden '
                                                   'finalize can resurrect the partially constructed instance.',
                                    'options': ['A subclass overrides finalize() to capture a partially initialized '
                                                'invalid object when constructor throws',
                                                'A hacker terminates the JVM via finalize()',
                                                'Finalizers bypass SSL certificate verification',
                                                'Finalizers overwrite disk sectors'],
                                    'question': "What is the security hazard of 'Finalizer Attacks' against partially "
                                                'constructed encapsulated objects in Java?'},
                                   {'correct_answer': 'Make the class final, or define a final empty finalize() method '
                                                      'in the class',
                                    'difficulty': 'Hard',
                                    'explanation': 'A final finalize() prevents subclasses from overriding it and '
                                                   'capturing the incomplete instance.',
                                    'options': ['Make the class final, or define a final empty finalize() method in '
                                                'the class',
                                                'Make all variables public',
                                                'Remove all constructors',
                                                'Use primitive types only'],
                                    'question': 'How can the Java class design defend against Finalizer Attacks?'},
                                   {'correct_answer': 'The compiler may reorder or insert padding bytes between access '
                                                      'specifiers or members to satisfy CPU alignment',
                                    'difficulty': 'Hard',
                                    'explanation': 'C++ allows compilers to order member sections separated by access '
                                                   'specifiers arbitrarily, subject to alignment.',
                                    'options': ['The compiler may reorder or insert padding bytes between access '
                                                'specifiers or members to satisfy CPU alignment',
                                                'Access specifiers prevent padding bytes from being added',
                                                'Encapsulated classes never have memory padding',
                                                'Padding bytes only exist in virtual classes'],
                                    'question': 'How does C++ memory alignment affect encapsulation and data member '
                                                'layout within an object?'},
                                   {'correct_answer': 'They provide transparent data-carrier semantics with immutable '
                                                      'fields, but cannot hide component names',
                                    'difficulty': 'Hard',
                                    'explanation': 'Records trade implementation hiding for clear, boilerplate-free '
                                                   'immutable data carrier contracts.',
                                    'options': ['They provide transparent data-carrier semantics with immutable '
                                                'fields, but cannot hide component names',
                                                'They consume 4x more heap memory',
                                                'They disable compiler optimizations',
                                                'They cannot be used in multithreaded applications'],
                                    'question': 'What is the trade-off of using record types in Java or readonly '
                                                'structs in C# regarding encapsulation?'}],
 'Inheritance Basics': [{'correct_answer': 'A mechanism where a derived class inherits fields and methods from a base '
                                           'class',
                         'difficulty': 'Easy',
                         'explanation': "Inheritance facilitates code reuse and establishes 'is-a' relationships.",
                         'options': ['A mechanism where a derived class inherits fields and methods from a base class',
                                     'A method of encrypting variables',
                                     'An algorithm to sort arrays',
                                     'A tool for memory garbage collection'],
                         'question': 'What is inheritance in Object-Oriented Programming?'},
                        {'correct_answer': 'extends',
                         'difficulty': 'Easy',
                         'explanation': "In Java, 'extends' specifies the parent class being derived from.",
                         'options': ['extends', 'implements', 'inherits', 'super'],
                         'question': 'Which keyword is used in Java to inherit a class?'},
                        {'correct_answer': 'The parent class whose members are inherited by another class',
                         'difficulty': 'Easy',
                         'explanation': 'A superclass provides properties and methods that subclasses can inherit and '
                                        'extend.',
                         'options': ['The parent class whose members are inherited by another class',
                                     'A class with maximum privileges in the operating system',
                                     'A class that contains only static methods',
                                     'A class instantiated without memory'],
                         'question': 'What is a superclass (or base class)?'},
                        {'correct_answer': 'A class that inherits from another class',
                         'difficulty': 'Easy',
                         'explanation': 'A subclass extends the functionality of its parent superclass.',
                         'options': ['A class that inherits from another class',
                                     'A class that cannot have methods',
                                     'A class stored in a database subfolder',
                                     'A primitive data type'],
                         'question': 'What is a subclass (or derived class)?'},
                        {'correct_answer': "An 'is-a' relationship",
                         'difficulty': 'Easy',
                         'explanation': "Inheritance represents an 'is-a' taxonomy (e.g., Dog is a Mammal).",
                         'options': ["An 'is-a' relationship",
                                     "A 'has-a' relationship",
                                     "A 'uses-a' relationship",
                                     "A 'contains-a' relationship"],
                         'question': 'What kind of relationship does inheritance model between classes?'},
                        {'correct_answer': 'super',
                         'difficulty': 'Easy',
                         'explanation': "'super' is used to refer directly to immediate parent class members and "
                                        'constructors.',
                         'options': ['super', 'this', 'base', 'parent'],
                         'question': 'Which keyword is used in Java to access members of the parent class?'},
                        {'correct_answer': 'No, private members are not directly accessible in derived classes',
                         'difficulty': 'Easy',
                         'explanation': 'Private members remain private to the defining class and cannot be directly '
                                        'named by subclasses.',
                         'options': ['No, private members are not directly accessible in derived classes',
                                     'Yes, always directly accessible',
                                     'Only if both classes are in the same directory',
                                     'Yes, using the super keyword'],
                         'question': 'Are private members of a parent class directly accessible by a subclass?'},
                        {'correct_answer': 'protected',
                         'difficulty': 'Easy',
                         'explanation': 'Protected members are accessible within the package and by subclasses.',
                         'options': ['protected', 'private', 'public', 'internal'],
                         'question': 'Which access specifier allows derived classes to access parent members while '
                                     'keeping them hidden from outside classes?'},
                        {'correct_answer': 'A class inherits from exactly one immediate base class',
                         'difficulty': 'Easy',
                         'explanation': 'In single inheritance, a derived class has only one direct parent class.',
                         'options': ['A class inherits from exactly one immediate base class',
                                     'A class has only one method',
                                     'An object can only be instantiated once',
                                     'A class that cannot be extended'],
                         'question': 'What is single inheritance?'},
                        {'correct_answer': 'No, Java does not support multiple class inheritance to avoid ambiguity',
                         'difficulty': 'Easy',
                         'explanation': 'Java forbids multiple class inheritance to prevent the Diamond Problem.',
                         'options': ['No, Java does not support multiple class inheritance to avoid ambiguity',
                                     'Yes, fully supported with classes',
                                     'Yes, up to 3 parent classes',
                                     'Only if all parent classes are final'],
                         'question': 'Does Java support multiple inheritance of classes (e.g., class C extends A, B)?'},
                        {'correct_answer': 'class Derived : public Base { ... }',
                         'difficulty': 'Medium',
                         'explanation': 'C++ uses a colon followed by access specifier (public Base) for inheritance.',
                         'options': ['class Derived : public Base { ... }',
                                     'class Derived extends Base { ... }',
                                     'class Derived inherits Base { ... }',
                                     'class Derived(Base) { ... }'],
                         'question': 'In C++, which syntax correctly inherits class Base publicly?'},
                        {'correct_answer': 'The compiler automatically inserts a call to the parameterless super() '
                                           'constructor',
                         'difficulty': 'Medium',
                         'explanation': 'If omitted, super() with zero arguments is implicitly invoked at the start of '
                                        'derived constructor.',
                         'options': ['The compiler automatically inserts a call to the parameterless super() '
                                     'constructor',
                                     'A compilation error is always raised',
                                     'The base class is never initialized',
                                     'The program crashes at runtime'],
                         'question': 'What happens if a derived class constructor does not explicitly call super() in '
                                     'Java?'},
                        {'correct_answer': 'Public and protected members of Base become private in Derived',
                         'difficulty': 'Medium',
                         'explanation': 'Private inheritance in C++ inherits implementation rather than interface, '
                                        'hiding base members from users of Derived.',
                         'options': ['Public and protected members of Base become private in Derived',
                                     'Base class members become invisible and deleted',
                                     'Derived class cannot access any Base members',
                                     'Derived class becomes an interface'],
                         'question': 'What happens in C++ if public inheritance is changed to private inheritance '
                                     '(class D : private B)?'},
                        {'correct_answer': 'No, constructors are not inherited; subclasses must define their own '
                                           'constructors',
                         'difficulty': 'Medium',
                         'explanation': 'Subclasses do not inherit constructors, though they can invoke parent '
                                        'constructors via super().',
                         'options': ['No, constructors are not inherited; subclasses must define their own '
                                     'constructors',
                                     'Yes, all constructors are automatically inherited',
                                     'Only the default constructor is inherited',
                                     'Constructors are inherited if marked public'],
                         'question': 'Can constructors be inherited directly in standard Java (prior to '
                                     'records/factories)?'},
                        {'correct_answer': 'Objects of a superclass should be replaceable with objects of a subclass '
                                           'without breaking correctness',
                         'difficulty': 'Medium',
                         'explanation': 'LSP guarantees that derived classes honor the behavioral contract of their '
                                        'base types.',
                         'options': ['Objects of a superclass should be replaceable with objects of a subclass without '
                                     'breaking correctness',
                                     'Every class must have a copy constructor',
                                     'Classes should only inherit from abstract classes',
                                     'Subclasses must duplicate base class code'],
                         'question': 'What is the Liskov Substitution Principle (LSP) in relation to inheritance?'},
                        {'correct_answer': "Inheritance is 'is-a' (white-box reuse); composition is 'has-a' (black-box "
                                           'reuse)',
                         'difficulty': 'Medium',
                         'explanation': 'Composition embeds component objects, promoting looser coupling than class '
                                        'inheritance.',
                         'options': ["Inheritance is 'is-a' (white-box reuse); composition is 'has-a' (black-box "
                                     'reuse)',
                                     'Inheritance is faster than composition at runtime',
                                     'Composition is only allowed in Python',
                                     'Inheritance cannot use interfaces'],
                         'question': 'What is the difference between inheritance and composition?'},
                        {'correct_answer': 'The subclass field shadows/hides the superclass field',
                         'difficulty': 'Medium',
                         'explanation': 'Variable shadowing hides the parent field; super.field can still access the '
                                        "parent's copy.",
                         'options': ['The subclass field shadows/hides the superclass field',
                                     'The superclass field is deleted',
                                     'A compiler syntax error is generated',
                                     'Both fields merge into an array'],
                         'question': 'What happens when a subclass declares a field with the exact same name as a '
                                     'field in its superclass?'},
                        {'correct_answer': 'class SubClass(SuperClass):',
                         'difficulty': 'Medium',
                         'explanation': 'Python specifies parent classes inside parentheses after the class name.',
                         'options': ['class SubClass(SuperClass):',
                                     'class SubClass extends SuperClass:',
                                     'class SubClass : public SuperClass:',
                                     'class SubClass implements SuperClass:'],
                         'question': 'In Python, how is single inheritance defined?'},
                        {'correct_answer': 'They create tight coupling, fragility, and difficulty in reasoning about '
                                           'state modifications across levels',
                         'difficulty': 'Medium',
                         'explanation': "Deep hierarchies lead to the 'fragile base class' problem and make "
                                        'refactoring risky.',
                         'options': ['They create tight coupling, fragility, and difficulty in reasoning about state '
                                     'modifications across levels',
                                     'They consume exponential CPU cache',
                                     'They prevent the use of garbage collection',
                                     'They are forbidden by language specifications'],
                         'question': 'Why should deep inheritance hierarchies (e.g. 7+ levels) generally be avoided?'},
                        {'correct_answer': 'Multiple derived classes inherit from a single common base class',
                         'difficulty': 'Medium',
                         'explanation': 'Hierarchical inheritance occurs when multiple subclasses branch out from one '
                                        'parent class.',
                         'options': ['Multiple derived classes inherit from a single common base class',
                                     'A single class inherits from multiple base classes',
                                     'A chain of inheritance from class A to B to C',
                                     'Inheriting without constructors'],
                         'question': 'What is hierarchical inheritance?'},
                        {'correct_answer': 'A seemingly harmless modification to a base class unintentionally breaks '
                                           'derived subclasses',
                         'difficulty': 'Hard',
                         'explanation': 'Tight coupling in inheritance causes base class changes to produce unexpected '
                                        'side-effects in subclasses.',
                         'options': ['A seemingly harmless modification to a base class unintentionally breaks derived '
                                     'subclasses',
                                     'The base class file becomes corrupted on disk',
                                     'Base classes cannot be serialized to JSON',
                                     'Memory leaks occur when base classes are freed'],
                         'question': "What is the 'Fragile Base Class' problem in object-oriented architecture?"},
                        {'correct_answer': 'The base class subobject data members are placed first, followed by '
                                           'derived class data members',
                         'difficulty': 'Hard',
                         'explanation': 'Standard layout appends derived fields directly after the base subobject '
                                        'layout in contiguous memory.',
                         'options': ['The base class subobject data members are placed first, followed by derived '
                                     'class data members',
                                     'Derived members are placed first, followed by base',
                                     'Base and derived members are stored in separate heap segments',
                                     'Base members are discarded'],
                         'question': 'In C++, how does memory layout represent a single-inherited class object?'},
                        {'correct_answer': 'An overriding method can return a subtype of the return type declared in '
                                           'the base method',
                         'difficulty': 'Hard',
                         'explanation': 'Covariant returns allow derived classes to return more specific types while '
                                        'remaining type-safe.',
                         'options': ['An overriding method can return a subtype of the return type declared in the '
                                     'base method',
                                     'An overriding method can return a completely unrelated type',
                                     'Return types must match with exact primitive byte size',
                                     'The method must return void'],
                         'question': 'What is covariance of return types in overriding inherited methods?'},
                        {'correct_answer': 'To prevent ambiguity with method overloading; parameter types must match '
                                           'exactly for an override',
                         'difficulty': 'Hard',
                         'explanation': 'Changing parameter types creates an overload rather than an override in Java.',
                         'options': ['To prevent ambiguity with method overloading; parameter types must match exactly '
                                     'for an override',
                                     'Because the JVM has no stack space',
                                     'Because parameters are immutable in Java',
                                     'To maintain backwards compatibility with C'],
                         'question': 'Why does Java prohibit contravariance of method parameters in overridden '
                                     'methods?'},
                        {'correct_answer': 'Public and protected members of B become protected members in D',
                         'difficulty': 'Hard',
                         'explanation': 'Protected inheritance prevents public callers of D from treating it as B '
                                        'while passing access to subclasses of D.',
                         'options': ['Public and protected members of B become protected members in D',
                                     'All members of B become public in D',
                                     'D cannot call any functions in B',
                                     'Only friends of B can access D'],
                         'question': "In C++, what does 'protected inheritance' (class D : protected B) mean for "
                                     'access outside?'},
                        {'correct_answer': "Class inheritance uses 'invokevirtual'; interface invocation uses "
                                           "'invokeinterface' with separate ITable lookups",
                         'difficulty': 'Hard',
                         'explanation': 'invokeinterface requires dynamic table scanning because a class can implement '
                                        'multiple interfaces in arbitrary order.',
                         'options': ["Class inheritance uses 'invokevirtual'; interface invocation uses "
                                     "'invokeinterface' with separate ITable lookups",
                                     'Interfaces generate larger binaries',
                                     'Class inheritance creates no object headers',
                                     'Interface methods are always inlined by the compiler'],
                         'question': 'What is the difference between inheriting from a class vs inheriting from an '
                                     'interface in Java bytecode?'},
                        {'correct_answer': 'It explicitly permits only a designated list of subclasses to extend the '
                                           'sealed class',
                         'difficulty': 'Hard',
                         'explanation': 'Sealed classes allow developers to restrict the hierarchy to known, '
                                        'exhaustive implementations.',
                         'options': ['It explicitly permits only a designated list of subclasses to extend the sealed '
                                     'class',
                                     'It prevents all subclasses from being instantiated',
                                     'It encrypts the bytecode with a cryptographic seal',
                                     'It allows inheritance only within a single thread'],
                         'question': "How does Java's 'sealed' class feature (introduced in Java 17) restrict "
                                     'inheritance?'},
                        {'correct_answer': 'Subclasses cannot override or hide that method',
                         'difficulty': 'Hard',
                         'explanation': 'The final modifier on a method locks its implementation against overriding.',
                         'options': ['Subclasses cannot override or hide that method',
                                     'The method can only be called once per run',
                                     'The method must return a final variable',
                                     'The method is deleted by the JIT'],
                         'question': "What happens when an inherited method is marked 'final' in Java?"},
                        {'correct_answer': 'dynamic_cast inspects runtime type descriptors in the vtable to verify the '
                                           'target type',
                         'difficulty': 'Hard',
                         'explanation': 'dynamic_cast uses type_info structures linked to polymorphic vtables to '
                                        'validate derived casts at runtime.',
                         'options': ['dynamic_cast inspects runtime type descriptors in the vtable to verify the '
                                     'target type',
                                     'static_cast does runtime safety checks on pointers',
                                     'reinterpret_cast throws std::bad_alloc on mismatch',
                                     'The OS memory manager verifies the pointer'],
                         'question': 'In C++, how does RTTI (Run-Time Type Information) verify safe downcasting in '
                                     'polymorphic inheritance?'},
                        {'correct_answer': 'Concrete base classes mix abstraction with implementation details, '
                                           'complicating testing and mocking',
                         'difficulty': 'Hard',
                         'explanation': 'Designing for inheritance requires abstract contracts; subclassing concrete '
                                        'types binds subclasses to implementation quirks.',
                         'options': ['Concrete base classes mix abstraction with implementation details, complicating '
                                     'testing and mocking',
                                     'Concrete classes cannot have constructors',
                                     'Inheritance from concrete classes is disallowed by modern compilers',
                                     'Concrete base classes require virtual inheritance'],
                         'question': "Why does the 'inherits from concrete classes' antipattern violate clean "
                                     'architecture?'}],
 'Method Overloading': [{'correct_answer': 'Defining multiple methods in the same class with the same name but '
                                           'different parameter lists',
                         'difficulty': 'Easy',
                         'explanation': 'Method overloading provides multiple variants of a method distinguished by '
                                        'argument types or counts.',
                         'options': ['Defining multiple methods in the same class with the same name but different '
                                     'parameter lists',
                                     'Redefining a base class method in a subclass with the same signature',
                                     'Calling a method recursively',
                                     'Passing methods as arguments to other methods'],
                         'question': 'What is method overloading in OOP?'},
                        {'correct_answer': 'Compile-time (Static binding / early binding)',
                         'difficulty': 'Easy',
                         'explanation': 'Overload resolution is performed statically by the compiler based on argument '
                                        'types at the call site.',
                         'options': ['Compile-time (Static binding / early binding)',
                                     'Runtime (Dynamic dispatch)',
                                     'Link-time only',
                                     'During garbage collection'],
                         'question': 'At what stage is method overloading resolved by the compiler?'},
                        {'correct_answer': 'No, methods cannot be overloaded based on return type alone',
                         'difficulty': 'Easy',
                         'explanation': 'The method signature consists of method name and parameter types, not the '
                                        'return type.',
                         'options': ['No, methods cannot be overloaded based on return type alone',
                                     'Yes, if the return types are primitives',
                                     'Yes, if one is void and the other is int',
                                     'Yes, in all modern compilers'],
                         'question': 'Can two methods in the same class be overloaded solely by differing return types '
                                     'in Java or C++?'},
                        {'correct_answer': 'By changing the number, types, or order of parameters',
                         'difficulty': 'Easy',
                         'explanation': 'Overloading requires distinct parameter lists (count, types, or sequence of '
                                        'types).',
                         'options': ['By changing the number, types, or order of parameters',
                                     'By changing the access specifier only',
                                     'By changing parameter names only',
                                     'By adding comments to the method body'],
                         'question': 'How can methods be overloaded?'},
                        {'correct_answer': 'Having multiple constructors in a class with different parameter lists',
                         'difficulty': 'Easy',
                         'explanation': 'Constructor overloading allows objects to be initialized in different ways '
                                        'with different inputs.',
                         'options': ['Having multiple constructors in a class with different parameter lists',
                                     'Calling a constructor inside a loop',
                                     'Having constructors in different namespaces',
                                     'Constructing multiple objects simultaneously'],
                         'question': 'What is constructor overloading?'},
                        {'correct_answer': 'No, defining a method with the same name replaces the previous definition',
                         'difficulty': 'Easy',
                         'explanation': 'In Python, the latest method definition overwrites earlier ones; default '
                                        'arguments or *args are used instead.',
                         'options': ['No, defining a method with the same name replaces the previous definition',
                                     'Yes, Python checks type hints at compile time',
                                     'Yes, using the @overload runtime engine',
                                     'Yes, up to 5 overloads'],
                         'question': 'Does Python natively support static method overloading by parameter types like '
                                     'Java?'},
                        {'correct_answer': 'Giving special user-defined meaning to standard operators (like +, -, *) '
                                           'for user-defined types',
                         'difficulty': 'Easy',
                         'explanation': 'Operator overloading allows classes to define custom implementations for '
                                        'operators using operator keyword.',
                         'options': ['Giving special user-defined meaning to standard operators (like +, -, *) for '
                                     'user-defined types',
                                     'Changing operator precedence in expressions',
                                     'Using mathematical operators in strings only',
                                     'Deleting operators from the compiler'],
                         'question': 'What is operator overloading in C++?'},
                        {'correct_answer': 'No, Java does not support user-defined operator overloading (except '
                                           "built-in '+' for strings)",
                         'difficulty': 'Easy',
                         'explanation': 'Java deliberately excluded user-defined operator overloading to maintain '
                                        'simplicity and readability.',
                         'options': ["No, Java does not support user-defined operator overloading (except built-in '+' "
                                     'for strings)',
                                     'Yes, fully supported via the operator keyword',
                                     'Yes, for arithmetic operators only',
                                     'Yes, when implementing the Comparable interface'],
                         'question': 'Does Java support user-defined operator overloading?'},
                        {'correct_answer': 'void print(String s)',
                         'difficulty': 'Easy',
                         'explanation': 'print(String s) has a different parameter type, creating a valid overload.',
                         'options': ['void print(String s)',
                                     'int print(int a)',
                                     'private void print(int a)',
                                     'void print(int b)'],
                         'question': "Which of the following method signatures is a valid overload of 'void print(int "
                                     "a)'?"},
                        {'correct_answer': 'It improves code readability by using consistent naming for logically '
                                           'similar operations with different inputs',
                         'difficulty': 'Easy',
                         'explanation': 'Overloading enables intuitive APIs where the method name reflects the '
                                        'high-level intent across diverse arguments.',
                         'options': ['It improves code readability by using consistent naming for logically similar '
                                     'operations with different inputs',
                                     'It makes methods run twice as fast',
                                     'It reduces binary executable size',
                                     'It disables the need for type checking'],
                         'question': 'Why is method overloading beneficial for API design?'},
                        {'correct_answer': 'The compiler selects the method with the narrowest matching conversion '
                                           '(widening primitive conversion)',
                         'difficulty': 'Medium',
                         'explanation': 'Compilers apply primitive widening rules when an exact match is not '
                                        'available.',
                         'options': ['The compiler selects the method with the narrowest matching conversion (widening '
                                     'primitive conversion)',
                                     'A compile-time ambiguity error is always thrown',
                                     'The method taking int is converted to string',
                                     'A NullPointerException is raised'],
                         'question': 'What happens when calling an overloaded method with an argument that matches '
                                     'through automatic type promotion (e.g., int promoted to long)?'},
                        {'correct_answer': 'test(int a), because exact primitive matching precedes autoboxing',
                         'difficulty': 'Medium',
                         'explanation': 'Java overload resolution prioritizes exact primitive matches over autoboxing.',
                         'options': ['test(int a), because exact primitive matching precedes autoboxing',
                                     'test(Integer a), because objects have priority',
                                     'The call is ambiguous and fails to compile',
                                     'Both methods execute sequentially'],
                         'question': "In Java, if class C has 'void test(int a)' and 'void test(Integer a)', which "
                                     'method executes when calling test(5)?'},
                        {'correct_answer': 'Variable-length arguments (...); it has the lowest priority during '
                                           'overload resolution',
                         'difficulty': 'Medium',
                         'explanation': 'Varargs is evaluated only if neither exact matches nor boxing/widening '
                                        'matches succeed.',
                         'options': ['Variable-length arguments (...); it has the lowest priority during overload '
                                     'resolution',
                                     'A tool to create global variables; highest priority',
                                     'A compiler directive; runs before constructors',
                                     'An array that cannot be resized'],
                         'question': 'What is varargs in Java, and how does it rank in overload resolution '
                                     'precedence?'},
                        {'correct_answer': 'Yes, if argument matching rules and namespaces allow it',
                         'difficulty': 'Medium',
                         'explanation': 'Free functions and member functions can share names in different scopes, '
                                        'subject to lookup rules.',
                         'options': ['Yes, if argument matching rules and namespaces allow it',
                                     'No, non-member functions can never have the same name as member functions',
                                     'Only if marked static',
                                     'Only if declared in the main function'],
                         'question': 'In C++, can non-member functions be overloaded alongside member functions?'},
                        {'correct_answer': 'Scope resolution (::), Member access (.), Pointer-to-member (.*), and '
                                           'Ternary (?:)',
                         'difficulty': 'Medium',
                         'explanation': 'C++ explicitly forbids overloading ::, ., .*, and ?: to preserve syntactic '
                                        'integrity.',
                         'options': ['Scope resolution (::), Member access (.), Pointer-to-member (.*), and Ternary '
                                     '(?:)',
                                     'Addition (+) and Subtraction (-)',
                                     'Assignment (=) and Subscript ([])',
                                     'Function call (()) and Arrow (->)'],
                         'question': 'In C++, which operators CANNOT be overloaded?'},
                        {'correct_answer': 'A derived class method hides all overloads of that name in the base class '
                                           "unless brought in via 'using Base::method'",
                         'difficulty': 'Medium',
                         'explanation': 'In C++, declaring a function in a derived scope hides all functions with that '
                                        'name in the outer base scope.',
                         'options': ['A derived class method hides all overloads of that name in the base class unless '
                                     "brought in via 'using Base::method'",
                                     'The compiler deletes base class method symbols',
                                     'Method names are encrypted in the symbol table',
                                     'Private methods become public automatically'],
                         'question': "What is 'Name Hiding' when overloading methods across base and derived classes "
                                     'in C++?'},
                        {'correct_answer': "Using the 'functools.singledispatch' decorator for type-based dispatch",
                         'difficulty': 'Medium',
                         'explanation': 'functools.singledispatch transforms functions into single-dispatch generic '
                                        'functions based on first argument type.',
                         'options': ["Using the 'functools.singledispatch' decorator for type-based dispatch",
                                     'By writing multiple functions with identical names',
                                     "By importing the 'overload' C extension",
                                     'By disabling dynamic typing'],
                         'question': 'How can Python simulate method overloading effectively using the standard '
                                     'library?'},
                        {'correct_answer': 'When the compiler finds two or more equally specific matching overloaded '
                                           'methods for given arguments',
                         'difficulty': 'Medium',
                         'explanation': 'Ambiguity occurs when conversions for multiple overloaded methods are equally '
                                        'viable without a most specific match.',
                         'options': ['When the compiler finds two or more equally specific matching overloaded methods '
                                     'for given arguments',
                                     'When a method name contains spelling errors',
                                     'When a method has too many lines of code',
                                     'When return types are void'],
                         'question': 'What is an ambiguous method call error during compilation?'},
                        {'correct_answer': "Yes, 'const' qualifies the implicit 'this' pointer, forming a distinct "
                                           'signature',
                         'difficulty': 'Medium',
                         'explanation': "Const-qualification modifies the 'this' parameter type (const Class* vs "
                                        'Class*), allowing valid overloading.',
                         'options': ["Yes, 'const' qualifies the implicit 'this' pointer, forming a distinct signature",
                                     'No, const is ignored in method signatures',
                                     'Only if they return different types',
                                     'Only in template structs'],
                         'question': "In C++, can member functions be overloaded based on 'const' qualifiers (e.g., "
                                     'void show() vs void show() const)?'},
                        {'correct_answer': 'Because after type erasure at compile time, both signatures become '
                                           'identical (List), causing conflict',
                         'difficulty': 'Medium',
                         'explanation': 'Both methods erase to the same raw type descriptor in bytecode, producing an '
                                        'identical signature.',
                         'options': ['Because after type erasure at compile time, both signatures become identical '
                                     '(List), causing conflict',
                                     'Because generics do not work with lists',
                                     'Because List is a final class',
                                     'Because Java 5 removed generics'],
                         'question': 'Why does Java prohibit overloading a method where the only difference is generic '
                                     'type parameters after type erasure (e.g. void process(List<String>) vs void '
                                     'process(List<Integer>))?'},
                        {'correct_answer': 'The compiler encodes the method name, parameter types, and namespaces into '
                                           'a unique linker symbol',
                         'difficulty': 'Hard',
                         'explanation': 'Name mangling decorates function names with parameter type information to '
                                        'create unique linker symbols.',
                         'options': ['The compiler encodes the method name, parameter types, and namespaces into a '
                                     'unique linker symbol',
                                     'It assigns a random 128-bit UUID to each method',
                                     'It keeps an index table in the operating system registry',
                                     'It converts all method calls into switch statements'],
                         'question': 'How does C++ perform name mangling to implement static method overloading in '
                                     'compiled object files?'},
                        {'correct_answer': 'Unqualified function calls look up candidates in the namespaces of the '
                                           'function argument types',
                         'difficulty': 'Hard',
                         'explanation': 'ADL expands overload candidate search to include namespaces where argument '
                                        'types are declared.',
                         'options': ['Unqualified function calls look up candidates in the namespaces of the function '
                                     'argument types',
                                     'Searching only inside the current class body',
                                     'Calling functions over a TCP socket',
                                     'Resolving method calls via the kernel table'],
                         'question': 'What is Argument-Dependent Lookup (ADL / Koenig Lookup) in C++ during overload '
                                     'resolution?'},
                        {'correct_answer': 'If substituting a template parameter causes an invalid type/expression, '
                                           'the candidate is discarded rather than failing compilation',
                         'difficulty': 'Hard',
                         'explanation': 'SFINAE allows template overloads to be selectively enabled or disabled based '
                                        'on type traits.',
                         'options': ['If substituting a template parameter causes an invalid type/expression, the '
                                     'candidate is discarded rather than failing compilation',
                                     'Compiler crashes are caught by try/catch blocks',
                                     'All template errors are suppressed at runtime',
                                     'Templates are only compiled when run'],
                         'question': 'In C++ template metaprogramming, what is SFINAE (Substitution Failure Is Not An '
                                     'Error) in overload resolution?'},
                        {'correct_answer': 'Phase 1: subtyping without boxing/varargs; Phase 2: subtyping with boxing; '
                                           'Phase 3: varargs',
                         'difficulty': 'Hard',
                         'explanation': 'Java checks without conversions first, then allows boxing/unboxing, and only '
                                        'considers varargs last.',
                         'options': ['Phase 1: subtyping without boxing/varargs; Phase 2: subtyping with boxing; Phase '
                                     '3: varargs',
                                     'Phase 1: names; Phase 2: return types; Phase 3: access modifiers',
                                     'Phase 1: JIT profiling; Phase 2: inlining; Phase 3: bytecode generation',
                                     'Phase 1: file scan; Phase 2: syntax parse; Phase 3: link'],
                         'question': "How does Java's three-phase overload resolution process operate (JLS 15.12.2)?"},
                        {'correct_answer': 'Overloads that constrain invocation based on whether the calling object is '
                                           'an lvalue (&) or rvalue (&&)',
                         'difficulty': 'Hard',
                         'explanation': 'Ref-qualifiers enable optimizing operations by distinguishing temporary '
                                        '(rvalue) instances from named (lvalue) ones.',
                         'options': ['Overloads that constrain invocation based on whether the calling object is an '
                                     'lvalue (&) or rvalue (&&)',
                                     'Functions that accept pointer references only',
                                     'Functions that cannot throw exceptions',
                                     'Functions compiled with fast-call calling convention'],
                         'question': 'In C++, what are ref-qualified member functions (e.g., void move() && vs void '
                                     'copy() &)?'},
                        {'correct_answer': 'If every parameter of M1 can be passed to M2 without conversion, M1 is '
                                           'more specific; fails if two methods cross-subsume',
                         'difficulty': 'Hard',
                         'explanation': 'When multiple applicable methods exist without one being strictly more '
                                        'specific than all others, ambiguity occurs.',
                         'options': ['If every parameter of M1 can be passed to M2 without conversion, M1 is more '
                                     'specific; fails if two methods cross-subsume',
                                     'The method with the shortest name is chosen; fails if names are equal',
                                     'The method declared first in source code wins',
                                     'The method with the fewest lines of code is chosen'],
                         'question': "What is the 'Most Specific Method' rule in Java overload resolution, and when "
                                     'does it fail?'},
                        {'correct_answer': "Concepts provide clean constraint syntax via 'requires' clauses and clear "
                                           'compiler diagnostics on overload mismatch',
                         'difficulty': 'Hard',
                         'explanation': 'Concepts constrain template overloads with explicit, readable predicates, '
                                        'subsuming complex SFINAE enable_if tricks.',
                         'options': ["Concepts provide clean constraint syntax via 'requires' clauses and clear "
                                     'compiler diagnostics on overload mismatch',
                                     'Concepts remove the need for compilers',
                                     'Concepts convert all overloads into virtual functions',
                                     'Concepts make functions run on the GPU'],
                         'question': 'How do C++20 Concepts enhance method overloading over traditional SFINAE?'},
                        {'correct_answer': 'The non-template function is preferred over the function template '
                                           'specialization',
                         'difficulty': 'Hard',
                         'explanation': 'When both a non-template and a template offer an exact match, C++ standard '
                                        'gives preference to the non-template function.',
                         'options': ['The non-template function is preferred over the function template specialization',
                                     'The template specialization is always chosen',
                                     'The compiler throws a duplicate symbol error',
                                     'The compiler invokes both in undefined order'],
                         'question': 'In C++, what happens when a function template overload and a non-template '
                                     'function have identical signatures?'},
                        {'correct_answer': 'invokestatic / invokespecial',
                         'difficulty': 'Hard',
                         'explanation': 'Static methods use invokestatic, while private/constructor methods use '
                                        'invokespecial (non-virtual dispatch).',
                         'options': ['invokestatic / invokespecial',
                                     'invokedynamic',
                                     'invokeinterface',
                                     'invokevirtual'],
                         'question': 'What is the JVM instruction used to invoke statically overloaded or non-virtual '
                                     'methods?'},
                        {'correct_answer': 'It destroys the built-in sequencing guarantee (evaluating left-to-right) '
                                           'and breaks comma expressions',
                         'difficulty': 'Hard',
                         'explanation': 'User-defined operator, evaluates as a function call, losing the fundamental '
                                        'sequence point property of the built-in comma.',
                         'options': ['It destroys the built-in sequencing guarantee (evaluating left-to-right) and '
                                     'breaks comma expressions',
                                     'It deletes all variables separated by commas',
                                     'It changes the syntax of function argument lists',
                                     'It forces all commas to be semicolons'],
                         'question': 'Why can overloading the comma operator (,) in C++ lead to dangerous and '
                                     'unintuitive bugs?'}],
 'Method Overriding and Dynamic Dispatch': [{'correct_answer': 'A subclass providing a specific implementation of a '
                                                               'method already defined in its superclass',
                                             'difficulty': 'Easy',
                                             'explanation': 'Method overriding replaces base class behavior with '
                                                            'subclass-specific behavior for the same signature.',
                                             'options': ['A subclass providing a specific implementation of a method '
                                                         'already defined in its superclass',
                                                         'Defining multiple methods with the same name in the same '
                                                         'class',
                                                         'Hiding fields in a parent class',
                                                         'Calling a method using reflection'],
                                             'question': 'What is method overriding in OOP?'},
                                            {'correct_answer': '@Override',
                                             'difficulty': 'Easy',
                                             'explanation': 'The @Override annotation asks the compiler to verify that '
                                                            'the method correctly overrides a superclass method.',
                                             'options': ['@Override', '@Overload', '@Inherit', '@Virtual'],
                                             'question': 'What annotation is used in Java to indicate that a method is '
                                                         'intended to override a superclass method?'},
                                            {'correct_answer': 'Runtime (Dynamic binding / late binding)',
                                             'difficulty': 'Easy',
                                             'explanation': 'Overriding uses dynamic dispatch to determine the target '
                                                            'method based on the actual runtime object type.',
                                             'options': ['Runtime (Dynamic binding / late binding)',
                                                         'Compile-time (Static binding)',
                                                         'Pre-processing time',
                                                         'Packaging time'],
                                             'question': 'At what stage is method overriding resolved during program '
                                                         'execution?'},
                                            {'correct_answer': 'virtual',
                                             'difficulty': 'Easy',
                                             'explanation': "Declaring a method 'virtual' in C++ signals the compiler "
                                                            'to use vtable dispatch at runtime.',
                                             'options': ['virtual', 'override', 'dynamic', 'abstract'],
                                             'question': 'Which keyword in C++ is required in the base class to enable '
                                                         'method overriding with dynamic dispatch?'},
                                            {'correct_answer': 'No, static methods are bonded at compile-time and can '
                                                               'only be shadowed/hidden',
                                             'difficulty': 'Easy',
                                             'explanation': 'Static methods belong to the class type, not instance '
                                                            'vtables, so dynamic dispatch does not apply.',
                                             'options': ['No, static methods are bonded at compile-time and can only '
                                                         'be shadowed/hidden',
                                                         'Yes, static methods override dynamically like instance '
                                                         'methods',
                                                         'Only if marked with @Override',
                                                         'Only in abstract classes'],
                                             'question': 'Can static methods be overridden in Java?'},
                                            {'correct_answer': 'No, private methods are not visible to subclasses and '
                                                               'cannot be overridden',
                                             'difficulty': 'Easy',
                                             'explanation': 'Subclasses cannot see private base methods; re-declaring '
                                                            'the same name simply creates an independent method.',
                                             'options': ['No, private methods are not visible to subclasses and cannot '
                                                         'be overridden',
                                                         'Yes, private methods are always overridden',
                                                         'Yes, if the subclass is public',
                                                         'Only if both classes share the same package'],
                                             'question': 'Can private methods be overridden in a subclass?'},
                                            {'correct_answer': "The subclass's overridden implementation executes",
                                             'difficulty': 'Easy',
                                             'explanation': 'Polymorphism ensures the runtime type determines the '
                                                            'method implementation executed.',
                                             'options': ["The subclass's overridden implementation executes",
                                                         "The superclass's implementation executes",
                                                         'A ClassCastException is thrown',
                                                         'The program halts with an error'],
                                             'question': 'What happens when an overridden method is called on a '
                                                         'superclass reference holding a subclass object in Java?'},
                                            {'correct_answer': 'No, an overriding method cannot reduce the visibility '
                                                               'of the inherited method',
                                             'difficulty': 'Easy',
                                             'explanation': 'Java enforces LSP: derived classes cannot restrict access '
                                                            '(e.g. public cannot become protected or private).',
                                             'options': ['No, an overriding method cannot reduce the visibility of the '
                                                         'inherited method',
                                                         'Yes, public methods can be made private in subclasses',
                                                         'Yes, protected methods can be made private',
                                                         'Access modifiers must always be ignored in overriding'],
                                             'question': 'Can an overriding method in Java have a more restrictive '
                                                         'access modifier than the superclass method?'},
                                            {'correct_answer': 'It prevents the method from being overridden by any '
                                                               'subclass',
                                             'difficulty': 'Easy',
                                             'explanation': 'Marking a method final forbids subclasses from altering '
                                                            'its implementation.',
                                             'options': ['It prevents the method from being overridden by any subclass',
                                                         'It makes the method execute asynchronously',
                                                         'It forces the method to be static',
                                                         'It deletes the method from memory after execution'],
                                             'question': "What is the purpose of the 'final' keyword on a method in "
                                                         'Java?'},
                                            {'correct_answer': 'Yes, Python resolves all method lookups dynamically at '
                                                               'runtime',
                                             'difficulty': 'Easy',
                                             'explanation': 'Python is inherently dynamic; all attribute and method '
                                                            'accesses use late binding.',
                                             'options': ['Yes, Python resolves all method lookups dynamically at '
                                                         'runtime',
                                                         'No, methods must be decorated with @virtual',
                                                         'Only methods starting with test_',
                                                         'Only methods inside dataclasses'],
                                             'question': 'In Python, are all methods virtual by default?'},
                                            {'correct_answer': 'Virtual Method Table (vtable)',
                                             'difficulty': 'Medium',
                                             'explanation': 'A vtable contains pointers to the virtual functions for '
                                                            'each class, resolved at runtime via vptr.',
                                             'options': ['Virtual Method Table (vtable)',
                                                         'Hash map stored on disk',
                                                         'Linked list of function pointers',
                                                         'Binary search tree of symbols'],
                                             'question': 'What data structure is utilized under the hood in C++ to '
                                                         'achieve dynamic dispatch?'},
                                            {'correct_answer': 'It points to the vtable containing the function '
                                                               "pointers for that object's concrete class",
                                             'difficulty': 'Medium',
                                             'explanation': 'Every polymorphic object carries a hidden vptr pointing '
                                                            "to its class's virtual table.",
                                             'options': ['It points to the vtable containing the function pointers for '
                                                         "that object's concrete class",
                                                         "It tracks the object's reference count",
                                                         'It points to the next object on the heap',
                                                         "It stores the object's hash code"],
                                             'question': "What is the purpose of the 'vptr' (virtual table pointer) in "
                                                         'C++ polymorphic objects?'},
                                            {'correct_answer': 'It tells the compiler to verify that the function '
                                                               'actually overrides a virtual base function',
                                             'difficulty': 'Medium',
                                             'explanation': "The 'override' identifier prevents subtle bugs where "
                                                            'slight signature mismatches fail to override base '
                                                            'methods.',
                                             'options': ['It tells the compiler to verify that the function actually '
                                                         'overrides a virtual base function',
                                                         'It creates a new virtual table entry',
                                                         'It makes the function run faster',
                                                         'It converts the function to a lambda'],
                                             'question': "In C++11, what is the role of the 'override' specifier on a "
                                                         'derived class member function?'},
                                            {'correct_answer': 'No, an overriding method can only declare narrower or '
                                                               'fewer checked exceptions',
                                             'difficulty': 'Medium',
                                             'explanation': 'Subclasses cannot broaden checked exceptions because '
                                                            'callers catching superclass exceptions would be '
                                                            'surprised.',
                                             'options': ['No, an overriding method can only declare narrower or fewer '
                                                         'checked exceptions',
                                                         'Yes, any checked exception can be added',
                                                         'Yes, Exception and Throwable are always permitted',
                                                         'Checked exceptions are ignored in overriding'],
                                             'question': 'Can an overriding method declare checked exceptions that are '
                                                         'broader than those declared by the superclass method in '
                                                         'Java?'},
                                            {'correct_answer': 'It explicitly calls the superclass implementation of '
                                                               'that method, bypassing dynamic dispatch',
                                             'difficulty': 'Medium',
                                             'explanation': 'super.method() explicitly targets the parent '
                                                            'implementation, avoiding infinite recursion.',
                                             'options': ['It explicitly calls the superclass implementation of that '
                                                         'method, bypassing dynamic dispatch',
                                                         'It restarts the method from the beginning',
                                                         'It calls all implementations in all subclasses',
                                                         'It throws an UnsupportedOperationException'],
                                             'question': "What happens when invoking a method via 'super.methodName()' "
                                                         'in an overridden method?'},
                                            {'correct_answer': 'The overriding method returns a narrower (more '
                                                               'derived) type than the method in the superclass',
                                             'difficulty': 'Medium',
                                             'explanation': 'Covariant returns allow derived methods to provide more '
                                                            'specific return types without breaking polymorphism.',
                                             'options': ['The overriding method returns a narrower (more derived) type '
                                                         'than the method in the superclass',
                                                         'The overriding method returns void instead of an object',
                                                         'The method returns an array of numbers',
                                                         'Return types cannot be modified in any language'],
                                             'question': 'What is covariant return type in method overriding?'},
                                            {'correct_answer': 'Yes, all non-static, non-private, non-final methods in '
                                                               'Java are virtual by default',
                                             'difficulty': 'Medium',
                                             'explanation': 'Unlike C++, Java instance methods are polymorphic/virtual '
                                                            'by default unless declared static, private, or final.',
                                             'options': ['Yes, all non-static, non-private, non-final methods in Java '
                                                         'are virtual by default',
                                                         'No, methods must be declared with the virtual keyword',
                                                         'Only abstract methods are virtual',
                                                         'Only methods in interfaces are virtual'],
                                             'question': 'In Java, are methods virtual by default?'},
                                            {'correct_answer': 'Invoking a pure virtual function where no '
                                                               'implementation exists, typically during '
                                                               'construction/destruction',
                                             'difficulty': 'Medium',
                                             'explanation': 'If base constructors call a pure virtual function before '
                                                            'derived vtables are set up, this fatal error occurs.',
                                             'options': ['Invoking a pure virtual function where no implementation '
                                                         'exists, typically during construction/destruction',
                                                         'Calling a function with null arguments',
                                                         'A stack overflow caused by recursion',
                                                         'A failure to allocate heap memory'],
                                             'question': 'What is pure virtual function call runtime error in C++?'},
                                            {'correct_answer': 'Monomorphic sites always dispatch to one concrete '
                                                               'class; polymorphic sites encounter multiple class '
                                                               'implementations',
                                             'difficulty': 'Medium',
                                             'explanation': 'JIT compilers inline monomorphic calls directly, '
                                                            'bypassing vtable lookups for peak performance.',
                                             'options': ['Monomorphic sites always dispatch to one concrete class; '
                                                         'polymorphic sites encounter multiple class implementations',
                                                         'Monomorphic means single-threaded; polymorphic means '
                                                         'multi-threaded',
                                                         'Monomorphic calls return int; polymorphic return objects',
                                                         'Monomorphic uses vtable; polymorphic does not'],
                                             'question': 'What is monomorphic vs polymorphic call site in modern JIT '
                                                         'compilers?'},
                                            {'correct_answer': 'It caches the target method address of recent receiver '
                                                               'classes directly at the call site',
                                             'difficulty': 'Medium',
                                             'explanation': 'Inline caching avoids expensive vtable or hash lookups by '
                                                            'remembering the last observed class and target address.',
                                             'options': ['It caches the target method address of recent receiver '
                                                         'classes directly at the call site',
                                                         'It replaces RAM with CPU cache memory',
                                                         'It pre-compiles all possible classes at boot time',
                                                         'It disables dynamic dispatch across the VM'],
                                             'question': 'How does inline caching (IC) optimize dynamic dispatch in '
                                                         'VMs like V8 or HotSpot?'},
                                            {'correct_answer': 'The compiler analyzes the class hierarchy (CHA) to '
                                                               'prove only one target exists and replaces indirect '
                                                               'calls with direct calls/inlining',
                                             'difficulty': 'Hard',
                                             'explanation': 'Class Hierarchy Analysis (CHA) allows compilers to '
                                                            'eliminate vtable indirection when no subclasses override '
                                                            'the target.',
                                             'options': ['The compiler analyzes the class hierarchy (CHA) to prove '
                                                         'only one target exists and replaces indirect calls with '
                                                         'direct calls/inlining',
                                                         'It removes virtual functions from the source code',
                                                         'It moves methods into the CPU instruction cache',
                                                         'It converts polymorphic calls into recursive loops'],
                                             'question': 'How does devirtualization optimize virtual method calls in '
                                                         'optimizing compilers (like LLVM / HotSpot)?'},
                                            {'correct_answer': 'invokevirtual (standard class virtual dispatch), '
                                                               'invokeinterface (interface dispatch), invokespecial '
                                                               '(direct super/private), invokestatic (static)',
                                             'difficulty': 'Hard',
                                             'explanation': 'The JVM provides distinct opcodes tailored for static, '
                                                            'direct, virtual table, and interface dispatch mechanisms.',
                                             'options': ['invokevirtual (standard class virtual dispatch), '
                                                         'invokeinterface (interface dispatch), invokespecial (direct '
                                                         'super/private), invokestatic (static)',
                                                         'invokeall, invokenone, invoketemp',
                                                         'call, jump, branch, ret',
                                                         'load, store, push, pop'],
                                             'question': 'What are the JVM bytecode instructions used for method '
                                                         'invocation and their roles in dynamic dispatch?'},
                                            {'correct_answer': 'Because interface methods can occupy different slot '
                                                               'indices in the vtables of different implementing '
                                                               'classes',
                                             'difficulty': 'Hard',
                                             'explanation': 'Unlike single-inheritance vtables with fixed offsets, '
                                                            'interface tables (itables) require searching or stub '
                                                            'tables.',
                                             'options': ['Because interface methods can occupy different slot indices '
                                                         'in the vtables of different implementing classes',
                                                         'Because interface methods are encrypted',
                                                         'Because interfaces require internet access',
                                                         'Because interfaces cannot be compiled by JIT'],
                                             'question': 'Why is invokeinterface historically slower than '
                                                         'invokevirtual in the HotSpot JVM?'},
                                            {'correct_answer': 'Offset-to-top, RTTI pointer, followed by function '
                                                               'pointers for virtual methods in declaration order',
                                             'difficulty': 'Hard',
                                             'explanation': 'The standard vtable layout places offset-to-top and RTTI '
                                                            'metadata right before the array of virtual function '
                                                            'pointers.',
                                             'options': ['Offset-to-top, RTTI pointer, followed by function pointers '
                                                         'for virtual methods in declaration order',
                                                         'Function code strings, author info, hash table',
                                                         'List of class member variables, followed by locks',
                                                         'A binary search tree of function names'],
                                             'question': 'How does the Itanium C++ ABI lay out a virtual method table '
                                                         '(vtable)?'},
                                            {'correct_answer': 'JIT inlines a virtual method assuming the receiver is '
                                                               'monomorphic, inserting a guard check that deoptimizes '
                                                               'if a new subclass loads',
                                             'difficulty': 'Hard',
                                             'explanation': 'Speculative inlining achieves C-like speed; if class '
                                                            'loading invalidates the assumption, the VM falls back to '
                                                            'interpreter.',
                                             'options': ['JIT inlines a virtual method assuming the receiver is '
                                                         'monomorphic, inserting a guard check that deoptimizes if a '
                                                         'new subclass loads',
                                                         'JIT compiles methods before they are written',
                                                         'The JVM deletes unused classes from disk',
                                                         'The CPU predicts branches without instructions'],
                                             'question': 'What is speculative inlining with deoptimization in Java '
                                                         'HotSpot VM?'},
                                            {'correct_answer': 'Multiple dispatch selects method implementation based '
                                                               'on runtime types of multiple arguments, not just the '
                                                               'receiver',
                                             'difficulty': 'Hard',
                                             'explanation': 'Standard OOP dispatches dynamically only on the receiver '
                                                            "('this'); multimethods dispatch on all participating "
                                                            'argument types.',
                                             'options': ['Multiple dispatch selects method implementation based on '
                                                         'runtime types of multiple arguments, not just the receiver',
                                                         'Calling multiple methods at once on different threads',
                                                         'Writing methods with multiple return types',
                                                         'Overriding methods across multiple files'],
                                             'question': 'What is multiple dispatch (multimethods) and how does it '
                                                         'contrast with standard OOP single dispatch?'},
                                            {'correct_answer': 'Using the Visitor design pattern, where elements '
                                                               'accept visitors and pass themselves to visit methods',
                                             'difficulty': 'Hard',
                                             'explanation': 'The Visitor pattern chains two single-dispatch calls '
                                                            '(element.accept(v) -> visitor.visit(this)) to simulate '
                                                            'double dispatch.',
                                             'options': ['Using the Visitor design pattern, where elements accept '
                                                         'visitors and pass themselves to visit methods',
                                                         'Using nested while loops',
                                                         'Using multithreaded queues',
                                                         'Using global pointer arrays'],
                                             'question': 'How is double dispatch commonly implemented in '
                                                         'single-dispatch languages like Java and C++?'},
                                            {'correct_answer': 'One extra memory dereference (vptr -> vtable -> method '
                                                               'pointer) and inhibition of compiler inlining',
                                             'difficulty': 'Hard',
                                             'explanation': 'The primary cost of virtual dispatch is not the pointer '
                                                            'dereference, but preventing the compiler from inlining.',
                                             'options': ['One extra memory dereference (vptr -> vtable -> method '
                                                         'pointer) and inhibition of compiler inlining',
                                                         '1000x slower execution',
                                                         'Consumes 10MB of heap per invocation',
                                                         'Causes a thread context switch'],
                                             'question': 'What is the performance overhead of a virtual method call '
                                                         'compared to a direct non-virtual function call in C++?'},
                                            {'correct_answer': 'The vtable contains a pointer to the complete object '
                                                               'destructor or deleting destructor to correctly free '
                                                               'memory',
                                             'difficulty': 'Hard',
                                             'explanation': 'Virtual destructors have vtable entries (including '
                                                            'deleting destructors that call operator delete after '
                                                            'destruction).',
                                             'options': ['The vtable contains a pointer to the complete object '
                                                         'destructor or deleting destructor to correctly free memory',
                                                         "Destructors don't use vtables; they are static",
                                                         'It points to the malloc memory header',
                                                         'It invokes the operating system process terminator'],
                                             'question': 'In C++, what is a virtual destructor table slot and why does '
                                                         'deleting through a base pointer require it?'},
                                            {'correct_answer': 'It decouples method call sites from bytecode types, '
                                                               'binding via user-defined Bootstrap Methods (BSM) and '
                                                               'MethodHandles',
                                             'difficulty': 'Hard',
                                             'explanation': 'invokedynamic defers call-site linkage to runtime '
                                                            'bootstrap methods, providing ultra-fast dynamic dispatch.',
                                             'options': ['It decouples method call sites from bytecode types, binding '
                                                         'via user-defined Bootstrap Methods (BSM) and MethodHandles',
                                                         'It executes code without JVM validation',
                                                         'It converts Java bytecode into raw x86 machine code directly',
                                                         'It bypasses all garbage collection rules'],
                                             'question': "How does Java 7's 'invokedynamic' instruction support "
                                                         'dynamically typed languages and polymorphic lambdas?'}],
 'Multilevel and Multiple Inheritance': [{'correct_answer': 'A class inherits from a derived class, forming an '
                                                            'inheritance chain (A -> B -> C)',
                                          'difficulty': 'Easy',
                                          'explanation': 'In multilevel inheritance, a subclass acts as the superclass '
                                                         'for another class.',
                                          'options': ['A class inherits from a derived class, forming an inheritance '
                                                      'chain (A -> B -> C)',
                                                      'A class inheriting from multiple classes simultaneously',
                                                      'A class with multiple constructors',
                                                      'A class containing multiple arrays'],
                                          'question': 'What is multilevel inheritance?'},
                                         {'correct_answer': 'A single derived class inheriting directly from more than '
                                                            'one base class',
                                          'difficulty': 'Easy',
                                          'explanation': 'Multiple inheritance allows a child class to have two or '
                                                         'more parent classes.',
                                          'options': ['A single derived class inheriting directly from more than one '
                                                      'base class',
                                                      'A class with multiple methods',
                                                      'An object instantiated across multiple processes',
                                                      'A file containing multiple class declarations'],
                                          'question': 'What is multiple inheritance?'},
                                         {'correct_answer': 'C++',
                                          'difficulty': 'Easy',
                                          'explanation': 'C++ allows a class to inherit from multiple base classes '
                                                         'directly.',
                                          'options': ['C++',
                                                      'Java (for classes)',
                                                      'C# (for classes)',
                                                      'PHP (for classes)'],
                                          'question': 'Which programming language natively supports multiple class '
                                                      'inheritance?'},
                                         {'correct_answer': 'By implementing multiple interfaces',
                                          'difficulty': 'Easy',
                                          'explanation': 'Java permits implementing any number of interfaces while '
                                                         'allowing only one parent class.',
                                          'options': ['By implementing multiple interfaces',
                                                      'By using multiple extends keywords',
                                                      'By declaring classes static',
                                                      'By nesting classes inside functions'],
                                          'question': 'How does Java achieve multiple inheritance of type and '
                                                      'behavior?'},
                                         {'correct_answer': 'The Diamond Problem',
                                          'difficulty': 'Easy',
                                          'explanation': 'The Diamond Problem occurs when two parent classes inherit '
                                                         'from the same grandparent, causing duplicate or ambiguous '
                                                         'base members.',
                                          'options': ['The Diamond Problem',
                                                      'The Binary Tree Dilemma',
                                                      'The Circular Reference Deadlock',
                                                      'The Stack Overflow Paradox'],
                                          'question': 'What classic dilemma arises from multiple inheritance when two '
                                                      'parent classes share a common ancestor?'},
                                         {'correct_answer': 'Yes, class C inherits accessible members from both B and '
                                                            'A',
                                          'difficulty': 'Easy',
                                          'explanation': 'Inheritance is transitive: descendants inherit all '
                                                         'accessible members along the ancestry chain.',
                                          'options': ['Yes, class C inherits accessible members from both B and A',
                                                      'No, C only inherits from B',
                                                      'Only if A has no constructors',
                                                      'Only static members are passed down'],
                                          'question': 'In multilevel inheritance (A -> B -> C), does class C inherit '
                                                      'members of class A?'},
                                         {'correct_answer': "A's constructor, then B's constructor, then C's "
                                                            'constructor',
                                          'difficulty': 'Easy',
                                          'explanation': 'Construction proceeds from the root base class down to the '
                                                         'most derived class.',
                                          'options': ["A's constructor, then B's constructor, then C's constructor",
                                                      "C's constructor, then B's, then A's",
                                                      'B runs first, then A and C concurrently',
                                                      "Only C's constructor executes"],
                                          'question': 'What is the order of constructor execution in multilevel '
                                                      'inheritance (A -> B -> C)?'},
                                         {'correct_answer': 'Separated by commas: class C : public A, public B',
                                          'difficulty': 'Easy',
                                          'explanation': 'C++ lists multiple base classes separated by commas in the '
                                                         'class header.',
                                          'options': ['Separated by commas: class C : public A, public B',
                                                      "Using the 'and' keyword: class C extends A and B",
                                                      'Using multiple colon operators: class C : A : B',
                                                      'By defining nested classes'],
                                          'question': 'In C++, how are multiple base classes specified in the derived '
                                                      'class definition?'},
                                         {'correct_answer': 'Yes, an interface can extend multiple interfaces using '
                                                            'commas',
                                          'difficulty': 'Easy',
                                          'explanation': 'Interfaces in Java support multiple inheritance from other '
                                                         "interfaces via 'extends I1, I2'.",
                                          'options': ['Yes, an interface can extend multiple interfaces using commas',
                                                      'No, interfaces cannot extend other interfaces',
                                                      'Only if they have no abstract methods',
                                                      'Only up to two interfaces'],
                                          'question': 'Can an interface in Java extend multiple other interfaces?'},
                                         {'correct_answer': 'Yes, Python fully supports multiple inheritance',
                                          'difficulty': 'Easy',
                                          'explanation': 'Python permits syntax such as class Derived(Base1, Base2): '
                                                         'natively.',
                                          'options': ['Yes, Python fully supports multiple inheritance',
                                                      'No, Python only allows single inheritance',
                                                      'Only if using the PyMulti metaclass',
                                                      'Only if all parent classes are abstract'],
                                          'question': 'In Python, can a class inherit from multiple classes?'},
                                         {'correct_answer': "By using 'virtual' inheritance: class B : virtual public "
                                                            'A',
                                          'difficulty': 'Medium',
                                          'explanation': 'Virtual base classes ensure only one shared copy of the '
                                                         'common ancestor subobject exists in the derived class.',
                                          'options': ["By using 'virtual' inheritance: class B : virtual public A",
                                                      'By making base methods private',
                                                      'By using smart pointers',
                                                      'By overloading the destructor'],
                                          'question': 'How is the Diamond Problem resolved in C++ to prevent duplicate '
                                                      'base class subobjects?'},
                                         {'correct_answer': 'C3 Linearization algorithm',
                                          'difficulty': 'Medium',
                                          'explanation': 'Python uses C3 linearization to guarantee monotonicity and '
                                                         'preserve local precedence in MRO.',
                                          'options': ['C3 Linearization algorithm',
                                                      'Depth-First Search without cycles',
                                                      "Dijkstra's Shortest Path",
                                                      'Breadth-First Greedy Ordering'],
                                          'question': 'What algorithm does Python use to determine method resolution '
                                                      'order (MRO) in multiple inheritance?'},
                                         {'correct_answer': 'ClassName.__mro__ or ClassName.mro()',
                                          'difficulty': 'Medium',
                                          'explanation': 'The __mro__ attribute or mro() method returns the tuple of '
                                                         'classes in method lookup order.',
                                          'options': ['ClassName.__mro__ or ClassName.mro()',
                                                      'ClassName.order()',
                                                      'ClassName.__trace__',
                                                      'inspect(ClassName)'],
                                          'question': 'In Python, how can you inspect the method resolution order of a '
                                                      'class?'},
                                         {'correct_answer': 'By qualifying the method with the scope resolution '
                                                            'operator: Base1::display()',
                                          'difficulty': 'Medium',
                                          'explanation': 'The scope resolution operator (Base1::) disambiguates which '
                                                         'parent method to invoke.',
                                          'options': ['By qualifying the method with the scope resolution operator: '
                                                      'Base1::display()',
                                                      'The compiler randomly picks one',
                                                      'It automatically calls both methods',
                                                      'The code cannot compile even if qualified'],
                                          'question': 'In C++, if two parent classes Base1 and Base2 have a method '
                                                      "with the exact same name 'void display()', how does Derived "
                                                      'resolve calling it?'},
                                         {'correct_answer': 'The implementing class MUST override the conflicting '
                                                            'method and specify which to call '
                                                            '(InterfaceName.super.method())',
                                          'difficulty': 'Medium',
                                          'explanation': 'Java requires the developer to explicitly resolve '
                                                         'ambiguities between colliding interface default methods.',
                                          'options': ['The implementing class MUST override the conflicting method and '
                                                      'specify which to call (InterfaceName.super.method())',
                                                      'The compiler picks the interface declared first',
                                                      'The method is silently removed',
                                                      'A runtime ExceptionInInitializerError is thrown'],
                                          'question': 'How does Java resolve default method conflicts when a class '
                                                      'implements two interfaces with the identical default method?'},
                                         {'correct_answer': '~C(), then ~B(), then ~A()',
                                          'difficulty': 'Medium',
                                          'explanation': 'Destruction unwinds in reverse order of construction, from '
                                                         'the leaf class up to the root.',
                                          'options': ['~C(), then ~B(), then ~A()',
                                                      '~A(), then ~B(), then ~C()',
                                                      '~B() first, then ~A() and ~C()',
                                                      'Destructors execute in arbitrary order'],
                                          'question': 'What is the destructor call order in multilevel inheritance (A '
                                                      '-> B -> C)?'},
                                         {'correct_answer': 'The derived object contains both fields; access must be '
                                                            'qualified with BaseName::field',
                                          'difficulty': 'Medium',
                                          'explanation': 'Without virtual inheritance, two separate subobjects exist, '
                                                         'requiring explicit qualification to avoid ambiguity.',
                                          'options': ['The derived object contains both fields; access must be '
                                                      'qualified with BaseName::field',
                                                      'The compiler merges the two fields into one',
                                                      'A fatal linker crash occurs at runtime',
                                                      'One field is deleted automatically'],
                                          'question': 'What happens in C++ if a class inherits from two base classes '
                                                      'that both declare non-virtual fields of the same name?'},
                                         {'correct_answer': 'It delegates method calls to the next class in the C3 MRO '
                                                            'chain, not necessarily the direct parent',
                                          'difficulty': 'Medium',
                                          'explanation': 'In cooperative multiple inheritance, super() follows the '
                                                         'computed linear MRO order.',
                                          'options': ['It delegates method calls to the next class in the C3 MRO '
                                                      'chain, not necessarily the direct parent',
                                                      'It always calls the first class listed in the class definition',
                                                      'It calls all parent classes simultaneously on multiple CPU '
                                                      'threads',
                                                      'It restarts execution from the global module'],
                                          'question': 'In Python, what does the super() function do in the presence of '
                                                      'multiple inheritance?'},
                                         {'correct_answer': 'A class containing methods designed to be inherited by '
                                                            'multiple classes for reusable functionality without being '
                                                            'a standalone parent',
                                          'difficulty': 'Medium',
                                          'explanation': 'Mixins provide modular behavioral building blocks in '
                                                         'languages supporting multiple inheritance.',
                                          'options': ['A class containing methods designed to be inherited by multiple '
                                                      'classes for reusable functionality without being a standalone '
                                                      'parent',
                                                      'A tool to compile C++ into JavaScript',
                                                      'A design pattern used only for database connections',
                                                      'A class with only static member variables'],
                                          'question': 'What is a mixin in object-oriented programming?'},
                                         {'correct_answer': 'To prevent diamond ambiguity, complex pointer arithmetic, '
                                                            'and runtime overhead associated with multiple inheritance '
                                                            'layouts',
                                          'difficulty': 'Medium',
                                          'explanation': 'Excluding multiple class inheritance eliminated the '
                                                         'architectural pitfalls of diamond hierarchies.',
                                          'options': ['To prevent diamond ambiguity, complex pointer arithmetic, and '
                                                      'runtime overhead associated with multiple inheritance layouts',
                                                      'Because multiple inheritance is impossible in bytecode',
                                                      'Because computer monitors in the 1990s could not render '
                                                      'multiple parent classes',
                                                      'Because interfaces were not invented yet'],
                                          'question': 'Why did the creators of Java and C# intentionally omit multiple '
                                                      'class inheritance?'},
                                         {'correct_answer': 'Derived objects store an offset pointer (vbase_offset) in '
                                                            'the vtable to locate the shared virtual base subobject',
                                          'difficulty': 'Hard',
                                          'explanation': 'Compilers use virtual base pointer (vptr) tables with '
                                                         'offsets to access shared virtual bases whose position '
                                                         'varies.',
                                          'options': ['Derived objects store an offset pointer (vbase_offset) in the '
                                                      'vtable to locate the shared virtual base subobject',
                                                      "The virtual base is stored in a separate thread's memory",
                                                      'The virtual base is duplicated at every level',
                                                      'Virtual bases are converted to C-style unions'],
                                          'question': 'How is a virtual base class laid out in memory in C++ '
                                                      'implementations like GCC/Clang?'},
                                         {'correct_answer': 'The most-derived class instantiated in the hierarchy must '
                                                            'initialize the virtual base constructor',
                                          'difficulty': 'Hard',
                                          'explanation': 'Because the virtual base is shared, the most derived class '
                                                         'directly calls its constructor, ignoring intermediate calls.',
                                          'options': ['The most-derived class instantiated in the hierarchy must '
                                                      'initialize the virtual base constructor',
                                                      'The immediate base class initializes it',
                                                      'The compiler initializes it to zero without constructor',
                                                      'The operating system loader'],
                                          'question': 'In C++ with virtual inheritance, which class is responsible for '
                                                      'initializing the virtual base class?'},
                                         {'correct_answer': 'The compiler adds or subtracts constant byte offsets to '
                                                            "adjust the 'this' pointer to match the target base "
                                                            'subobject layout',
                                          'difficulty': 'Hard',
                                          'explanation': 'In multiple inheritance, subobjects reside at non-zero '
                                                         'offsets from the object start, requiring pointer adjustment.',
                                          'options': ['The compiler adds or subtracts constant byte offsets to adjust '
                                                      "the 'this' pointer to match the target base subobject layout",
                                                      'A dynamic system call reallocates the object',
                                                      'The pointer value remains identical in all cases',
                                                      "A runtime exception is thrown if pointers don't match"],
                                          'question': "How does pointer adjustment ('this' pointer fixup) occur when "
                                                      'casting between multiple base pointers in C++?'},
                                         {'correct_answer': "A small wrapper function that adjusts the 'this' pointer "
                                                            'by an offset before jumping to the actual virtual method',
                                          'difficulty': 'Hard',
                                          'explanation': "Thunks adjust the 'this' pointer to the expected subobject "
                                                         'offset before dispatching to the overriding method.',
                                          'options': ["A small wrapper function that adjusts the 'this' pointer by an "
                                                      'offset before jumping to the actual virtual method',
                                                      'A function that terminates corrupted processes',
                                                      'A constructor helper for stack objects',
                                                      'A memory garbage collector thread'],
                                          'question': 'In C++, what is the thunk function used for in multiple '
                                                      'inheritance vtables?'},
                                         {'correct_answer': 'Python rejects the class definition at definition time '
                                                            'with a TypeError: Cannot create a consistent method '
                                                            'resolution order',
                                          'difficulty': 'Hard',
                                          'explanation': 'C3 linearization guarantees consistent ordering; if a '
                                                         'hierarchy is contradictory, class creation fails '
                                                         'immediately.',
                                          'options': ['Python rejects the class definition at definition time with a '
                                                      'TypeError: Cannot create a consistent method resolution order',
                                                      'Python falls back to breadth-first search',
                                                      'Python randomly selects an order',
                                                      'The script crashes with a segmentation fault'],
                                          'question': "What happens when Python's C3 linearization fails to produce a "
                                                      'monotonic inheritance graph?'},
                                         {'correct_answer': 'A name in a derived class dominates a name in a virtual '
                                                            'base class if the derived class inherits from that base',
                                          'difficulty': 'Hard',
                                          'explanation': 'The dominance rule resolves ambiguity when an overriding '
                                                         'method along one branch shadows the virtual base method.',
                                          'options': ['A name in a derived class dominates a name in a virtual base '
                                                      'class if the derived class inherits from that base',
                                                      'The base class with the largest memory size dominates all calls',
                                                      'The class declared first dominates all lookups',
                                                      'Pure virtual functions dominate normal functions'],
                                          'question': "What is the 'Dominance Rule' in C++ virtual inheritance?"},
                                         {'correct_answer': 'A pattern where every class in the hierarchy invokes '
                                                            'super() with consistent argument passing to ensure all '
                                                            'parents run',
                                          'difficulty': 'Hard',
                                          'explanation': 'Cooperative multiple inheritance relies on all participating '
                                                         'classes calling super() to traverse the full MRO.',
                                          'options': ['A pattern where every class in the hierarchy invokes super() '
                                                      'with consistent argument passing to ensure all parents run',
                                                      'Classes running on separate CPU cores cooperating via IPC',
                                                      'Inheriting from classes in different modules',
                                                      'Using threading.Lock inside subclasses'],
                                          'question': 'What is cooperative multiple inheritance in Python?'},
                                         {'correct_answer': 'It returns a pointer to the complete most-derived object '
                                                            'instance starting address regardless of current base '
                                                            'pointer offset',
                                          'difficulty': 'Hard',
                                          'explanation': 'Casting to void* on a polymorphic object retrieves the start '
                                                         'of the whole memory block containing all subobjects.',
                                          'options': ['It returns a pointer to the complete most-derived object '
                                                      'instance starting address regardless of current base pointer '
                                                      'offset',
                                                      'It casts the object to raw assembly code',
                                                      "It frees the object's virtual table",
                                                      'It converts the object into an integer hash'],
                                          'question': 'Why can dynamic_cast<void*> be useful in C++ with multiple '
                                                      'inheritance?'},
                                         {'correct_answer': 'Accessing the field without interface qualification '
                                                            'results in a compile-time ambiguity error',
                                          'difficulty': 'Hard',
                                          'explanation': 'Colliding interface fields must be disambiguated explicitly '
                                                         'with InterfaceName.CONSTANT.',
                                          'options': ['Accessing the field without interface qualification results in '
                                                      'a compile-time ambiguity error',
                                                      'The value from the first listed interface is chosen',
                                                      'The JVM throws a LinkageError at startup',
                                                      'Both constants are bitwise ORed together'],
                                          'question': 'What happens in Java if a class implements two interfaces that '
                                                      'declare the same constant field with different values?'},
                                         {'correct_answer': 'It complicates class hierarchy analysis (CHA) because '
                                                            "secondary vtables and non-zero 'this' offsets must be "
                                                            'tracked',
                                          'difficulty': 'Hard',
                                          'explanation': 'Devirtualization must verify that multiple subobject paths '
                                                         'do not introduce alternative overrides.',
                                          'options': ['It complicates class hierarchy analysis (CHA) because secondary '
                                                      "vtables and non-zero 'this' offsets must be tracked",
                                                      'It completely disables all compiler optimizations forever',
                                                      'It forces all functions to be inlined',
                                                      'It eliminates the need for symbol tables'],
                                          'question': 'How does multiple inheritance impact compiler optimizations '
                                                      'like devirtualization?'}],
 'SOLID Principles and Design Patterns': [{'correct_answer': 'Single Responsibility Principle (SRP)',
                                           'difficulty': 'Easy',
                                           'explanation': 'SRP states that a class should have one, and only one, '
                                                          'reason to change.',
                                           'options': ['Single Responsibility Principle (SRP)',
                                                       'Static Routine Principle',
                                                       'Software Safety Principle',
                                                       'Synchronized State Pattern'],
                                           'question': "What does the 'S' in SOLID principles stand for?"},
                                          {'correct_answer': 'Open/Closed Principle (OCP)',
                                           'difficulty': 'Easy',
                                           'explanation': 'OCP states that software entities should be open for '
                                                          'extension, but closed for modification.',
                                           'options': ['Open/Closed Principle (OCP)',
                                                       'Object Creation Principle',
                                                       'Ordered Execution Principle',
                                                       'Output Formatting Principle'],
                                           'question': "What does the 'O' in SOLID principles stand for?"},
                                          {'correct_answer': 'Liskov Substitution Principle (LSP)',
                                           'difficulty': 'Easy',
                                           'explanation': 'LSP states that subtypes must be substitutable for their '
                                                          'base types without altering correctness.',
                                           'options': ['Liskov Substitution Principle (LSP)',
                                                       'Linear Hierarchy Principle',
                                                       'Loose Coupling Principle',
                                                       'Logical Separation Principle'],
                                           'question': "What does the 'L' in SOLID principles stand for?"},
                                          {'correct_answer': 'Interface Segregation Principle (ISP)',
                                           'difficulty': 'Easy',
                                           'explanation': 'ISP states that no client should be forced to depend on '
                                                          'methods it does not use.',
                                           'options': ['Interface Segregation Principle (ISP)',
                                                       'Instance Initialization Principle',
                                                       'Immutable State Pattern',
                                                       'Inheritance Sharing Principle'],
                                           'question': "What does the 'I' in SOLID principles stand for?"},
                                          {'correct_answer': 'Dependency Inversion Principle (DIP)',
                                           'difficulty': 'Easy',
                                           'explanation': 'DIP states that high-level modules should not depend on '
                                                          'low-level modules; both should depend on abstractions.',
                                           'options': ['Dependency Inversion Principle (DIP)',
                                                       'Dynamic Inlining Pattern',
                                                       'Data Encapsulation Principle',
                                                       'Direct Instantiation Pattern'],
                                           'question': "What does the 'D' in SOLID principles stand for?"},
                                          {'correct_answer': 'Ensuring a class has only one instance and providing a '
                                                             'global point of access to it',
                                           'difficulty': 'Easy',
                                           'explanation': 'Singleton restricts instantiation of a class to a single '
                                                          'unique instance.',
                                           'options': ['Ensuring a class has only one instance and providing a global '
                                                       'point of access to it',
                                                       'Creating instances across multiple threads',
                                                       'Deleting instances automatically',
                                                       'Allowing unlimited instances of a class'],
                                           'question': 'What is the primary objective of the Singleton design '
                                                       'pattern?'},
                                          {'correct_answer': 'Defining an interface for creating an object, but '
                                                             'letting subclasses decide which class to instantiate',
                                           'difficulty': 'Easy',
                                           'explanation': 'Factory Method delegates instantiation logic to derived '
                                                          'classes.',
                                           'options': ['Defining an interface for creating an object, but letting '
                                                       'subclasses decide which class to instantiate',
                                                       'Constructing database tables',
                                                       'Running unit tests in parallel',
                                                       'Compressing files'],
                                           'question': 'What is the primary objective of the Factory Method design '
                                                       'pattern?'},
                                          {'correct_answer': 'Defining a one-to-many dependency between objects so '
                                                             'that when one object changes state, all its dependents '
                                                             'are notified automatically',
                                           'difficulty': 'Easy',
                                           'explanation': 'Observer implements a publish-subscribe communication '
                                                          'mechanism between objects.',
                                           'options': ['Defining a one-to-many dependency between objects so that when '
                                                       'one object changes state, all its dependents are notified '
                                                       'automatically',
                                                       'Observing CPU performance metrics',
                                                       'Logging error messages to a disk file',
                                                       'Running code inside a debugger'],
                                           'question': 'What is the primary objective of the Observer design pattern?'},
                                          {'correct_answer': 'Creational patterns',
                                           'difficulty': 'Easy',
                                           'explanation': 'Creational patterns deal with object creation mechanisms to '
                                                          'create objects in a controlled manner.',
                                           'options': ['Creational patterns',
                                                       'Structural patterns',
                                                       'Behavioral patterns',
                                                       'Architectural patterns'],
                                           'question': 'Which design pattern category do Singleton, Factory Method, '
                                                       'and Builder belong to?'},
                                          {'correct_answer': 'Structural patterns',
                                           'difficulty': 'Easy',
                                           'explanation': 'Structural patterns explain how to assemble objects and '
                                                          'classes into larger structures while keeping them flexible.',
                                           'options': ['Structural patterns',
                                                       'Creational patterns',
                                                       'Behavioral patterns',
                                                       'Concurrency patterns'],
                                           'question': 'Which design pattern category do Adapter, Decorator, and '
                                                       'Facade belong to?'},
                                          {'correct_answer': 'High-level modules should not depend on low-level '
                                                             'modules; both should depend on abstractions (interfaces)',
                                           'difficulty': 'Medium',
                                           'explanation': 'DIP inverts traditional dependency relationships by '
                                                          'inserting abstractions between layers.',
                                           'options': ['High-level modules should not depend on low-level modules; '
                                                       'both should depend on abstractions (interfaces)',
                                                       'High-level modules should call low-level modules directly '
                                                       'using new',
                                                       'Low-level modules must be written in assembly',
                                                       'All modules must be static'],
                                           'question': 'What does the Dependency Inversion Principle (DIP) state '
                                                       'regarding high-level and low-level modules?'},
                                          {'correct_answer': 'Constructing complex objects step-by-step, especially '
                                                             'when an object has many optional parameters',
                                           'difficulty': 'Medium',
                                           'explanation': 'Builder avoids telescoping constructor anti-patterns and '
                                                          'creates immutable objects cleanly.',
                                           'options': ['Constructing complex objects step-by-step, especially when an '
                                                       'object has many optional parameters',
                                                       'Building executable binaries from source code',
                                                       'Creating classes on disk dynamically',
                                                       'Running automated build pipelines'],
                                           'question': 'What is the Builder design pattern primarily used for?'},
                                          {'correct_answer': 'Converting the interface of a class into another '
                                                             'interface clients expect, enabling incompatible '
                                                             'interfaces to collaborate',
                                           'difficulty': 'Medium',
                                           'explanation': 'Adapter acts as a wrapper between two mismatched '
                                                          'interfaces.',
                                           'options': ['Converting the interface of a class into another interface '
                                                       'clients expect, enabling incompatible interfaces to '
                                                       'collaborate',
                                                       'Adapting screen resolutions in UI',
                                                       'Translating programming languages',
                                                       'Connecting computers to power sockets'],
                                           'question': 'What is the role of the Adapter design pattern?'},
                                          {'correct_answer': 'Providing a simplified, unified high-level interface to '
                                                             'a complex subsystem of classes',
                                           'difficulty': 'Medium',
                                           'explanation': 'Facade offers a single convenient entry point to a '
                                                          'complicated subsystem.',
                                           'options': ['Providing a simplified, unified high-level interface to a '
                                                       'complex subsystem of classes',
                                                       'Hiding passwords inside a class',
                                                       'Displaying graphical user interfaces',
                                                       'A tool for code obfuscation'],
                                           'question': 'What is the Facade design pattern?'},
                                          {'correct_answer': 'A single reason to change, relating to a specific actor '
                                                             'or stakeholder',
                                           'difficulty': 'Medium',
                                           'explanation': "Robert C. Martin defines responsibility as 'a reason to "
                                                          "change' tied to a business role.",
                                           'options': ['A single reason to change, relating to a specific actor or '
                                                       'stakeholder',
                                                       'A single method per class',
                                                       'A single line of code per method',
                                                       'A single class per file'],
                                           'question': 'How does the Single Responsibility Principle (SRP) define '
                                                       "'responsibility'?"},
                                          {'correct_answer': 'Setting width independently of height in Rectangle '
                                                             'breaks the invariant of Square, violating client '
                                                             'behavioral expectations',
                                           'difficulty': 'Medium',
                                           'explanation': 'A client expecting Rectangle behavior will have its '
                                                          'assumptions invalidated if passed a Square.',
                                           'options': ['Setting width independently of height in Rectangle breaks the '
                                                       'invariant of Square, violating client behavioral expectations',
                                                       'Squares cannot have four sides in code',
                                                       'Rectangles are always abstract',
                                                       'LSP forbids geometry in programming'],
                                           'question': "What is the violation in the classic 'Square inherits from "
                                                       "Rectangle' example under Liskov Substitution Principle (LSP)?"},
                                          {'correct_answer': 'DI is a concrete technique where dependencies are '
                                                             "supplied ('injected') into an object from the outside "
                                                             'rather than created internally',
                                           'difficulty': 'Medium',
                                           'explanation': 'DI achieves IoC by shifting the responsibility of '
                                                          'instantiating dependencies to an external assembler or '
                                                          'framework.',
                                           'options': ['DI is a concrete technique where dependencies are supplied '
                                                       "('injected') into an object from the outside rather than "
                                                       'created internally',
                                                       'DI is a compiler plugin',
                                                       'DI is a database query language',
                                                       'DI is used exclusively in Android apps'],
                                           'question': 'What is Dependency Injection (DI) and how does it relate to '
                                                       'the Inversion of Control (IoC) concept?'},
                                          {'correct_answer': 'Encapsulating a request as an object, thereby allowing '
                                                             'parameterization, queuing, logging, and undoable '
                                                             'operations',
                                           'difficulty': 'Medium',
                                           'explanation': 'Command turns requests into standalone objects with an '
                                                          'execute() method, decoupling invoker from receiver.',
                                           'options': ['Encapsulating a request as an object, thereby allowing '
                                                       'parameterization, queuing, logging, and undoable operations',
                                                       'Running terminal commands in bash',
                                                       'A compiler optimization for function calls',
                                                       'Executing SQL queries synchronously'],
                                           'question': 'What is the Command design pattern?'},
                                          {'correct_answer': 'Factory Method creates a single product via inheritance; '
                                                             'Abstract Factory creates families of related products '
                                                             'via composition',
                                           'difficulty': 'Medium',
                                           'explanation': 'Abstract Factory provides an interface for producing '
                                                          'families of related or dependent objects without specifying '
                                                          'concrete classes.',
                                           'options': ['Factory Method creates a single product via inheritance; '
                                                       'Abstract Factory creates families of related products via '
                                                       'composition',
                                                       'Factory Method is creational; Abstract Factory is structural',
                                                       'Abstract Factory cannot use interfaces',
                                                       'They are completely identical in implementation'],
                                           'question': 'What is the difference between Abstract Factory and Factory '
                                                       'Method patterns?'},
                                          {'correct_answer': 'It couples lifecycle management with business logic and '
                                                             'introduces global mutable state that hinders unit test '
                                                             'isolation',
                                           'difficulty': 'Medium',
                                           'explanation': 'Singletons introduce global state, hidden dependencies, and '
                                                          'tight coupling that make mocking difficult.',
                                           'options': ['It couples lifecycle management with business logic and '
                                                       'introduces global mutable state that hinders unit test '
                                                       'isolation',
                                                       'It causes compiler crashes during tests',
                                                       'It prevents objects from being created',
                                                       'It requires 100% CPU usage'],
                                           'question': 'How can the Singleton pattern violate the Single '
                                                       'Responsibility Principle and testing best practices?'},
                                          {'correct_answer': 'It checks for null before and after acquiring a '
                                                             "synchronized lock, combined with a 'volatile' instance "
                                                             'reference to prevent instruction reordering',
                                           'difficulty': 'Hard',
                                           'explanation': 'The volatile keyword is crucial to prevent CPU instruction '
                                                          'reordering where partially constructed instances become '
                                                          'visible.',
                                           'options': ['It checks for null before and after acquiring a synchronized '
                                                       "lock, combined with a 'volatile' instance reference to prevent "
                                                       'instruction reordering',
                                                       'It acquires two locks simultaneously',
                                                       'It runs two threads to check the instance',
                                                       'It locks the operating system kernel'],
                                           'question': 'How does double-checked locking in the Singleton pattern '
                                                       'prevent race conditions in multi-threaded Java?'},
                                          {'correct_answer': 'It uses a private static inner helper class loaded '
                                                             'lazily by the ClassLoader upon first reference, '
                                                             'guaranteeing thread-safe initialization without '
                                                             'synchronization',
                                           'difficulty': 'Hard',
                                           'explanation': 'Inner classes are not loaded until referenced; class '
                                                          'loading in Java is inherently thread-safe.',
                                           'options': ['It uses a private static inner helper class loaded lazily by '
                                                       'the ClassLoader upon first reference, guaranteeing thread-safe '
                                                       'initialization without synchronization',
                                                       'It writes singletons to disk files',
                                                       'It uses atomic CPU instructions directly in assembly',
                                                       'It relies on finalizers to clean up instances'],
                                           'question': 'What is the Bill Pugh Singleton implementation in Java and why '
                                                       'is it preferred for thread safety?'},
                                          {'correct_answer': 'The JVM guarantees enum instances are instantiated '
                                                             'exactly once and serialization/reflection mechanisms '
                                                             'explicitly forbid creating extra enum instances',
                                           'difficulty': 'Hard',
                                           'explanation': 'Constructor.newInstance() throws an '
                                                          'IllegalArgumentException when invoked on an enum type.',
                                           'options': ['The JVM guarantees enum instances are instantiated exactly '
                                                       'once and serialization/reflection mechanisms explicitly forbid '
                                                       'creating extra enum instances',
                                                       'Enums are encrypted at runtime',
                                                       'Enums cannot be loaded into memory',
                                                       'Enums do not have class definitions'],
                                           'question': 'How can Enum Singletons in Java resist reflection and '
                                                       'serialization attacks?'},
                                          {'correct_answer': 'Requests pass sequentially along a chain of handlers, '
                                                             'where each handler decides to process, mutate, or pass '
                                                             'the request to the next handler',
                                           'difficulty': 'Hard',
                                           'explanation': 'Middleware and filter pipelines chain handlers that '
                                                          'intercept and process HTTP requests consecutively.',
                                           'options': ['Requests pass sequentially along a chain of handlers, where '
                                                       'each handler decides to process, mutate, or pass the request '
                                                       'to the next handler',
                                                       'A pattern to chain constructors in inheritance',
                                                       'A linked list data structure for numbers',
                                                       'A mechanism for database connection pooling'],
                                           'question': 'What is the Chain of Responsibility design pattern and how is '
                                                       'it utilized in web frameworks (e.g., HTTP middleware / servlet '
                                                       'filters)?'},
                                          {'correct_answer': "It captures an object's internal state in an opaque "
                                                             'memento object that only the originating class can '
                                                             'inspect and restore',
                                           'difficulty': 'Hard',
                                           'explanation': 'Memento serializes internal state into an opaque token '
                                                          'without exposing internal private members to caretakers.',
                                           'options': ["It captures an object's internal state in an opaque memento "
                                                       'object that only the originating class can inspect and restore',
                                                       'It creates a full duplicate process in the OS',
                                                       'It writes all variables to a public JSON file',
                                                       'It uses reflection to read private fields'],
                                           'question': 'How does the Memento design pattern achieve undo/redo '
                                                       'functionality without violating encapsulation?'},
                                          {'correct_answer': 'It encapsulates state-specific behaviors into distinct '
                                                             'state classes and delegates state transitions to the '
                                                             'current state object',
                                           'difficulty': 'Hard',
                                           'explanation': 'State pattern models finite state machines by letting state '
                                                          'classes encapsulate their own transition logic.',
                                           'options': ['It encapsulates state-specific behaviors into distinct state '
                                                       'classes and delegates state transitions to the current state '
                                                       'object',
                                                       'It stores state in a global SQLite database',
                                                       'It uses switch statements with hundreds of cases',
                                                       'It replaces objects with enum strings'],
                                           'question': 'What is the State design pattern and how does it eliminate '
                                                       'large, complex conditional statements?'},
                                          {'correct_answer': 'Proxy controls and manages access to its subject (lazy '
                                                             'loading, caching, security); Decorator adds enhanced '
                                                             'responsibilities dynamically',
                                           'difficulty': 'Hard',
                                           'explanation': 'Proxy manages the lifecycle and access to an underlying '
                                                          'object, whereas Decorator augments its functional behavior.',
                                           'options': ['Proxy controls and manages access to its subject (lazy '
                                                       'loading, caching, security); Decorator adds enhanced '
                                                       'responsibilities dynamically',
                                                       'Proxy is creational; Decorator is behavioral',
                                                       'Proxy cannot use interfaces',
                                                       'Decorator cannot hold references to components'],
                                           'question': 'How does the Proxy design pattern differ from the Decorator '
                                                       'design pattern in intent, despite similar structural '
                                                       'delegation?'},
                                          {'correct_answer': 'High-level domain entities define repository interfaces; '
                                                             'low-level database infrastructure implements them, '
                                                             'pointing dependencies inward',
                                           'difficulty': 'Hard',
                                           'explanation': 'Dependencies always point inwards toward domain entities, '
                                                          'protecting core business rules from external technology '
                                                          'changes.',
                                           'options': ['High-level domain entities define repository interfaces; '
                                                       'low-level database infrastructure implements them, pointing '
                                                       'dependencies inward',
                                                       'Databases dictate the shape of business domain classes',
                                                       'Domain entities import SQL drivers directly',
                                                       'Frameworks own the core business logic'],
                                           'question': 'In clean architecture, how does the Dependency Inversion '
                                                       'Principle enforce the boundary between business entities and '
                                                       'external databases/frameworks?'},
                                          {'correct_answer': 'It hides class dependencies inside a global registry '
                                                             'lookup rather than declaring them explicitly in '
                                                             'constructors, making testing and maintenance difficult',
                                           'difficulty': 'Hard',
                                           'explanation': 'Service Locator obscures component dependencies and couples '
                                                          'code to a global locator registry.',
                                           'options': ['It hides class dependencies inside a global registry lookup '
                                                       'rather than declaring them explicitly in constructors, making '
                                                       'testing and maintenance difficult',
                                                       'It is slower than database queries',
                                                       'It requires writing C code',
                                                       'It causes stack overflows during instantiation'],
                                           'question': 'What is the Service Locator pattern and why is it considered '
                                                       'an antipattern compared to explicit Dependency Injection?'},
                                          {'correct_answer': 'Systems are designed around abstract extension points '
                                                             '(plugins/interfaces) so new features can be added via '
                                                             'new classes without modifying core engine code',
                                           'difficulty': 'Hard',
                                           'explanation': 'Plugin architectures exemplify OCP: the application core is '
                                                          'closed to modification, but open to unlimited new plugins.',
                                           'options': ['Systems are designed around abstract extension points '
                                                       '(plugins/interfaces) so new features can be added via new '
                                                       'classes without modifying core engine code',
                                                       'Source code is closed source and cannot be viewed',
                                                       'All classes must be declared final',
                                                       'Plugins must be compiled directly into the OS kernel'],
                                           'question': "What is the Open/Closed Principle's relationship with "
                                                       'polymorphism and plugin architectures?'}]}

