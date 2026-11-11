import json

def q(text, options, correct, explanation, diff):
    assert len(options) == 4, f"Options length != 4: {text}"
    assert correct in options, f"Correct not in options: {text} -> {correct}"
    return {
        "question": text,
        "options": options,
        "correct_answer": correct,
        "explanation": explanation,
        "difficulty": diff
    }

topics_data = {}

# 1. Classes and Objects
topics_data["Classes and Objects"] = [
    # 10 Easy
    q("What is a class in Object-Oriented Programming?", 
      ["A user-defined blueprint or template for creating objects", "An instance of an object stored in heap memory", "A primitive data type in memory", "A function that executes automatically"],
      "A user-defined blueprint or template for creating objects", "A class defines variables and methods that represent the state and behavior of an object.", "Easy"),
    q("What is an object in OOP?",
      ["An instance of a class that holds state and behavior", "A global variable accessible everywhere", "A compiler directive", "A pointer to code segment"],
      "An instance of a class that holds state and behavior", "An object is a concrete instance created from a class blueprint.", "Easy"),
    q("Which keyword is commonly used in languages like Java, C++, and C# to instantiate an object?",
      ["new", "create", "alloc", "make"],
      "new", "The 'new' keyword dynamically allocates memory on the heap for a new object.", "Easy"),
    q("What does the 'state' of an object refer to?",
      ["The current values of its attributes or fields", "The location of its source file", "The execution thread ID", "The return type of its methods"],
      "The current values of its attributes or fields", "An object's state is defined by the values stored in its instance variables.", "Easy"),
    q("What does the 'behavior' of an object represent?",
      ["The actions and methods it can perform", "Its memory address", "Its visibility modifier", "The time it was allocated"],
      "The actions and methods it can perform", "Behavior represents the operations and methods available on the object.", "Easy"),
    q("Where are object instances typically allocated in memory during runtime in languages like Java and C#?",
      ["Heap memory", "Stack memory only", "CPU registers only", "Read-only text segment"],
      "Heap memory", "Objects instantiated dynamically with new are allocated on the heap.", "Easy"),
    q("What is an instance variable?",
      ["A variable declared in a class that belongs to a specific object", "A variable accessible across all classes without instantiation", "A variable defined inside a loop", "A constant that cannot change"],
      "A variable declared in a class that belongs to a specific object", "Each instance of a class maintains its own distinct copy of instance variables.", "Easy"),
    q("Which keyword refers to the current invoking instance of a class?",
      ["this / self", "super", "base", "parent"],
      "this / self", "'this' in Java/C++ or 'self' in Python refers to the current object instance.", "Easy"),
    q("What is the fundamental difference between a class and an object?",
      ["A class is a blueprint; an object is a concrete instance of that blueprint", "A class is stored in RAM; an object is stored on disk", "A class has values; an object only has types", "There is no difference between them"],
      "A class is a blueprint; an object is a concrete instance of that blueprint", "A class is the abstract template, while an object is the tangible instance in memory.", "Easy"),
    q("Can multiple independent objects be instantiated from a single class?",
      ["Yes, each object has its own separate state", "No, only one object per class is permitted", "Only if the class is declared static", "Yes, but they must share the exact same attribute values"],
      "Yes, each object has its own separate state", "Multiple objects can be created from one class, each maintaining independent state.", "Easy"),

    # 10 Medium
    q("What is the difference between an instance method and a static method?",
      ["An instance method operates on specific object state, whereas a static method belongs to the class itself", "An instance method runs faster than a static method", "A static method can access the 'this' reference directly", "An instance method cannot return any value"],
      "An instance method operates on specific object state, whereas a static method belongs to the class itself", "Static methods belong to the class namespace and do not operate on an individual instance.", "Medium"),
    q("What happens if you modify a static variable through one object instance?",
      ["The change is reflected across all instances of the class", "Only that single object sees the change", "A compile-time error occurs", "A new copy of the variable is created on the stack"],
      "The change is reflected across all instances of the class", "Static variables are shared among all instances of a class.", "Medium"),
    q("In Python, what is the role of the '__init__' method?",
      ["It serves as the initializer/constructor when an object is created", "It destroys the object from memory", "It compares two objects for equality", "It converts the object to a string"],
      "It serves as the initializer/constructor when an object is created", "The '__init__' method initializes newly created object instances in Python.", "Medium"),
    q("What is an anonymous object in languages like Java or C++?",
      ["An object instantiated without assigning it to a reference variable", "An object with private methods only", "An object without a class definition", "An object stored on the GPU"],
      "An object instantiated without assigning it to a reference variable", "Anonymous objects are used immediately upon creation without being bound to a named variable.", "Medium"),
    q("What determines the memory footprint of an object in memory?",
      ["Its instance fields, memory alignment padding, and object header overhead", "The length of the method names", "The comments in the class definition", "The number of lines of code in the class"],
      "Its instance fields, memory alignment padding, and object header overhead", "An object's footprint includes its fields, alignment padding, and runtime metadata headers.", "Medium"),
    q("Why can static methods not directly access instance variables?",
      ["Static methods do not have an implicit 'this' reference to any specific instance", "Static methods are stored in a different file", "Instance variables are always encrypted", "Static methods can only return void"],
      "Static methods do not have an implicit 'this' reference to any specific instance", "Because static methods run at the class level without an object context, there is no instance to read from.", "Medium"),
    q("What is a copy constructor?",
      ["A constructor that initializes an object using another object of the same class", "A constructor that duplicates a class bytecode", "A method that creates an exact clone on disk", "A constructor used exclusively in multi-threading"],
      "A constructor that initializes an object using another object of the same class", "Copy constructors create a new object by copying data members from an existing object.", "Medium"),
    q("What is the key distinction between shallow copy and deep copy of an object?",
      ["Shallow copy duplicates reference pointers, while deep copy recursively duplicates referenced objects", "Shallow copy works on heap; deep copy works on stack", "Deep copy is always done by the compiler automatically", "Shallow copy creates independent copies of all nested structures"],
      "Shallow copy duplicates reference pointers, while deep copy recursively duplicates referenced objects", "Shallow copy only copies top-level references, causing nested objects to be shared between copies.", "Medium"),
    q("What is object slicing in C++?",
      ["When a derived class object is assigned to a base class value, losing derived members", "When an object is split across two CPU cores", "When garbage collection fragments an object", "When private fields are exposed via reflection"],
      "When a derived class object is assigned to a base class value, losing derived members", "Object slicing occurs when assigning a derived object by value to a base object, discarding derived state.", "Medium"),
    q("What is the purpose of the 'final' keyword on a class in Java?",
      ["It prevents the class from being extended / subclassed", "It makes all methods static", "It forces the class to be abstract", "It allows the class to be garbage collected immediately"],
      "It prevents the class from being extended / subclassed", "Marking a class final prevents inheritance, ensuring its implementation cannot be altered.", "Medium"),

    # 10 Hard
    q("In managed runtimes (e.g. JVM/CLR), when does an object become eligible for garbage collection?",
      ["When it is no longer reachable through reference traversal from any GC roots", "As soon as its enclosing method returns, regardless of references", "When the CPU utilization exceeds 80%", "Only when the program explicitly terminates"],
      "When it is no longer reachable through reference traversal from any GC roots", "GC algorithms use reachability analysis starting from GC roots to find live objects.", "Hard"),
    q("How does dynamic memory layout of an object with virtual methods differ from a plain data struct in C++?",
      ["It contains an invisible virtual table pointer (vptr) prepended or appended to its layout", "It stores the source code of all virtual functions in the object", "It cannot contain primitive data types", "It is allocated on the stack instead of the heap"],
      "It contains an invisible virtual table pointer (vptr) prepended or appended to its layout", "Polymorphic objects include a vptr pointing to the class vtable to support dynamic dispatch.", "Hard"),
    q("What is the performance implication of false sharing in multi-threaded object manipulation?",
      ["Independent fields located on the same CPU cache line cause invalidation thrashing across cores", "Objects are mistakenly shared between threads leading to memory corruption", "The compiler creates unnecessary deep copies", "Memory leaks occur in the virtual method table"],
      "Independent fields located on the same CPU cache line cause invalidation thrashing across cores", "False sharing happens when threads modify independent variables residing on the same 64-byte cache line.", "Hard"),
    q("What is Compressed OOPs (Ordinary Object Pointers) in the 64-bit JVM?",
      ["A technique representing 64-bit heap references as 32-bit offsets by shifting them by 3 bits (8-byte alignment)", "A compression algorithm like gzip applied to serialized objects", "A tool to compress Java class files on disk", "A compiler optimization that removes private fields"],
      "A technique representing 64-bit heap references as 32-bit offsets by shifting them by 3 bits (8-byte alignment)", "Compressed OOPs allow 32-bit pointers to address up to 32GB of heap memory while reducing footprint.", "Hard"),
    q("How does Escape Analysis optimize object allocation in modern JIT compilers?",
      ["It allocates objects on the stack or scalar-replaces them if their reference does not escape the current method", "It moves long-lived objects to disk swap space", "It prevents objects from calling external libraries", "It disables garbage collection for all methods"],
      "It allocates objects on the stack or scalar-replaces them if their reference does not escape the current method", "Escape analysis determines if an object is accessible outside the creating scope, enabling stack allocation.", "Hard"),
    q("In C++, what is the consequence of declaring a member function 'static' with respect to name mangling and calling convention?",
      ["It omits the implicit 'this' pointer from the function argument list and uses standard calling convention", "It generates a polymorphic entry in the class vtable", "It makes the function executable only in kernel mode", "It changes its linkage from internal to inline"],
      "It omits the implicit 'this' pointer from the function argument list and uses standard calling convention", "Static member functions don't receive the hidden 'this' parameter, making their signatures identical to regular functions.", "Hard"),
    q("What problem does the Flyweight design pattern address regarding class and object instances?",
      ["Minimizing memory consumption by sharing common fine-grained object state across large numbers of objects", "Preventing more than one object from being instantiated globally", "Allowing objects to dynamically change their class at runtime", "Automating deep copying of hierarchical object graphs"],
      "Minimizing memory consumption by sharing common fine-grained object state across large numbers of objects", "Flyweight separates intrinsic (shared) state from extrinsic (context-dependent) state to support massive object counts.", "Hard"),
    q("What is the role of an Object Header in memory managed runtimes like HotSpot JVM?",
      ["It stores Mark Word (hash code, GC age, lock state) and Klass Word (pointer to metadata)", "It stores the source code comments and author name", "It holds the bytecode of the class methods", "It tracks network socket descriptors opened by the object"],
      "It stores Mark Word (hash code, GC age, lock state) and Klass Word (pointer to metadata)", "Hotspot object headers typically consist of two machine words: the Mark Word and the Klass Word.", "Hard"),
    q("Why can circular object references cause memory leaks in simple reference-counting garbage collectors?",
      ["Because the reference count of the mutually referencing objects never drops to zero", "Because circular references cause a stack overflow during invocation", "Because reference counters can only store prime numbers", "Because circular references trigger segmentation faults in the compiler"],
      "Because the reference count of the mutually referencing objects never drops to zero", "Reference counting fails to collect isolated cyclic groups because each object's refcount remains >= 1.", "Hard"),
    q("What is the Diamond Problem in object instantiation under multiple inheritance, and how is it resolved in C++?",
      ["Multiple inheritance causes duplicate copies of base subobjects; resolved using virtual inheritance", "The constructor runs infinitely; resolved by making base classes static", "Memory becomes corrupted; resolved using smart pointers", "Method names collide; resolved by deleting the base class"],
      "Multiple inheritance causes duplicate copies of base subobjects; resolved using virtual inheritance", "Virtual inheritance ensures only a single shared instance of the common ancestor base class is constructed.", "Hard")
]

print("Classes and Objects count:", len(topics_data["Classes and Objects"]))

