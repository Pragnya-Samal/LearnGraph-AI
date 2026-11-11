import { useState, useRef, useEffect } from 'react';
import { SparklesIcon, CloseIcon, SendIcon, BrainIcon } from './Icons';

const RESPONSES = [
  // --- Data Structures ---
  { keys: ['array'], reply: 'Arrays store elements at contiguous memory locations. Access by index is O(1), but insertion/deletion at the beginning is O(n) because all elements must shift.' },
  { keys: ['linked list'], reply: 'A Linked List is made of nodes, each holding data and a pointer to the next node. Head insertion is O(1), but searching is O(n). Doubly linked lists allow traversal in both directions.' },
  { keys: ['stack'], reply: 'A Stack follows LIFO (Last In First Out). Operations: push (add to top), pop (remove from top), peek. Used in function call management and undo operations.' },
  { keys: ['queue'], reply: 'A Queue follows FIFO (First In First Out). Operations: enqueue (add to rear), dequeue (remove from front). Used in BFS traversal and task scheduling.' },
  { keys: ['tree', 'bst', 'binary search tree'], reply: 'Trees are hierarchical structures with a root node and child nodes. A Binary Search Tree keeps smaller values left and larger values right, giving O(log n) average search. Traversals: Inorder (L→Root→R), Preorder, Postorder.' },
  { keys: ['graph'], reply: 'Graphs consist of vertices and edges. Directed graphs have one-way edges; undirected have two-way. BFS uses a queue for shortest path in unweighted graphs; DFS uses a stack/recursion.' },
  { keys: ['hashing', 'hash table', 'hash map'], reply: 'A Hash Table maps keys to indices using a hash function. Average O(1) for search/insert. Collisions are resolved by Chaining (linked lists at each index) or Open Addressing (linear probing).' },

  // --- Algorithms ---
  { keys: ['sorting', 'sort', 'quicksort', 'mergesort', 'bubble sort'], reply: 'Sorting algorithms: BubbleSort O(n²), SelectionSort O(n²), InsertionSort O(n²), MergeSort O(n log n) — stable, QuickSort O(n log n) average — divide and conquer. MergeSort is preferred for stability.' },
  { keys: ['searching', 'binary search', 'linear search'], reply: 'Linear Search checks every element — O(n). Binary Search requires a sorted array and checks the middle element each time — O(log n). Binary Search is much faster for large sorted datasets.' },
  { keys: ['dynamic programming', 'dp', 'memoization', 'tabulation'], reply: 'Dynamic Programming solves problems with overlapping subproblems and optimal substructure. Top-down uses recursion + memoization (caching results). Bottom-up uses iteration (tabulation). Classic examples: Fibonacci, Knapsack, Longest Common Subsequence.' },
  { keys: ['greedy'], reply: 'Greedy algorithms make the locally optimal choice at each step. Examples: Activity Selection, Dijkstra\'s shortest path, Huffman Coding. Greedy does not always give the globally optimal solution.' },
  { keys: ['backtracking'], reply: 'Backtracking tries all possible solutions and abandons (prunes) paths that cannot lead to a valid solution. Classic problems: N-Queens, Sudoku Solver, Subset Sum. It uses the call stack via recursion.' },

  // --- Database Systems ---
  { keys: ['er model', 'er diagram', 'entity relationship'], reply: 'ER Modeling represents entities (rectangles), attributes (ovals), and relationships (diamonds). Cardinality defines one-to-one, one-to-many, or many-to-many relationships. Primary keys uniquely identify each row.' },
  { keys: ['sql', 'select', 'database', 'query'], reply: 'SQL (Structured Query Language) is used to manage relational databases. Key commands: SELECT (retrieve), INSERT (add), UPDATE (modify), DELETE (remove). Use WHERE to filter rows, GROUP BY to aggregate, JOIN to combine tables.' },
  { keys: ['normalization', 'normal form', '1nf', '2nf', '3nf'], reply: 'Normalization reduces data redundancy. 1NF: atomic values, unique rows. 2NF: no partial dependencies (remove columns dependent on part of a composite key). 3NF: no transitive dependencies. BCNF is a stricter form of 3NF.' },
  { keys: ['transaction', 'acid', 'commit', 'rollback'], reply: 'Transactions follow ACID: Atomicity (all or nothing), Consistency (valid state), Isolation (concurrent transactions appear isolated), Durability (committed data persists). COMMIT saves changes; ROLLBACK undoes them.' },
  { keys: ['index', 'indexing', 'b-tree'], reply: 'Indexes speed up data retrieval using B-Tree structures. A clustered index physically sorts the table by the index key — only one per table. Non-clustered indexes are separate. Too many indexes slow down INSERT/UPDATE/DELETE.' },

  // --- Machine Learning ---
  { keys: ['linear regression'], reply: 'Linear Regression predicts a continuous value by fitting the best line that minimizes Mean Squared Error (MSE). R² score measures how well the model explains variance. Overfitting occurs when the model performs well on training data but poorly on new data.' },
  { keys: ['classification', 'logistic regression', 'knn', 'decision tree'], reply: 'Classification predicts a discrete class label. Algorithms: Logistic Regression (binary), KNN (majority vote of K neighbors), Decision Tree (rule-based splits), SVM. Evaluate using confusion matrix, precision, recall, and F1-score.' },
  { keys: ['clustering', 'k-means', 'unsupervised'], reply: 'Clustering is unsupervised learning — no labels needed. K-Means groups data into K clusters by minimizing distance to centroids. Use the Elbow Method to choose K. Unlike classification, clustering discovers patterns without predefined categories.' },
  { keys: ['neural network', 'deep learning', 'backpropagation', 'activation'], reply: 'Neural Networks are inspired by the human brain. Neurons apply weights to inputs and pass through an activation function (ReLU, Sigmoid, Tanh) to introduce non-linearity. Backpropagation calculates gradients and updates weights to minimize loss.' },
  { keys: ['evaluation', 'accuracy', 'precision', 'recall', 'f1', 'rmse', 'cross validation'], reply: 'Evaluation metrics: Accuracy = correct/total (misleading on imbalanced data). Precision = true positives / predicted positives. Recall = true positives / actual positives. F1 = harmonic mean of precision & recall. RMSE measures regression error. Cross-validation estimates generalization.' },

  // --- OOPS ---
  { keys: ['inheritance'], reply: 'Inheritance allows a child class to acquire properties and methods of a parent class, enabling code reusability. Types: Single, Multilevel, Hierarchical, Multiple. The child class can override parent methods.' },
  { keys: ['encapsulation'], reply: 'Encapsulation bundles data (fields) and methods inside a class and restricts direct access using access modifiers: private (class only), protected (subclasses), public (everywhere). Getters and setters provide controlled access to private data.' },
  { keys: ['polymorphism', 'overriding', 'overloading'], reply: 'Polymorphism means "one name, many forms". Compile-time polymorphism: method overloading (same name, different parameters). Runtime polymorphism: method overriding (child class redefines parent method, resolved at runtime via @Override in Java).' },
  { keys: ['abstraction', 'abstract class', 'interface'], reply: 'Abstraction hides implementation complexity and shows only essential details. Achieved via abstract classes (can have both abstract and concrete methods) and interfaces (only abstract methods by default). You cannot instantiate an abstract class directly.' },

  // --- Platform help ---
  { keys: ['assessment', 'test', 'quiz', 'exam'], reply: 'Go to the Learning page, select a subject and topic, then click Start Assessment. After submitting, you\'ll see your score, knowledge level, and a detailed review of each question with correct answers.' },
  { keys: ['recommendation', 'suggest', 'what to learn', 'next topic'], reply: 'Recommendations appear on your Dashboard after completing assessments. They are based on your performance and prerequisite relationships — e.g., complete Arrays before Trees is recommended.' },
  { keys: ['knowledge map', 'concept map'], reply: 'The Knowledge Map shows all curriculum concepts as interactive nodes. Click any node to see its description, prerequisites, and your current mastery level. You can filter by Strong, Uncertain, Weak, or Not Assessed.' },
  { keys: ['progress'], reply: 'The Progress page shows your overall average score, subject-level performance breakdown, strong concepts, and concepts needing attention — all based on your real assessment history.' },
  { keys: ['profile'], reply: 'Your Profile page shows your account details, performance statistics, and your current learner pathway classification (Beginner / Intermediate / Advanced) based on your average assessment score.' },
];

function getReply(text) {
  const lower = text.toLowerCase();
  for (const { keys, reply } of RESPONSES) {
    if (keys.some((k) => lower.includes(k))) return reply;
  }
  return "I can help with any topic in Data Structures, Algorithms, Database Systems, Machine Learning, or OOPS. Try asking about Arrays, Sorting, SQL, Neural Networks, Inheritance, or how to take an assessment!";
}

export default function AIAssistant() {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    { id: 1, sender: 'assistant', text: 'Hello! I am your AI Learning Assistant. Ask me about any topic — Arrays, Sorting, SQL, Neural Networks, Inheritance, and more!' },
  ]);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (isOpen) messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isOpen]);

  const handleSend = (e) => {
    e?.preventDefault();
    const userText = input.trim();
    if (!userText) return;

    setMessages((prev) => [...prev, { id: Date.now(), sender: 'user', text: userText }]);
    setInput('');

    setTimeout(() => {
      setMessages((prev) => [...prev, { id: Date.now() + 1, sender: 'assistant', text: getReply(userText) }]);
    }, 350);
  };

  const QUICK_PROMPTS = [
    { label: 'Arrays vs Linked Lists', text: 'Explain Arrays vs Linked Lists' },
    { label: 'Sorting Algorithms',     text: 'Explain sorting algorithms' },
    { label: 'What is SQL?',           text: 'Explain SQL basics' },
    { label: 'OOPS Concepts',          text: 'Explain inheritance and encapsulation' },
    { label: 'Neural Networks',        text: 'How do neural networks work?' },
    { label: 'Assessment Help',        text: 'How do I take an assessment?' },
  ];

  return (
    <>
      <button className="ai-assistant-toggle" onClick={() => setIsOpen(!isOpen)} aria-label="Open AI Learning Assistant">
        <SparklesIcon size={18} />
        <span>AI Assistant</span>
      </button>

      {isOpen && (
        <div className="ai-assistant-panel">
          <div className="ai-assistant-header">
            <div className="ai-assistant-title">
              <BrainIcon size={20} />
              <span>AI Learning Assistant</span>
            </div>
            <button className="ai-assistant-close" onClick={() => setIsOpen(false)} aria-label="Close Assistant">
              <CloseIcon size={18} />
            </button>
          </div>

          <div className="ai-assistant-messages">
            {messages.map((msg) => (
              <div key={msg.id} className={`ai-msg ${msg.sender}`}>{msg.text}</div>
            ))}
            <div ref={messagesEndRef} />
          </div>

          <div className="ai-quick-prompts">
            {QUICK_PROMPTS.map((p) => (
              <button key={p.label} className="ai-prompt-chip" onClick={() => setInput(p.text)}>
                {p.label}
              </button>
            ))}
          </div>

          <form onSubmit={handleSend} className="ai-assistant-input-bar">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about any topic..."
              className="ai-assistant-input"
            />
            <button type="submit" className="ai-send-btn" aria-label="Send message">
              <SendIcon size={16} />
            </button>
          </form>
        </div>
      )}
    </>
  );
}
