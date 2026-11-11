"""Data Structures Question Bank - 10 Topics, 30 Questions Each (10 Easy, 10 Medium, 10 Hard)"""

dsa_questions = {'Arrays and Memory Layouts': [{'correct_answer': 'Contiguous block of memory with elements stored at consecutive '
                                                  'memory addresses',
                                'difficulty': 'Easy',
                                'explanation': 'Arrays allocate sequential memory locations, enabling constant-time '
                                               'indexing arithmetic.',
                                'options': ['Contiguous block of memory with elements stored at consecutive memory '
                                            'addresses',
                                            'Scattered nodes connected via pointers across the heap',
                                            'Dynamic memory that automatically changes size without reallocation',
                                            'Non-linear memory mapped as a graph'],
                                'question': 'What is the primary memory characteristic of an array?'},
                               {'correct_answer': 'O(1) - Constant time',
                                'difficulty': 'Easy',
                                'explanation': 'Because elements are in contiguous memory, address = base_address + '
                                               '(index * element_size) computes in O(1).',
                                'options': ['O(1) - Constant time',
                                            'O(n) - Linear time',
                                            'O(log n) - Logarithmic time',
                                            'O(n^2) - Quadratic time'],
                                'question': 'What is the time complexity of accessing an element in an array by its '
                                            'index?'},
                               {'correct_answer': 'O(n) because all existing elements must be shifted right',
                                'difficulty': 'Easy',
                                'explanation': 'Inserting at index 0 requires shifting n elements one position to the '
                                               'right.',
                                'options': ['O(n) because all existing elements must be shifted right',
                                            'O(1) because array indexing is constant time',
                                            'O(log n) using binary search',
                                            'O(n log n)'],
                                'question': 'What is the time complexity of inserting an element at the beginning of '
                                            'an unsorted fixed-size array of size n?'},
                               {'correct_answer': 'O(1)',
                                'difficulty': 'Easy',
                                'explanation': 'Appending to the end of an array with available capacity takes '
                                               'constant time O(1).',
                                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n^2)'],
                                'question': 'What is the time complexity of inserting an element at the end of an '
                                            'array when space is available?'},
                               {'correct_answer': 'An ArrayIndexOutOfBoundsException is thrown at runtime',
                                'difficulty': 'Easy',
                                'explanation': 'Java performs runtime boundary checks and throws an exception on '
                                               'invalid indices.',
                                'options': ['An ArrayIndexOutOfBoundsException is thrown at runtime',
                                            'The program silently returns 0',
                                            'The system kernel restarts',
                                            'The array automatically expands'],
                                'question': 'What happens when an array index is accessed outside its valid bounds [0, '
                                            'n-1] in Java?'},
                               {'correct_answer': 'Undefined behavior (reads garbage or causes segmentation fault / '
                                                  'memory corruption)',
                                'difficulty': 'Easy',
                                'explanation': 'C/C++ does not perform bounds checking on raw arrays, resulting in '
                                               'undefined behavior.',
                                'options': ['Undefined behavior (reads garbage or causes segmentation fault / memory '
                                            'corruption)',
                                            'The compiler throws a SyntaxError',
                                            'The array doubles in capacity',
                                            'The CPU enters sleep mode'],
                                'question': 'In C or C++, what happens when you access an array index beyond its '
                                            'allocated size?'},
                               {'correct_answer': '9',
                                'difficulty': 'Easy',
                                'explanation': 'In 0-based indexing, valid indices range from 0 to length - 1.',
                                'options': ['9', '10', '11', '0'],
                                'question': 'In a 0-indexed array of length 10, what is the valid index of the last '
                                            'element?'},
                               {'correct_answer': 'An array whose size is fixed at allocation time and cannot change '
                                                  'during runtime',
                                'difficulty': 'Easy',
                                'explanation': 'Static arrays have a fixed capacity determined at compilation or '
                                               'creation time.',
                                'options': ['An array whose size is fixed at allocation time and cannot change during '
                                            'runtime',
                                            'An array that changes size automatically',
                                            'An array stored on an external hard drive',
                                            'An array that can store mixed data types'],
                                'question': 'What is a static array?'},
                               {'correct_answer': 'O(n) linear search',
                                'difficulty': 'Easy',
                                'explanation': 'In the worst case, every element must be inspected sequentially.',
                                'options': ['O(n) linear search',
                                            'O(1) direct access',
                                            'O(log n) binary search',
                                            'O(n!) factorial search'],
                                'question': 'What is the time complexity of searching for an element in an unsorted '
                                            'array of size n?'},
                               {'correct_answer': 'Contiguous memory layout enables CPU cache lines to prefetch '
                                                  'adjacent elements into L1/L2 cache',
                                'difficulty': 'Easy',
                                'explanation': 'Spatial locality allows the CPU hardware prefetcher to load subsequent '
                                               'elements into cache effectively.',
                                'options': ['Contiguous memory layout enables CPU cache lines to prefetch adjacent '
                                            'elements into L1/L2 cache',
                                            'Arrays use less RAM than registers',
                                            'Arrays prevent all page faults',
                                            'Array indices are stored on the GPU'],
                                'question': 'Why do arrays exhibit excellent cache locality?'},
                               {'correct_answer': 'base + (i * C + j) * element_size',
                                'difficulty': 'Medium',
                                'explanation': 'In row-major order, each row of length C is laid out consecutively.',
                                'options': ['base + (i * C + j) * element_size',
                                            'base + (j * R + i) * element_size',
                                            'base + (i + j) * element_size',
                                            'base + (i * j) * element_size'],
                                'question': 'In a 2D array arr[R][C] stored in Row-Major order, how is the memory '
                                            'address of arr[i][j] calculated?'},
                               {'correct_answer': 'base + (j * R + i) * element_size',
                                'difficulty': 'Medium',
                                'explanation': 'Column-major stores entire columns sequentially, so column j is '
                                               'preceded by j * R elements.',
                                'options': ['base + (j * R + i) * element_size',
                                            'base + (i * C + j) * element_size',
                                            'base + (i + j * C) * element_size',
                                            'base + (i * j * R) * element_size'],
                                'question': 'In a 2D array arr[R][C] stored in Column-Major order (e.g. Fortran, '
                                            'MATLAB), how is element arr[i][j] located?'},
                               {'correct_answer': 'O(1) amortized',
                                'difficulty': 'Medium',
                                'explanation': 'Dynamic arrays double their capacity upon filling, yielding O(1) '
                                               'amortized append complexity.',
                                'options': ['O(1) amortized', 'O(n) every single time', 'O(log n)', 'O(n^2)'],
                                'question': 'What is the amortized time complexity of appending an element to a '
                                            'dynamic array (like Python list or C++ std::vector)?'},
                               {'correct_answer': 'O(n) to allocate new buffer and copy n elements',
                                'difficulty': 'Medium',
                                'explanation': 'The resizing operation requires allocating new memory and copying all '
                                               'existing elements.',
                                'options': ['O(n) to allocate new buffer and copy n elements',
                                            'O(1)',
                                            'O(log n)',
                                            'O(n log n)'],
                                'question': 'When a dynamic array doubles its capacity during resize, what is the cost '
                                            'of that specific insertion?'},
                               {'correct_answer': 'Row-by-row accesses memory sequentially matching row-major layout, '
                                                  'minimizing CPU cache misses',
                                'difficulty': 'Medium',
                                'explanation': 'Row-major storage ensures adjacent loop iterations access adjacent '
                                               'cache line bytes.',
                                'options': ['Row-by-row accesses memory sequentially matching row-major layout, '
                                            'minimizing CPU cache misses',
                                            'Column-by-column uses more registers',
                                            'Row-by-row disables loop checking',
                                            'C++ compilers ignore columns'],
                                'question': 'Why is iterating through a 2D array row-by-row faster than '
                                            'column-by-column in C/C++?'},
                               {'correct_answer': 'An array of arrays where member sub-arrays can have differing '
                                                  'lengths',
                                'difficulty': 'Medium',
                                'explanation': 'Jagged arrays store arrays of references to independent rows of '
                                               'varying lengths.',
                                'options': ['An array of arrays where member sub-arrays can have differing lengths',
                                            'An array with broken memory sectors',
                                            'A 1D array sorted in zigzag order',
                                            'An array that contains only odd numbers'],
                                'question': 'What is a Jagged Array (Ragged Array)?'},
                               {'correct_answer': 'Unused allocated buffer capacity (typically up to 50% extra memory)',
                                'difficulty': 'Medium',
                                'explanation': 'Geometric resizing leaves unused slots between current size and '
                                               'allocated capacity.',
                                'options': ['Unused allocated buffer capacity (typically up to 50% extra memory)',
                                            'Pointers for every single element',
                                            'Separate thread headers',
                                            'Doubled bit-width of elements'],
                                'question': 'What is the space overhead of a dynamic array compared to a fixed array?'},
                               {'correct_answer': 'O(n - i) to shift trailing elements left',
                                'difficulty': 'Medium',
                                'explanation': 'Elements after index i must be shifted left by one position to fill '
                                               'the gap.',
                                'options': ['O(n - i) to shift trailing elements left', 'O(1)', 'O(log n)', 'O(n^2)'],
                                'question': 'What is the time complexity of deleting an element at index i from an '
                                            'array of size n?'},
                               {'correct_answer': 'By halving the search interval on each comparison',
                                'difficulty': 'Medium',
                                'explanation': 'Direct index arithmetic allows jumping to the middle element in O(1), '
                                               'halving the space repeatedly.',
                                'options': ['By halving the search interval on each comparison',
                                            'By pre-scanning all elements in parallel',
                                            'By hashing keys to indices',
                                            'By traversing elements backwards'],
                                'question': 'How does binary search achieve O(log n) time complexity on a sorted '
                                            'array?'},
                               {'correct_answer': 'Misaligned memory accesses cause hardware penalties or bus error '
                                                  'faults on architectures like ARM',
                                'difficulty': 'Medium',
                                'explanation': 'CPUs fetch data in word-sized chunks; misaligned data forces multiple '
                                               'memory fetches.',
                                'options': ['Misaligned memory accesses cause hardware penalties or bus error faults '
                                            'on architectures like ARM',
                                            'Aligned arrays use zero RAM',
                                            'Unaligned arrays cannot store negative numbers',
                                            'Memory alignment is only required for strings'],
                                'question': 'In low-level systems, why must array data structures respect CPU memory '
                                            'alignment (e.g. 4-byte or 8-byte boundaries)?'},
                               {'correct_answer': 'A growth factor < 2 allows reusing previously deallocated memory '
                                                  'blocks from prior resizes',
                                'difficulty': 'Hard',
                                'explanation': 'If growth factor >= 2, the sum of all previous chunk sizes is strictly '
                                               'less than the next chunk size, preventing memory reuse.',
                                'options': ['A growth factor < 2 allows reusing previously deallocated memory blocks '
                                            'from prior resizes',
                                            '1.5 consumes less CPU instructions to multiply',
                                            'Growth factor 2.0 triggers integer overflow',
                                            'Growth factor 1.5 disables garbage collection'],
                                'question': 'Why is a growth factor of 1.5 (e.g. MSVC vector) or 1.618 often preferred '
                                            'over 2.0 in dynamic array implementations?'},
                               {'correct_answer': 'SoA stores homogeneous fields consecutively, allowing vector '
                                                  'registers (AVX/NEON) to load data in single instructions without '
                                                  'striding',
                                'difficulty': 'Hard',
                                'explanation': 'SoA aligns identical attributes contiguously, optimizing vectorization '
                                               'pipelines.',
                                'options': ['SoA stores homogeneous fields consecutively, allowing vector registers '
                                            '(AVX/NEON) to load data in single instructions without striding',
                                            'AoS is always faster for GPU compute',
                                            'SoA cannot store floating point values',
                                            'AoS uses no memory padding'],
                                'question': 'What is the difference between Array of Structures (AoS) and Structure of '
                                            'Arrays (SoA) for SIMD vectorization?'},
                               {'correct_answer': 'Concurrent threads accessing different addresses in the same memory '
                                                  'bank are serialized, degrading throughput',
                                'difficulty': 'Hard',
                                'explanation': 'Shared memory is divided into banks; simultaneous requests to the same '
                                               'bank cause bank conflict stalls.',
                                'options': ['Concurrent threads accessing different addresses in the same memory bank '
                                            'are serialized, degrading throughput',
                                            'Bank conflicts cause permanent hardware failure',
                                            'Memory banks only store operating system kernels',
                                            'Bank conflicts corrupt floating point numbers'],
                                'question': 'How does memory bank conflict impact access latency in multi-channel or '
                                            'GPU shared memory arrays?'},
                               {'correct_answer': 'A fixed-size array using modulo arithmetic (index % capacity) to '
                                                  'implement a FIFO queue with O(1) head and tail operations',
                                'difficulty': 'Hard',
                                'explanation': 'Ring buffers wrap head and tail pointers seamlessly using modulo '
                                               'indexing without shifting elements.',
                                'options': ['A fixed-size array using modulo arithmetic (index % capacity) to '
                                            'implement a FIFO queue with O(1) head and tail operations',
                                            'An array bent in a physical circle',
                                            'An array that cannot be written to',
                                            'A circular linked list stored in ROM'],
                                'question': 'What is a Circular Buffer (Ring Buffer) implemented over an array?'},
                               {'correct_answer': 'Multiple CPU cores writing to adjacent array elements on the same '
                                                  "cache line repeatedly invalidate each other's L1 cache (false "
                                                  'sharing)',
                                'difficulty': 'Hard',
                                'explanation': 'Modifying separate variables on the same 64-byte line invalidates '
                                               'cache state across core interconnects.',
                                'options': ['Multiple CPU cores writing to adjacent array elements on the same cache '
                                            "line repeatedly invalidate each other's L1 cache (false sharing)",
                                            'Cache lines physically disconnect from CPU',
                                            'The operating system drops cache pages',
                                            'Threads crash with SIGBUS'],
                                'question': 'What is the cache line bouncing phenomenon in multi-threaded array '
                                            'operations?'},
                               {'correct_answer': 'It packs 8 boolean flags into each byte using bitwise shifts and '
                                                  'masks, using 1/8th the memory of bool arrays',
                                'difficulty': 'Hard',
                                'explanation': 'A standard bool takes 1 byte (8 bits); bitsets use exactly 1 bit per '
                                               'boolean.',
                                'options': ['It packs 8 boolean flags into each byte using bitwise shifts and masks, '
                                            'using 1/8th the memory of bool arrays',
                                            'It compresses bytes with zip algorithms',
                                            'It stores booleans in registers only',
                                            'It uses floating point numbers for true and false'],
                                'question': 'How does a Bitset (Bit Array) achieve optimal space efficiency for '
                                            'boolean flags?'},
                               {'correct_answer': 'An array storing prefix sum frequencies allowing both prefix sum '
                                                  'queries and point updates in O(log n) time and O(n) space',
                                'difficulty': 'Hard',
                                'explanation': 'Fenwick trees store cumulative tree data inside a flat 1D array using '
                                               'bitwise least significant bit arithmetic.',
                                'options': ['An array storing prefix sum frequencies allowing both prefix sum queries '
                                            'and point updates in O(log n) time and O(n) space',
                                            'An array that requires O(n^2) space',
                                            'A tree that requires pointer nodes on heap',
                                            'A static array that cannot be updated'],
                                'question': 'What is the Fenwick Tree (Binary Indexed Tree) array representation and '
                                            'its operational complexities?'},
                               {'correct_answer': 'Tiling / cache-blocking divides large matrices into sub-blocks that '
                                                  'fit into L1/L2 cache, preventing high stride cache thrashing',
                                'difficulty': 'Hard',
                                'explanation': 'Cache-oblivious matrix algorithms block arrays to maintain high '
                                               'temporal and spatial locality.',
                                'options': ['Tiling / cache-blocking divides large matrices into sub-blocks that fit '
                                            'into L1/L2 cache, preventing high stride cache thrashing',
                                            'Striding skips odd elements to speed up multiplication',
                                            'Strides reduce matrix dimensions',
                                            'Striding converts matrices to linked lists'],
                                'question': 'In memory management, what is the role of memory strides in matrix '
                                            'transposition algorithms?'},
                               {'correct_answer': 'O(n) time and O(1) auxiliary space',
                                'difficulty': 'Hard',
                                'explanation': "Kadane's algorithm maintains current max and global max in a single "
                                               'linear scan.',
                                'options': ['O(n) time and O(1) auxiliary space',
                                            'O(n log n) time and O(n) space',
                                            'O(n^2) time and O(1) space',
                                            'O(2^n) time and O(n) space'],
                                'question': 'What is the time and space complexity of finding the maximum subarray sum '
                                            "using Kadane's algorithm on a 1D array?"},
                               {'correct_answer': 'By directly addressing off-heap native memory addresses via 64-bit '
                                                  'pointers without garbage collection pauses or object header '
                                                  'overhead',
                                'difficulty': 'Hard',
                                'explanation': 'Off-heap memory access avoids GC overhead while enabling ultra-fast '
                                               'direct memory manipulation.',
                                'options': ['By directly addressing off-heap native memory addresses via 64-bit '
                                            'pointers without garbage collection pauses or object header overhead',
                                            'By converting arrays to string bytecodes',
                                            'By running code in kernel mode',
                                            'By disabling CPU memory management'],
                                'question': "How does Java's Unsafe / Foreign Function & Memory API (Project Panama) "
                                            'access off-heap native memory arrays?'}],
 'Binary Search Trees (BST)': [{'correct_answer': 'For any node, all keys in its left subtree are less, and all keys '
                                                  'in its right subtree are greater',
                                'difficulty': 'Easy',
                                'explanation': 'The BST invariant guarantees that left < root < right across all '
                                               'subtrees.',
                                'options': ['For any node, all keys in its left subtree are less, and all keys in its '
                                            'right subtree are greater',
                                            'All nodes have identical values',
                                            'The tree is always complete',
                                            'Leaves have higher values than root'],
                                'question': 'What is the defining property of a Binary Search Tree (BST)?'},
                               {'correct_answer': 'Inorder Traversal',
                                'difficulty': 'Easy',
                                'explanation': 'Visiting left subtree, root, then right subtree processes values in '
                                               'ascending sorted order.',
                                'options': ['Inorder Traversal',
                                            'Preorder Traversal',
                                            'Postorder Traversal',
                                            'Level-Order Traversal'],
                                'question': 'What traversal of a Binary Search Tree produces values in strictly sorted '
                                            'ascending order?'},
                               {'correct_answer': 'O(log n)',
                                'difficulty': 'Easy',
                                'explanation': 'Each comparison eliminates half of the remaining search space when the '
                                               'tree is balanced.',
                                'options': ['O(log n)', 'O(1)', 'O(n)', 'O(n log n)'],
                                'question': 'What is the average time complexity of search, insertion, and deletion in '
                                            'a balanced BST?'},
                               {'correct_answer': 'O(n) - Linear time',
                                'difficulty': 'Easy',
                                'explanation': 'Inserting sorted elements into an unbalancing BST creates a linked '
                                               'list of height n.',
                                'options': ['O(n) - Linear time', 'O(log n)', 'O(1)', 'O(n^2)'],
                                'question': 'What is the worst-case time complexity of searching in an unbalanced '
                                            '(skewed) BST?'},
                               {'correct_answer': 'The leftmost node in the tree (follow left pointers until left is '
                                                  'null)',
                                'difficulty': 'Easy',
                                'explanation': 'Because left children are strictly smaller, continuing left leads to '
                                               'the minimum element.',
                                'options': ['The leftmost node in the tree (follow left pointers until left is null)',
                                            'The root node',
                                            'The rightmost node',
                                            'Any leaf node'],
                                'question': 'Where is the minimum value located in a Binary Search Tree?'},
                               {'correct_answer': 'The rightmost node in the tree (follow right pointers until right '
                                                  'is null)',
                                'difficulty': 'Easy',
                                'explanation': 'Following right pointers leads to the largest element in the BST.',
                                'options': ['The rightmost node in the tree (follow right pointers until right is '
                                            'null)',
                                            'The root node',
                                            'The leftmost node',
                                            'At level 1'],
                                'question': 'Where is the maximum value located in a Binary Search Tree?'},
                               {'correct_answer': 'The minimum node in its right subtree (leftmost node of right '
                                                  'child)',
                                'difficulty': 'Easy',
                                'explanation': 'The next larger key is the smallest key in the right subtree.',
                                'options': ['The minimum node in its right subtree (leftmost node of right child)',
                                            'Its parent node',
                                            'Its left child',
                                            'The root node'],
                                'question': 'What is the in-order successor of a node with a non-empty right subtree '
                                            'in a BST?'},
                               {'correct_answer': 'The maximum node in its left subtree (rightmost node of left child)',
                                'difficulty': 'Easy',
                                'explanation': 'The next smaller key is the largest key in the left subtree.',
                                'options': ['The maximum node in its left subtree (rightmost node of left child)',
                                            'Its right child',
                                            'The root node',
                                            'Its deepest descendant'],
                                'question': 'What is the in-order predecessor of a node with a non-empty left subtree '
                                            'in a BST?'},
                               {'correct_answer': 'Replace its value with its in-order successor (or predecessor), '
                                                  'then delete that successor from the subtree',
                                'difficulty': 'Easy',
                                'explanation': 'Replacing with the successor preserves the BST invariant while '
                                               'reducing deletion to a 0- or 1-child case.',
                                'options': ['Replace its value with its in-order successor (or predecessor), then '
                                            'delete that successor from the subtree',
                                            'Delete both subtrees',
                                            'Move the root to the deleted node',
                                            'Convert the tree to an array'],
                                'question': 'How is a node with two children deleted from a BST?'},
                               {'correct_answer': 'Typically no; duplicates are either ignored, counted in a frequency '
                                                  'field, or routed to one side consistently',
                                'difficulty': 'Easy',
                                'explanation': 'Standard BST definitions require strict inequality (left < root < '
                                               'right).',
                                'options': ['Typically no; duplicates are either ignored, counted in a frequency '
                                            'field, or routed to one side consistently',
                                            'Yes, in the same node',
                                            'Yes, duplicates must become roots',
                                            'BSTs can only store duplicates'],
                                'question': 'Can duplicate keys be stored in a standard textbook BST?'},
                               {'correct_answer': 'A self-balancing BST where the height difference (balance factor) '
                                                  'between left and right subtrees is at most 1 for every node',
                                'difficulty': 'Medium',
                                'explanation': 'AVL trees maintain strict balance (balance factor in {-1, 0, 1}) via '
                                               'rotations.',
                                'options': ['A self-balancing BST where the height difference (balance factor) between '
                                            'left and right subtrees is at most 1 for every node',
                                            'A tree that allows 3 children per node',
                                            'A tree used to store audio files',
                                            'A tree with no rotations'],
                                'question': 'What is an AVL Tree?'},
                               {'correct_answer': 'Left-Left (LL), Right-Right (RR), Left-Right (LR), and Right-Left '
                                                  '(RL)',
                                'difficulty': 'Medium',
                                'explanation': 'Single rotations resolve LL/RR cases; double rotations resolve LR/RL '
                                               'zigzag cases.',
                                'options': ['Left-Left (LL), Right-Right (RR), Left-Right (LR), and Right-Left (RL)',
                                            'Up, Down, Left, Right',
                                            'Clockwise, Counter-clockwise, Flip, Slide',
                                            'Single, Double, Triple, Quad'],
                                'question': 'What are the four types of tree rotations used to restore balance in an '
                                            'AVL Tree?'},
                               {'correct_answer': 'A self-balancing BST where nodes are colored Red or Black, ensuring '
                                                  'no red node has a red child and black-height is equal across paths',
                                'difficulty': 'Medium',
                                'explanation': 'Red-black properties guarantee the longest path is at most twice the '
                                               'length of the shortest path.',
                                'options': ['A self-balancing BST where nodes are colored Red or Black, ensuring no '
                                            'red node has a red child and black-height is equal across paths',
                                            'A tree colored for terminal graphics',
                                            'A tree that only stores binary bits',
                                            'A tree with no height guarantees'],
                                'question': 'What is a Red-Black Tree?'},
                               {'correct_answer': '2 * log2(n + 1)',
                                'difficulty': 'Medium',
                                'explanation': 'Red-black trees guarantee height <= 2 * log2(n + 1), ensuring O(log n) '
                                               'operations.',
                                'options': ['2 * log2(n + 1)', 'n / 2', 'log2(n) exactly', 'n^2'],
                                'question': 'What is the maximum height of a Red-Black Tree with n internal nodes?'},
                               {'correct_answer': 'AVL trees are more rigidly balanced (faster lookups); Red-Black '
                                                  'trees require fewer rotations on insert/delete (faster mutations)',
                                'difficulty': 'Medium',
                                'explanation': "Java's TreeMap and C++'s std::map choose Red-Black trees for superior "
                                               'insertion/deletion performance.',
                                'options': ['AVL trees are more rigidly balanced (faster lookups); Red-Black trees '
                                            'require fewer rotations on insert/delete (faster mutations)',
                                            'Red-Black trees take O(n) search',
                                            'AVL trees cannot store strings',
                                            'They have identical rotation behavior'],
                                'question': 'How does a Red-Black Tree compare to an AVL Tree in practice?'},
                               {'correct_answer': 'Perform DFS passing valid range (min_val, max_val); verify node.val '
                                                  'is strictly between bounds and recurse on children',
                                'difficulty': 'Medium',
                                'explanation': 'Checking immediate children is insufficient; subtrees must honor '
                                               'global ancestral bounds.',
                                'options': ['Perform DFS passing valid range (min_val, max_val); verify node.val is '
                                            'strictly between bounds and recurse on children',
                                            'Check if root > left and root < right only at root',
                                            'Count total nodes in tree',
                                            'Check if tree has no cycles'],
                                'question': 'How do you validate if a given binary tree is a valid Binary Search '
                                            'Tree?'},
                               {'correct_answer': 'Traverse from root: if both p and q are smaller, go left; if both '
                                                  'greater, go right; otherwise current node is LCA',
                                'difficulty': 'Medium',
                                'explanation': 'The first node where paths to p and q diverge is their Lowest Common '
                                               'Ancestor in a BST.',
                                'options': ['Traverse from root: if both p and q are smaller, go left; if both '
                                            'greater, go right; otherwise current node is LCA',
                                            'Use a hash map to store all ancestors',
                                            "Run Dijkstra's algorithm",
                                            'Count depths of p and q'],
                                'question': 'How can you find the Lowest Common Ancestor (LCA) of two nodes p and q in '
                                            'a BST in O(h) time?'},
                               {'correct_answer': 'Perform an iterative Inorder traversal and decrement k on each '
                                                  'visited node; return when k reaches 0',
                                'difficulty': 'Medium',
                                'explanation': 'Inorder traversal visits elements in ascending order, so the k-th '
                                               'visited node is the k-th smallest.',
                                'options': ['Perform an iterative Inorder traversal and decrement k on each visited '
                                            'node; return when k reaches 0',
                                            'Sort all elements using quicksort',
                                            'Find root and subtract k',
                                            'Check the k-th leaf node'],
                                'question': 'How can you find the k-th smallest element in a BST in O(k + h) time?'},
                               {'correct_answer': 'O(n) time by picking the middle element as root and recursing on '
                                                  'left and right halves',
                                'difficulty': 'Medium',
                                'explanation': 'Divide and conquer creates balanced subtrees in linear time.',
                                'options': ['O(n) time by picking the middle element as root and recursing on left and '
                                            'right halves',
                                            'O(n log n) time',
                                            'O(n^2) time',
                                            'O(log n) time'],
                                'question': 'What is the time complexity of converting a sorted array into a '
                                            'height-balanced BST?'},
                               {'correct_answer': 'A self-adjusting BST that moves recently accessed nodes to the root '
                                                  'via splaying rotations, achieving O(log n) amortized time',
                                'difficulty': 'Medium',
                                'explanation': 'Splay trees exploit temporal locality: frequently accessed items '
                                               'remain near the root.',
                                'options': ['A self-adjusting BST that moves recently accessed nodes to the root via '
                                            'splaying rotations, achieving O(log n) amortized time',
                                            'A tree stored in linear arrays',
                                            'A tree with 4-way branching',
                                            'A static tree that cannot be modified'],
                                'question': 'What is a Splay Tree?'},
                               {'correct_answer': 'A randomized data structure where keys satisfy the BST property and '
                                                  'randomly assigned priorities satisfy the Max-Heap property',
                                'difficulty': 'Hard',
                                'explanation': 'Randomized priorities prevent degenerate trees, guaranteeing O(log n) '
                                               'expected operations.',
                                'options': ['A randomized data structure where keys satisfy the BST property and '
                                            'randomly assigned priorities satisfy the Max-Heap property',
                                            'A tree used to store file paths',
                                            'A ternary search tree',
                                            'A tree with no root'],
                                'question': 'What is a Treap (Tree-Heap)?'},
                               {'correct_answer': 'A multi-way balanced search tree with high branching factor that '
                                                  'minimizes slow disk I/O reads by matching node size to page size',
                                'difficulty': 'Hard',
                                'explanation': 'High fanout makes B-trees very shallow, reducing expensive disk head '
                                               'seeks.',
                                'options': ['A multi-way balanced search tree with high branching factor that '
                                            'minimizes slow disk I/O reads by matching node size to page size',
                                            'A binary tree with red and black nodes',
                                            'A tree stored in memory caches only',
                                            'A tree that does not support range queries'],
                                'question': 'What is a B-Tree and why is it preferred over BSTs for database storage '
                                            'engines and filesystems?'},
                               {'correct_answer': 'All data records are stored exclusively in leaf nodes linked '
                                                  'sequentially, enabling ultra-fast range scans while internal nodes '
                                                  'store keys only',
                                'difficulty': 'Hard',
                                'explanation': 'Leaf chaining enables linear range scans without traversing internal '
                                               'tree nodes.',
                                'options': ['All data records are stored exclusively in leaf nodes linked '
                                            'sequentially, enabling ultra-fast range scans while internal nodes store '
                                            'keys only',
                                            'B+ trees store data only at the root',
                                            'B+ trees have no leaf nodes',
                                            'B+ trees cannot store strings'],
                                'question': 'What is the B+ Tree variation and its advantage over standard B-Trees?'},
                               {'correct_answer': 'A balanced BST augmented with subtree size metadata in each node, '
                                                  'allowing finding k-th smallest element and rank in O(log n) time',
                                'difficulty': 'Hard',
                                'explanation': 'Subtree size fields allow skipping entire subtrees during rank '
                                               'selection in O(log n).',
                                'options': ['A balanced BST augmented with subtree size metadata in each node, '
                                            'allowing finding k-th smallest element and rank in O(log n) time',
                                            'A tree that sorts numbers in linear time',
                                            'A tree with no duplicate keys',
                                            'A tree that logs every operation'],
                                'question': 'What is an Order Statistic Tree?'},
                               {'correct_answer': 'A self-balancing search tree where nodes can have 2, 3, or 4 '
                                                  'children; isometrically equivalent to Red-Black Trees',
                                'difficulty': 'Hard',
                                'explanation': 'Red-black trees are binary representations of 2-3-4 trees, where red '
                                               'edges glue 3- and 4-nodes.',
                                'options': ['A self-balancing search tree where nodes can have 2, 3, or 4 children; '
                                            'isometrically equivalent to Red-Black Trees',
                                            'A tree with 24 leaves',
                                            'A tree used in quantum physics',
                                            'A tree with no balance rules'],
                                'question': 'What is a 2-3-4 Tree and what is its direct equivalence in binary search '
                                            'trees?'},
                               {'correct_answer': "By starting search from a previously specified 'finger' node "
                                                  'pointer rather than the root, taking O(log d) where d is distance '
                                                  'between nodes',
                                'difficulty': 'Hard',
                                'explanation': 'Finger searches exploit spatial locality when queries target keys near '
                                               'recent accesses.',
                                'options': ["By starting search from a previously specified 'finger' node pointer "
                                            'rather than the root, taking O(log d) where d is distance between nodes',
                                            'By using touchscreen hardware',
                                            'By guessing random nodes',
                                            'By searching leaves first'],
                                'question': 'How does finger search optimize lookups in augmented search trees?'},
                               {'correct_answer': 'Color flip: recolor parent and uncle to Black, recolor grandparent '
                                                  'to Red, and continue checks upward',
                                'difficulty': 'Hard',
                                'explanation': 'When uncle is red, a color flip pushes the red violation two levels up '
                                               'the tree without rotations.',
                                'options': ['Color flip: recolor parent and uncle to Black, recolor grandparent to '
                                            'Red, and continue checks upward',
                                            'Perform a double rotation immediately',
                                            'Delete the uncle node',
                                            'Rebalance the entire heap'],
                                'question': "In Red-Black Trees, what happens during insertion when the new node's "
                                            'parent and uncle are BOTH red?'},
                               {'correct_answer': 'It transforms an unbalanced BST into a degenerate linked list '
                                                  '(vine) via right rotations, then performs left rotations to produce '
                                                  'a balanced tree in O(n) time and O(1) space',
                                'difficulty': 'Hard',
                                'explanation': 'DSW balances arbitrary BSTs in-place in linear time with zero extra '
                                               'heap memory.',
                                'options': ['It transforms an unbalanced BST into a degenerate linked list (vine) via '
                                            'right rotations, then performs left rotations to produce a balanced tree '
                                            'in O(n) time and O(1) space',
                                            'It runs quicksort on tree pointers',
                                            'It uses an auxiliary array of size n',
                                            'It randomly deletes nodes'],
                                'question': 'What is Day-Stout-Warren (DSW) algorithm for balancing an arbitrary BST?'},
                               {'correct_answer': 'It monitors tree sizes and rebuilds the highest scapegoat subtree '
                                                  'from scratch whenever an insertion causes height to exceed an alpha '
                                                  'factor',
                                'difficulty': 'Hard',
                                'explanation': 'Scapegoat trees store zero per-node balance overhead, achieving '
                                               'amortized O(log n) operations.',
                                'options': ['It monitors tree sizes and rebuilds the highest scapegoat subtree from '
                                            'scratch whenever an insertion causes height to exceed an alpha factor',
                                            'It deletes corrupted nodes',
                                            'It balances nodes randomly',
                                            'It uses red and black flags'],
                                'question': 'What is a Scapegoat Tree and how does it maintain balance without storing '
                                            'balance metadata in nodes?'},
                               {'correct_answer': 'A data structure representing a forest of trees supporting '
                                                  'connectivity, link, and cut operations in O(log n) amortized time '
                                                  'using Splay Trees',
                                'difficulty': 'Hard',
                                'explanation': 'Link-Cut trees maintain preferred paths inside splay trees, crucial '
                                               'for dynamic graph algorithms.',
                                'options': ['A data structure representing a forest of trees supporting connectivity, '
                                            'link, and cut operations in O(log n) amortized time using Splay Trees',
                                            'A tree with no branches',
                                            'A tree stored in flat binary files',
                                            'A graph with no cycles'],
                                'question': 'What is Link-Cut Tree and its operational complexity?'}],
 'Binary Trees and Traversals': [{'correct_answer': 'A hierarchical tree data structure where each node has at most '
                                                    'two children (left and right)',
                                  'difficulty': 'Easy',
                                  'explanation': 'In a binary tree, every parent node has at most two descendants.',
                                  'options': ['A hierarchical tree data structure where each node has at most two '
                                              'children (left and right)',
                                              'A tree where each node has infinite children',
                                              'An array with two elements',
                                              'A graph with no vertices'],
                                  'question': 'What is a Binary Tree?'},
                                 {'correct_answer': 'The topmost node in the tree hierarchy with no incoming parent '
                                                    'edge',
                                  'difficulty': 'Easy',
                                  'explanation': 'The root is the foundational ancestor of all nodes in the tree.',
                                  'options': ['The topmost node in the tree hierarchy with no incoming parent edge',
                                              'The lowest leaf node',
                                              'A node with two children',
                                              'The middle node'],
                                  'question': 'What is the root of a binary tree?'},
                                 {'correct_answer': 'A node that has neither a left child nor a right child (both '
                                                    'null)',
                                  'difficulty': 'Easy',
                                  'explanation': 'Leaves are terminal nodes at the bottom of tree branches.',
                                  'options': ['A node that has neither a left child nor a right child (both null)',
                                              'The root node',
                                              'A node with two children',
                                              'An internal node'],
                                  'question': 'What is a leaf node in a binary tree?'},
                                 {'correct_answer': 'The number of edges from the tree root to that specific node',
                                  'difficulty': 'Easy',
                                  'explanation': 'Depth measures distance from the root, with root depth defined as 0.',
                                  'options': ['The number of edges from the tree root to that specific node',
                                              'The number of children the node has',
                                              'The total count of leaves',
                                              'The memory address of the node'],
                                  'question': 'What is the depth (or level) of a node in a binary tree?'},
                                 {'correct_answer': 'The number of edges on the longest path from the root node to any '
                                                    'leaf node',
                                  'difficulty': 'Easy',
                                  'explanation': 'Height represents the maximum downward distance from root to leaf.',
                                  'options': ['The number of edges on the longest path from the root node to any leaf '
                                              'node',
                                              'The total number of nodes in the tree',
                                              'The number of leaves',
                                              'The memory size in kilobytes'],
                                  'question': 'What is the height of a binary tree?'},
                                 {'correct_answer': 'Left child, Root (current node), Right child',
                                  'difficulty': 'Easy',
                                  'explanation': 'Inorder traversal visits left subtree first, then current node, then '
                                                 'right subtree.',
                                  'options': ['Left child, Root (current node), Right child',
                                              'Root, Left child, Right child',
                                              'Left child, Right child, Root',
                                              'Right child, Root, Left child'],
                                  'question': 'In what order does an Inorder traversal process a binary tree node?'},
                                 {'correct_answer': 'Root (current node), Left child, Right child',
                                  'difficulty': 'Easy',
                                  'explanation': 'Preorder visits current node first before recursing on children.',
                                  'options': ['Root (current node), Left child, Right child',
                                              'Left child, Root, Right child',
                                              'Left child, Right child, Root',
                                              'Right child, Left child, Root'],
                                  'question': 'In what order does a Preorder traversal process a binary tree node?'},
                                 {'correct_answer': 'Left child, Right child, Root (current node)',
                                  'difficulty': 'Easy',
                                  'explanation': 'Postorder processes both children subtrees before visiting the '
                                                 'parent.',
                                  'options': ['Left child, Right child, Root (current node)',
                                              'Root, Left child, Right child',
                                              'Left child, Root, Right child',
                                              'Right child, Root, Left child'],
                                  'question': 'In what order does a Postorder traversal process a binary tree node?'},
                                 {'correct_answer': 'Level-Order Traversal (Breadth-First Traversal)',
                                  'difficulty': 'Easy',
                                  'explanation': 'Level-order traverses nodes horizontally across each level using a '
                                                 'queue.',
                                  'options': ['Level-Order Traversal (Breadth-First Traversal)',
                                              'Inorder Traversal',
                                              'Preorder Traversal',
                                              'Postorder Traversal'],
                                  'question': 'What traversal visits nodes level by level from top to bottom and left '
                                              'to right?'},
                                 {'correct_answer': '2^L nodes',
                                  'difficulty': 'Easy',
                                  'explanation': 'Each level can double the capacity of the previous level (1, 2, 4, '
                                                 '8, ...).',
                                  'options': ['2^L nodes', '2 * L nodes', 'L^2 nodes', '2^(L - 1) nodes'],
                                  'question': 'What is the maximum number of nodes at level L (where root is level 0) '
                                              'in a binary tree?'},
                                 {'correct_answer': 'A binary tree where every node has either exactly 0 or 2 children',
                                  'difficulty': 'Medium',
                                  'explanation': 'No node in a full binary tree has exactly 1 child.',
                                  'options': ['A binary tree where every node has either exactly 0 or 2 children',
                                              'A tree where all leaves are at the exact same depth',
                                              'A tree with all left children filled',
                                              'A tree where all nodes have 1 child'],
                                  'question': 'What is a Full Binary Tree (Strict Binary Tree)?'},
                                 {'correct_answer': 'A tree where all levels are completely filled except possibly the '
                                                    'last, which is filled from left to right',
                                  'difficulty': 'Medium',
                                  'explanation': 'Complete binary trees can be packed efficiently into flat arrays '
                                                 'without gaps (e.g. Heaps).',
                                  'options': ['A tree where all levels are completely filled except possibly the last, '
                                              'which is filled from left to right',
                                              'A tree with no leaves',
                                              'A tree that contains all numbers from 1 to n',
                                              'A tree where left subtree equals right subtree'],
                                  'question': 'What is a Complete Binary Tree?'},
                                 {'correct_answer': 'A binary tree where all internal nodes have 2 children and all '
                                                    'leaf nodes are at the same depth',
                                  'difficulty': 'Medium',
                                  'explanation': 'A perfect binary tree of height h contains exactly 2^(h+1) - 1 '
                                                 'nodes.',
                                  'options': ['A binary tree where all internal nodes have 2 children and all leaf '
                                              'nodes are at the same depth',
                                              'A tree with only 3 nodes',
                                              'A tree that has no right children',
                                              'An empty tree'],
                                  'question': 'What is a Perfect Binary Tree?'},
                                 {'correct_answer': 'O(n) time because every node is visited exactly once',
                                  'difficulty': 'Medium',
                                  'explanation': 'Every tree node is traversed a constant number of times during '
                                                 'standard traversals.',
                                  'options': ['O(n) time because every node is visited exactly once',
                                              'O(log n) time',
                                              'O(n log n) time',
                                              'O(n^2) time'],
                                  'question': 'What is the time complexity of Inorder, Preorder, and Postorder '
                                              'traversals on a binary tree of n nodes?'},
                                 {'correct_answer': 'O(n) auxiliary space due to recursion call stack depth',
                                  'difficulty': 'Medium',
                                  'explanation': 'Degenerate trees resemble linked lists, causing recursion depth '
                                                 'equal to n.',
                                  'options': ['O(n) auxiliary space due to recursion call stack depth',
                                              'O(log n) space',
                                              'O(1) space',
                                              'O(n^2) space'],
                                  'question': 'What is the space complexity of recursive tree traversals on a skewed '
                                              '(degenerate) binary tree?'},
                                 {'correct_answer': 'Using an explicit Stack to push left nodes until null, then '
                                                    'popping, processing, and moving to right child',
                                  'difficulty': 'Medium',
                                  'explanation': 'An explicit stack simulates the recursion stack by holding deferred '
                                                 'ancestor nodes.',
                                  'options': ['Using an explicit Stack to push left nodes until null, then popping, '
                                              'processing, and moving to right child',
                                              'Using a FIFO Queue',
                                              'Using two pointers',
                                              'Using binary search'],
                                  'question': 'How can Inorder traversal be performed iteratively without recursion?'},
                                 {'correct_answer': 'Queue (FIFO)',
                                  'difficulty': 'Medium',
                                  'explanation': 'A queue buffers nodes of the current level while discovering nodes '
                                                 'for the next level.',
                                  'options': ['Queue (FIFO)', 'Stack (LIFO)', 'Priority Queue', 'Hash Set'],
                                  'question': 'What data structure is used to implement Level-Order traversal '
                                              'iteratively?'},
                                 {'correct_answer': 'No, unless the tree is known to be a full binary tree',
                                  'difficulty': 'Medium',
                                  'explanation': 'Without knowing left/right placement for single-child nodes, '
                                                 'Pre+Post order is ambiguous.',
                                  'options': ['No, unless the tree is known to be a full binary tree',
                                              'Yes, always reconstructible uniquely',
                                              'Only if all nodes are positive numbers',
                                              'Only in Java'],
                                  'question': 'Can a unique binary tree be reconstructed from Preorder and Postorder '
                                              'traversals alone without restrictions?'},
                                 {'correct_answer': 'Inorder and Preorder (or Inorder and Postorder)',
                                  'difficulty': 'Medium',
                                  'explanation': 'Inorder splits left and right subtrees around the root identified by '
                                                 'Preorder/Postorder.',
                                  'options': ['Inorder and Preorder (or Inorder and Postorder)',
                                              'Preorder and Postorder',
                                              'Level-order and Preorder alone',
                                              'Postorder alone'],
                                  'question': 'Which pair of traversals is guaranteed to uniquely reconstruct ANY '
                                              'binary tree with unique values?'},
                                 {'correct_answer': 'The deepest node that has both u and v as descendants',
                                  'difficulty': 'Medium',
                                  'explanation': 'LCA is the shared ancestor farthest from the root.',
                                  'options': ['The deepest node that has both u and v as descendants',
                                              'The root node always',
                                              'The node with highest numerical value',
                                              'The parent of the root'],
                                  'question': 'What is the Lowest Common Ancestor (LCA) of two nodes u and v in a '
                                              'binary tree?'},
                                 {'correct_answer': 'An algorithm that threads the tree using right child pointers of '
                                                    'in-order predecessors, achieving O(1) auxiliary space',
                                  'difficulty': 'Hard',
                                  'explanation': 'Morris traversal establishes temporary back-links to avoid stack '
                                                 'frames, then restores the tree.',
                                  'options': ['An algorithm that threads the tree using right child pointers of '
                                              'in-order predecessors, achieving O(1) auxiliary space',
                                              'A traversal taking O(n) space',
                                              'A traversal using three queues',
                                              'A parallel traversal on GPUs'],
                                  'question': 'What is Morris Inorder Traversal and what is its space complexity?'},
                                 {'correct_answer': 'A tree where null child pointers are repurposed to point to '
                                                    'in-order predecessor or successor nodes',
                                  'difficulty': 'Hard',
                                  'explanation': 'Threaded trees eliminate stack/recursion requirements for linear '
                                                 'in-order traversal.',
                                  'options': ['A tree where null child pointers are repurposed to point to in-order '
                                              'predecessor or successor nodes',
                                              'A tree running on multiple OS threads',
                                              'A tree stored across network sockets',
                                              'A tree with mutex locks on every node'],
                                  'question': 'What is a Threaded Binary Tree?'},
                                 {'correct_answer': 'The length of the longest path between any two nodes in the tree, '
                                                    'computed in O(n) time via post-order depth calculations',
                                  'difficulty': 'Hard',
                                  'explanation': 'Tracking left_height + right_height at each node during DFS finds '
                                                 'the diameter in O(n).',
                                  'options': ['The length of the longest path between any two nodes in the tree, '
                                              'computed in O(n) time via post-order depth calculations',
                                              'The width of the root node',
                                              'The total count of leaf nodes',
                                              'O(n^2) using pairwise distance'],
                                  'question': 'What is the diameter of a binary tree and what is its optimal time '
                                              'complexity?'},
                                 {'correct_answer': 'Flattening tree subtree intervals into a 1D array by recording '
                                                    'entry and exit times during DFS, enabling subtree range queries '
                                                    'via Fenwick/Segment trees',
                                  'difficulty': 'Hard',
                                  'explanation': 'Euler tour maps tree subtrees into contiguous array intervals [tin, '
                                                 'tout].',
                                  'options': ['Flattening tree subtree intervals into a 1D array by recording entry '
                                              'and exit times during DFS, enabling subtree range queries via '
                                              'Fenwick/Segment trees',
                                              'Finding Eulerian circuits in cycles',
                                              'Eulerian graph coloring',
                                              'Balancing AVL trees'],
                                  'question': 'What is Euler Tour Technique on trees and its primary application?'},
                                 {'correct_answer': 'Decomposing a tree into disjoint linear paths (heavy chains) to '
                                                    'support path queries and updates in O(log^2 n) using Segment '
                                                    'Trees',
                                  'difficulty': 'Hard',
                                  'explanation': 'HLD partitions tree edges by subtree size, guaranteeing any path '
                                                 'traverses at most O(log n) heavy chains.',
                                  'options': ['Decomposing a tree into disjoint linear paths (heavy chains) to support '
                                              'path queries and updates in O(log^2 n) using Segment Trees',
                                              'Weighing nodes on a physical scale',
                                              'Splitting trees into left and right halves',
                                              'A garbage collection algorithm'],
                                  'question': 'What is Heavy-Light Decomposition (HLD) on trees?'},
                                 {'correct_answer': 'Preprocessing ancestors in powers of two (2^k) in O(n log n) time '
                                                    'to answer Lowest Common Ancestor (LCA) queries in O(log n) time',
                                  'difficulty': 'Hard',
                                  'explanation': 'Binary lifting hops up ancestor ladders by powers of two to locate '
                                                 'LCAs in logarithmic time.',
                                  'options': ['Preprocessing ancestors in powers of two (2^k) in O(n log n) time to '
                                              'answer Lowest Common Ancestor (LCA) queries in O(log n) time',
                                              'Lifting trees into RAM',
                                              'Converting binary trees to binary heaps',
                                              'Deleting leaf nodes in parallel'],
                                  'question': 'What is the binary lifting technique used for in tree data structures?'},
                                 {'correct_answer': '2^h leaves',
                                  'difficulty': 'Hard',
                                  'explanation': 'A complete perfect tree of height h has exactly 2^h leaves at level '
                                                 'h.',
                                  'options': ['2^h leaves', 'h^2 leaves', '2 * h leaves', '2^(h-1) leaves'],
                                  'question': 'What is the maximum number of leaves in a binary tree of height h?'},
                                 {'correct_answer': "Using sentinel markers (e.g. '#' or 'null') in pre-order "
                                                    'traversal sequence',
                                  'difficulty': 'Hard',
                                  'explanation': 'Explicit sentinel markers denote missing children, allowing '
                                                 'unambiguous pre-order deserialization.',
                                  'options': ["Using sentinel markers (e.g. '#' or 'null') in pre-order traversal "
                                              'sequence',
                                              'By storing node memory pointers to disk',
                                              'By converting the tree to a string hash',
                                              'By sorting all node values'],
                                  'question': 'How does serialization and deserialization of a binary tree encode null '
                                              'pointers for reconstruction?'},
                                 {'correct_answer': 'Finding a non-empty path with maximum sum of values, computed in '
                                                    'O(n) time by tracking maximum gain at each node',
                                  'difficulty': 'Hard',
                                  'explanation': 'At each node, max_gain = max(0, left) + max(0, right) + node.val '
                                                 'updates the global maximum.',
                                  'options': ['Finding a non-empty path with maximum sum of values, computed in O(n) '
                                              'time by tracking maximum gain at each node',
                                              'Summing all values in the tree',
                                              'Finding path from root to deepest leaf',
                                              'Finding average node value'],
                                  'question': 'What is the Maximum Path Sum problem in a binary tree (where node '
                                              'values can be negative)?'},
                                 {'correct_answer': 'L = I + 1 (number of leaves is always one more than number of '
                                                    'internal nodes)',
                                  'difficulty': 'Hard',
                                  'explanation': 'Every internal node adds 2 edges while consuming 1, yielding L = I + '
                                                 '1 strictly.',
                                  'options': ['L = I + 1 (number of leaves is always one more than number of internal '
                                              'nodes)',
                                              'L = 2 * I',
                                              'L = I',
                                              'L = I - 1'],
                                  'question': 'In memory-constrained environments, what is the leaf count property for '
                                              'any non-empty full binary tree with L leaves and I internal nodes?'}],
 'Doubly and Circular Linked Lists': [{'correct_answer': 'A linked list where each node contains pointers to both the '
                                                         'next node and the previous node',
                                       'difficulty': 'Easy',
                                       'explanation': "Doubly linked lists enable bidirectional traversal via 'prev' "
                                                      "and 'next' references.",
                                       'options': ['A linked list where each node contains pointers to both the next '
                                                   'node and the previous node',
                                                   'A list with two heads',
                                                   'A list containing only even numbers',
                                                   'An array with two dimensions'],
                                       'question': 'What is a doubly linked list (DLL)?'},
                                      {'correct_answer': 'A linked list where the next pointer of the last node points '
                                                         'back to the head node',
                                       'difficulty': 'Easy',
                                       'explanation': 'In circular lists, traversing from head will cycle infinitely '
                                                      'unless monitored.',
                                       'options': ['A linked list where the next pointer of the last node points back '
                                                   'to the head node',
                                                   'A list that forms a figure-8',
                                                   'A list whose nodes are arranged in a circle in RAM',
                                                   'A list that has no nodes'],
                                       'question': 'What is a circular singly linked list?'},
                                      {'correct_answer': 'null / None / nullptr',
                                       'difficulty': 'Easy',
                                       'explanation': 'The head node has no preceding node, so its prev pointer is '
                                                      'null.',
                                       'options': ['null / None / nullptr',
                                                   'A pointer to tail',
                                                   'Zero integer',
                                                   'A pointer to itself'],
                                       'question': "What value does the 'prev' pointer of the head node hold in a "
                                                   'standard non-circular DLL?'},
                                      {'correct_answer': 'The node can be deleted in O(1) time without needing to '
                                                         'traverse from the head to find the predecessor',
                                       'difficulty': 'Easy',
                                       'explanation': 'Access to node.prev allows re-linking node.prev.next = '
                                                      'node.next directly in O(1).',
                                       'options': ['The node can be deleted in O(1) time without needing to traverse '
                                                   'from the head to find the predecessor',
                                                   'DLL uses less memory than SLL',
                                                   'DLL allows binary search in O(1)',
                                                   'DLL does not require heap allocation'],
                                       'question': 'What is the advantage of a doubly linked list over a singly linked '
                                                   'list when deleting a given node pointer?'},
                                      {'correct_answer': "Yes, by following the 'prev' pointers backwards",
                                       'difficulty': 'Easy',
                                       'explanation': 'DLL explicitly stores backwards links for bidirectional '
                                                      'navigation.',
                                       'options': ["Yes, by following the 'prev' pointers backwards",
                                                   'No, linked lists can only be traversed forward',
                                                   'Only if the list is sorted',
                                                   'Only using recursion'],
                                       'question': 'Can you traverse a doubly linked list in reverse (from tail to '
                                                   'head)?'},
                                      {'correct_answer': 'A DLL where head.prev points to tail and tail.next points to '
                                                         'head',
                                       'difficulty': 'Easy',
                                       'explanation': 'Both forward and backward chains wrap circularly between head '
                                                      'and tail.',
                                       'options': ['A DLL where head.prev points to tail and tail.next points to head',
                                                   'A DLL with no pointers',
                                                   'A list that cannot be edited',
                                                   'A single node linked to itself only'],
                                       'question': 'What is a circular doubly linked list?'},
                                      {'correct_answer': 'O(1)',
                                       'difficulty': 'Easy',
                                       'explanation': 'Direct access to tail enables updating tail.next and tail in '
                                                      'constant time.',
                                       'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n^2)'],
                                       'question': 'What is the time complexity of inserting a node at the tail of a '
                                                   'DLL with a maintained tail pointer?'},
                                      {'correct_answer': 'Two pointers (prev and next)',
                                       'difficulty': 'Easy',
                                       'explanation': 'Each DLL node tracks two memory addresses for neighbor '
                                                      'connectivity.',
                                       'options': ['Two pointers (prev and next)',
                                                   'One pointer',
                                                   'Three pointers',
                                                   'Zero pointers'],
                                       'question': 'How many pointers does each node store in a doubly linked list?'},
                                      {'correct_answer': 'Round-robin CPU process scheduling and media playlist '
                                                         'looping',
                                       'difficulty': 'Easy',
                                       'explanation': 'Continuous cyclic traversal naturally models round-robin queues '
                                                      'and looped playlists.',
                                       'options': ['Round-robin CPU process scheduling and media playlist looping',
                                                   'Calculating square roots',
                                                   'Storing relational database tables',
                                                   'Compressing image files'],
                                       'question': 'What is a common real-world use case for a circular linked list?'},
                                      {'correct_answer': 'An infinite loop occurs because the next pointer never '
                                                         'becomes null',
                                       'difficulty': 'Easy',
                                       'explanation': 'Circular lists lack null sentinels; traversal must stop when '
                                                      'current returns to head.',
                                       'options': ['An infinite loop occurs because the next pointer never becomes '
                                                   'null',
                                                   'The loop terminates after one pass',
                                                   'A NullPointerException is thrown immediately',
                                                   'The CPU shuts down'],
                                       'question': "What happens if a loop condition 'while (current != null)' is used "
                                                   'on a circular linked list?'},
                                      {'correct_answer': 'As a doubly linked list (implementing both List and Deque '
                                                         'interfaces)',
                                       'difficulty': 'Medium',
                                       'explanation': "Java's LinkedList is a classic doubly linked list supporting "
                                                      'deque operations at both ends.',
                                       'options': ['As a doubly linked list (implementing both List and Deque '
                                                   'interfaces)',
                                                   'As a dynamic resizable array',
                                                   'As a binary tree',
                                                   'As a singly circular list'],
                                       'question': "How does Java's java.util.LinkedList implement its underlying data "
                                                   'structure?'},
                                      {'correct_answer': 'O(1) time',
                                       'difficulty': 'Medium',
                                       'explanation': 'Unlinking requires node.prev.next = node.next and '
                                                      'node.next.prev = node.prev in O(1).',
                                       'options': ['O(1) time', 'O(n) time', 'O(log n) time', 'O(n^2) time'],
                                       'question': 'What is the time complexity of deleting a node at a known pointer '
                                                   'location in a circular doubly linked list?'},
                                      {'correct_answer': 'Use fast and slow pointers; when fast completes cycle, cut '
                                                         'the list at slow and close both circular loops',
                                       'difficulty': 'Medium',
                                       'explanation': 'Tortoise and hare locates the midpoint and tail, allowing both '
                                                      'halves to be tied into circular lists in O(n).',
                                       'options': ['Use fast and slow pointers; when fast completes cycle, cut the '
                                                   'list at slow and close both circular loops',
                                                   'Count nodes, copy to array, split array',
                                                   'Delete odd nodes',
                                                   'Reverse the entire list'],
                                       'question': 'How can you split a circular linked list into two equal halves?'},
                                      {'correct_answer': 'DLL requires an additional pointer per node (typically 8 '
                                                         'bytes on 64-bit architectures)',
                                       'difficulty': 'Medium',
                                       'explanation': 'Storing prev references doubles pointer metadata overhead per '
                                                      'node.',
                                       'options': ['DLL requires an additional pointer per node (typically 8 bytes on '
                                                   '64-bit architectures)',
                                                   'DLL uses 50% less memory',
                                                   'DLL requires static memory allocation',
                                                   'DLL cannot store generic objects'],
                                       'question': 'What is the memory trade-off of a doubly linked list compared to a '
                                                   'singly linked list?'},
                                      {'correct_answer': 'newNode.next = curr; newNode.prev = curr.prev; '
                                                         'curr.prev.next = newNode; curr.prev = newNode;',
                                       'difficulty': 'Medium',
                                       'explanation': 'Four pointer re-assignments safely splice the new node into the '
                                                      'bidirectional chain.',
                                       'options': ['newNode.next = curr; newNode.prev = curr.prev; curr.prev.next = '
                                                   'newNode; curr.prev = newNode;',
                                                   'curr.next = newNode; newNode.next = null;',
                                                   'newNode = curr.prev;',
                                                   'curr.prev = newNode;'],
                                       'question': 'How is a node inserted before a given node in a DLL?'},
                                      {'correct_answer': 'An elimination game where every k-th person is executed '
                                                         'until one remains, modeled by cycling through nodes and '
                                                         'deleting the k-th node',
                                       'difficulty': 'Medium',
                                       'explanation': 'Traversing and deleting in a circular list models counting out '
                                                      'members in a circle.',
                                       'options': ['An elimination game where every k-th person is executed until one '
                                                   'remains, modeled by cycling through nodes and deleting the k-th '
                                                   'node',
                                                   'A pathfinding puzzle in graphs',
                                                   'A sorting algorithm for strings',
                                                   'A memory alignment problem'],
                                       'question': 'What is the Josephus problem and how is it traditionally modeled '
                                                   'using circular linked lists?'},
                                      {'correct_answer': 'Hash map provides O(1) key lookup; DLL allows O(1) removal '
                                                         'and re-insertion of nodes to the front',
                                       'difficulty': 'Medium',
                                       'explanation': 'DLL allows moving accessed nodes to the MRU head and evicting '
                                                      'LRU tail in O(1) time.',
                                       'options': ['Hash map provides O(1) key lookup; DLL allows O(1) removal and '
                                                   're-insertion of nodes to the front',
                                                   'DLL sorts keys alphabetically',
                                                   'Hash map compresses node data',
                                                   'DLL prevents hash collisions'],
                                       'question': 'In an LRU (Least Recently Used) Cache, why is a doubly linked list '
                                                   'combined with a hash map?'},
                                      {'correct_answer': 'Prevents checking for null when inserting/removing at '
                                                         'boundaries (head or tail)',
                                       'difficulty': 'Medium',
                                       'explanation': 'Dummy boundaries eliminate boundary condition if-statements, '
                                                      'simplifying pointer re-linking.',
                                       'options': ['Prevents checking for null when inserting/removing at boundaries '
                                                   '(head or tail)',
                                                   'Halves memory consumption',
                                                   'Eliminates need for garbage collection',
                                                   'Makes DLL nodes contiguous in memory'],
                                       'question': 'What is the advantage of using sentinel dummy head and dummy tail '
                                                   'nodes in a DLL implementation?'},
                                      {'correct_answer': 'O(n) time by swapping prev and next pointers for each node',
                                       'difficulty': 'Medium',
                                       'explanation': 'Swapping prev and next pointers in a single pass reverses the '
                                                      'entire DLL in linear time.',
                                       'options': ['O(n) time by swapping prev and next pointers for each node',
                                                   'O(n^2) time',
                                                   'O(1) time',
                                                   'O(log n) time'],
                                       'question': 'What is the time complexity to reverse a doubly linked list?'},
                                      {'correct_answer': 'It is embedded directly inside target structs (intrusive '
                                                         'list), allowing heterogeneous structures to be linked '
                                                         'without separate wrappers',
                                       'difficulty': 'Medium',
                                       'explanation': 'The Linux list_head pattern uses container_of macro to obtain '
                                                      'enclosing structs without extra heap allocations.',
                                       'options': ['It is embedded directly inside target structs (intrusive list), '
                                                   'allowing heterogeneous structures to be linked without separate '
                                                   'wrappers',
                                                   'It uses void* data pointers in external nodes',
                                                   'It allocates on GPU memory',
                                                   'It uses global static arrays'],
                                       'question': 'In the Linux Kernel, how is the circular doubly linked list '
                                                   '(struct list_head) designed?'},
                                      {'correct_answer': 'Node links (prev/next) are embedded inside user data '
                                                         'objects, eliminating separate node heap allocations and '
                                                         'cache misses',
                                       'difficulty': 'Hard',
                                       'explanation': 'Intrusive lists require zero dynamic node allocations, '
                                                      'eliminating memory allocation overhead.',
                                       'options': ['Node links (prev/next) are embedded inside user data objects, '
                                                   'eliminating separate node heap allocations and cache misses',
                                                   'It prevents objects from being modified',
                                                   'It compiles to assembly macros',
                                                   'It runs without operating system intervention'],
                                       'question': 'What is an Intrusive Doubly Linked List and its primary '
                                                   'performance advantage in high-performance systems?'},
                                      {'correct_answer': 'Allows concatenation, insertion, and deletion of trees in '
                                                         'O(1) amortized time by splicing circular pointer loops',
                                       'difficulty': 'Hard',
                                       'explanation': 'Circular DLLs allow merging two tree collections in O(1) by '
                                                      'cross-linking their circular ends.',
                                       'options': ['Allows concatenation, insertion, and deletion of trees in O(1) '
                                                   'amortized time by splicing circular pointer loops',
                                                   'Allows binary search across roots',
                                                   'Compresses trees into arrays',
                                                   'Prevents tree rotations'],
                                       'question': 'How does Fibonacci Heap utilize circular doubly linked lists for '
                                                   'its root list and child lists?'},
                                      {'correct_answer': 'Maintaining consistency across two independent pointers '
                                                         '(prev and next) simultaneously requires multi-word CAS '
                                                         '(MCAS) or complex multi-phase commit protocols',
                                       'difficulty': 'Hard',
                                       'explanation': 'Single CAS can only update one pointer atomically; dual pointer '
                                                      'updates risk torn intermediate states.',
                                       'options': ['Maintaining consistency across two independent pointers (prev and '
                                                   'next) simultaneously requires multi-word CAS (MCAS) or complex '
                                                   'multi-phase commit protocols',
                                                   'Because DLL nodes take double memory',
                                                   'Because CPU hardware does not support DLLs',
                                                   'Because prev pointers cannot be atomic'],
                                       'question': 'In lock-free concurrent programming, why is implementing a '
                                                   'lock-free doubly linked list significantly harder than a singly '
                                                   'linked list?'},
                                      {'correct_answer': 'It implements Algorithm X by removing and restoring matrix '
                                                         'rows/columns in O(1) using 2D circular doubly linked nodes '
                                                         '(toroidal mesh)',
                                       'difficulty': 'Hard',
                                       'explanation': 'DLX exploits node.prev.next = node.next and node.next.prev = '
                                                      'node.prev to cleanly cover and backtrack exact cover sets.',
                                       'options': ['It implements Algorithm X by removing and restoring matrix '
                                                   'rows/columns in O(1) using 2D circular doubly linked nodes '
                                                   '(toroidal mesh)',
                                                   'It sorts numbers using musical beats',
                                                   'It creates animated graphics in terminal',
                                                   'It compresses matrices using wavelets'],
                                       'question': 'How does the Dancing Links (DLX) technique by Donald Knuth utilize '
                                                   'doubly linked lists for exact cover problems?'},
                                      {'correct_answer': 'O(n) search in DLL; adding multi-level express pointers '
                                                         '(Skip List) reduces search to O(log n)',
                                       'difficulty': 'Hard',
                                       'explanation': 'Direct sequential DLL search cannot skip nodes; skip links '
                                                      'create multi-level fast lanes.',
                                       'options': ['O(n) search in DLL; adding multi-level express pointers (Skip '
                                                   'List) reduces search to O(log n)',
                                                   'O(log n) in standard DLL; skip list makes it O(1)',
                                                   'O(1) in DLL; skip list makes it O(n)',
                                                   'Search cannot be done in DLL'],
                                       'question': 'What is the time complexity of searching in a sorted doubly linked '
                                                   'list of size n, and why does skip-listing improve it?'},
                                      {'correct_answer': 'Each node belongs to two circular DLLs: one horizontal row '
                                                         'list and one vertical column list (left, right, up, down '
                                                         'pointers)',
                                       'difficulty': 'Hard',
                                       'explanation': 'Toroidal meshes link rows and columns in 4 directions, allowing '
                                                      '2D matrix manipulation.',
                                       'options': ['Each node belongs to two circular DLLs: one horizontal row list '
                                                   'and one vertical column list (left, right, up, down pointers)',
                                                   'It maps pointers to geometric toruses in memory',
                                                   'It uses 4D arrays in C++',
                                                   'It uses GPU texture memory'],
                                       'question': 'How does a Toroidal Doubly Linked Mesh represent 2D matrices in '
                                                   'algorithms like DLX?'},
                                      {'correct_answer': 'Infinite recursion / circular reference error causes stack '
                                                         'overflow or stream hangs',
                                       'difficulty': 'Hard',
                                       'explanation': 'Serializers blindly traversing next references loop '
                                                      'indefinitely without an object identity visited set.',
                                       'options': ['Infinite recursion / circular reference error causes stack '
                                                   'overflow or stream hangs',
                                                   'The JSON file becomes empty',
                                                   'The compiler crashes',
                                                   'Characters are converted to hexadecimal'],
                                       'question': 'What problem occurs when serializing a circular linked list to '
                                                   'JSON or binary streams without cycle tracking?'},
                                      {'correct_answer': 'A pointer changes from A to B and back to A, tricking a CAS '
                                                         'into succeeding despite underlying state changes; solved '
                                                         'using tagged pointers (version counters)',
                                       'difficulty': 'Hard',
                                       'explanation': 'Versioned pointers (pointer + incrementing tag) ensure CAS '
                                                      'fails if the node was modified and recycled.',
                                       'options': ['A pointer changes from A to B and back to A, tricking a CAS into '
                                                   'succeeding despite underlying state changes; solved using tagged '
                                                   'pointers (version counters)',
                                                   'A memory allocation failure',
                                                   'A race condition between threads A and B',
                                                   'A syntax error in C++'],
                                       'question': 'What is the ABA problem in concurrent linked list manipulation and '
                                                   'how is it mitigated?'},
                                      {'correct_answer': 'CPUs hardware prefetchers struggle with DLL because '
                                                         'prev/next pointers point to unpredictable heap addresses, '
                                                         'stalling the pipeline on cache misses',
                                       'difficulty': 'Hard',
                                       'explanation': 'Hardware prefetch engines detect linear strides, which array '
                                                      'layouts provide but pointer hops do not.',
                                       'options': ['CPUs hardware prefetchers struggle with DLL because prev/next '
                                                   'pointers point to unpredictable heap addresses, stalling the '
                                                   'pipeline on cache misses',
                                                   'DLLs prefetch faster than arrays',
                                                   'Hardware prefetchers ignore arrays',
                                                   'Prefetching only works with floating point numbers'],
                                       'question': 'How does memory prefetching in modern CPUs impact doubly linked '
                                                   'list traversal vs array traversal?'},
                                      {'correct_answer': 'Exactly 2 pointer widths (16 bytes on 64-bit systems) with '
                                                         'zero heap allocation overhead',
                                       'difficulty': 'Hard',
                                       'explanation': 'Intrusive design embeds two pointer members directly into host '
                                                      'struct without metadata headers.',
                                       'options': ['Exactly 2 pointer widths (16 bytes on 64-bit systems) with zero '
                                                   'heap allocation overhead',
                                                   '64 bytes',
                                                   '1 kilobyte',
                                                   'Zero bytes'],
                                       'question': 'What is the space complexity of an embedded circular doubly linked '
                                                   'list (like Linux list_head) per node?'}],
 'Graphs and Graph Traversals': [{'correct_answer': 'A non-linear data structure consisting of a set of vertices '
                                                    '(nodes) and edges connecting pairs of vertices',
                                  'difficulty': 'Easy',
                                  'explanation': 'Graphs model pairwise relationships between objects using vertices '
                                                 'and edges.',
                                  'options': ['A non-linear data structure consisting of a set of vertices (nodes) and '
                                              'edges connecting pairs of vertices',
                                              'A 2D line chart in Excel',
                                              'A sorted array of numbers',
                                              'A balanced binary search tree'],
                                  'question': 'What is a Graph in computer science?'},
                                 {'correct_answer': 'Edges in directed graphs have an orientation (arrow from u to v); '
                                                    'undirected edges are bidirectional',
                                  'difficulty': 'Easy',
                                  'explanation': 'Directed edges imply a one-way path, whereas undirected edges permit '
                                                 'traversal in both directions.',
                                  'options': ['Edges in directed graphs have an orientation (arrow from u to v); '
                                              'undirected edges are bidirectional',
                                              'Directed graphs cannot have cycles',
                                              'Undirected graphs cannot store weights',
                                              'Directed graphs must be trees'],
                                  'question': 'What is the difference between a directed graph (digraph) and an '
                                              'undirected graph?'},
                                 {'correct_answer': 'A V x V 2D matrix where matrix[i][j] indicates whether an edge '
                                                    'exists between vertex i and vertex j',
                                  'difficulty': 'Easy',
                                  'explanation': 'Adjacency matrices provide O(1) edge existence checks but require '
                                                 'O(V^2) space.',
                                  'options': ['A V x V 2D matrix where matrix[i][j] indicates whether an edge exists '
                                              'between vertex i and vertex j',
                                              'A linked list of edges',
                                              'A hash table of vertex names',
                                              'An array of vertex degrees'],
                                  'question': 'What is an Adjacency Matrix representation of a graph with V vertices?'},
                                 {'correct_answer': 'An array or list of lists where list[u] stores all adjacent '
                                                    'neighboring vertices connected to u',
                                  'difficulty': 'Easy',
                                  'explanation': 'Adjacency lists store only existing edges, consuming O(V + E) space.',
                                  'options': ['An array or list of lists where list[u] stores all adjacent neighboring '
                                              'vertices connected to u',
                                              'A 2D matrix of size V x V',
                                              'A single linked list containing all edges',
                                              'A binary search tree of edges'],
                                  'question': 'What is an Adjacency List representation of a graph with V vertices and '
                                              'E edges?'},
                                 {'correct_answer': 'Adjacency Matrix is O(V^2); Adjacency List is O(V + E)',
                                  'difficulty': 'Easy',
                                  'explanation': 'Adjacency lists are much more space-efficient for sparse graphs '
                                                 'where E << V^2.',
                                  'options': ['Adjacency Matrix is O(V^2); Adjacency List is O(V + E)',
                                              'Both are O(V + E)',
                                              'Both are O(V^2)',
                                              'Adjacency List is O(V^2)'],
                                  'question': 'What is the space complexity of an Adjacency Matrix vs an Adjacency '
                                              'List?'},
                                 {'correct_answer': 'Breadth-First Search (BFS)',
                                  'difficulty': 'Easy',
                                  'explanation': 'BFS systematically explores nodes layer by layer using a queue.',
                                  'options': ['Breadth-First Search (BFS)',
                                              'Depth-First Search (DFS)',
                                              "Dijkstra's Algorithm",
                                              "Kruskal's Algorithm"],
                                  'question': 'What graph traversal algorithm uses a FIFO Queue to visit neighbors '
                                              'level-by-level?'},
                                 {'correct_answer': 'Depth-First Search (DFS)',
                                  'difficulty': 'Easy',
                                  'explanation': 'DFS follows paths to dead ends before retreating, using recursion or '
                                                 'an explicit stack.',
                                  'options': ['Depth-First Search (DFS)',
                                              'Breadth-First Search (BFS)',
                                              "Prim's Algorithm",
                                              'Binary Search'],
                                  'question': 'What graph traversal algorithm explores as deep as possible along each '
                                              'branch before backtracking?'},
                                 {'correct_answer': 'O(V + E) linear time',
                                  'difficulty': 'Easy',
                                  'explanation': 'Every vertex is visited once and every edge is examined once or '
                                                 'twice.',
                                  'options': ['O(V + E) linear time',
                                              'O(V^2) time',
                                              'O(E log V) time',
                                              'O(V * E) time'],
                                  'question': 'What is the time complexity of BFS and DFS when using an Adjacency List '
                                              'representation?'},
                                 {'correct_answer': 'A graph where each edge has an associated numerical cost, length, '
                                                    'or capacity',
                                  'difficulty': 'Easy',
                                  'explanation': 'Weights represent distance, latency, toll, or bandwidth on edges.',
                                  'options': ['A graph where each edge has an associated numerical cost, length, or '
                                              'capacity',
                                              'A graph stored on a heavy hard drive',
                                              'A graph with more than 100 vertices',
                                              'A graph whose vertices are integers'],
                                  'question': 'What is a weighted graph?'},
                                 {'correct_answer': 'To prevent infinite loops caused by cycles in the graph',
                                  'difficulty': 'Easy',
                                  'explanation': 'Tracking visited states prevents traversing circular paths '
                                                 'indefinitely.',
                                  'options': ['To prevent infinite loops caused by cycles in the graph',
                                              'To sort the vertices alphabetically',
                                              'To calculate edge weights',
                                              'To compress the graph in memory'],
                                  'question': 'Why must visited nodes be tracked during BFS or DFS on a general '
                                              'graph?'},
                                 {'correct_answer': "Dijkstra's Algorithm",
                                  'difficulty': 'Medium',
                                  'explanation': 'Dijkstra uses a priority queue (min-heap) to greedily expand the '
                                                 'shortest known distance.',
                                  'options': ["Dijkstra's Algorithm",
                                              "Prim's Algorithm",
                                              "Kruskal's Algorithm",
                                              'Floyd-Warshall Algorithm'],
                                  'question': 'What algorithm finds the shortest path between a single source vertex '
                                              'and all other vertices in a graph with non-negative edge weights?'},
                                 {'correct_answer': 'O((V + E) log V)',
                                  'difficulty': 'Medium',
                                  'explanation': 'Each vertex extraction takes O(log V) and each edge relaxation takes '
                                                 'O(log V) in a binary heap.',
                                  'options': ['O((V + E) log V)', 'O(V^2)', 'O(V * E)', 'O(E^2)'],
                                  'question': "What is the time complexity of Dijkstra's algorithm implemented with a "
                                              'Min-Heap (Priority Queue)?'},
                                 {'correct_answer': 'Greedy choice assumes path distance can never decrease; negative '
                                                    'edges can shorten already finalized paths',
                                  'difficulty': 'Medium',
                                  'explanation': "Negative cycles or edges invalidate Dijkstra's greedy invariant that "
                                                 'visited nodes are finalized.',
                                  'options': ['Greedy choice assumes path distance can never decrease; negative edges '
                                              'can shorten already finalized paths',
                                              'Because negative numbers cannot be stored in heaps',
                                              'Because negative edges cause division by zero',
                                              'It does not fail; it works on all graphs'],
                                  'question': "Why does Dijkstra's algorithm fail on graphs with negative edge "
                                              'weights?'},
                                 {'correct_answer': 'Bellman-Ford Algorithm',
                                  'difficulty': 'Medium',
                                  'explanation': 'Bellman-Ford relaxes all edges V-1 times; a further relaxation '
                                                 'indicates a negative weight cycle.',
                                  'options': ['Bellman-Ford Algorithm',
                                              "Dijkstra's Algorithm",
                                              'BFS',
                                              "Kruskal's Algorithm"],
                                  'question': 'Which algorithm can find single-source shortest paths on graphs with '
                                              'negative edge weights and detect negative weight cycles?'},
                                 {'correct_answer': 'O(V * E)',
                                  'difficulty': 'Medium',
                                  'explanation': 'Bellman-Ford iterates V-1 times, relaxing all E edges in each pass.',
                                  'options': ['O(V * E)', 'O((V + E) log V)', 'O(V^3)', 'O(E log E)'],
                                  'question': 'What is the time complexity of the Bellman-Ford algorithm?'},
                                 {'correct_answer': 'A subgraph connecting all vertices with minimum total edge weight '
                                                    'and zero cycles',
                                  'difficulty': 'Medium',
                                  'explanation': 'An MST spans all V vertices using exactly V-1 edges with the lowest '
                                                 'possible total cost.',
                                  'options': ['A subgraph connecting all vertices with minimum total edge weight and '
                                              'zero cycles',
                                              'A tree that has the minimum number of leaves',
                                              'A shortest path between two vertices',
                                              'A binary search tree with minimum depth'],
                                  'question': 'What is a Minimum Spanning Tree (MST)?'},
                                 {'correct_answer': 'Sort all edges by weight; greedily add edges that do not form a '
                                                    'cycle using a Disjoint Set Union (DSU / Union-Find)',
                                  'difficulty': 'Medium',
                                  'explanation': 'Kruskal processes edges in ascending weight order, using Union-Find '
                                                 'to avoid cycle creation.',
                                  'options': ['Sort all edges by weight; greedily add edges that do not form a cycle '
                                              'using a Disjoint Set Union (DSU / Union-Find)',
                                              'Grow a tree outward from a single starting vertex',
                                              'Use BFS from the root',
                                              'Traverse edges in reverse topological order'],
                                  'question': "How does Kruskal's algorithm find a Minimum Spanning Tree?"},
                                 {'correct_answer': 'O(E log E) or O(E log V) dominated by sorting edges',
                                  'difficulty': 'Medium',
                                  'explanation': 'Sorting E edges takes O(E log E); union-find operations take '
                                                 'near-linear time.',
                                  'options': ['O(E log E) or O(E log V) dominated by sorting edges',
                                              'O(V^2)',
                                              'O(V * E)',
                                              'O(V + E)'],
                                  'question': "What is the time complexity of Kruskal's algorithm?"},
                                 {'correct_answer': 'A linear ordering of vertices such that for every directed edge '
                                                    '(u, v), vertex u comes before vertex v',
                                  'difficulty': 'Medium',
                                  'explanation': 'Topological sorting models prerequisite and dependency scheduling.',
                                  'options': ['A linear ordering of vertices such that for every directed edge (u, v), '
                                              'vertex u comes before vertex v',
                                              'Sorting vertices by degree',
                                              'Sorting vertices alphabetically',
                                              'Reversing all edges in a graph'],
                                  'question': 'What is Topological Sorting of a Directed Acyclic Graph (DAG)?'},
                                 {'correct_answer': 'A BFS-based algorithm that repeatedly removes vertices with '
                                                    'in-degree 0 and decrements neighbor in-degrees',
                                  'difficulty': 'Medium',
                                  'explanation': 'Vertices with 0 in-degrees have no remaining dependencies and can be '
                                                 'scheduled.',
                                  'options': ['A BFS-based algorithm that repeatedly removes vertices with in-degree 0 '
                                              'and decrements neighbor in-degrees',
                                              'A DFS algorithm using back-edges',
                                              'A sorting algorithm for edge weights',
                                              'An algorithm that finds bridges'],
                                  'question': "What is Kahn's Algorithm for topological sorting?"},
                                 {'correct_answer': 'A DFS-based algorithm that finds all maximal strongly connected '
                                                    'subgraphs in linear O(V + E) time using low-link values and a '
                                                    'stack',
                                  'difficulty': 'Hard',
                                  'explanation': 'Tarjan computes discovery and low-link numbers to isolate SCCs in a '
                                                 'single DFS pass.',
                                  'options': ['A DFS-based algorithm that finds all maximal strongly connected '
                                              'subgraphs in linear O(V + E) time using low-link values and a stack',
                                              'A pathfinding algorithm for GPS maps',
                                              'A minimum spanning tree algorithm',
                                              'An algorithm for bipartite matching'],
                                  'question': "What is Tarjan's strongly connected components (SCC) algorithm?"},
                                 {'correct_answer': 'A dynamic programming algorithm that finds all-pairs shortest '
                                                    'paths in O(V^3) time',
                                  'difficulty': 'Hard',
                                  'explanation': 'Floyd-Warshall computes shortest paths between all pairs of vertices '
                                                 'in O(V^3) time using dynamic programming.',
                                  'options': ['A dynamic programming algorithm that finds all-pairs shortest paths in '
                                              'O(V^3) time',
                                              'A single-source shortest path algorithm in O(V log V)',
                                              'A flow network algorithm in O(V^2 E)',
                                              'A topological sorting algorithm in O(V + E)'],
                                  'question': 'What is the Floyd-Warshall algorithm and what is its time complexity?'},
                                 {'correct_answer': 'It reweights edges using Bellman-Ford to eliminate negative '
                                                    'weights, then runs Dijkstra from every vertex in O(V * E log V)',
                                  'difficulty': 'Hard',
                                  'explanation': 'Reweighting preserves shortest paths while allowing ultra-fast '
                                                 'Dijkstra runs from all sources.',
                                  'options': ['It reweights edges using Bellman-Ford to eliminate negative weights, '
                                              'then runs Dijkstra from every vertex in O(V * E log V)',
                                              'It runs BFS on all vertices',
                                              'It computes matrix powers',
                                              'It converts the graph into an Eulerian circuit'],
                                  'question': "What is Johnson's Algorithm for all-pairs shortest paths on sparse "
                                              'graphs?'},
                                 {'correct_answer': 'A* evaluates f(n) = g(n) + h(n); it is guaranteed optimal if the '
                                                    'heuristic h(n) is admissible (never overestimates distance)',
                                  'difficulty': 'Hard',
                                  'explanation': 'Admissibility ensures A* never overlooks shorter paths by '
                                                 'overestimating remaining distance.',
                                  'options': ['A* evaluates f(n) = g(n) + h(n); it is guaranteed optimal if the '
                                              'heuristic h(n) is admissible (never overestimates distance)',
                                              'A* guesses random paths',
                                              'A* requires h(n) to overestimate distance',
                                              'A* only works on unweighted graphs'],
                                  'question': 'What is the A* Search algorithm and how does its heuristic function '
                                              'h(n) guarantee finding the optimal path?'},
                                 {'correct_answer': 'The maximum amount of flow passing from source to sink equals the '
                                                    'total capacity of the minimum capacity cut separating them',
                                  'difficulty': 'Hard',
                                  'explanation': 'Ford-Fulkerson established that max flow is fundamentally '
                                                 'bottlenecked by the minimum cut capacity.',
                                  'options': ['The maximum amount of flow passing from source to sink equals the total '
                                              'capacity of the minimum capacity cut separating them',
                                              'Flow can exceed network capacity',
                                              'Cuts cannot be calculated in polynomial time',
                                              'Max flow equals total vertex degree'],
                                  'question': 'What is the Maximum Flow problem and what does the Max-Flow Min-Cut '
                                              'Theorem state?'},
                                 {'correct_answer': 'O(V * E^2) using BFS to find shortest augmenting paths in the '
                                                    'residual graph',
                                  'difficulty': 'Hard',
                                  'explanation': 'Using BFS to pick augmenting paths bounds total augmentations to O(V '
                                                 '* E), yielding O(V * E^2).',
                                  'options': ['O(V * E^2) using BFS to find shortest augmenting paths in the residual '
                                              'graph',
                                              'O(V^3)',
                                              'O(E log V)',
                                              'O(2^V)'],
                                  'question': 'What is the time complexity of the Edmonds-Karp algorithm for maximum '
                                              'flow?'},
                                 {'correct_answer': 'An edge or vertex whose removal strictly increases the number of '
                                                    'connected components (disconnects the graph)',
                                  'difficulty': 'Hard',
                                  'explanation': 'Bridges and cut-vertices represent critical vulnerability points in '
                                                 'network topology.',
                                  'options': ['An edge or vertex whose removal strictly increases the number of '
                                              'connected components (disconnects the graph)',
                                              'The edge with highest weight',
                                              'A vertex with in-degree 0',
                                              'A cycle in the graph'],
                                  'question': 'What is a Bridge (cut-edge) and Articulation Point (cut-vertex) in a '
                                              'connected graph?'},
                                 {'correct_answer': 'By finding multiple vertex-disjoint shortest augmenting paths '
                                                    'simultaneously in each phase using BFS and DFS',
                                  'difficulty': 'Hard',
                                  'explanation': 'Augmenting along multiple shortest paths simultaneously speeds up '
                                                 'bipartite matching to O(E * sqrt(V)).',
                                  'options': ['By finding multiple vertex-disjoint shortest augmenting paths '
                                              'simultaneously in each phase using BFS and DFS',
                                              'By sorting edges using quicksort',
                                              'By transforming the graph into a binary search tree',
                                              'By running Bellman-Ford on bipartite partitions'],
                                  'question': 'How does Hopcroft-Karp algorithm solve Maximum Bipartite Matching in '
                                              'O(E * sqrt(V)) time?'},
                                 {'correct_answer': 'Converting boolean clauses (A or B) into implication edges (~A -> '
                                                    'B) and testing if any variable x and ~x belong to the same SCC',
                                  'difficulty': 'Hard',
                                  'explanation': 'An implication graph is satisfiable if and only if no variable and '
                                                 'its negation share a strongly connected component.',
                                  'options': ['Converting boolean clauses (A or B) into implication edges (~A -> B) '
                                              'and testing if any variable x and ~x belong to the same SCC',
                                              'Evaluating truth tables taking O(2^n) time',
                                              'Using dynamic programming on arrays',
                                              '2-SAT is NP-complete and cannot be solved in linear time'],
                                  'question': 'What is 2-SAT (2-Satisfiability) and how is it solved in linear O(V + '
                                              'E) time using graphs?'},
                                 {'correct_answer': 'O(V + E) linear time by following unused edges and splicing '
                                                    'sub-tours',
                                  'difficulty': 'Hard',
                                  'explanation': 'Hierholzer finds Eulerian circuits in linear time by following edges '
                                                 'until a cycle closes, then splicing.',
                                  'options': ['O(V + E) linear time by following unused edges and splicing sub-tours',
                                              'O(V^2) time',
                                              'O(E log E) time',
                                              'O(V * E) time'],
                                  'question': "What is the time complexity of Hierholzer's Algorithm for finding an "
                                              'Eulerian Path / Circuit?'}],
 'Hash Tables and Hashing': [{'correct_answer': 'To map keys to values for fast O(1) average lookup, insertion, and '
                                                'deletion',
                              'difficulty': 'Easy',
                              'explanation': 'Hash tables use hash functions to compute array bucket indices for rapid '
                                             'data retrieval.',
                              'options': ['To map keys to values for fast O(1) average lookup, insertion, and deletion',
                                          'To sort elements in ascending order',
                                          'To compress files',
                                          'To encrypt passwords irreversibly'],
                              'question': 'What is the primary purpose of a Hash Table?'},
                             {'correct_answer': 'A mathematical function that converts an input key into an integer '
                                                'array index',
                              'difficulty': 'Easy',
                              'explanation': 'Hash functions map large or variable key domains into a fixed range of '
                                             'bucket indices.',
                              'options': ['A mathematical function that converts an input key into an integer array '
                                          'index',
                                          'A function that generates random numbers',
                                          'A compiler parser',
                                          'A graphics rendering shader'],
                              'question': 'What is a hash function?'},
                             {'correct_answer': 'When two distinct keys produce the exact same hash code or bucket '
                                                'index',
                              'difficulty': 'Easy',
                              'explanation': 'Collisions are inevitable by the Pigeonhole Principle when the key space '
                                             'exceeds the bucket array size.',
                              'options': ['When two distinct keys produce the exact same hash code or bucket index',
                                          'When two computers crash at the same time',
                                          'When an array runs out of memory',
                                          'When a hash table is deleted'],
                              'question': 'What is a hash collision?'},
                             {'correct_answer': 'Each bucket contains a linked list (or tree) of all entries that '
                                                'mapped to that index',
                              'difficulty': 'Easy',
                              'explanation': 'Separate chaining keeps colliding elements in a chain data structure '
                                             'attached to the bucket.',
                              'options': ['Each bucket contains a linked list (or tree) of all entries that mapped to '
                                          'that index',
                                          'Probing adjacent slots in the array',
                                          'Doubling array size on collision',
                                          'Deleting colliding keys'],
                              'question': 'What is Separate Chaining in hash collision resolution?'},
                             {'correct_answer': 'Storing all elements directly within the hash table array by probing '
                                                'alternative slots when collisions occur',
                              'difficulty': 'Easy',
                              'explanation': 'Open addressing avoids pointer overhead by finding unoccupied slots '
                                             'within the array itself.',
                              'options': ['Storing all elements directly within the hash table array by probing '
                                          'alternative slots when collisions occur',
                                          'Sharing the table across a network',
                                          'Allowing public access to all keys',
                                          'Using open source hash functions'],
                              'question': 'What is Open Addressing in hash collision resolution?'},
                             {'correct_answer': 'An open addressing technique where collisions are resolved by '
                                                'sequentially checking the next bucket (index + 1)',
                              'difficulty': 'Easy',
                              'explanation': 'Linear probing inspects consecutive buckets until an empty slot is '
                                             'encountered.',
                              'options': ['An open addressing technique where collisions are resolved by sequentially '
                                          'checking the next bucket (index + 1)',
                                          'Searching arrays from end to beginning',
                                          'Calculating linear regression lines',
                                          'Probing memory with hardware probes'],
                              'question': 'What is Linear Probing?'},
                             {'correct_answer': 'The ratio of stored elements to total bucket capacity (n / k)',
                              'difficulty': 'Easy',
                              'explanation': 'Load factor measures table fullness and triggers resizing when exceeding '
                                             'a threshold.',
                              'options': ['The ratio of stored elements to total bucket capacity (n / k)',
                                          'The percentage of CPU used by hashing',
                                          'The time taken to compute a hash',
                                          'The weight of the RAM modules'],
                              'question': 'What is the load factor of a hash table?'},
                             {'correct_answer': 'O(1) - Constant time',
                              'difficulty': 'Easy',
                              'explanation': 'Good hash distribution maps keys uniformly, achieving constant-time '
                                             'operations on average.',
                              'options': ['O(1) - Constant time', 'O(n) - Linear time', 'O(log n)', 'O(n^2)'],
                              'question': 'What is the average time complexity of lookup, insert, and delete in a '
                                          'well-distributed hash table?'},
                             {'correct_answer': 'O(n) linear scan',
                              'difficulty': 'Easy',
                              'explanation': 'If all keys hash to the same bucket, the table degenerates into a single '
                                             'linked list.',
                              'options': ['O(n) linear scan', 'O(1)', 'O(log n)', 'O(n!)'],
                              'question': 'What is the worst-case time complexity of search in a hash table with '
                                          'separate chaining when all keys collide into one bucket?'},
                             {'correct_answer': 'Rehashing occurs: a larger array is allocated and all existing keys '
                                                'are re-inserted',
                              'difficulty': 'Easy',
                              'explanation': 'Resizing doubles capacity and recalculates bucket placements to keep '
                                             'chains short.',
                              'options': ['Rehashing occurs: a larger array is allocated and all existing keys are '
                                          're-inserted',
                                          'The table throws an OutOfMemoryError',
                                          'Oldest keys are deleted automatically',
                                          'The hash function is deleted'],
                              'question': "What happens when a hash table's load factor exceeds its threshold "
                                          '(typically 0.75)?'},
                             {'correct_answer': 'If two objects are equal according to equals(), they MUST have the '
                                                'same hashCode() value',
                              'difficulty': 'Medium',
                              'explanation': 'Violating this contract causes hash tables to fail finding existing '
                                             'keys.',
                              'options': ['If two objects are equal according to equals(), they MUST have the same '
                                          'hashCode() value',
                                          'If two objects have the same hashCode(), they must be equal',
                                          'hashCode() must always return positive numbers',
                                          'equals() must run in O(1) time'],
                              'question': 'What is the contract between equals() and hashCode() in Java?'},
                             {'correct_answer': "If a key's fields mutate after insertion, its hash code changes, "
                                                'making it unfindable in its original bucket',
                              'difficulty': 'Medium',
                              'explanation': 'Mutating a key strands it in the wrong bucket, causing silent lookup '
                                             'failures.',
                              'options': ["If a key's fields mutate after insertion, its hash code changes, making it "
                                          'unfindable in its original bucket',
                                          'Because mutable objects cannot be compiled',
                                          'Because memory cannot store mutable keys',
                                          'To prevent compiler warnings'],
                              'question': 'Why must hash table keys be immutable?'},
                             {'correct_answer': 'Long contiguous runs of occupied buckets build up, increasing '
                                                'collision frequency and probe lengths',
                              'difficulty': 'Medium',
                              'explanation': 'Linear probing causes adjacent occupied slots to merge into large '
                                             'blocks, worsening search times.',
                              'options': ['Long contiguous runs of occupied buckets build up, increasing collision '
                                          'frequency and probe lengths',
                                          'Grouping keys by first letter',
                                          'Storing hash tables in the primary CPU cache',
                                          'Clustering computers in a cluster'],
                              'question': 'What is Primary Clustering in open addressing with linear probing?'},
                             {'correct_answer': 'By using a quadratic polynomial function of the probe attempt number '
                                                '(e.g. hash + c1*i + c2*i^2)',
                              'difficulty': 'Medium',
                              'explanation': 'Quadratic spacing skips over local clusters, mitigating primary '
                                             'clustering.',
                              'options': ['By using a quadratic polynomial function of the probe attempt number (e.g. '
                                          'hash + c1*i + c2*i^2)',
                                          'By calculating square roots of keys',
                                          'By multiplying table size by 4',
                                          'By using a 2D array'],
                              'question': 'How does Quadratic Probing alleviate primary clustering?'},
                             {'correct_answer': 'An open addressing collision technique where the step size between '
                                                'probes is calculated by a second independent hash function',
                              'difficulty': 'Medium',
                              'explanation': 'Double hashing eliminates both primary and secondary clustering by '
                                             'varying step size per key.',
                              'options': ['An open addressing collision technique where the step size between probes '
                                          'is calculated by a second independent hash function',
                                          'Hashing the key twice with MD5',
                                          'Using two hash tables simultaneously',
                                          'Hashing keys and values together'],
                              'question': 'What is Double Hashing?'},
                             {'correct_answer': 'When a bucket chain length exceeds 8 (TREEIFY_THRESHOLD), the linked '
                                                'list converts to a Red-Black Tree with O(log n) worst-case lookup',
                              'difficulty': 'Medium',
                              'explanation': 'Transforming degraded chains to balanced trees protects against Denial '
                                             'of Service collision attacks.',
                              'options': ['When a bucket chain length exceeds 8 (TREEIFY_THRESHOLD), the linked list '
                                          'converts to a Red-Black Tree with O(log n) worst-case lookup',
                                          'It terminates the offending HTTP connection',
                                          'It switches to a cryptographic hash function',
                                          'It bans duplicate keys'],
                              'question': "How does Java 8's HashMap mitigate worst-case O(n) hash collision attacks?"},
                             {'correct_answer': 'To ensure the probe sequence traverses every bucket in the table '
                                                'without getting trapped in a sub-cycle',
                              'difficulty': 'Medium',
                              'explanation': 'Co-prime table size and step size guarantee covering the full table '
                                             'before repeating.',
                              'options': ['To ensure the probe sequence traverses every bucket in the table without '
                                          'getting trapped in a sub-cycle',
                                          'Prime numbers use less RAM',
                                          'Because CPUs divide prime numbers faster',
                                          'To encrypt table keys'],
                              'question': 'Why should the capacity of an open-addressing hash table using double '
                                          'hashing be a prime number?'},
                             {'correct_answer': 'An open addressing technique where richer keys (probed fewer times) '
                                                'yield their slots to poorer keys (probed more times) to minimize '
                                                'variance in probe lengths',
                              'difficulty': 'Medium',
                              'explanation': 'Robin Hood hashing equalizes probe lengths, resulting in predictable '
                                             'fast lookups.',
                              'options': ['An open addressing technique where richer keys (probed fewer times) yield '
                                          'their slots to poorer keys (probed more times) to minimize variance in '
                                          'probe lengths',
                                          'A hash function that steals keys from rich buckets',
                                          'An encryption algorithm for banks',
                                          'A hash table stored on green hardware'],
                              'question': 'What is Robin Hood Hashing?'},
                             {'correct_answer': 'A marker placed in a deleted slot indicating it is empty for '
                                                'insertion but must not terminate search probe chains',
                              'difficulty': 'Medium',
                              'explanation': 'Tombstones preserve continuity of probe sequences for keys inserted '
                                             'beyond the deleted slot.',
                              'options': ['A marker placed in a deleted slot indicating it is empty for insertion but '
                                          'must not terminate search probe chains',
                                          'A corrupted memory sector',
                                          'A key that expired due to TTL',
                                          'A pointer to null'],
                              'question': 'What is a Tombstone in open addressing deletion?'},
                             {'correct_answer': 'It uses two hash functions and two tables; keys are kicked to '
                                                'alternative slots, providing O(1) worst-case lookup time',
                              'difficulty': 'Medium',
                              'explanation': 'Lookup inspects at most two locations, guaranteeing strict O(1) '
                                             'worst-case search.',
                              'options': ['It uses two hash functions and two tables; keys are kicked to alternative '
                                          'slots, providing O(1) worst-case lookup time',
                                          'It uses bird flocking algorithms',
                                          'It takes O(n^2) worst case',
                                          'It stores keys in nested trees'],
                              'question': 'What is Cuckoo Hashing and what is its worst-case lookup guarantee?'},
                             {'correct_answer': 'It maps both nodes and keys onto a circular hash ring (0 to 2^32-1) '
                                                'so adding/removing nodes only re-keys K/N keys rather than all keys',
                              'difficulty': 'Hard',
                              'explanation': 'Consistent hashing avoids catastrophic cache invalidation when scaling '
                                             'cluster nodes.',
                              'options': ['It maps both nodes and keys onto a circular hash ring (0 to 2^32-1) so '
                                          'adding/removing nodes only re-keys K/N keys rather than all keys',
                                          'It ensures all hash functions produce identical bits',
                                          'It synchronizes clocks across database servers',
                                          'It encrypts distributed data packets'],
                              'question': 'What is Consistent Hashing and why is it critical for distributed caches '
                                          '(e.g. Memcached, DynamoDB)?'},
                             {'correct_answer': 'A space-efficient probabilistic data structure that tests set '
                                                'membership: zero false negatives, but possible false positives',
                              'difficulty': 'Hard',
                              'explanation': 'If a Bloom filter reports an element is absent, it is guaranteed absent; '
                                             'positive results may be false.',
                              'options': ['A space-efficient probabilistic data structure that tests set membership: '
                                          'zero false negatives, but possible false positives',
                                          'A filter that allows false negatives but no false positives',
                                          'A lossless compression algorithm',
                                          'A hash table that stores full keys'],
                              'question': 'What is a Bloom Filter and what are its error guarantees?'},
                             {'correct_answer': 'A sub-linear space probabilistic data structure that estimates '
                                                'frequency of events/tokens using multiple hash functions',
                              'difficulty': 'Hard',
                              'explanation': 'Count-Min Sketch tracks heavy hitters in multi-gigabit network traffic '
                                             'using fixed memory.',
                              'options': ['A sub-linear space probabilistic data structure that estimates frequency of '
                                          'events/tokens using multiple hash functions',
                                          'Counting lines of code in large projects',
                                          'Compressing text files',
                                          'Generating random integers'],
                              'question': 'What is a Count-Min Sketch used for in high-volume streaming data?'},
                             {'correct_answer': 'They are non-cryptographic hash functions optimized for extreme CPU '
                                                'throughput, low collision rates, and excellent avalanche behavior',
                              'difficulty': 'Hard',
                              'explanation': 'Non-cryptographic hashes execute in a few CPU cycles while maintaining '
                                             'superb entropy.',
                              'options': ['They are non-cryptographic hash functions optimized for extreme CPU '
                                          'throughput, low collision rates, and excellent avalanche behavior',
                                          'They are military-grade encryption ciphers',
                                          'They run on GPUs only',
                                          'They prevent all hash collisions'],
                              'question': 'What is MurmurHash / xxHash and why are they favored over MD5/SHA-256 for '
                                          'in-memory hash tables?'},
                             {'correct_answer': 'It uses 1-byte control metadata arrays evaluated with SIMD (SSE/AVX) '
                                                'instructions to probe 16 buckets in a single CPU instruction',
                              'difficulty': 'Hard',
                              'explanation': 'SIMD vector instructions check 16 bucket hashes in parallel, slashing '
                                             'probe overhead.',
                              'options': ['It uses 1-byte control metadata arrays evaluated with SIMD (SSE/AVX) '
                                          'instructions to probe 16 buckets in a single CPU instruction',
                                          'It converts tables into binary search trees',
                                          'It eliminates collisions using quantum memory',
                                          'It runs inside kernel space'],
                              'question': "How does Google's Swiss Table (absl::flat_hash_map) achieve "
                                          'state-of-the-art hash table speed?'},
                             {'correct_answer': 'An attacker crafts thousands of malicious keys that all produce '
                                                'identical hash codes, degrading O(1) hash tables to O(n^2) CPU '
                                                'exhaustion',
                              'difficulty': 'Hard',
                              'explanation': 'Targeted collision generation forces servers to spend 100% CPU '
                                             'traversing degraded bucket lists.',
                              'options': ['An attacker crafts thousands of malicious keys that all produce identical '
                                          'hash codes, degrading O(1) hash tables to O(n^2) CPU exhaustion',
                                          'Flooding a server with UDP packets',
                                          'Cracking passwords using rainbow tables',
                                          'Deleting the hash table file on disk'],
                              'question': 'What is a Hash DoS (Denial of Service) vulnerability?'},
                             {'correct_answer': 'SipHash is a keyed pseudo-random hash function initialized with a '
                                                'random per-process secret seed, making collisions computationally '
                                                'unpredictable',
                              'difficulty': 'Hard',
                              'explanation': 'Random seed salts make it impossible for attackers to pre-compute '
                                             'colliding payloads.',
                              'options': ['SipHash is a keyed pseudo-random hash function initialized with a random '
                                          'per-process secret seed, making collisions computationally unpredictable',
                                          'By encrypting keys with RSA',
                                          'By banning web requests with duplicate strings',
                                          'By storing tables in read-only memory'],
                              'question': 'How do SipHash and randomized hash seed salts defend against Hash DoS '
                                          'attacks?'},
                             {'correct_answer': 'A collision-free hash function that maps a known static set of keys '
                                                'to unique integers in O(1) time with O(n) space',
                              'difficulty': 'Hard',
                              'explanation': 'When the dictionary is static (e.g. language keywords), perfect hashing '
                                             'guarantees zero collisions.',
                              'options': ['A collision-free hash function that maps a known static set of keys to '
                                          'unique integers in O(1) time with O(n) space',
                                          'A hash function that never overflows 32 bits',
                                          'A hash function that works on infinite keys',
                                          'An algorithm used in quantum cryptography'],
                              'question': 'What is a Perfect Hash Function and when is it applicable?'},
                             {'correct_answer': 'An open addressing algorithm that combines linear probing with '
                                                'cuckoo-style displacements to ensure elements stay within a fixed '
                                                'neighborhood (H slots) of their hash bucket',
                              'difficulty': 'Hard',
                              'explanation': 'Hopscotch guarantees lookups inspect only H contiguous buckets, yielding '
                                             'exceptional cache locality.',
                              'options': ['An open addressing algorithm that combines linear probing with cuckoo-style '
                                          'displacements to ensure elements stay within a fixed neighborhood (H slots) '
                                          'of their hash bucket',
                                          'A hashing algorithm that hops between servers',
                                          'A distributed sorting algorithm',
                                          'A compression method for audio'],
                              'question': 'What is Hopscotch Hashing?'},
                             {'correct_answer': 'Using fine-grained bucket synchronization (synchronized on bucket '
                                                'head nodes) alongside volatile reads and CAS operations',
                              'difficulty': 'Hard',
                              'explanation': 'Locking only the specific bucket being modified allows independent '
                                             'threads to write concurrently.',
                              'options': ['Using fine-grained bucket synchronization (synchronized on bucket head '
                                          'nodes) alongside volatile reads and CAS operations',
                                          'Using a single global ReentrantLock',
                                          'Running every operation on a dedicated thread',
                                          'Copying the entire map on every write'],
                              'question': "How does Java's ConcurrentHashMap achieve high-throughput thread-safe "
                                          'concurrency without global locking?'}],
 'Queues and Deques (FIFO)': [{'correct_answer': 'FIFO (First In, First Out)',
                               'difficulty': 'Easy',
                               'explanation': 'Queues process items in the exact arrival sequence.',
                               'options': ['FIFO (First In, First Out)',
                                           'LIFO (Last In, First Out)',
                                           'Priority order',
                                           'Random access'],
                               'question': 'What order of element processing does a standard Queue follow?'},
                              {'correct_answer': 'enqueue / offer / add',
                               'difficulty': 'Easy',
                               'explanation': 'Enqueue appends a new item to the back of the queue.',
                               'options': ['enqueue / offer / add', 'dequeue', 'peek', 'pop'],
                               'question': 'Which operation adds an element to the rear (tail) of a queue?'},
                              {'correct_answer': 'dequeue / poll / remove',
                               'difficulty': 'Easy',
                               'explanation': 'Dequeue extracts the oldest item from the front of the queue.',
                               'options': ['dequeue / poll / remove', 'enqueue', 'push', 'peek'],
                               'question': 'Which operation removes and returns the front (head) element of a queue?'},
                              {'correct_answer': 'A queue data structure that allows insertion and deletion at both '
                                                 'front and rear ends',
                               'difficulty': 'Easy',
                               'explanation': 'Deques support push/pop at both front and back in O(1) time.',
                               'options': ['A queue data structure that allows insertion and deletion at both front '
                                           'and rear ends',
                                           'A queue that contains two elements only',
                                           'A queue stored across two computers',
                                           'A queue with decimal priorities'],
                               'question': 'What is a Deque (Double-Ended Queue)?'},
                              {'correct_answer': 'O(1) - Constant time',
                               'difficulty': 'Easy',
                               'explanation': 'Front removal and rear addition take constant time when '
                                              'pointers/indices are maintained.',
                               'options': ['O(1) - Constant time', 'O(n) - Linear time', 'O(log n)', 'O(n^2)'],
                               'question': 'What is the time complexity of enqueue and dequeue operations in an '
                                           'optimal queue implementation?'},
                              {'correct_answer': 'Breadth-First Search (BFS)',
                               'difficulty': 'Easy',
                               'explanation': 'BFS explores graph vertices level-by-level using a FIFO queue.',
                               'options': ['Breadth-First Search (BFS)',
                                           'Depth-First Search (DFS)',
                                           'Bellman-Ford',
                                           "Tarjan's strongly connected components"],
                               'question': 'Which graph traversal algorithm fundamentally relies on a FIFO queue?'},
                              {'correct_answer': 'Dequeuing from index 0 requires shifting all remaining elements left '
                                                 'by one, costing O(n) time',
                               'difficulty': 'Easy',
                               'explanation': 'Removing elements from the front of a flat array necessitates shifting '
                                              'remaining elements.',
                               'options': ['Dequeuing from index 0 requires shifting all remaining elements left by '
                                           'one, costing O(n) time',
                                           'Arrays cannot store numbers',
                                           'Arrays do not allow appending',
                                           'Arrays crash when full'],
                               'question': 'Why is implementing a queue using a simple flat array inefficient without '
                                           'circular wrapping?'},
                              {'correct_answer': 'Modulo arithmetic (% capacity)',
                               'difficulty': 'Easy',
                               'explanation': 'Modulo (rear = (rear + 1) % capacity) wraps pointers back to index 0.',
                               'options': ['Modulo arithmetic (% capacity)',
                                           'Bitwise XOR',
                                           'Square root',
                                           'Floor division'],
                               'question': 'What mathematical operation allows an array-based queue to wrap around its '
                                           'buffer circularly?'},
                              {'correct_answer': 'Print job scheduling, message brokers (Kafka/RabbitMQ), and web '
                                                 'server request buffering',
                               'difficulty': 'Easy',
                               'explanation': 'Tasks needing sequential first-come first-served handling use queues.',
                               'options': ['Print job scheduling, message brokers (Kafka/RabbitMQ), and web server '
                                           'request buffering',
                                           'Browser Back button',
                                           'Function call stack',
                                           'Undo text editing'],
                               'question': 'Which real-world application is a classic use case for a queue?'},
                              {'correct_answer': 'Returns the element at the front of the queue without removing it',
                               'difficulty': 'Easy',
                               'explanation': 'Peek inspects the next item to be dequeued without altering queue '
                                              'contents.',
                               'options': ['Returns the element at the front of the queue without removing it',
                                           'Removes the oldest element',
                                           'Clears all elements',
                                           'Reverses the queue'],
                               'question': "What does 'peek' or 'front' operation do in a queue?"},
                              {'correct_answer': 'Enqueue into queue 1; to pop, transfer all elements except the last '
                                                 'to queue 2, then dequeue the remaining element',
                               'difficulty': 'Medium',
                               'explanation': 'Cycling elements through two queues isolates the last-added element for '
                                              'LIFO retrieval.',
                               'options': ['Enqueue into queue 1; to pop, transfer all elements except the last to '
                                           'queue 2, then dequeue the remaining element',
                                           'Reverse both queues simultaneously',
                                           'Merge the queues into an array',
                                           'Stacks cannot be simulated with queues'],
                               'question': 'How can a Stack be implemented using two Queues?'},
                              {'correct_answer': 'O(n) time and O(k) space',
                               'difficulty': 'Medium',
                               'explanation': 'A monotonic deque maintains candidate maximums, with each element '
                                              'pushed and popped at most once.',
                               'options': ['O(n) time and O(k) space',
                                           'O(n * k) time',
                                           'O(n log k) time',
                                           'O(n^2) time'],
                               'question': 'What is the time complexity of finding the maximum value in every sliding '
                                           'window of size k in an array of size n using a Monotonic Deque?'},
                              {'correct_answer': "By maintaining an explicit 'size' counter or keeping one buffer slot "
                                                 'intentionally empty',
                               'difficulty': 'Medium',
                               'explanation': 'When head == tail, an empty vs full condition is ambiguous without a '
                                              'size counter or empty slot.',
                               'options': ["By maintaining an explicit 'size' counter or keeping one buffer slot "
                                           'intentionally empty',
                                           'By checking if head == 0',
                                           'By reading memory bytes with sizeof',
                                           'By using a random number'],
                               'question': 'How does a Circular Queue distinguish between an empty queue and a '
                                           'completely full queue?'},
                              {'correct_answer': 'ArrayDeque uses a contiguous circular array with better cache '
                                                 'locality, less memory overhead, and no node allocations',
                               'difficulty': 'Medium',
                               'explanation': 'ArrayDeque avoids per-element node heap allocations, offering superior '
                                              'throughput and cache utilization.',
                               'options': ['ArrayDeque uses a contiguous circular array with better cache locality, '
                                           'less memory overhead, and no node allocations',
                                           'ArrayDeque is synchronized by default',
                                           'LinkedList cannot store objects',
                                           'ArrayDeque runs on the GPU'],
                               'question': 'In Java, why is ArrayDeque preferred over LinkedList when implementing a '
                                           'queue or stack?'},
                              {'correct_answer': 'Elements are dequeued based on priority value (highest/lowest first) '
                                                 'rather than arrival order, typically backed by a heap',
                               'difficulty': 'Medium',
                               'explanation': 'Priority queues order elements by relevance/weight rather than arrival '
                                              'time.',
                               'options': ['Elements are dequeued based on priority value (highest/lowest first) '
                                           'rather than arrival order, typically backed by a heap',
                                           'Elements are dequeued randomly',
                                           'Elements are sorted alphabetically only',
                                           'It can only hold numbers'],
                               'question': 'What is a Priority Queue and how does its ordering differ from a standard '
                                           'FIFO queue?'},
                              {'correct_answer': 'O(log n) insert and O(log n) extract-min',
                               'difficulty': 'Medium',
                               'explanation': 'Heapify operations bubble up or sift down along the tree height of log '
                                              'n.',
                               'options': ['O(log n) insert and O(log n) extract-min',
                                           'O(1) insert and O(n) extract',
                                           'O(1) for both',
                                           'O(n) for both'],
                               'question': 'What are the time complexities of insert and extract-min in a Binary '
                                           'Heap-based Priority Queue?'},
                              {'correct_answer': 'A thread-safe queue that blocks producers when full and blocks '
                                                 'consumers when empty until items become available',
                               'difficulty': 'Medium',
                               'explanation': 'Blocking queues synchronize producers and consumers without '
                                              'busy-waiting polling.',
                               'options': ['A thread-safe queue that blocks producers when full and blocks consumers '
                                           'when empty until items become available',
                                           'A queue that blocks network traffic',
                                           'A queue that cannot be read',
                                           'A queue that deletes dropped items'],
                               'question': 'What is a Blocking Queue in concurrent programming?'},
                              {'correct_answer': 'By using atomic memory orderings (acquire-release) on head and tail '
                                                 'pointers without mutex locks',
                               'difficulty': 'Medium',
                               'explanation': 'Because only one thread writes to head and one to tail, memory fences '
                                              'guarantee safe concurrency.',
                               'options': ['By using atomic memory orderings (acquire-release) on head and tail '
                                           'pointers without mutex locks',
                                           'By running producer and consumer on the same core',
                                           'By duplicating the queue every second',
                                           'By using global semaphores'],
                               'question': 'How can a circular buffer achieve lock-free Single-Producer '
                                           'Single-Consumer (SPSC) thread safety?'},
                              {'correct_answer': 'O(n) time and O(k) space',
                               'difficulty': 'Medium',
                               'explanation': 'Dequeuing k elements into a stack, popping back to queue, and rotating '
                                              'remaining n-k elements runs in linear time.',
                               'options': ['O(n) time and O(k) space', 'O(n^2) time', 'O(log n) time', 'O(k^2) time'],
                               'question': 'What is the time complexity to reverse the first k elements of a queue '
                                           'using an auxiliary stack?'},
                              {'correct_answer': 'ArrayBlockingQueue uses a fixed bounded array with a single lock; '
                                                 'LinkedBlockingQueue uses linked nodes with separate putLock and '
                                                 'takeLock',
                               'difficulty': 'Medium',
                               'explanation': 'Separate locks for head and tail in LinkedBlockingQueue enable '
                                              'concurrent enqueue and dequeue.',
                               'options': ['ArrayBlockingQueue uses a fixed bounded array with a single lock; '
                                           'LinkedBlockingQueue uses linked nodes with separate putLock and takeLock',
                                           'ArrayBlockingQueue has no locks',
                                           'LinkedBlockingQueue is unbounded only',
                                           'ArrayBlockingQueue is deprecated'],
                               'question': 'What is the difference between ArrayBlockingQueue and LinkedBlockingQueue '
                                           'in Java?'},
                              {'correct_answer': 'A lock-free FIFO queue using linked nodes and CAS operations on both '
                                                 'head and tail pointers with cooperative helper updates',
                               'difficulty': 'Hard',
                               'explanation': "The MS-queue is the foundational algorithm behind Java's "
                                              'ConcurrentLinkedQueue.',
                               'options': ['A lock-free FIFO queue using linked nodes and CAS operations on both head '
                                           'and tail pointers with cooperative helper updates',
                                           'A queue using two read-write locks',
                                           'A queue running in the Linux kernel interrupt handler',
                                           'A queue using spinlocks on arrays'],
                               'question': 'What is the Michael-Scott Non-Blocking Concurrent Queue algorithm?'},
                              {'correct_answer': 'A high-performance inter-thread messaging library using a '
                                                 'pre-allocated circular ring buffer with cache line padding and '
                                                 'lock-free CAS sequencing',
                               'difficulty': 'Hard',
                               'explanation': 'The Disruptor eliminates GC garbage, avoids false sharing via padding, '
                                              'and uses lock-free ring buffers.',
                               'options': ['A high-performance inter-thread messaging library using a pre-allocated '
                                           'circular ring buffer with cache line padding and lock-free CAS sequencing',
                                           'A multithreaded binary search tree',
                                           'A hardware network switch',
                                           'An asynchronous database query queue'],
                               'question': 'What is the LMAX Disruptor pattern and why is it faster than standard '
                                           'concurrent queues?'},
                              {'correct_answer': 'Each worker thread pushes/pops tasks from its own deque head, while '
                                                 "idle workers steal tasks from the tail of busy workers' deques",
                               'difficulty': 'Hard',
                               'explanation': 'Work-stealing minimizes contention because workers access opposite ends '
                                              'of the deque.',
                               'options': ['Each worker thread pushes/pops tasks from its own deque head, while idle '
                                           "workers steal tasks from the tail of busy workers' deques",
                                           'Workers steal memory from other processes',
                                           'Workers delete uncompleted tasks',
                                           'Workers swap CPU affinity dynamically'],
                               'question': 'What is work-stealing in task scheduling deques (e.g. Java ForkJoinPool, '
                                           'Go scheduler)?'},
                              {'correct_answer': 'Nodes embed queue pointer linkages directly inside domain data '
                                                 'structs, eliminating heap allocation overhead (common in OS kernels '
                                                 'and game engines)',
                               'difficulty': 'Hard',
                               'explanation': 'Intrusive design eliminates dynamic node wrappers, critical for '
                                              'real-time and embedded systems.',
                               'options': ['Nodes embed queue pointer linkages directly inside domain data structs, '
                                           'eliminating heap allocation overhead (common in OS kernels and game '
                                           'engines)',
                                           'A queue that monitors user keystrokes',
                                           'A queue that logs private data',
                                           'A queue stored on external flash memory'],
                               'question': 'What is an intrusive queue and where is it predominantly used?'},
                              {'correct_answer': 'Pop all elements from the rear of the deque that are less than (or '
                                                 'greater than) x before pushing x',
                               'difficulty': 'Hard',
                               'explanation': 'Purging suboptimal elements maintains strict monotonic order and bounds '
                                              'total operations to 2n.',
                               'options': ['Pop all elements from the rear of the deque that are less than (or greater '
                                           'than) x before pushing x',
                                           'Sort the deque completely',
                                           'Clear the deque if size > 10',
                                           'Multiply all elements by x'],
                               'question': 'In Monotonic Deque algorithms, what invariant must be preserved when '
                                           'pushing a new element x?'},
                              {'correct_answer': 'A priority queue supporting O(log n) extraction of both minimum and '
                                                 'maximum elements (implemented via Min-Max Heap or Interval Heap)',
                               'difficulty': 'Hard',
                               'explanation': 'Min-max heaps alternate min and max levels in a single binary tree to '
                                              'support both extremes in logarithmic time.',
                               'options': ['A priority queue supporting O(log n) extraction of both minimum and '
                                           'maximum elements (implemented via Min-Max Heap or Interval Heap)',
                                           'A queue that reverses on every pop',
                                           'A standard binary heap with two arrays',
                                           'A linked list with random pointers'],
                               'question': 'What is a double-ended priority queue (DEPQ) and what data structures '
                                           'efficiently implement it?'},
                              {'correct_answer': "Replacing 'index % capacity' with bitwise AND 'index & (capacity - "
                                                 "1)', which executes in a single CPU cycle",
                               'difficulty': 'Hard',
                               'explanation': 'Bitwise AND with (2^k - 1) is drastically faster than hardware integer '
                                              'division modulo instructions.',
                               'options': ["Replacing 'index % capacity' with bitwise AND 'index & (capacity - 1)', "
                                           'which executes in a single CPU cycle',
                                           'By removing index bounds checking',
                                           'By doubling CPU clock frequency',
                                           'By storing indices in float registers'],
                               'question': 'How does power-of-two capacity optimization speed up circular queue modulo '
                                           'indexing?'},
                              {'correct_answer': 'A lock-free/wait-free deque where the owning thread operates on the '
                                                 'bottom using LIFO order and stealers take from top using FIFO order '
                                                 'via CAS',
                               'difficulty': 'Hard',
                               'explanation': 'Chase-Lev is the standard algorithm for high-performance fork-join '
                                              'parallel runtimes.',
                               'options': ['A lock-free/wait-free deque where the owning thread operates on the bottom '
                                           'using LIFO order and stealers take from top using FIFO order via CAS',
                                           'A queue that runs on GPU compute shaders',
                                           'A queue used exclusively in distributed databases',
                                           'A queue with three heads'],
                               'question': 'What is the Chase-Lev Work-Stealing Deque algorithm?'},
                              {'correct_answer': 'A flow-control mechanism where consumers signal demand to producers '
                                                 'to prevent queue buffer overflow when producers outpace consumers',
                               'difficulty': 'Hard',
                               'explanation': 'Backpressure protects message queues from unbounded memory growth and '
                                              'OutOfMemory crashes.',
                               'options': ['A flow-control mechanism where consumers signal demand to producers to '
                                           'prevent queue buffer overflow when producers outpace consumers',
                                           'Air pressure inside cooling fans',
                                           'A hardware interrupt that halts the CPU',
                                           'A technique to encrypt queued messages'],
                               'question': 'What is backpressure in reactive streams and queue-based architectures?'},
                              {'correct_answer': 'O(n) linear time',
                               'difficulty': 'Hard',
                               'explanation': 'Sifting down from the lowest internal nodes up to root converges '
                                              'geometrically to O(n) total operations.',
                               'options': ['O(n) linear time', 'O(n log n) time', 'O(n^2) time', 'O(log n) time'],
                               'question': 'What is the time complexity of building a Binary Heap from an unordered '
                                           "array of n elements using Floyd's build-heap algorithm?"}],
 'Singly Linked Lists': [{'correct_answer': 'A linear data structure where each node contains data and a '
                                            'pointer/reference to the next node',
                          'difficulty': 'Easy',
                          'explanation': 'Singly linked lists store nodes dynamically connected via forward '
                                         'references.',
                          'options': ['A linear data structure where each node contains data and a pointer/reference '
                                      'to the next node',
                                      'An array with dynamic resizing',
                                      'A non-linear graph with cycles',
                                      'A tree with two child pointers per node'],
                          'question': 'What is a singly linked list?'},
                         {'correct_answer': 'The first node in the list',
                          'difficulty': 'Easy',
                          'explanation': 'The head pointer serves as the entry anchor to the linked list.',
                          'options': ['The first node in the list',
                                      'The last node in the list',
                                      'The middle node in the list',
                                      'The total count of nodes'],
                          'question': "What does the 'head' pointer in a linked list refer to?"},
                         {'correct_answer': 'null / None / nullptr',
                          'difficulty': 'Easy',
                          'explanation': 'The final node points to null, marking the end of the chain.',
                          'options': ['null / None / nullptr',
                                      'A pointer back to the head',
                                      'Zero',
                                      'A pointer to itself'],
                          'question': "What value does the 'next' pointer of the tail node hold in a standard singly "
                                      'linked list?'},
                         {'correct_answer': 'O(1) - Constant time',
                          'difficulty': 'Easy',
                          'explanation': 'Prepend requires setting newNode.next = head and head = newNode, which is '
                                         'O(1).',
                          'options': ['O(1) - Constant time', 'O(n) - Linear time', 'O(log n)', 'O(n^2)'],
                          'question': 'What is the time complexity of inserting a node at the head (beginning) of a '
                                      'singly linked list?'},
                         {'correct_answer': 'O(k) or O(n) because nodes must be traversed sequentially from head',
                          'difficulty': 'Easy',
                          'explanation': 'Linked lists do not support random access; traversal from head is required.',
                          'options': ['O(k) or O(n) because nodes must be traversed sequentially from head',
                                      'O(1) using index arithmetic',
                                      'O(log n) using binary search',
                                      'O(n^2)'],
                          'question': 'What is the time complexity of accessing an element at index k in a singly '
                                      'linked list?'},
                         {'correct_answer': 'O(1)',
                          'difficulty': 'Easy',
                          'explanation': 'Head deletion simply updates head = head.next, executing in constant time.',
                          'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n^2)'],
                          'question': 'What is the time complexity of deleting the first node (head) of a singly '
                                      'linked list?'},
                         {'correct_answer': 'Array elements are stored contiguously; linked list nodes can be '
                                            'scattered across the heap',
                          'difficulty': 'Easy',
                          'explanation': 'Linked list nodes are allocated independently and linked via reference '
                                         'pointers.',
                          'options': ['Array elements are stored contiguously; linked list nodes can be scattered '
                                      'across the heap',
                                      'Arrays use pointers for every element',
                                      'Linked lists use less memory than arrays',
                                      'Arrays cannot store objects'],
                          'question': 'What is the primary memory difference between an array and a linked list?'},
                         {'correct_answer': 'Each node stores an extra reference pointer alongside the data payload',
                          'difficulty': 'Easy',
                          'explanation': 'Node reference pointers (4 to 8 bytes each) add memory overhead to every '
                                         'stored element.',
                          'options': ['Each node stores an extra reference pointer alongside the data payload',
                                      'Linked lists allocate on the GPU',
                                      'Linked lists compress data',
                                      'Linked lists duplicate each value'],
                          'question': 'Why does a singly linked list require more memory per element than an array of '
                                      'the same data type?'},
                         {'correct_answer': 'head == null',
                          'difficulty': 'Easy',
                          'explanation': 'When the head reference is null, no nodes exist in the list.',
                          'options': ['head == null', 'head.next == null', 'head.data == 0', 'tail == head'],
                          'question': 'What condition indicates that a singly linked list is empty?'},
                         {'correct_answer': 'O(n) linear scan',
                          'difficulty': 'Easy',
                          'explanation': "Finding an element requires sequential traversal comparing each node's data.",
                          'options': ['O(n) linear scan', 'O(1)', 'O(log n)', 'O(n log n)'],
                          'question': 'What is the time complexity of searching for a value in an unsorted singly '
                                      'linked list of n nodes?'},
                         {'correct_answer': 'Detecting if a linked list contains a cycle using two pointers moving at '
                                            'different speeds (1 step and 2 steps)',
                          'difficulty': 'Medium',
                          'explanation': 'If a cycle exists, the fast pointer will eventually lap and meet the slow '
                                         'pointer.',
                          'options': ['Detecting if a linked list contains a cycle using two pointers moving at '
                                      'different speeds (1 step and 2 steps)',
                                      'Sorting nodes in O(n log n)',
                                      'Finding the maximum value in O(1)',
                                      'Deleting duplicate nodes'],
                          'question': "What is Floyd's Cycle-Finding Algorithm (Tortoise and Hare) used for in linked "
                                      'lists?'},
                         {'correct_answer': 'O(n) time and O(1) auxiliary space',
                          'difficulty': 'Medium',
                          'explanation': 'Iterative reversal uses three pointers (prev, current, next) in a single '
                                         'linear pass.',
                          'options': ['O(n) time and O(1) auxiliary space',
                                      'O(n) time and O(n) space',
                                      'O(n^2) time and O(1) space',
                                      'O(log n) time and O(1) space'],
                          'question': 'What is the time and space complexity of reversing a singly linked list '
                                      'iteratively?'},
                         {'correct_answer': 'Use slow and fast pointers; when fast reaches the end, slow is at the '
                                            'middle',
                          'difficulty': 'Medium',
                          'explanation': 'Fast advances 2 steps while slow advances 1 step, landing slow at the '
                                         'midpoint.',
                          'options': ['Use slow and fast pointers; when fast reaches the end, slow is at the middle',
                                      'Count all nodes first and divide by 2',
                                      'Use binary search on node values',
                                      'Traverse backwards from tail'],
                          'question': 'How do you find the middle node of a singly linked list in a single pass?'},
                         {'correct_answer': 'O(n) because we must traverse from head to find the second-to-last node',
                          'difficulty': 'Medium',
                          'explanation': 'To unlink the tail in a singly linked list, the preceding node must be '
                                         'reached via traversal.',
                          'options': ['O(n) because we must traverse from head to find the second-to-last node',
                                      'O(1)',
                                      'O(log n)',
                                      'O(n^2)'],
                          'question': 'What is the time complexity of deleting a node at the end (tail) of a singly '
                                      'linked list without a tail pointer reference to the second-to-last node?'},
                         {'correct_answer': 'Move first pointer k steps ahead, then move both first and second '
                                            'pointers together until first reaches null',
                          'difficulty': 'Medium',
                          'explanation': 'Maintaining a fixed gap of k nodes between two pointers locates the target '
                                         'in a single pass.',
                          'options': ['Move first pointer k steps ahead, then move both first and second pointers '
                                      'together until first reaches null',
                                      'Reverse the entire list twice',
                                      'Store all nodes in an external file',
                                      'Use recursion to double the speed'],
                          'question': 'How do you find the k-th node from the end of a singly linked list in one '
                                      'pass?'},
                         {'correct_answer': 'A placeholder node placed before head to eliminate edge cases for '
                                            'insertions and deletions at index 0',
                          'difficulty': 'Medium',
                          'explanation': 'Dummy heads standardize operations so inserting/removing at the front '
                                         'requires no special if-statements.',
                          'options': ['A placeholder node placed before head to eliminate edge cases for insertions '
                                      'and deletions at index 0',
                                      'A node that encrypts list data',
                                      'A node with infinite data value',
                                      'A node that marks memory errors'],
                          'question': 'What is a Sentinel Node (Dummy Head) in linked list implementations?'},
                         {'correct_answer': 'It sorts linked lists in O(n log n) time with O(1) auxiliary space '
                                            'because pointer re-linking requires no extra buffer',
                          'difficulty': 'Medium',
                          'explanation': 'Merging two sorted lists only requires rearranging pointer references '
                                         'without copying buffers.',
                          'options': ['It sorts linked lists in O(n log n) time with O(1) auxiliary space because '
                                      'pointer re-linking requires no extra buffer',
                                      'It requires O(n^2) extra space',
                                      'It runs in O(n!) time',
                                      'Merge sort cannot be used on linked lists'],
                          'question': 'How does merge sort perform on singly linked lists compared to arrays?'},
                         {'correct_answer': 'No, because finding the midpoint requires O(n) traversal, resulting in '
                                            'O(n) total time instead of O(log n)',
                          'difficulty': 'Medium',
                          'explanation': 'Without O(1) random indexing, binary search degenerates to linear time.',
                          'options': ['No, because finding the midpoint requires O(n) traversal, resulting in O(n) '
                                      'total time instead of O(log n)',
                                      'Yes, it runs in O(log n) time',
                                      'Yes, using pointer arithmetic',
                                      'Only if nodes store integers'],
                          'question': 'Can binary search be implemented efficiently on a sorted singly linked list?'},
                         {'correct_answer': 'It deletes the node in O(1) without access to the predecessor, provided '
                                            'the node is not the tail',
                          'difficulty': 'Medium',
                          'explanation': "Copying next node's value and bypassing next node simulates deletion of the "
                                         'current node.',
                          'options': ['It deletes the node in O(1) without access to the predecessor, provided the '
                                      'node is not the tail',
                                      'It crashes the program with a bus error',
                                      'It creates a cycle in the list',
                                      'It reverses the list'],
                          'question': "What happens if you delete a node by doing 'node.data = node.next.data; "
                                      "node.next = node.next.next;'?"},
                         {'correct_answer': 'Non-contiguous node heap allocations cause pointer-chasing and frequent '
                                            'L1/L2 cache misses',
                          'difficulty': 'Medium',
                          'explanation': 'Following scattered heap pointers requires fetching non-adjacent cache lines '
                                         'on each hop.',
                          'options': ['Non-contiguous node heap allocations cause pointer-chasing and frequent L1/L2 '
                                      'cache misses',
                                      'Nodes take up too many registers',
                                      'Linked lists disable hardware pipelining',
                                      'Cache memories only store arrays'],
                          'question': 'Why do linked lists typically exhibit poor CPU cache performance?'},
                         {'correct_answer': 'Reset slow to head; advance both slow and fast by 1 step simultaneously; '
                                            'their collision point is the cycle start',
                          'difficulty': 'Hard',
                          'explanation': 'Mathematical proof shows distance from head to cycle start equals distance '
                                         'from collision to cycle start modulo L.',
                          'options': ['Reset slow to head; advance both slow and fast by 1 step simultaneously; their '
                                      'collision point is the cycle start',
                                      'Advance fast 2 steps and slow 0 steps',
                                      'Reverse all pointers until meeting null',
                                      'Count the total nodes and divide by cycle length'],
                          'question': "In Floyd's cycle detection, how is the exact start node of the cycle located "
                                      'after slow and fast pointers meet?'},
                         {'correct_answer': 'A linked list where each node stores a small array of elements, balancing '
                                            'O(1) insertions with array cache locality',
                          'difficulty': 'Hard',
                          'explanation': 'Unrolled lists reduce pointer overhead and boost cache performance by '
                                         'batching elements into chunked nodes.',
                          'options': ['A linked list where each node stores a small array of elements, balancing O(1) '
                                      'insertions with array cache locality',
                                      'A linked list with no pointers',
                                      'A list unrolled by compiler optimization loops',
                                      'A list stored on tape drives'],
                          'question': 'What is an Unrolled Linked List and what problem does it solve?'},
                         {'correct_answer': 'By maintaining multiple probabilistic layers of forward pointers that '
                                            'skip over intermediate nodes',
                          'difficulty': 'Hard',
                          'explanation': 'Skip lists use randomized tower heights to skip spans of nodes in '
                                         'logarithmic steps.',
                          'options': ['By maintaining multiple probabilistic layers of forward pointers that skip over '
                                      'intermediate nodes',
                                      'By converting the list to a balanced binary search tree',
                                      'By indexing nodes with hash tables',
                                      'By storing pointers in CPU registers'],
                          'question': 'How does a Skip List achieve O(log n) search, insertion, and deletion using '
                                      'linked lists?'},
                         {'correct_answer': "Interleave copied nodes directly after original nodes (A -> A' -> B -> "
                                            "B'), assign random pointers, then separate lists",
                          'difficulty': 'Hard',
                          'explanation': 'Interleaving links original nodes to copies without needing an auxiliary '
                                         'hash map.',
                          'options': ["Interleave copied nodes directly after original nodes (A -> A' -> B -> B'), "
                                      'assign random pointers, then separate lists',
                                      'Store all nodes in a HashMap taking O(n) space',
                                      "Use Floyd's cycle finder",
                                      "Run Dijkstra's algorithm"],
                          'question': 'What is the algorithm to clone a linked list with random pointers in O(n) time '
                                      'and O(1) auxiliary space?'},
                         {'correct_answer': 'A list where each node stores the XOR of previous and next node addresses '
                                            '(npx = prev ^ next) in a single pointer field',
                          'difficulty': 'Hard',
                          'explanation': 'XORing adjacent addresses allows bidirectional traversal using only one '
                                         'pointer word per node.',
                          'options': ['A list where each node stores the XOR of previous and next node addresses (npx '
                                      '= prev ^ next) in a single pointer field',
                                      'A list encrypted with XOR cipher',
                                      'A list that only stores boolean values',
                                      'A list running on quantum computers'],
                          'question': 'What is a XOR Linked List (Memory Efficient Doubly Linked List)?'},
                         {'correct_answer': 'Using AtomicMarkableReference (marking next pointer bit before logical '
                                            'deletion, then CAS physical removal)',
                          'difficulty': 'Hard',
                          'explanation': 'Logical deletion marks the low-order bit of the pointer atomically, '
                                         'preventing concurrent insertion into deleted nodes.',
                          'options': ['Using AtomicMarkableReference (marking next pointer bit before logical '
                                      'deletion, then CAS physical removal)',
                                      'Using global mutex locks around the entire list',
                                      'By disabling interrupts during traversal',
                                      'By creating new copies of the entire list'],
                          'question': "How does lock-free linked list insertion (Harris's Algorithm) handle concurrent "
                                      'insertions and deletions safely?'},
                         {'correct_answer': 'O(N log K) time and O(K) space',
                          'difficulty': 'Hard',
                          'explanation': 'A heap of size K extracts minimum node and advances in O(log K) for each of '
                                         'the N total nodes.',
                          'options': ['O(N log K) time and O(K) space',
                                      'O(N * K) time and O(1) space',
                                      'O(N^2) time and O(N) space',
                                      'O(K log N) time and O(N) space'],
                          'question': 'What is the time complexity of merging K sorted linked lists of total N nodes '
                                      'using a Min-Heap (Priority Queue)?'},
                         {'correct_answer': 'Prepending an element shares the entire existing tail without copying, '
                                            'achieving structural sharing',
                          'difficulty': 'Hard',
                          'explanation': 'Immutability allows new lists to point directly to existing node tails '
                                         'without mutation hazards.',
                          'options': ['Prepending an element shares the entire existing tail without copying, '
                                      'achieving structural sharing',
                                      'Functional lists are stored in ROM',
                                      'Functional lists cannot be read',
                                      'Every operation deep-copies the entire list'],
                          'question': 'In functional programming languages (like Haskell or Scala), why are singly '
                                      'linked lists persistent data structures?'},
                         {'correct_answer': 'O(n) time and O(1) space (find middle, reverse second half, merge halves '
                                            'alternately)',
                          'difficulty': 'Hard',
                          'explanation': 'Finding mid, reversing half, and interleaving all run in O(n) linear time '
                                         'with constant pointers.',
                          'options': ['O(n) time and O(1) space (find middle, reverse second half, merge halves '
                                      'alternately)',
                                      'O(n^2) time',
                                      'O(n log n) time',
                                      'O(2^n) time'],
                          'question': 'What is the time complexity of reordering a linked list as L0 -> Ln -> L1 -> '
                                      'Ln-1 using three sequential operations?'},
                         {'correct_answer': 'Frequent individual node allocations/deallocations on the heap scatter '
                                            'free memory into unusable fragments',
                          'difficulty': 'Hard',
                          'explanation': 'Small object allocations cause external heap fragmentation, mitigated by '
                                         'object pools or custom allocators.',
                          'options': ['Frequent individual node allocations/deallocations on the heap scatter free '
                                      'memory into unusable fragments',
                                      'Memory fragmentation speeds up allocation',
                                      'Nodes are compressed automatically by RAM',
                                      'Fragmentation only affects disk files'],
                          'question': 'How does memory fragmentation affect massive linked list allocations in '
                                      'long-running processes?'}],
 'Stacks (LIFO Operations)': [{'correct_answer': 'LIFO (Last In, First Out)',
                               'difficulty': 'Easy',
                               'explanation': 'A stack processes the most recently added item first.',
                               'options': ['LIFO (Last In, First Out)',
                                           'FIFO (First In, First Out)',
                                           'Random access',
                                           'Priority based'],
                               'question': 'What order of element processing does a Stack follow?'},
                              {'correct_answer': 'push',
                               'difficulty': 'Easy',
                               'explanation': 'Push adds an element to the top of the stack.',
                               'options': ['push', 'pop', 'peek', 'enqueue'],
                               'question': 'Which operation inserts an element onto the top of a stack?'},
                              {'correct_answer': 'pop',
                               'difficulty': 'Easy',
                               'explanation': 'Pop removes the element currently at the top of the stack.',
                               'options': ['pop', 'push', 'dequeue', 'poll'],
                               'question': 'Which operation removes and returns the top element of a stack?'},
                              {'correct_answer': 'peek / top',
                               'difficulty': 'Easy',
                               'explanation': 'Peek returns the top item without mutating stack state.',
                               'options': ['peek / top', 'pop', 'front', 'poll'],
                               'question': 'Which operation inspects the top element of a stack without removing it?'},
                              {'correct_answer': 'O(1) - Constant time',
                               'difficulty': 'Easy',
                               'explanation': 'Both operations manipulate only the top element, requiring constant '
                                              'time.',
                               'options': ['O(1) - Constant time', 'O(n) - Linear time', 'O(log n)', 'O(n^2)'],
                               'question': 'What is the time complexity of push and pop operations in a stack?'},
                              {'correct_answer': 'Attempting to push an element onto a stack that has exceeded its '
                                                 'maximum allocated memory/capacity',
                               'difficulty': 'Easy',
                               'explanation': 'Stack overflow occurs when call stack or fixed stack memory is '
                                              'exhausted.',
                               'options': ['Attempting to push an element onto a stack that has exceeded its maximum '
                                           'allocated memory/capacity',
                                           'Attempting to pop from an empty stack',
                                           'Accessing a null pointer in array',
                                           'A syntax error in stack code'],
                               'question': "What condition causes a 'Stack Overflow' error?"},
                              {'correct_answer': 'Attempting to pop or peek from an empty stack',
                               'difficulty': 'Easy',
                               'explanation': 'Underflow happens when removing elements from a stack with zero items.',
                               'options': ['Attempting to pop or peek from an empty stack',
                                           'Pushing too many elements',
                                           'Allocating stack on heap',
                                           'Running out of disk space'],
                               'question': "What condition causes a 'Stack Underflow' error?"},
                              {'correct_answer': 'Undo / Redo functionality in text editors and browser back button '
                                                 'navigation',
                               'difficulty': 'Easy',
                               'explanation': 'Tracking previous actions in reverse chronological order requires a '
                                              'LIFO stack.',
                               'options': ['Undo / Redo functionality in text editors and browser back button '
                                           'navigation',
                                           'Printer print queue',
                                           'Round-robin scheduler',
                                           'Customer service ticket queue'],
                               'question': 'Which real-world feature is commonly implemented using a stack?'},
                              {'correct_answer': 'Call Stack (Runtime Stack)',
                               'difficulty': 'Easy',
                               'explanation': 'Function activation frames are pushed upon invocation and popped upon '
                                              'return.',
                               'options': ['Call Stack (Runtime Stack)', 'Free Heap', 'I/O Buffer', 'Disk Cache'],
                               'question': 'Which memory structure does the CPU use to manage function calls, local '
                                           'variables, and return addresses?'},
                              {'correct_answer': 'O(1)',
                               'difficulty': 'Easy',
                               'explanation': 'Checking if size == 0 or top == -1 takes constant time.',
                               'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n^2)'],
                               'question': 'What is the time complexity of checking if a stack is empty (isEmpty)?'},
                              {'correct_answer': 'Push opening brackets onto stack; when encountering a closing '
                                                 'bracket, pop and verify matching type',
                               'difficulty': 'Medium',
                               'explanation': 'LIFO property ensures the most recently opened bracket matches the next '
                                              'closed bracket.',
                               'options': ['Push opening brackets onto stack; when encountering a closing bracket, pop '
                                           'and verify matching type',
                                           'Count opening and closing brackets without stack',
                                           'Convert string to an integer',
                                           'Use binary search on brackets'],
                               'question': 'How does a stack verify balanced parentheses in an expression (e.g., '
                                           "'{[()]}')?"},
                              {'correct_answer': 'Shunting-Yard Algorithm (Edsger Dijkstra)',
                               'difficulty': 'Medium',
                               'explanation': 'Shunting-Yard uses an operator stack to enforce mathematical precedence '
                                              'and associativity.',
                               'options': ['Shunting-Yard Algorithm (Edsger Dijkstra)',
                                           "Kadane's Algorithm",
                                           'Floyd-Warshall Algorithm',
                                           "Kruskal's Algorithm"],
                               'question': 'What algorithm uses a stack to convert Infix mathematical expressions to '
                                           'Postfix (Reverse Polish Notation)?'},
                              {'correct_answer': 'O(n) time and O(n) space',
                               'difficulty': 'Medium',
                               'explanation': 'Scanning tokens once, pushing operands, and popping for operators runs '
                                              'in linear time.',
                               'options': ['O(n) time and O(n) space', 'O(n^2) time', 'O(n log n) time', 'O(2^n) time'],
                               'question': 'What is the time complexity of evaluating a Postfix expression of length n '
                                           'using a stack?'},
                              {'correct_answer': 'A stack whose elements are kept strictly increasing or decreasing, '
                                                 'used to find Next Greater / Smaller Element in O(n)',
                               'difficulty': 'Medium',
                               'explanation': 'Monotonic stacks solve next-greater element and histogram rectangle '
                                              'problems in linear time.',
                               'options': ['A stack whose elements are kept strictly increasing or decreasing, used to '
                                           'find Next Greater / Smaller Element in O(n)',
                                           'A stack that can store only one data type',
                                           'A stack that never overflows',
                                           'A stack implemented with a single pointer'],
                               'question': 'What is a Monotonic Stack and what is its primary application?'},
                              {'correct_answer': 'Push new items to inbox; to dequeue, if outbox is empty, pop all '
                                                 'inbox items into outbox and pop from outbox',
                               'difficulty': 'Medium',
                               'explanation': 'Pouring inbox into outbox inverts the order, providing FIFO behavior in '
                                              'amortized O(1) time.',
                               'options': ['Push new items to inbox; to dequeue, if outbox is empty, pop all inbox '
                                           'items into outbox and pop from outbox',
                                           'Alternate pushing between stack 1 and stack 2',
                                           'Reverse both stacks simultaneously',
                                           'Queues cannot be implemented with stacks'],
                               'question': 'How can a Queue be implemented using two Stacks (inbox and outbox)?'},
                              {'correct_answer': 'O(n) time and O(n) space',
                               'difficulty': 'Medium',
                               'explanation': 'Each bar is pushed and popped at most once, achieving linear time.',
                               'options': ['O(n) time and O(n) space', 'O(n^2) time', 'O(n log n) time', 'O(n^3) time'],
                               'question': "What is the time complexity to find the 'Largest Rectangle in Histogram' "
                                           'using a monotonic increasing stack?'},
                              {'correct_answer': 'Maintain an auxiliary stack (or paired tuple) that tracks the '
                                                 'minimum value at each stack depth',
                               'difficulty': 'Medium',
                               'explanation': 'Storing current minimum at each level allows constant-time retrieval of '
                                              'the minimum element.',
                               'options': ['Maintain an auxiliary stack (or paired tuple) that tracks the minimum '
                                           'value at each stack depth',
                                           'Sort the stack after every push',
                                           'Search the stack linearly in getMin()',
                                           'Use a binary heap inside the stack'],
                               'question': 'How can a Min-Stack be designed to support push, pop, and getMin() in O(1) '
                                           'time?'},
                              {'correct_answer': 'DFS uses a stack (either the call stack via recursion or an explicit '
                                                 'iterative stack) to explore deeply along branches',
                               'difficulty': 'Medium',
                               'explanation': 'LIFO exploration guarantees advancing down a path before backtracking.',
                               'options': ['DFS uses a stack (either the call stack via recursion or an explicit '
                                           'iterative stack) to explore deeply along branches',
                                           'DFS uses a queue instead of a stack',
                                           'DFS does not use any data structures',
                                           'DFS uses a hash table for traversal'],
                               'question': 'How does Depth-First Search (DFS) on a graph relate to a stack?'},
                              {'correct_answer': 'The compiler replaces a recursive call at the tail position of a '
                                                 'function with a jump/loop, reusing the current stack frame',
                               'difficulty': 'Medium',
                               'explanation': 'TCO avoids creating new stack frames when the function call is the '
                                              'final action in the caller.',
                               'options': ['The compiler replaces a recursive call at the tail position of a function '
                                           'with a jump/loop, reusing the current stack frame',
                                           'It allocates stack frames on disk',
                                           'It terminates deep recursion after 100 calls',
                                           'It runs recursive calls in parallel'],
                               'question': 'What is tail call optimization (TCO) and how does it prevent call stack '
                                           'overflow?'},
                              {'correct_answer': 'Yes, by using an explicit stack data structure to simulate function '
                                                 'activation frames',
                               'difficulty': 'Medium',
                               'explanation': 'Any recursive process can be simulated iteratively with an explicit '
                                              'stack storing parameters and state.',
                               'options': ['Yes, by using an explicit stack data structure to simulate function '
                                           'activation frames',
                                           'No, some algorithms require hardware recursion',
                                           'Only sorting algorithms can be converted',
                                           'Only if recursion depth is less than 10'],
                               'question': 'Can every recursive algorithm be converted into an iterative algorithm?'},
                              {'correct_answer': 'It uses atomic Compare-And-Swap (CAS) in a loop to update the head '
                                                 'pointer without blocking mutexes',
                               'difficulty': 'Hard',
                               'explanation': 'Treiber stacks achieve non-blocking concurrency using CAS on the top '
                                              'node reference.',
                               'options': ['It uses atomic Compare-And-Swap (CAS) in a loop to update the head pointer '
                                           'without blocking mutexes',
                                           'It uses reentrant locks on every push',
                                           'It duplicates the stack per thread',
                                           'It disables thread preemption in kernel'],
                               'question': 'What is a Lock-Free Stack (Treiber Stack) and how does it handle '
                                           'concurrent pushes and pops?'},
                              {'correct_answer': 'It pairs colliding concurrent push and pop operations in an '
                                                 'elimination array so they cancel out without touching the top '
                                                 'pointer',
                               'difficulty': 'Hard',
                               'explanation': 'Elimination arrays alleviate extreme contention on the top pointer '
                                              'under heavy multi-core load.',
                               'options': ['It pairs colliding concurrent push and pop operations in an elimination '
                                           'array so they cancel out without touching the top pointer',
                                           'It deletes corrupted elements',
                                           'It expands stack capacity exponentially',
                                           'It converts stacks into ring buffers'],
                               'question': 'What is an Elimination Backoff Stack and what high-concurrency problem '
                                           'does it solve?'},
                              {'correct_answer': 'O(n) time and O(n) space',
                               'difficulty': 'Hard',
                               'explanation': 'A monotonic decreasing stack computes bounded water reservoirs in a '
                                              'single linear pass.',
                               'options': ['O(n) time and O(n) space', 'O(n^2) time', 'O(n log n) time', 'O(2^n) time'],
                               'question': "What is the time complexity of the 'Trapping Rain Water' problem using a "
                                           'monotonic stack?'},
                              {'correct_answer': 'It pushes tokens (shift) and replaces matching grammar rule handles '
                                                 'on the stack with non-terminals (reduce)',
                               'difficulty': 'Hard',
                               'explanation': 'Shift-reduce parsers maintain parser states and grammar symbols on a '
                                              'stack to parse deterministic CFGs.',
                               'options': ['It pushes tokens (shift) and replaces matching grammar rule handles on the '
                                           'stack with non-terminals (reduce)',
                                           'It compiles source code directly to microcode',
                                           'It parses strings using regular expressions',
                                           'It eliminates parse trees'],
                               'question': 'In compiler design, what is an LR Parser (Shift-Reduce Parser) and how '
                                           'does it use a parse stack?'},
                              {'correct_answer': 'O(n) auxiliary space to represent the 3 peg stacks',
                               'difficulty': 'Hard',
                               'explanation': 'Disks are stored across three peg stacks of maximum height n.',
                               'options': ['O(n) auxiliary space to represent the 3 peg stacks',
                                           'O(2^n) space',
                                           'O(1) space',
                                           'O(n^2) space'],
                               'question': 'What is the space complexity of solving the Tower of Hanoi problem '
                                           'iteratively using 3 stacks?'},
                              {'correct_answer': 'It places a random integer sentinel value right before the return '
                                                 'address; checking it before function return detects overwrite',
                               'difficulty': 'Hard',
                               'explanation': 'If a buffer overflows into the return address, the canary value '
                                              'changes, triggering abort.',
                               'options': ['It places a random integer sentinel value right before the return address; '
                                           'checking it before function return detects overwrite',
                                           'It encrypts the entire heap',
                                           'It disables pointer arithmetic',
                                           'It runs code inside a virtual sandbox'],
                               'question': 'How does Stack Canary protect against stack buffer overflow attacks in '
                                           'compiled code (GCC -fstack-protector)?'},
                              {'correct_answer': 'A stack where push and pop operations return a new stack reference '
                                                 'while preserving the previous version via structural sharing',
                               'difficulty': 'Hard',
                               'explanation': 'A persistent stack shares its tail node with previous versions, '
                                              'allowing time-traveling without copying.',
                               'options': ['A stack where push and pop operations return a new stack reference while '
                                           'preserving the previous version via structural sharing',
                                           'A stack saved to an SQL database',
                                           'A stack that cannot be popped',
                                           'A stack stored in non-volatile NVRAM'],
                               'question': 'What is a Persistent Stack (Purely Functional Stack)?'},
                              {'correct_answer': "Segmented stacks allocate linked stack chunks (causing 'hot split' "
                                                 'issues); contiguous stacks allocate a 2x larger stack and copy '
                                                 'frames',
                               'difficulty': 'Hard',
                               'explanation': 'Go moved from segmented stacks to copying stacks to avoid thrashing on '
                                              'function boundaries.',
                               'options': ["Segmented stacks allocate linked stack chunks (causing 'hot split' "
                                           'issues); contiguous stacks allocate a 2x larger stack and copy frames',
                                           'Segmented stacks never resize',
                                           'Contiguous stacks run on separate threads',
                                           'Goroutines do not use stacks'],
                               'question': 'What is the difference between segmented stacks and contiguous stack '
                                           'reallocation in language runtimes (e.g. Go goroutines)?'},
                              {'correct_answer': 'It maintains an operand stack and an operator stack; closing '
                                                 'parentheses trigger popping operator and two operands',
                               'difficulty': 'Hard',
                               'explanation': 'Two stacks separate numbers and operations, evaluating sub-expressions '
                                              'inside parentheses cleanly.',
                               'options': ['It maintains an operand stack and an operator stack; closing parentheses '
                                           'trigger popping operator and two operands',
                                           'It sorts numbers first',
                                           'It converts expressions to tree graphs',
                                           'It hashes strings'],
                               'question': "How does Dijkstra's Two-Stack Algorithm evaluate fully parenthesized infix "
                                           'arithmetic expressions?'},
                              {'correct_answer': 'Stackful coroutines have their own allocated call stack and can '
                                                 'yield from nested calls; stackless coroutines compile into state '
                                                 'machines sharing caller stack',
                               'difficulty': 'Hard',
                               'explanation': 'Stackless coroutines (like C# async/await, Python asyncio) serialize '
                                              'state into a heap object without private call stacks.',
                               'options': ['Stackful coroutines have their own allocated call stack and can yield from '
                                           'nested calls; stackless coroutines compile into state machines sharing '
                                           'caller stack',
                                           'Stackful coroutines are always faster',
                                           'Stackless coroutines cannot run async code',
                                           'Stackful coroutines run without RAM'],
                               'question': 'In coroutine implementations, what is the distinction between stackful '
                                           'coroutines and stackless coroutines?'}],
 'Strings and String Manipulation': [{'correct_answer': 'A sequence of characters stored in memory',
                                      'difficulty': 'Easy',
                                      'explanation': 'Strings represent textual data as an ordered sequence of '
                                                     'characters.',
                                      'options': ['A sequence of characters stored in memory',
                                                  'A primitive integer data type',
                                                  'A binary tree node',
                                                  'A database record'],
                                      'question': 'What is a string in computer science?'},
                                     {'correct_answer': 'To ensure security, caching of hash codes, thread safety, and '
                                                        'string pool optimization',
                                      'difficulty': 'Easy',
                                      'explanation': 'Immutability allows safe sharing across threads and caching in '
                                                     'string literal pools.',
                                      'options': ['To ensure security, caching of hash codes, thread safety, and '
                                                  'string pool optimization',
                                                  'Because strings cannot store numbers',
                                                  'Because memory cannot store letters',
                                                  'To prevent strings from being printed'],
                                      'question': 'Why are strings immutable in languages like Java and Python?'},
                                     {'correct_answer': 'O(1) - Constant time',
                                      'difficulty': 'Easy',
                                      'explanation': 'Languages that track length as an internal field return length '
                                                     'in O(1).',
                                      'options': ['O(1) - Constant time', 'O(n) - Linear time', 'O(log n)', 'O(n^2)'],
                                      'question': 'What is the time complexity of finding the length of a string in '
                                                  'languages that store length metadata (e.g. Java, Python)?'},
                                     {'correct_answer': "With a null character '\\0' (ASCII 0)",
                                      'difficulty': 'Easy',
                                      'explanation': "C strings are terminated by a sentinel null byte '\\0'.",
                                      'options': ["With a null character '\\0' (ASCII 0)",
                                                  "With a newline '\\n'",
                                                  "With a dollar sign '$'",
                                                  'With an EOF byte'],
                                      'question': 'In C, how is the end of a null-terminated string marked?'},
                                     {'correct_answer': "O(n) because it must scan characters until encountering '\\0'",
                                      'difficulty': 'Easy',
                                      'explanation': 'C null-terminated strings require traversing characters '
                                                     'sequentially to determine length.',
                                      'options': ["O(n) because it must scan characters until encountering '\\0'",
                                                  'O(1)',
                                                  'O(log n)',
                                                  'O(n^2)'],
                                      'question': 'What is the time complexity of strlen() in C?'},
                                     {'correct_answer': 'A string that reads the same forwards and backwards (e.g. '
                                                        "'racecar')",
                                      'difficulty': 'Easy',
                                      'explanation': 'Palindromes have symmetrical character sequences.',
                                      'options': ['A string that reads the same forwards and backwards (e.g. '
                                                  "'racecar')",
                                                  'A string containing only vowels',
                                                  'A string with unique characters',
                                                  'An encrypted string'],
                                      'question': 'What is a palindrome string?'},
                                     {'correct_answer': 'StringBuilder',
                                      'difficulty': 'Easy',
                                      'explanation': 'StringBuilder is mutable and un-synchronized, making '
                                                     'single-threaded concatenation fast.',
                                      'options': ['StringBuilder', 'String', 'StringBuffer', 'ArrayString'],
                                      'question': 'What class is recommended in Java for performing frequent string '
                                                  'concatenations in a single thread?'},
                                     {'correct_answer': 'A word formed by rearranging the exact letters of another '
                                                        "word (e.g. 'listen' and 'silent')",
                                      'difficulty': 'Easy',
                                      'explanation': 'Anagrams share identical character counts and frequencies in '
                                                     'different permutations.',
                                      'options': ['A word formed by rearranging the exact letters of another word '
                                                  "(e.g. 'listen' and 'silent')",
                                                  'A word with opposite meaning',
                                                  'A word with no consonants',
                                                  'A capitalized word'],
                                      'question': 'What is an anagram of a string?'},
                                     {'correct_answer': 'O(1)',
                                      'difficulty': 'Easy',
                                      'explanation': 'Random access by index in a contiguous character array takes '
                                                     'O(1) time.',
                                      'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n^2)'],
                                      'question': 'What is the time complexity of accessing a character at index i in '
                                                  'a string stored as an array of bytes?'},
                                     {'correct_answer': 'A special memory region in heap storing unique string '
                                                        'literals to prevent duplicate allocations',
                                      'difficulty': 'Easy',
                                      'explanation': 'String interning stores one canonical copy of each literal in '
                                                     'the string pool.',
                                      'options': ['A special memory region in heap storing unique string literals to '
                                                  'prevent duplicate allocations',
                                                  'A database table storing passwords',
                                                  'A cache for SQL queries',
                                                  'A thread pool for string manipulation'],
                                      'question': 'What is the String Constant Pool in Java?'},
                                     {'correct_answer': 'O(N * M)',
                                      'difficulty': 'Medium',
                                      'explanation': "In the worst case (e.g. 'AAAAAB' matching 'AAA'), naive "
                                                     'comparison checks M characters per text position.',
                                      'options': ['O(N * M)', 'O(N + M)', 'O(log N)', 'O(N^2 * M)'],
                                      'question': 'What is the time complexity of naive string pattern matching for '
                                                  'text of length N and pattern of length M?'},
                                     {'correct_answer': 'O(N + M)',
                                      'difficulty': 'Medium',
                                      'explanation': 'KMP preprocesses the pattern into a Longest Prefix Suffix (LPS) '
                                                     'array, achieving linear time.',
                                      'options': ['O(N + M)', 'O(N * M)', 'O(N log M)', 'O(M^2)'],
                                      'question': 'What is the time complexity of the Knuth-Morris-Pratt (KMP) string '
                                                  'matching algorithm?'},
                                     {'correct_answer': 'Length of the longest proper prefix of pattern[0..i] that is '
                                                        'also a suffix of pattern[0..i]',
                                      'difficulty': 'Medium',
                                      'explanation': 'The LPS array allows KMP to avoid re-examining characters that '
                                                     'have already been matched.',
                                      'options': ['Length of the longest proper prefix of pattern[0..i] that is also a '
                                                  'suffix of pattern[0..i]',
                                                  'Positions of vowels in the pattern',
                                                  'ASCII values of characters',
                                                  'Hash values of words'],
                                      'question': 'What does the Longest Prefix Suffix (LPS) array store in the KMP '
                                                  'algorithm?'},
                                     {'correct_answer': 'Using rolling hash values to compare pattern and text '
                                                        'substrings in O(1) average time per shift',
                                      'difficulty': 'Medium',
                                      'explanation': 'Rabin-Karp calculates hash of sliding window in O(1), only doing '
                                                     'character checks on hash matches.',
                                      'options': ['Using rolling hash values to compare pattern and text substrings in '
                                                  'O(1) average time per shift',
                                                  'Building a binary tree of letters',
                                                  'Sorting text alphabetically before searching',
                                                  'Using recursion to invert characters'],
                                      'question': 'What is the core idea of the Rabin-Karp string search algorithm?'},
                                     {'correct_answer': 'It creates a new string object and copies all characters on '
                                                        'every iteration, leading to O(n^2) time',
                                      'difficulty': 'Medium',
                                      'explanation': "Because strings are immutable, each '+' allocates a new buffer "
                                                     'and copies accumulated characters.',
                                      'options': ['It creates a new string object and copies all characters on every '
                                                  'iteration, leading to O(n^2) time',
                                                  'It causes compiler stack overflows',
                                                  'It disables multithreading',
                                                  'It converts strings to ASCII'],
                                      'question': "Why is repeated string concatenation using the '+' operator in a "
                                                  'loop inefficient in Java/Python?'},
                                     {'correct_answer': 'ASCII characters take 1 byte (0-127); higher code points take '
                                                        '2, 3, or 4 bytes',
                                      'difficulty': 'Medium',
                                      'explanation': 'UTF-8 is backward-compatible with ASCII and uses 1 to 4 bytes '
                                                     'depending on the Unicode code point.',
                                      'options': ['ASCII characters take 1 byte (0-127); higher code points take 2, 3, '
                                                  'or 4 bytes',
                                                  'All characters take exactly 4 bytes',
                                                  'All characters take exactly 2 bytes',
                                                  'Characters are compressed with gzip'],
                                      'question': 'How does UTF-8 encoding represent variable-length characters in '
                                                  'memory?'},
                                     {'correct_answer': 'Trie (Prefix Tree)',
                                      'difficulty': 'Medium',
                                      'explanation': 'Tries share common prefixes among keys, making prefix queries '
                                                     'proportional to key length O(L).',
                                      'options': ['Trie (Prefix Tree)',
                                                  'Min-Heap',
                                                  'Singly Linked List',
                                                  'Circular Queue'],
                                      'question': 'What data structure is optimal for autocomplete search and prefix '
                                                  'dictionary lookups?'},
                                     {'correct_answer': 'O(n) time and O(1) auxiliary space (constant 26 or 256 size '
                                                        'alphabet array)',
                                      'difficulty': 'Medium',
                                      'explanation': 'A fixed-size array counting character frequencies achieves O(n) '
                                                     'linear time.',
                                      'options': ['O(n) time and O(1) auxiliary space (constant 26 or 256 size '
                                                  'alphabet array)',
                                                  'O(n^2) time',
                                                  'O(n log n) using sorting',
                                                  'O(2^n) time'],
                                      'question': 'What is the time complexity to check if two strings of length n are '
                                                  'anagrams using frequency counting?'},
                                     {'correct_answer': 'Returns the canonical instance of the string from the String '
                                                        'Constant Pool',
                                      'difficulty': 'Medium',
                                      'explanation': 'intern() searches the pool and adds or returns the cached shared '
                                                     'literal reference.',
                                      'options': ['Returns the canonical instance of the string from the String '
                                                  'Constant Pool',
                                                  'Converts string to an integer',
                                                  'Translates string into international characters',
                                                  'Deletes string from RAM'],
                                      'question': "What is the purpose of Java's String.intern() method?"},
                                     {'correct_answer': 'The minimum number of single-character edits (insertions, '
                                                        'deletions, substitutions) to transform one string into the '
                                                        'other',
                                      'difficulty': 'Medium',
                                      'explanation': 'Levenshtein distance is a standard edit-distance metric computed '
                                                     'using dynamic programming.',
                                      'options': ['The minimum number of single-character edits (insertions, '
                                                  'deletions, substitutions) to transform one string into the other',
                                                  'The length difference between the strings',
                                                  'The number of matching vowels',
                                                  'The Euclidean distance between string hash codes'],
                                      'question': 'What is the Levenshtein Distance between two strings?'},
                                     {'correct_answer': 'A directed acyclic word graph (DAWG) representing all '
                                                        'substrings of a string in O(n) states and transitions',
                                      'difficulty': 'Hard',
                                      'explanation': 'Suffix automata encode all substrings of a string in linear O(n) '
                                                     'space and time.',
                                      'options': ['A directed acyclic word graph (DAWG) representing all substrings of '
                                                  'a string in O(n) states and transitions',
                                                  'A binary tree taking O(n^2) space',
                                                  'A linked list of characters',
                                                  'A stack taking O(2^n) memory'],
                                      'question': 'What is a Suffix Automaton and what is its space complexity for a '
                                                  'string of length n?'},
                                     {'correct_answer': 'Constructing a Suffix Tree online in linear O(n) time',
                                      'difficulty': 'Hard',
                                      'explanation': "Ukkonen's algorithm builds a suffix tree character by character "
                                                     'in linear time using suffix links.',
                                      'options': ['Constructing a Suffix Tree online in linear O(n) time',
                                                  'Sorting strings alphabetically',
                                                  'Finding shortest paths in graphs',
                                                  'Compressing text with LZW'],
                                      'question': "What is Ukkonen's algorithm used for?"},
                                     {'correct_answer': 'It constructs a trie with failure transitions (suffix links), '
                                                        'matching all patterns in O(Text + Patterns + Matches)',
                                      'difficulty': 'Hard',
                                      'explanation': 'Aho-Corasick generalizes KMP to tries, finding all dictionary '
                                                     'keywords in a single pass.',
                                      'options': ['It constructs a trie with failure transitions (suffix links), '
                                                  'matching all patterns in O(Text + Patterns + Matches)',
                                                  'It hashes each pattern independently',
                                                  'It runs KMP sequentially for each pattern',
                                                  'It sorts text using quicksort'],
                                      'question': 'How does the Aho-Corasick algorithm achieve simultaneous '
                                                  'multi-pattern dictionary matching?'},
                                     {'correct_answer': 'An algorithm that computes the longest common prefix (LCP) '
                                                        'between text and every suffix of text in O(n) time',
                                      'difficulty': 'Hard',
                                      'explanation': 'The Z-algorithm produces the Z-array in linear time, useful for '
                                                     'pattern matching and period finding.',
                                      'options': ['An algorithm that computes the longest common prefix (LCP) between '
                                                  'text and every suffix of text in O(n) time',
                                                  'A tool for compressing data with zip',
                                                  'A sorting algorithm for unicode strings',
                                                  'A machine learning algorithm for text classification'],
                                      'question': 'What is the Z-algorithm in string processing?'},
                                     {'correct_answer': 'Finding the longest palindromic substring in linear O(n) time',
                                      'difficulty': 'Hard',
                                      'explanation': "Manacher's algorithm eliminates duplicate work around "
                                                     'palindromic symmetry to find longest palindrome in O(n).',
                                      'options': ['Finding the longest palindromic substring in linear O(n) time',
                                                  'Finding all anagrams in O(n log n)',
                                                  'Counting vowels in O(1)',
                                                  'Compressing palindromes'],
                                      'question': "What is Manacher's algorithm used for?"},
                                     {'correct_answer': 'It permutes characters into runs of similar characters using '
                                                        'cyclic shifts, making text highly compressible and indexable',
                                      'difficulty': 'Hard',
                                      'explanation': 'BWT groups identical characters together without losing '
                                                     'information, enabling FM-index searches.',
                                      'options': ['It permutes characters into runs of similar characters using cyclic '
                                                  'shifts, making text highly compressible and indexable',
                                                  'It encrypts strings using RSA',
                                                  'It converts text to binary integers',
                                                  'It removes whitespace from documents'],
                                      'question': 'What is the Burrows-Wheeler Transform (BWT) and why is it essential '
                                                  'for text compression (bzip2) and bioinformatics?'},
                                     {'correct_answer': 'A data structure combining BWT and suffix arrays that allows '
                                                        'exact pattern searching in sub-linear time within compressed '
                                                        'memory',
                                      'difficulty': 'Hard',
                                      'explanation': 'FM-index enables fast genomic sequence alignment directly on '
                                                     'compressed text representations.',
                                      'options': ['A data structure combining BWT and suffix arrays that allows exact '
                                                  'pattern searching in sub-linear time within compressed memory',
                                                  'An audio processing index for frequency modulation',
                                                  'A hash table of all words on disk',
                                                  'A binary search tree of tokens'],
                                      'question': 'What is the FM-Index (Full-text index in Minute space)?'},
                                     {'correct_answer': 'A binary tree of short string fragments that enables '
                                                        'efficient insertion, deletion, and concatenation in O(log n) '
                                                        'time',
                                      'difficulty': 'Hard',
                                      'explanation': 'Ropes avoid reallocating and copying large contiguous arrays '
                                                     'when editing massive documents.',
                                      'options': ['A binary tree of short string fragments that enables efficient '
                                                  'insertion, deletion, and concatenation in O(log n) time',
                                                  'A long contiguous char array',
                                                  'A linked list of characters taking O(n) time',
                                                  'A circular buffer in kernel memory'],
                                      'question': 'What is a Rope data structure and why is it preferred over flat '
                                                  'strings in text editors?'},
                                     {'correct_answer': 'By scanning patterns from right to left and skipping text '
                                                        'characters using the bad-character and good-suffix heuristics',
                                      'difficulty': 'Hard',
                                      'explanation': 'In the best case, Boyer-Moore skips up to M characters per step, '
                                                     'achieving O(N / M) lookup speed.',
                                      'options': ['By scanning patterns from right to left and skipping text '
                                                  'characters using the bad-character and good-suffix heuristics',
                                                  'By guessing random indices',
                                                  'By pre-sorting all text letters',
                                                  'By using binary search on text'],
                                      'question': 'How does the Boyer-Moore string search algorithm achieve sub-linear '
                                                  'performance in best-case scenarios?'},
                                     {'correct_answer': 'Strings store a byte[] instead of char[] with a coder flag '
                                                        '(LATIN1 = 1 byte/char, UTF16 = 2 bytes/char)',
                                      'difficulty': 'Hard',
                                      'explanation': 'Compact Strings halves the heap footprint of strings containing '
                                                     'only 1-byte ISO-8859-1 characters.',
                                      'options': ['Strings store a byte[] instead of char[] with a coder flag (LATIN1 '
                                                  '= 1 byte/char, UTF16 = 2 bytes/char)',
                                                  'Strings compress with snappy',
                                                  'Strings discard punctuation',
                                                  'Strings store pointers to external dictionary'],
                                      'question': 'In Java 9+, how does Compact Strings optimize memory footprint for '
                                                  'Latin-1 characters?'}]}

