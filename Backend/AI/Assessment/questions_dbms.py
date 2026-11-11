"""Database Systems Question Bank - 10 Topics, 30 Questions Each (10 Easy, 10 Medium, 10 Hard)"""

dbms_questions = {'Aggregate Functions and GROUP BY': [{'correct_answer': 'To group rows sharing identical values in specified columns '
                                                         'into summary rows',
                                       'difficulty': 'Easy',
                                       'explanation': 'GROUP BY collapses rows with identical keys into aggregate '
                                                      'groups.',
                                       'options': ['To group rows sharing identical values in specified columns into '
                                                   'summary rows',
                                                   'To sort rows in alphabetical order',
                                                   'To filter single rows before aggregation',
                                                   'To create a new database table'],
                                       'question': 'What is the primary role of the GROUP BY clause in SQL?'},
                                      {'correct_answer': 'COUNT()',
                                       'difficulty': 'Easy',
                                       'explanation': 'COUNT() tallies the total count of matching rows or non-null '
                                                      'values.',
                                       'options': ['COUNT()', 'SUM()', 'TOTAL()', 'ROWS()'],
                                       'question': 'Which aggregate function returns the total number of rows matching '
                                                   'a condition?'},
                                      {'correct_answer': 'SUM()',
                                       'difficulty': 'Easy',
                                       'explanation': 'SUM() returns the mathematical sum of values in a numerical '
                                                      'column.',
                                       'options': ['SUM()', 'TOTAL()', 'ADD()', 'COUNT()'],
                                       'question': 'Which aggregate function calculates the total sum of numerical '
                                                   'values in a column?'},
                                      {'correct_answer': 'AVG()',
                                       'difficulty': 'Easy',
                                       'explanation': 'AVG() computes the average of non-null numerical values.',
                                       'options': ['AVG()', 'MEAN()', 'MEDIAN()', 'SUM()'],
                                       'question': 'Which aggregate function calculates the arithmetic mean of a '
                                                   'numerical column?'},
                                      {'correct_answer': 'MIN() and MAX()',
                                       'difficulty': 'Easy',
                                       'explanation': 'MIN() returns the smallest value and MAX() returns the largest '
                                                      'value.',
                                       'options': ['MIN() and MAX()',
                                                   'LEAST() and GREATEST()',
                                                   'FIRST() and LAST()',
                                                   'LOW() and HIGH()'],
                                       'question': 'Which aggregate functions find the lowest and highest values in a '
                                                   'column?'},
                                      {'correct_answer': 'WHERE filters individual rows before grouping; HAVING '
                                                         'filters aggregated groups after GROUP BY',
                                       'difficulty': 'Easy',
                                       'explanation': 'HAVING applies conditions to aggregated summary values computed '
                                                      'by GROUP BY.',
                                       'options': ['WHERE filters individual rows before grouping; HAVING filters '
                                                   'aggregated groups after GROUP BY',
                                                   'WHERE works on strings; HAVING works on numbers',
                                                   'WHERE is optional; HAVING is mandatory',
                                                   'They are identical synonyms'],
                                       'question': 'What is the critical difference between the WHERE clause and the '
                                                   'HAVING clause in SQL?'},
                                      {'correct_answer': 'No, aggregate functions cannot appear in a WHERE clause (use '
                                                         'HAVING instead)',
                                       'difficulty': 'Easy',
                                       'explanation': 'WHERE executes before aggregation occurs, so aggregate '
                                                      'functions are invalid in WHERE.',
                                       'options': ['No, aggregate functions cannot appear in a WHERE clause (use '
                                                   'HAVING instead)',
                                                   'Yes, anytime in standard SQL',
                                                   'Only if there is no GROUP BY clause',
                                                   'Only in MySQL'],
                                       'question': "Can the WHERE clause contain an aggregate function (e.g. 'WHERE "
                                                   "SUM(salary) > 50000')?"},
                                      {'correct_answer': 'COUNT(*) counts all rows including NULLs; COUNT(col) counts '
                                                         'only non-NULL values in that column',
                                       'difficulty': 'Easy',
                                       'explanation': 'COUNT(*) counts matching tuples regardless of column '
                                                      'nullability.',
                                       'options': ['COUNT(*) counts all rows including NULLs; COUNT(col) counts only '
                                                   'non-NULL values in that column',
                                                   'COUNT(*) only counts numbers',
                                                   'COUNT(col) is always faster',
                                                   'COUNT(*) ignores primary keys'],
                                       'question': 'What does COUNT(*) count compared to COUNT(column_name)?'},
                                      {'correct_answer': 'NULL values are ignored (skipped) during calculation',
                                       'difficulty': 'Easy',
                                       'explanation': 'Standard SQL aggregate functions eliminate NULLs prior to '
                                                      'computing the result.',
                                       'options': ['NULL values are ignored (skipped) during calculation',
                                                   'NULL causes the entire aggregate result to become NULL',
                                                   'NULL is converted to 0',
                                                   'An error is raised'],
                                       'question': 'What happens to NULL values when calculating SUM(), AVG(), MIN(), '
                                                   'or MAX()?'},
                                      {'correct_answer': 'NULL',
                                       'difficulty': 'Easy',
                                       'explanation': 'If no non-null rows exist to aggregate, SUM() and AVG() return '
                                                      'NULL.',
                                       'options': ['NULL', '0', 'An exception is thrown', 'Empty string'],
                                       'question': 'What is the result of applying SUM() or AVG() on a column where '
                                                   'ALL values are NULL?'},
                                      {'correct_answer': 'Only columns specified in the GROUP BY clause or columns '
                                                         'wrapped in aggregate functions',
                                       'difficulty': 'Medium',
                                       'explanation': 'Including unaggregated, non-grouped columns creates '
                                                      'non-deterministic results forbidden by SQL standards.',
                                       'options': ['Only columns specified in the GROUP BY clause or columns wrapped '
                                                   'in aggregate functions',
                                                   'Any column from the queried table',
                                                   'Only primary key columns',
                                                   'Only numerical columns'],
                                       'question': 'In standard SQL, which columns can be included in the SELECT list '
                                                   'when using a GROUP BY clause?'},
                                      {'correct_answer': 'The count of unique, non-null values in the specified column',
                                       'difficulty': 'Medium',
                                       'explanation': 'DISTINCT inside COUNT eliminates duplicate values before '
                                                      'tallying the count.',
                                       'options': ['The count of unique, non-null values in the specified column',
                                                   'The total count of all duplicate values',
                                                   'The distinct primary keys',
                                                   'The number of distinct tables'],
                                       'question': 'What does COUNT(DISTINCT column_name) compute?'},
                                      {'correct_answer': 'Generates hierarchical subtotal rows and a grand total row '
                                                         'across the specified grouping columns',
                                       'difficulty': 'Medium',
                                       'explanation': 'ROLLUP creates progressive hierarchical subtotals from right to '
                                                      'left, plus a grand total.',
                                       'options': ['Generates hierarchical subtotal rows and a grand total row across '
                                                   'the specified grouping columns',
                                                   'Rolls back uncommitted transactions',
                                                   'Sorts groups in reverse order',
                                                   'Converts columns into rows'],
                                       'question': 'What does the GROUP BY ROLLUP extension do in SQL?'},
                                      {'correct_answer': 'Generates subtotal aggregations for all possible '
                                                         'cross-combinations of the specified grouping columns '
                                                         '(multidimensional analysis)',
                                       'difficulty': 'Medium',
                                       'explanation': 'CUBE produces 2^N grouping sets containing every combination of '
                                                      'dimension subtotals.',
                                       'options': ['Generates subtotal aggregations for all possible '
                                                   'cross-combinations of the specified grouping columns '
                                                   '(multidimensional analysis)',
                                                   'Calculates the cube of numerical values',
                                                   'Creates a 3D visualization table',
                                                   'Compresses data into cubes'],
                                       'question': 'What does the GROUP BY CUBE extension do in SQL?'},
                                      {'correct_answer': 'A clause that allows selectively specifying multiple '
                                                         'distinct grouping criteria in a single query pass',
                                       'difficulty': 'Medium',
                                       'explanation': 'GROUPING SETS computes specified aggregations in one query '
                                                      'without multiple UNION ALLs.',
                                       'options': ['A clause that allows selectively specifying multiple distinct '
                                                   'grouping criteria in a single query pass',
                                                   'A set of user accounts',
                                                   'A cluster of database servers',
                                                   'A group of primary keys'],
                                       'question': 'What are GROUPING SETS in SQL?'},
                                      {'correct_answer': '1 if the column is currently aggregated (NULL due to '
                                                         'subtotal row), or 0 if it represents normal row data',
                                       'difficulty': 'Medium',
                                       'explanation': 'GROUPING() distinguishes real NULL values from generated '
                                                      'subtotal placeholder NULLs.',
                                       'options': ['1 if the column is currently aggregated (NULL due to subtotal '
                                                   'row), or 0 if it represents normal row data',
                                                   'The row index',
                                                   'The group count',
                                                   'The number of groups'],
                                       'question': 'What does the GROUPING() scalar function return when used with '
                                                   'ROLLUP or CUBE?'},
                                      {'correct_answer': 'Aggregate functions collapse multiple rows into a single '
                                                         'summary row; Window functions retain individual row '
                                                         'identities while computing aggregates',
                                       'difficulty': 'Medium',
                                       'explanation': 'Window functions evaluate across a partition of rows without '
                                                      'collapsing the result set.',
                                       'options': ['Aggregate functions collapse multiple rows into a single summary '
                                                   'row; Window functions retain individual row identities while '
                                                   'computing aggregates',
                                                   'Window functions only work in Microsoft Windows',
                                                   'Aggregate functions run after ORDER BY',
                                                   'Window functions cannot calculate sums'],
                                       'question': 'What is the difference between an Aggregate Function and a Window '
                                                   'Function (OVER clause)?'},
                                      {'correct_answer': 'Divides query rows into groups to which the window function '
                                                         'is independently applied',
                                       'difficulty': 'Medium',
                                       'explanation': 'PARTITION BY scopes window calculations (like running totals) '
                                                      'per group.',
                                       'options': ['Divides query rows into groups to which the window function is '
                                                   'independently applied',
                                                   'Splits the table on physical hard drives',
                                                   'Creates separate database schemas',
                                                   'Filters rows like WHERE'],
                                       'question': 'What does the PARTITION BY clause do inside a window function?'},
                                      {'correct_answer': 'A unique sequential integer starting from 1 to each row '
                                                         'within its partition',
                                       'difficulty': 'Medium',
                                       'explanation': 'ROW_NUMBER() assigns deterministic sequential ranks regardless '
                                                      'of duplicate values.',
                                       'options': ['A unique sequential integer starting from 1 to each row within its '
                                                   'partition',
                                                   'The physical disk block number',
                                                   "The row's primary key",
                                                   'The number of duplicate rows'],
                                       'question': 'What does the ROW_NUMBER() window function assign?'},
                                      {'correct_answer': 'RANK() skips rank numbers after ties (e.g. 1, 2, 2, 4); '
                                                         'DENSE_RANK() leaves no gaps (e.g. 1, 2, 2, 3)',
                                       'difficulty': 'Medium',
                                       'explanation': 'DENSE_RANK() avoids rank number gaps when handling tied scores.',
                                       'options': ['RANK() skips rank numbers after ties (e.g. 1, 2, 2, 4); '
                                                   'DENSE_RANK() leaves no gaps (e.g. 1, 2, 2, 3)',
                                                   'RANK() is random; DENSE_RANK() is sorted',
                                                   'DENSE_RANK() only works with integers',
                                                   'They are identical functions'],
                                       'question': 'What is the difference between RANK() and DENSE_RANK() window '
                                                   'functions?'},
                                      {'correct_answer': 'Hash Aggregate (building in-memory hash table of group keys) '
                                                         'and Stream/Sort Aggregate (sorting by group keys first)',
                                       'difficulty': 'Hard',
                                       'explanation': 'Hash aggregation is used when groups fit in memory; sort '
                                                      'aggregation leverages pre-sorted data or disk spill.',
                                       'options': ['Hash Aggregate (building in-memory hash table of group keys) and '
                                                   'Stream/Sort Aggregate (sorting by group keys first)',
                                                   'B-Tree scan and Linear probing',
                                                   'Nested loop and Merge join',
                                                   'Quick scan and Radial aggregate'],
                                       'question': 'What are the two primary execution strategies used by SQL query '
                                                   'engines to execute GROUP BY queries?'},
                                      {'correct_answer': 'The query engine partitions keys into hybrid hash buckets on '
                                                         'disk (temp files), degrading query throughput',
                                       'difficulty': 'Hard',
                                       'explanation': 'Hash aggregate spill incurs heavy disk I/O as bucket partitions '
                                                      'are written to and read from temporary storage.',
                                       'options': ['The query engine partitions keys into hybrid hash buckets on disk '
                                                   '(temp files), degrading query throughput',
                                                   'The query is terminated with an out of memory error',
                                                   'The table data is corrupted',
                                                   'The engine skips un-grouped rows'],
                                       'question': 'What happens when an in-memory Hash Aggregate spills to disk '
                                                   '(work_mem exhaustion in PostgreSQL)?'},
                                      {'correct_answer': 'RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW',
                                       'difficulty': 'Hard',
                                       'explanation': 'Omitting frame specification defaults to cumulative aggregation '
                                                      'up to the current row.',
                                       'options': ['RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW',
                                                   'ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING',
                                                   'ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING',
                                                   'RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING'],
                                       'question': 'What is the default window frame specification when ORDER BY is '
                                                   'present in an OVER() clause in standard SQL?'},
                                      {'correct_answer': 'ROWS uses physical row offsets (fast index navigation); '
                                                         'RANGE evaluates peer value comparisons, requiring sorting '
                                                         'and buffering',
                                       'difficulty': 'Hard',
                                       'explanation': 'ROWS avoids value comparison overhead by counting physical '
                                                      'tuples directly.',
                                       'options': ['ROWS uses physical row offsets (fast index navigation); RANGE '
                                                   'evaluates peer value comparisons, requiring sorting and buffering',
                                                   'RANGE is always faster than ROWS',
                                                   'ROWS can only be used with COUNT',
                                                   'There is no performance difference'],
                                       'question': "What is the performance difference between 'ROWS BETWEEN' and "
                                                   "'RANGE BETWEEN' in SQL window frames?"},
                                      {'correct_answer': 'Accessing attribute values from subsequent (LEAD) or '
                                                         'preceding (LAG) rows relative to the current row without '
                                                         'self-joins',
                                       'difficulty': 'Hard',
                                       'explanation': 'LEAD/LAG enable calculating period-over-period differences '
                                                      'without costly self-joins.',
                                       'options': ['Accessing attribute values from subsequent (LEAD) or preceding '
                                                   '(LAG) rows relative to the current row without self-joins',
                                                   'Finding lead times in manufacturing',
                                                   'Delaying query execution by milliseconds',
                                                   'Measuring network latency'],
                                       'question': 'What is the purpose of LEAD() and LAG() analytic window '
                                                   'functions?'},
                                      {'correct_answer': 'Estimating approximate cardinality (COUNT DISTINCT) of '
                                                         'billions of items in O(1) space with a small standard error '
                                                         '(~1%)',
                                       'difficulty': 'Hard',
                                       'explanation': 'HyperLogLog calculates distinct counts across massive '
                                                      'distributed streams using negligible memory.',
                                       'options': ['Estimating approximate cardinality (COUNT DISTINCT) of billions of '
                                                   'items in O(1) space with a small standard error (~1%)',
                                                   'Calculating exact average values',
                                                   'Compressing database logs',
                                                   'Generating cryptographic tokens'],
                                       'question': 'What is the HyperLogLog algorithm used for in distributed database '
                                                   'analytics (e.g. BigQuery, Redis, Presto)?'},
                                      {'correct_answer': 'It reads only the first entry of each distinct group from '
                                                         'the B-Tree index, skipping intermediate duplicate index leaf '
                                                         'pages',
                                       'difficulty': 'Hard',
                                       'explanation': 'Skip scans hop directly from one distinct key boundary to the '
                                                      'next in the B-Tree, achieving sub-linear time.',
                                       'options': ['It reads only the first entry of each distinct group from the '
                                                   'B-Tree index, skipping intermediate duplicate index leaf pages',
                                                   'It scans the entire table sequentially',
                                                   'It deletes duplicate index entries',
                                                   'It caches values in memory'],
                                       'question': "How does a Loose Index Scan (Index Skip Scan) optimize 'SELECT "
                                                   "DISTINCT col FROM table' in MySQL/PostgreSQL?"},
                                      {'correct_answer': 'Aggregates only rows satisfying the filter condition without '
                                                         "collapsing the main query's WHERE clause",
                                       'difficulty': 'Hard',
                                       'explanation': 'Aggregate FILTER clauses clean up complex conditional '
                                                      'aggregations without cumbersome CASE WHEN statements.',
                                       'options': ['Aggregates only rows satisfying the filter condition without '
                                                   "collapsing the main query's WHERE clause",
                                                   'Filters the entire query output',
                                                   'Creates an index on the column',
                                                   'Deletes non-matching rows'],
                                       'question': 'What is a FILTER (WHERE condition) clause attached to an aggregate '
                                                   'function in SQL:2003 (e.g., COUNT(*) FILTER (WHERE '
                                                   "status='active'))?"},
                                      {'correct_answer': 'Maintaining running sum and count by subtracting the leaving '
                                                         'row and adding the entering row instead of re-summing the '
                                                         'window',
                                       'difficulty': 'Hard',
                                       'explanation': 'Segmented sliding aggregation maintains running accumulators, '
                                                      'avoiding O(W) re-evaluation per row.',
                                       'options': ['Maintaining running sum and count by subtracting the leaving row '
                                                   'and adding the entering row instead of re-summing the window',
                                                   'Storing all previous windows in temporary tables',
                                                   'Recalculating sum from start of partition every time',
                                                   'Running window functions on GPU threads'],
                                       'question': 'What is the Sliding Window Frame problem with large moving '
                                                   'averages, and how do optimizing engines maintain O(1) per-row '
                                                   'cost?'},
                                      {'correct_answer': 'It divides rows into n roughly equal buckets, assigning one '
                                                         'extra row to the lowest-numbered buckets first',
                                       'difficulty': 'Hard',
                                       'explanation': 'NTILE distributes uneven row remainders starting with bucket 1 '
                                                      'through bucket remainder.',
                                       'options': ['It divides rows into n roughly equal buckets, assigning one extra '
                                                   'row to the lowest-numbered buckets first',
                                                   'It drops remainder rows',
                                                   'It puts all remainder rows in the last bucket',
                                                   'It throws an ArithmeticException'],
                                       'question': 'What is the NTILE(n) window function and how does it distribute '
                                                   'remainder rows when the partition size is not divisible by n?'}],
 'Basic SQL Queries': [{'correct_answer': 'Structured Query Language',
                        'difficulty': 'Easy',
                        'explanation': 'SQL is the standard declarative language for interacting with relational '
                                       'database management systems.',
                        'options': ['Structured Query Language',
                                    'Simple Question Language',
                                    'Sequential Query Logic',
                                    'Standard Quotation Library'],
                        'question': 'What does SQL stand for?'},
                       {'correct_answer': 'SELECT',
                        'difficulty': 'Easy',
                        'explanation': 'The SELECT statement queries the database and returns a matching tabular '
                                       'result set.',
                        'options': ['SELECT', 'GET', 'FETCH', 'EXTRACT'],
                        'question': 'Which SQL statement is used to retrieve data from a database?'},
                       {'correct_answer': 'WHERE',
                        'difficulty': 'Easy',
                        'explanation': 'The WHERE clause restricts rows returned to those satisfying the specified '
                                       'filter criteria.',
                        'options': ['WHERE', 'ORDER BY', 'GROUP BY', 'HAVING'],
                        'question': 'Which clause in a SELECT statement is used to filter rows based on specific '
                                    'conditions?'},
                       {'correct_answer': 'INSERT INTO',
                        'difficulty': 'Easy',
                        'explanation': 'INSERT INTO creates new data records in a specified table.',
                        'options': ['INSERT INTO', 'ADD ROW', 'NEW RECORD', 'CREATE ROW'],
                        'question': 'Which SQL statement is used to insert a new row of data into a table?'},
                       {'correct_answer': 'UPDATE',
                        'difficulty': 'Easy',
                        'explanation': 'UPDATE alters existing attribute values in one or more records.',
                        'options': ['UPDATE', 'MODIFY', 'ALTER', 'CHANGE'],
                        'question': 'Which SQL statement is used to modify existing records in a table?'},
                       {'correct_answer': 'DELETE FROM',
                        'difficulty': 'Easy',
                        'explanation': 'DELETE FROM removes specified rows that match the WHERE clause.',
                        'options': ['DELETE FROM', 'REMOVE', 'DROP RECORD', 'UNLINK'],
                        'question': 'Which SQL statement is used to remove records from a table?'},
                       {'correct_answer': 'ALL rows in the table will be updated or deleted',
                        'difficulty': 'Easy',
                        'explanation': 'Without a WHERE clause, DML statements apply unconditionally across every row '
                                       'in the table.',
                        'options': ['ALL rows in the table will be updated or deleted',
                                    'The query will fail with a SyntaxError',
                                    'Only the first row will be affected',
                                    'A warning is logged but no rows are touched'],
                        'question': 'What happens if you execute an UPDATE or DELETE statement without a WHERE '
                                    'clause?'},
                       {'correct_answer': 'DISTINCT',
                        'difficulty': 'Easy',
                        'explanation': 'SELECT DISTINCT filters out duplicate tuple rows from the returned result set.',
                        'options': ['DISTINCT', 'UNIQUE', 'DIFFERENT', 'FILTER'],
                        'question': 'Which keyword is used in a SELECT statement to eliminate duplicate rows from the '
                                    'result set?'},
                       {'correct_answer': 'ORDER BY',
                        'difficulty': 'Easy',
                        'explanation': 'ORDER BY sorts the returned output rows based on specified columns.',
                        'options': ['ORDER BY', 'SORT BY', 'ALIGN', 'GROUP BY'],
                        'question': 'Which clause is used to sort the result set in ascending or descending order?'},
                       {'correct_answer': 'ASC (Ascending)',
                        'difficulty': 'Easy',
                        'explanation': 'If omitted, ORDER BY defaults to ascending order (ASC).',
                        'options': ['ASC (Ascending)', 'DESC (Descending)', 'Random', 'Creation order'],
                        'question': 'What is the default sorting direction of the ORDER BY clause?'},
                       {'correct_answer': 'LIKE',
                        'difficulty': 'Medium',
                        'explanation': 'The LIKE operator evaluates wildcard pattern matching in string attributes.',
                        'options': ['LIKE', 'MATCH', 'CONTAINS', 'SIMILAR'],
                        'question': 'Which operator is used in a WHERE clause to search for a specified pattern in a '
                                    'column?'},
                       {'correct_answer': "'%' represents zero or more characters; '_' represents exactly one single "
                                          'character',
                        'difficulty': 'Medium',
                        'explanation': '% and _ are the standard SQL pattern matching wildcards.',
                        'options': ["'%' represents zero or more characters; '_' represents exactly one single "
                                    'character',
                                    "'%' is single character; '_' is multiple",
                                    "'%' matches numbers; '_' matches letters",
                                    "'%' is escape character"],
                        'question': "What do the '%' and '_' wildcards represent in SQL LIKE expressions?"},
                       {'correct_answer': 'IN',
                        'difficulty': 'Medium',
                        'explanation': 'The IN operator checks if an operand matches any member of a specified literal '
                                       'set or subquery.',
                        'options': ['IN', 'BETWEEN', 'EXISTS', 'ANY'],
                        'question': 'Which operator tests whether a value matches any value within a comma-separated '
                                    'list?'},
                       {'correct_answer': 'IS NULL (or IS NOT NULL)',
                        'difficulty': 'Medium',
                        'explanation': 'Because NULL represents unknown state, standard equality (=) fails; IS NULL is '
                                       'required.',
                        'options': ['IS NULL (or IS NOT NULL)', '= NULL', '== NULL', 'EQUALS NULL'],
                        'question': 'How do you test for missing or NULL values in a SQL WHERE clause?'},
                       {'correct_answer': 'DELETE is DML (logs row-by-row, fires triggers, can be filtered); TRUNCATE '
                                          'is DDL (deallocates pages, faster, no WHERE clause)',
                        'difficulty': 'Medium',
                        'explanation': 'TRUNCATE quickly empties a table by deallocating data pages with minimal '
                                       'logging.',
                        'options': ['DELETE is DML (logs row-by-row, fires triggers, can be filtered); TRUNCATE is DDL '
                                    '(deallocates pages, faster, no WHERE clause)',
                                    'DELETE removes the table schema; TRUNCATE removes data',
                                    'TRUNCATE can be rolled back always; DELETE cannot',
                                    'They are identical in performance'],
                        'question': 'What is the difference between DELETE and TRUNCATE in SQL?'},
                       {'correct_answer': 'DROP deletes table data AND table schema definition; TRUNCATE deletes data '
                                          'but preserves table structure',
                        'difficulty': 'Medium',
                        'explanation': 'DROP TABLE destroys the table definition entirely from the database catalog.',
                        'options': ['DROP deletes table data AND table schema definition; TRUNCATE deletes data but '
                                    'preserves table structure',
                                    'DROP only works on views',
                                    'TRUNCATE deletes the database entirely',
                                    'DROP is faster than TRUNCATE'],
                        'question': 'What is the difference between DROP TABLE and TRUNCATE TABLE?'},
                       {'correct_answer': 'LIMIT',
                        'difficulty': 'Medium',
                        'explanation': 'LIMIT (or FETCH FIRST n ROWS ONLY in standard SQL) caps the output row count.',
                        'options': ['LIMIT', 'TOP', 'RESTRICT', 'MAXROWS'],
                        'question': 'Which clause in SQL limits the number of rows returned in the result set '
                                    '(PostgreSQL / MySQL)?'},
                       {'correct_answer': 'It skips the specified number of rows before beginning to return rows from '
                                          'the query',
                        'difficulty': 'Medium',
                        'explanation': 'LIMIT y OFFSET x skips x rows and returns the subsequent y rows.',
                        'options': ['It skips the specified number of rows before beginning to return rows from the '
                                    'query',
                                    'It sorts rows backwards',
                                    'It sets database time zones',
                                    'It filters null values'],
                        'question': 'How does the OFFSET clause work in SQL pagination queries?'},
                       {'correct_answer': 'col >= 10 AND col <= 20 (inclusive of both endpoints 10 and 20)',
                        'difficulty': 'Medium',
                        'explanation': 'BETWEEN in standard SQL is inclusive of boundary limits.',
                        'options': ['col >= 10 AND col <= 20 (inclusive of both endpoints 10 and 20)',
                                    'col > 10 AND col < 20 (exclusive)',
                                    'col = 10 OR col = 20',
                                    'col in (10, 20)'],
                        'question': "What does the SQL expression 'col BETWEEN 10 AND 20' evaluate to?"},
                       {'correct_answer': 'DDL defines structure (CREATE, ALTER); DML manipulates data (INSERT, '
                                          'UPDATE); DCL manages permissions (GRANT, REVOKE)',
                        'difficulty': 'Medium',
                        'explanation': 'SQL commands are partitioned into Data Definition, Data Manipulation, and Data '
                                       'Control languages.',
                        'options': ['DDL defines structure (CREATE, ALTER); DML manipulates data (INSERT, UPDATE); DCL '
                                    'manages permissions (GRANT, REVOKE)',
                                    'DDL is for joins; DML is for indexes; DCL is for triggers',
                                    'They are different SQL dialects',
                                    'DDL runs on client; DML runs on server'],
                        'question': 'What is the difference between DDL, DML, and DCL in SQL?'},
                       {'correct_answer': 'Attackers inject malicious SQL into input strings; prepared statements '
                                          'separate query structure from parameters, preventing execution of injected '
                                          'code',
                        'difficulty': 'Hard',
                        'explanation': 'Parameterized queries treat input strictly as data literals rather than '
                                       'executable commands.',
                        'options': ['Attackers inject malicious SQL into input strings; prepared statements separate '
                                    'query structure from parameters, preventing execution of injected code',
                                    'Attackers inject viruses into RAM; solved by antivirus',
                                    'A technique to optimize slow queries',
                                    'A database backup format'],
                        'question': 'What is SQL Injection and how do Prepared Statements (Parameterized Queries) '
                                    'prevent it?'},
                       {'correct_answer': 'FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> '
                                          'LIMIT',
                        'difficulty': 'Hard',
                        'explanation': 'Understanding query execution phases explains why aliases created in SELECT '
                                       'cannot be used in WHERE.',
                        'options': ['FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT',
                                    'SELECT -> FROM -> WHERE -> ORDER BY',
                                    'WHERE -> FROM -> SELECT -> GROUP BY',
                                    'ORDER BY -> SELECT -> FROM -> WHERE'],
                        'question': 'What is the operational execution order of clauses in a SQL SELECT query?'},
                       {'correct_answer': "Because NULL represents UNKNOWN; comparing anything with NULL using '=' "
                                          'yields UNKNOWN (falsy in WHERE)',
                        'difficulty': 'Hard',
                        'explanation': 'In 3-valued logic, UNKNOWN conditions are rejected by WHERE filters.',
                        'options': ["Because NULL represents UNKNOWN; comparing anything with NULL using '=' yields "
                                    'UNKNOWN (falsy in WHERE)',
                                    'Because NULL is converted to empty string',
                                    "Because database drivers reject '='",
                                    'Because NULL is equal to zero'],
                        'question': "Why does 'WHERE column = NULL' always return zero rows in SQL?"},
                       {'correct_answer': 'The database engine must read and discard 1,000,000 rows before returning '
                                          'the 10 target rows',
                        'difficulty': 'Hard',
                        'explanation': 'High offsets force full index or table scans over all discarded records.',
                        'options': ['The database engine must read and discard 1,000,000 rows before returning the 10 '
                                    'target rows',
                                    'The query runs out of disk space',
                                    'The OFFSET keyword disables all indexes permanently',
                                    'The database crashes with out of memory'],
                        'question': "How does pagination using 'LIMIT 10 OFFSET 1000000' cause performance degradation "
                                    '(deep pagination problem)?'},
                       {'correct_answer': "By filtering with 'WHERE id > last_seen_id ORDER BY id LIMIT 10' using "
                                          'index seek rather than scanning offset rows',
                        'difficulty': 'Hard',
                        'explanation': 'Keyset pagination leverages B-Tree indexes to seek directly to the next page '
                                       'in O(log n) time.',
                        'options': ["By filtering with 'WHERE id > last_seen_id ORDER BY id LIMIT 10' using index seek "
                                    'rather than scanning offset rows',
                                    'By caching all rows in RAM',
                                    'By deleting previous rows',
                                    'By using multiple threads for OFFSET'],
                        'question': 'How does Keyset Pagination (Seek Method) resolve the deep pagination bottleneck?'},
                       {'correct_answer': 'UNION removes duplicate rows between result sets (requires '
                                          'sorting/hashing); UNION ALL retains duplicates and executes faster',
                        'difficulty': 'Hard',
                        'explanation': 'UNION ALL skips expensive duplicate elimination passes, providing superior '
                                       'performance.',
                        'options': ['UNION removes duplicate rows between result sets (requires sorting/hashing); '
                                    'UNION ALL retains duplicates and executes faster',
                                    'UNION combines columns; UNION ALL combines rows',
                                    'UNION is DDL; UNION ALL is DML',
                                    'They are identical in speed and behavior'],
                        'question': 'What is the difference between UNION and UNION ALL?'},
                       {'correct_answer': 'Provides conditional branching logic (if-then-else) inside SELECT, UPDATE, '
                                          'or ORDER BY statements',
                        'difficulty': 'Hard',
                        'explanation': 'CASE WHEN evaluates expressions conditionally within declarative SQL queries.',
                        'options': ['Provides conditional branching logic (if-then-else) inside SELECT, UPDATE, or '
                                    'ORDER BY statements',
                                    'Declares local variables in stored procedures',
                                    'Creates test cases in databases',
                                    'Changes text to uppercase'],
                        'question': 'What is the purpose of the CASE WHEN statement in SQL?'},
                       {'correct_answer': 'Returns specified columns of the affected rows directly from the mutation '
                                          'without requiring a second SELECT query',
                        'difficulty': 'Hard',
                        'explanation': 'RETURNING enables retrieving generated keys or mutated state atomically in a '
                                       'single network round-trip.',
                        'options': ['Returns specified columns of the affected rows directly from the mutation without '
                                    'requiring a second SELECT query',
                                    'Rolls back changes automatically',
                                    'Returns execution time metrics',
                                    'Redirects query output to an email'],
                        'question': "In PostgreSQL, what is the 'RETURNING' clause in INSERT/UPDATE/DELETE "
                                    'statements?'},
                       {'correct_answer': 'Collation defines rules for character encoding, case sensitivity (CI vs '
                                          'CS), and linguistic sorting order (accent sensitivity)',
                        'difficulty': 'Hard',
                        'explanation': "Collation governs whether 'a' == 'A' and how diacritics and cultural alphabets "
                                       'are ordered.',
                        'options': ['Collation defines rules for character encoding, case sensitivity (CI vs CS), and '
                                    'linguistic sorting order (accent sensitivity)',
                                    'A method of compressing string tables',
                                    'A backup mechanism across servers',
                                    'A security encryption standard'],
                        'question': 'What is collation in SQL databases and how does it affect string comparisons and '
                                    'sorting?'},
                       {'correct_answer': 'Atomically inserts a new row or updates existing row if a unique constraint '
                                          'or primary key collision occurs',
                        'difficulty': 'Hard',
                        'explanation': 'UPSERT eliminates race conditions between separate SELECT and INSERT/UPDATE '
                                       'checks.',
                        'options': ['Atomically inserts a new row or updates existing row if a unique constraint or '
                                    'primary key collision occurs',
                                    'An update that runs on Sundays',
                                    'A query that rolls back changes',
                                    'A query that updates server settings'],
                        'question': 'What is an UPSERT operation in SQL (e.g. INSERT ... ON CONFLICT DO UPDATE / ON '
                                    'DUPLICATE KEY UPDATE)?'}],
 'Concurrency Control and Locking': [{'correct_answer': 'The mechanism that coordinates simultaneous execution of '
                                                        'transactions while preserving ACID properties and data '
                                                        'consistency',
                                      'difficulty': 'Easy',
                                      'explanation': 'Concurrency control ensures multiple transactions execute '
                                                     'simultaneously without interfering or corrupting state.',
                                      'options': ['The mechanism that coordinates simultaneous execution of '
                                                  'transactions while preserving ACID properties and data consistency',
                                                  'A tool to measure CPU thread speed',
                                                  'An algorithm to connect databases to the internet',
                                                  'A backup scheduling system'],
                                      'question': 'What is Concurrency Control in a Database Management System?'},
                                     {'correct_answer': 'A lock that permits multiple transactions to read a resource '
                                                        'concurrently, but prevents any transaction from writing to it',
                                      'difficulty': 'Easy',
                                      'explanation': 'Multiple S-locks can coexist, but no exclusive lock can be '
                                                     'acquired until all S-locks release.',
                                      'options': ['A lock that permits multiple transactions to read a resource '
                                                  'concurrently, but prevents any transaction from writing to it',
                                                  'A lock that allows everyone to modify data',
                                                  'A lock shared across all databases in the cloud',
                                                  'An administrative lock on database files'],
                                      'question': 'What is a Shared Lock (S-Lock / Read Lock)?'},
                                     {'correct_answer': 'A lock that grants sole access to a transaction for writing; '
                                                        'no other transaction can read or write that resource',
                                      'difficulty': 'Easy',
                                      'explanation': 'X-locks enforce mutual exclusion: only one transaction can hold '
                                                     'an X-lock on a resource.',
                                      'options': ['A lock that grants sole access to a transaction for writing; no '
                                                  'other transaction can read or write that resource',
                                                  'A lock that allows multiple writers simultaneously',
                                                  'A lock that cannot be released',
                                                  'A temporary lock on memory buffers'],
                                      'question': 'What is an Exclusive Lock (X-Lock / Write Lock)?'},
                                     {'correct_answer': 'A situation where two or more transactions are blocked '
                                                        'waiting for locks held by each other, forming a circular wait '
                                                        'cycle',
                                      'difficulty': 'Easy',
                                      'explanation': 'Neither transaction can advance because each waits for a '
                                                     'resource locked by the other.',
                                      'options': ['A situation where two or more transactions are blocked waiting for '
                                                  'locks held by each other, forming a circular wait cycle',
                                                  'A transaction that runs out of memory',
                                                  'A database server that cannot connect to internet',
                                                  'A query that returns zero rows'],
                                      'question': 'What is a Deadlock in database transactions?'},
                                     {'correct_answer': 'Deadlock detection runs periodically (wait-for graph '
                                                        'analysis), picks a victim transaction, and rolls it back',
                                      'difficulty': 'Easy',
                                      'explanation': 'The engine detects cycles in its wait-for graph and aborts a '
                                                     'victim to break the deadlock.',
                                      'options': ['Deadlock detection runs periodically (wait-for graph analysis), '
                                                  'picks a victim transaction, and rolls it back',
                                                  'By shutting down the database server',
                                                  'By converting all locks to read locks',
                                                  'By ignoring the deadlocked queries'],
                                      'question': 'How does an RDBMS handle deadlocks automatically?'},
                                     {'correct_answer': 'PCC locks resources upfront assuming conflicts will occur; '
                                                        'OCC executes without locks and checks for conflicts at commit '
                                                        'time',
                                      'difficulty': 'Easy',
                                      'explanation': 'PCC prevents conflicts via locking; OCC validates at commit time '
                                                     'and rolls back on collision.',
                                      'options': ['PCC locks resources upfront assuming conflicts will occur; OCC '
                                                  'executes without locks and checks for conflicts at commit time',
                                                  'PCC is for fast computers; OCC is for slow computers',
                                                  'OCC uses passwords; PCC does not',
                                                  'PCC is deprecated in modern SQL'],
                                      'question': 'What is the difference between Optimistic Concurrency Control (OCC) '
                                                  'and Pessimistic Concurrency Control (PCC)?'},
                                     {'correct_answer': 'The level of detail of the data item being locked (database, '
                                                        'table, page, or row level)',
                                      'difficulty': 'Easy',
                                      'explanation': 'Finer granularity (row-level) increases concurrency but '
                                                     'increases lock memory overhead.',
                                      'options': ['The level of detail of the data item being locked (database, table, '
                                                  'page, or row level)',
                                                  'The size of the lock in bytes',
                                                  'The speed at which locks are acquired',
                                                  'The number of locks allowed per user'],
                                      'question': 'What is lock granularity in database management?'},
                                     {'correct_answer': 'Row-Level Locking',
                                      'difficulty': 'Easy',
                                      'explanation': 'Row-level locks isolate specific records, allowing concurrent '
                                                     'transactions to touch other rows in the same table.',
                                      'options': ['Row-Level Locking',
                                                  'Table-Level Locking',
                                                  'Database-Level Locking',
                                                  'Page-Level Locking'],
                                      'question': 'Which lock granularity allows the highest degree of concurrent '
                                                  'access?'},
                                     {'correct_answer': 'Two transactions read the same data and simultaneously update '
                                                        'it; the second write overwrites the first without '
                                                        'incorporating its changes',
                                      'difficulty': 'Easy',
                                      'explanation': 'Blind overwrites wipe out previous committed changes, corrupting '
                                                     'account balances or inventories.',
                                      'options': ['Two transactions read the same data and simultaneously update it; '
                                                  'the second write overwrites the first without incorporating its '
                                                  'changes',
                                                  'A query that loses internet connection',
                                                  'A table whose name is deleted',
                                                  'An error during software upgrade'],
                                      'question': 'What is a Lost Update anomaly in concurrent transactions?'},
                                     {'correct_answer': 'SELECT ... FOR UPDATE',
                                      'difficulty': 'Easy',
                                      'explanation': 'FOR UPDATE places X-locks on queried rows, blocking other '
                                                     'transactions from modifying them.',
                                      'options': ['SELECT ... FOR UPDATE',
                                                  'SELECT ... FOR READ',
                                                  'SELECT ... LOCK NOW',
                                                  'SELECT ... EXCLUSIVE'],
                                      'question': 'What SQL clause explicitly acquires exclusive row-level locks on '
                                                  'selected rows (pessimistic locking)?'},
                                     {'correct_answer': 'A locking protocol where a transaction has a Growing Phase '
                                                        '(acquiring locks) and a Shrinking Phase (releasing locks)',
                                      'difficulty': 'Medium',
                                      'explanation': '2PL guarantees serializability by forbidding lock acquisition '
                                                     'after any lock has been released.',
                                      'options': ['A locking protocol where a transaction has a Growing Phase '
                                                  '(acquiring locks) and a Shrinking Phase (releasing locks)',
                                                  'A transaction that executes two times',
                                                  'A protocol that uses two database servers',
                                                  'A protocol that locks two tables at once'],
                                      'question': 'What is Two-Phase Locking (2PL) protocol?'},
                                     {'correct_answer': 'All exclusive (write) locks held by a transaction are '
                                                        'retained until the transaction COMMITs or ROLLBACKs, '
                                                        'preventing cascading aborts',
                                      'difficulty': 'Medium',
                                      'explanation': 'Holding X-locks until commit ensures uncommitted data is never '
                                                     'read by others, preventing cascading rollbacks.',
                                      'options': ['All exclusive (write) locks held by a transaction are retained '
                                                  'until the transaction COMMITs or ROLLBACKs, preventing cascading '
                                                  'aborts',
                                                  'Locks are released immediately after statement',
                                                  'Transactions cannot abort',
                                                  'It eliminates deadlocks'],
                                      'question': 'What is Strict Two-Phase Locking (Strict 2PL) and what is its '
                                                  'primary benefit?'},
                                     {'correct_answer': 'ALL locks (both shared and exclusive) are held until the '
                                                        'transaction commits or aborts',
                                      'difficulty': 'Medium',
                                      'explanation': 'Rigorous 2PL enforces that transactions can be serialized in '
                                                     'their commit order.',
                                      'options': ['ALL locks (both shared and exclusive) are held until the '
                                                  'transaction commits or aborts',
                                                  'Locks are acquired in alphabetical order',
                                                  'Transactions are verified by two administrators',
                                                  'Locks cannot be released during crashes'],
                                      'question': 'What is Rigorous Two-Phase Locking (Rigorous 2PL)?'},
                                     {'correct_answer': 'Locks placed on higher-level containers (tables/pages) '
                                                        'indicating that a transaction holds or intends to acquire '
                                                        'locks on lower-level rows',
                                      'difficulty': 'Medium',
                                      'explanation': 'Intent locks allow the engine to detect table-level lock '
                                                     'conflicts without inspecting every individual row.',
                                      'options': ['Locks placed on higher-level containers (tables/pages) indicating '
                                                  'that a transaction holds or intends to acquire locks on lower-level '
                                                  'rows',
                                                  'Locks that express future intentions without blocking',
                                                  'Locks placed on database users',
                                                  'Temporary locks on log files'],
                                      'question': "What are Intent Locks (Intent Shared 'IS', Intent Exclusive 'IX') "
                                                  'in Multiple Granularity Locking (MGL)?'},
                                     {'correct_answer': 'The DBMS automatically converts many fine-grained row locks '
                                                        'into a single coarse-grained table lock when lock memory '
                                                        'thresholds are exceeded',
                                      'difficulty': 'Medium',
                                      'explanation': 'Escalation frees lock manager RAM at the expense of reducing '
                                                     'concurrency on that table.',
                                      'options': ['The DBMS automatically converts many fine-grained row locks into a '
                                                  'single coarse-grained table lock when lock memory thresholds are '
                                                  'exceeded',
                                                  'Increasing the priority of a locked query',
                                                  'Selling locks on database marketplaces',
                                                  'Releasing locks before commit'],
                                      'question': 'What is Lock Escalation?'},
                                     {'correct_answer': 'A directed graph where vertices represent transactions and '
                                                        'edges represent wait dependencies; a directed cycle indicates '
                                                        'a deadlock',
                                      'difficulty': 'Medium',
                                      'explanation': "Cycle detection algorithms (e.g. Tarjan's or DFS) on the WFG "
                                                     'detect deadlocks.',
                                      'options': ['A directed graph where vertices represent transactions and edges '
                                                  'represent wait dependencies; a directed cycle indicates a deadlock',
                                                  'A graph measuring server uptime',
                                                  'A chart of query response times',
                                                  'A graph of database foreign keys'],
                                      'question': 'What is a Wait-For Graph (WFG) and how is it used in deadlock '
                                                  'detection?'},
                                     {'correct_answer': 'Wait-Die: older waits, younger dies; Wound-Wait: older wounds '
                                                        '(preempts) younger, younger waits',
                                      'difficulty': 'Medium',
                                      'explanation': 'Both use timestamps to ensure no cyclic waiting can occur, '
                                                     'preventing deadlocks proactively.',
                                      'options': ['Wait-Die: older waits, younger dies; Wound-Wait: older wounds '
                                                  '(preempts) younger, younger waits',
                                                  'Both abort older transactions',
                                                  'Both are lock-free protocols',
                                                  'They are identical in priority'],
                                      'question': 'What is the difference between Wait-Die and Wound-Wait deadlock '
                                                  'prevention schemes based on transaction timestamps?'},
                                     {'correct_answer': 'By checking a version number (or timestamp) column; if the '
                                                        'version has changed since read time, the update aborts with '
                                                        'an OptimisticLockException',
                                      'difficulty': 'Medium',
                                      'explanation': "Checking 'WHERE id = ? AND version = ?' verifies no other "
                                                     'transaction updated the row in the interim.',
                                      'options': ['By checking a version number (or timestamp) column; if the version '
                                                  'has changed since read time, the update aborts with an '
                                                  'OptimisticLockException',
                                                  'By locking the entire database table',
                                                  'By asking the database user to confirm',
                                                  'By re-running the entire application'],
                                      'question': 'How does Optimistic Concurrency Control implement collision '
                                                  'detection during its Validation Phase?'},
                                     {'correct_answer': 'A combination of a record lock on the index record and a gap '
                                                        'lock on the gap before it, preventing phantom reads in '
                                                        'REPEATABLE READ',
                                      'difficulty': 'Medium',
                                      'explanation': 'Next-key locks freeze the index gap between existing keys, '
                                                     'preventing concurrent transactions from inserting phantoms.',
                                      'options': ['A combination of a record lock on the index record and a gap lock '
                                                  'on the gap before it, preventing phantom reads in REPEATABLE READ',
                                                  'Locking the next primary key value',
                                                  'A lock on foreign keys only',
                                                  'A lock that expires after 1 second'],
                                      'question': 'What is Next-Key Locking in MySQL InnoDB?'},
                                     {'correct_answer': 'A lock on the empty space between index records (or before '
                                                        'the first / after the last) to prevent insertions into that '
                                                        'interval',
                                      'difficulty': 'Medium',
                                      'explanation': 'Gap locks prohibit other transactions from inserting rows into '
                                                     'the locked index range.',
                                      'options': ['A lock on the empty space between index records (or before the '
                                                  'first / after the last) to prevent insertions into that interval',
                                                  'A lock on corrupted disk sectors',
                                                  'A lock on memory gaps',
                                                  'A lock that allows all reads'],
                                      'question': 'What is a Gap Lock in MySQL InnoDB?'},
                                     {'correct_answer': 'A schedule is conflict serializable if and only if its '
                                                        'precedence graph has no directed cycles',
                                      'difficulty': 'Hard',
                                      'explanation': 'A topological sort of an acyclic precedence graph yields an '
                                                     'equivalent serial execution order.',
                                      'options': ['A schedule is conflict serializable if and only if its precedence '
                                                  'graph has no directed cycles',
                                                  'A schedule where all transactions commit at the same time',
                                                  'A schedule with no aborts',
                                                  'A schedule verified by human auditors'],
                                      'question': 'What is Conflict Serializability and how is it proven using a '
                                                  'Precedence Graph (Serialization Graph)?'},
                                     {'correct_answer': 'View serializability checks if final states and read-from '
                                                        'relations match a serial schedule; testing it is NP-Complete',
                                      'difficulty': 'Hard',
                                      'explanation': 'Testing view serializability is NP-complete, which is why '
                                                     'engines rely on conflict serializability.',
                                      'options': ['View serializability checks if final states and read-from relations '
                                                  'match a serial schedule; testing it is NP-Complete',
                                                  'View serializability runs in O(n) time',
                                                  'View serializability is polynomial time',
                                                  'View serializability applies only to views'],
                                      'question': 'What is View Serializability and what is its computational '
                                                  'complexity compared to Conflict Serializability?'},
                                     {'correct_answer': "Thomas' Write Rule safely discards an obsolete write if a "
                                                        'newer write has already executed, without aborting the '
                                                        'transaction',
                                      'difficulty': 'Hard',
                                      'explanation': "Thomas' write rule allows greater concurrency by ignoring "
                                                     'outdated writes that have been superseded.',
                                      'options': ["Thomas' Write Rule safely discards an obsolete write if a newer "
                                                  'write has already executed, without aborting the transaction',
                                                  "Thomas' Write Rule forces all transactions to roll back",
                                                  'A rule that requires atomic clocks',
                                                  'A rule that deletes historical records'],
                                      'question': "What is Timestamp Ordering (T/O) concurrency control and Thomas' "
                                                  'Write Rule?'},
                                     {'correct_answer': 'Transactions see a consistent snapshot as of start time, but '
                                                        'concurrent updates can produce write skew anomalies that '
                                                        'violate serializability',
                                      'difficulty': 'Hard',
                                      'explanation': 'Snapshot isolation avoids read locks but allows disjoint '
                                                     'concurrent writes to violate multi-row invariants.',
                                      'options': ['Transactions see a consistent snapshot as of start time, but '
                                                  'concurrent updates can produce write skew anomalies that violate '
                                                  'serializability',
                                                  'Snapshot isolation allows dirty reads',
                                                  'Snapshot isolation is identical to serializable in every way',
                                                  'Snapshot isolation cannot execute writes'],
                                      'question': 'What is Snapshot Isolation and why is it technically NOT true '
                                                  'serializability?'},
                                     {'correct_answer': 'A hypothetical lock on all current and future rows that '
                                                        'satisfy a search predicate condition (e.g. salary > 50000), '
                                                        'eliminating phantoms',
                                      'difficulty': 'Hard',
                                      'explanation': 'Predicate locking is theoretically optimal for serializability '
                                                     'but computationally impractical, leading to index gap locking.',
                                      'options': ['A hypothetical lock on all current and future rows that satisfy a '
                                                  'search predicate condition (e.g. salary > 50000), eliminating '
                                                  'phantoms',
                                                  'A lock on SQL grammar rules',
                                                  'A lock on table columns only',
                                                  'A lock that checks user credentials'],
                                      'question': 'What is a Predicate Lock in relational database theory?'},
                                     {'correct_answer': 'Using synchronized GPS and atomic clocks with bounded time '
                                                        'uncertainty [t_earliest, t_latest] and waiting out '
                                                        'uncertainty (commit wait) before releasing locks',
                                      'difficulty': 'Hard',
                                      'explanation': 'TrueTime wait-out bounds ensure globally ordered transaction '
                                                     'commit timestamps across planetary data centers.',
                                      'options': ['Using synchronized GPS and atomic clocks with bounded time '
                                                  'uncertainty [t_earliest, t_latest] and waiting out uncertainty '
                                                  '(commit wait) before releasing locks',
                                                  'Using software NTP servers only',
                                                  'By locking all computers on Earth',
                                                  'By running all transactions on a single mainframe'],
                                      'question': 'In distributed consensus, how does TrueTime (used in Google '
                                                  'Spanner) guarantee global external consistency (Linearizability)?'},
                                     {'correct_answer': 'Transactions are ordered by an independent consensus layer '
                                                        'before execution, eliminating dynamic 2PL locking and '
                                                        'distributed commit protocols',
                                      'difficulty': 'Hard',
                                      'explanation': 'Deterministic execution removes distributed lock contention and '
                                                     'eliminates 2PC overhead.',
                                      'options': ['Transactions are ordered by an independent consensus layer before '
                                                  'execution, eliminating dynamic 2PL locking and distributed commit '
                                                  'protocols',
                                                  'A protocol that rolls back all transactions',
                                                  'A protocol that uses random numbers for timestamps',
                                                  'A database backup algorithm'],
                                      'question': 'What is the Calvin deterministic transaction scheduling protocol?'},
                                     {'correct_answer': 'A false deadlock detected by a distributed deadlock detector '
                                                        'caused by delayed propagation of lock release messages across '
                                                        'the network',
                                      'difficulty': 'Hard',
                                      'explanation': 'Network latency can cause lock release messages to lag behind '
                                                     'wait messages, creating phantom cycles.',
                                      'options': ['A false deadlock detected by a distributed deadlock detector caused '
                                                  'by delayed propagation of lock release messages across the network',
                                                  'A deadlock between deleted tables',
                                                  'A deadlock caused by hacker intrusions',
                                                  'A deadlock that crashes the OS kernel'],
                                      'question': 'What is a Phantom Deadlock in distributed databases?'},
                                     {'correct_answer': 'Locks protect logical database entities (rows/tables) for '
                                                        'transaction duration; Latches are short-lived physical memory '
                                                        'synchronization primitives (mutexes/rwlocks) protecting '
                                                        'in-memory data structures (buffer pages/B-Tree nodes)',
                                      'difficulty': 'Hard',
                                      'explanation': 'Latches protect physical buffer pages and tree pointers without '
                                                     'transactional rollback semantics.',
                                      'options': ['Locks protect logical database entities (rows/tables) for '
                                                  'transaction duration; Latches are short-lived physical memory '
                                                  'synchronization primitives (mutexes/rwlocks) protecting in-memory '
                                                  'data structures (buffer pages/B-Tree nodes)',
                                                  'Locks are in C++; Latches are in Java',
                                                  'Latches are for users; Locks are for DBAs',
                                                  'They are identical synonyms'],
                                      'question': 'What is the difference between a Lock and a Latch in database '
                                                  'internals?'},
                                     {'correct_answer': 'It reads the older historical version that was active as of '
                                                        "the reading transaction's timestamp without blocking or "
                                                        'aborting',
                                      'difficulty': 'Hard',
                                      'explanation': 'MVTO delivers consistent past versions directly from version '
                                                     'chains, eliminating read aborts.',
                                      'options': ['It reads the older historical version that was active as of the '
                                                  "reading transaction's timestamp without blocking or aborting",
                                                  'It aborts the transaction immediately',
                                                  'It rolls back the database to that timestamp',
                                                  'It converts the read to a write'],
                                      'question': 'How does Multi-Version Timestamp Ordering (MVTO) handle read '
                                                  'operations that arrive with timestamps older than the latest '
                                                  'written version?'}],
 'Database Indexing and B-Trees': [{'correct_answer': 'A specialized data structure that speeds up data retrieval '
                                                      'operations on a table at the cost of additional storage and '
                                                      'write overhead',
                                    'difficulty': 'Easy',
                                    'explanation': 'Indexes avoid full table scans by organizing pointers to rows in '
                                                   'sorted order.',
                                    'options': ['A specialized data structure that speeds up data retrieval operations '
                                                'on a table at the cost of additional storage and write overhead',
                                                'A list of database user passwords',
                                                'A table containing system settings',
                                                'A summary of database errors'],
                                    'question': 'What is a database index?'},
                                   {'correct_answer': 'B-Tree (or B+ Tree)',
                                    'difficulty': 'Easy',
                                    'explanation': 'B-Trees provide balanced O(log n) lookups, range scans, and prefix '
                                                   'searches on disk-backed storage.',
                                    'options': ['B-Tree (or B+ Tree)',
                                                'Hash Table',
                                                'Binary Search Tree',
                                                'Linked List'],
                                    'question': 'What is the most common default index data structure used in '
                                                'relational databases?'},
                                   {'correct_answer': 'An index that defines the physical storage order of the actual '
                                                      'table rows on disk (only one clustered index per table)',
                                    'difficulty': 'Easy',
                                    'explanation': 'A clustered index stores actual table data in its leaf pages, '
                                                   'eliminating row-pointer indirection.',
                                    'options': ['An index that defines the physical storage order of the actual table '
                                                'rows on disk (only one clustered index per table)',
                                                'An index shared across a cluster of servers',
                                                'An index containing only text columns',
                                                'An index that has no leaf nodes'],
                                    'question': 'What is a Clustered Index?'},
                                   {'correct_answer': 'An index with a separate storage structure from table data; '
                                                      'leaf nodes contain pointers (or primary keys) to the actual '
                                                      'data rows',
                                    'difficulty': 'Easy',
                                    'explanation': 'Secondary indexes store index keys and row pointers (RID/PK) '
                                                   'without changing table row layout.',
                                    'options': ['An index with a separate storage structure from table data; leaf '
                                                'nodes contain pointers (or primary keys) to the actual data rows',
                                                'An index that cannot be searched',
                                                'An index that does not use memory',
                                                'A temporary index deleted on disconnect'],
                                    'question': 'What is a Non-Clustered (Secondary) Index?'},
                                   {'correct_answer': 'Exactly one, because table rows can only be physically sorted '
                                                      'in one order on disk',
                                    'difficulty': 'Easy',
                                    'explanation': 'Because physical table rows can only have one sorted order on '
                                                   'disk, only one clustered index can exist.',
                                    'options': ['Exactly one, because table rows can only be physically sorted in one '
                                                'order on disk',
                                                'Up to two',
                                                'Any number up to 10',
                                                'Zero'],
                                    'question': 'How many Clustered Indexes can a single table have?'},
                                   {'correct_answer': 'Slows down write operations because the index data structure '
                                                      'must also be updated on every modification',
                                    'difficulty': 'Easy',
                                    'explanation': 'Every mutation must rebalance and update corresponding entries '
                                                   'across all defined indexes.',
                                    'options': ['Slows down write operations because the index data structure must '
                                                'also be updated on every modification',
                                                'Speeds up write operations by 50%',
                                                'Has zero impact on write performance',
                                                'Disables all updates'],
                                    'question': 'How does creating an index impact INSERT, UPDATE, and DELETE '
                                                'operations?'},
                                   {'correct_answer': 'The query engine inspects every single row in the table from '
                                                      'start to finish to find matching records',
                                    'difficulty': 'Easy',
                                    'explanation': 'Sequential scans take O(n) time, occurring when no applicable '
                                                   'index is available.',
                                    'options': ['The query engine inspects every single row in the table from start to '
                                                'finish to find matching records',
                                                'Scanning a table using an index',
                                                'Scanning table metadata only',
                                                'Printing all rows to terminal'],
                                    'question': 'What is a Full Table Scan (Sequential Scan)?'},
                                   {'correct_answer': 'CREATE INDEX',
                                    'difficulty': 'Easy',
                                    'explanation': 'CREATE INDEX index_name ON table_name (column_name); creates a new '
                                                   'index.',
                                    'options': ['CREATE INDEX', 'ADD INDEX', 'NEW INDEX', 'MAKE INDEX'],
                                    'question': 'Which SQL statement is used to create an index on a table?'},
                                   {'correct_answer': 'An index created on two or more columns of a table',
                                    'difficulty': 'Easy',
                                    'explanation': 'Composite indexes index multiple columns in a specified '
                                                   'left-to-right hierarchy.',
                                    'options': ['An index created on two or more columns of a table',
                                                'An index combining two separate tables',
                                                'An index that stores composite numbers',
                                                'An encrypted index'],
                                    'question': 'What is a Composite Index (Multi-Column Index)?'},
                                   {'correct_answer': 'The index can only be used by queries that filter by column A, '
                                                      'or (A, B), or (A, B, C) — skipping A renders the index unusable',
                                    'difficulty': 'Easy',
                                    'explanation': 'Queries must utilize the leading leftmost columns of the composite '
                                                   'key to leverage the B-Tree index.',
                                    'options': ['The index can only be used by queries that filter by column A, or (A, '
                                                'B), or (A, B, C) — skipping A renders the index unusable',
                                                'The index only stores the leftmost letter',
                                                'The index sorts from right to left',
                                                'All columns must be queried in reverse'],
                                    'question': 'What is the Leftmost Prefix Rule for composite indexes (e.g. index on '
                                                '(A, B, C))?'},
                                   {'correct_answer': 'An index that contains all columns requested by a query, '
                                                      'allowing the query to be answered entirely from the index '
                                                      'without visiting the table',
                                    'difficulty': 'Medium',
                                    'explanation': 'Index-only scans eliminate random I/O reads to main table storage '
                                                   'pages.',
                                    'options': ['An index that contains all columns requested by a query, allowing the '
                                                'query to be answered entirely from the index without visiting the '
                                                'table',
                                                'An index that covers all tables in the database',
                                                'An index that hides column names',
                                                'An index backed up to tape'],
                                    'question': 'What is a Covering Index (Index-Only Scan)?'},
                                   {'correct_answer': 'Index Seek traverses B-Tree root-to-leaf in O(log n) to locate '
                                                      'specific keys; Index Scan traverses all or a range of leaf '
                                                      'pages in O(n)',
                                    'difficulty': 'Medium',
                                    'explanation': 'Index seeks navigate branch nodes directly; scans read across '
                                                   'sequential leaf chains.',
                                    'options': ['Index Seek traverses B-Tree root-to-leaf in O(log n) to locate '
                                                'specific keys; Index Scan traverses all or a range of leaf pages in '
                                                'O(n)',
                                                'Index Seek is slower than Index Scan',
                                                'Index Seek only works on primary keys',
                                                'They are identical operations'],
                                    'question': 'What is an Index Seek vs an Index Scan?'},
                                   {'correct_answer': 'Provides O(1) equality lookups (=), but CANNOT support range '
                                                      'queries (<, >, BETWEEN) or sorted order',
                                    'difficulty': 'Medium',
                                    'explanation': 'Hash indexing does not preserve relative key ordering, making '
                                                   'range scans impossible.',
                                    'options': ['Provides O(1) equality lookups (=), but CANNOT support range queries '
                                                '(<, >, BETWEEN) or sorted order',
                                                'Cannot store strings',
                                                'Requires manual rebuilds daily',
                                                'Only works on temporary tables'],
                                    'question': 'What is a Hash Index and what is its primary limitation compared to a '
                                                'B-Tree index?'},
                                   {'correct_answer': 'Uses bit arrays (bitmaps) to represent row occurrences for '
                                                      'low-cardinality columns, predominantly in Data Warehouses / '
                                                      'OLAP',
                                    'difficulty': 'Medium',
                                    'explanation': 'Bitmap indexes allow bitwise AND/OR operations across columns with '
                                                   'few distinct values (e.g. gender, status).',
                                    'options': ['Uses bit arrays (bitmaps) to represent row occurrences for '
                                                'low-cardinality columns, predominantly in Data Warehouses / OLAP',
                                                'An index storing JPEG image files',
                                                'An index that cannot be compressed',
                                                'An index used in web browsers'],
                                    'question': 'What is a Bitmap Index and where is it predominantly used?'},
                                   {'correct_answer': 'The number of unique (distinct) values in an indexed column '
                                                      'relative to the total number of rows',
                                    'difficulty': 'Medium',
                                    'explanation': 'High cardinality (e.g. UUIDs, emails) indicates high selectivity, '
                                                   'where indexes are most effective.',
                                    'options': ['The number of unique (distinct) values in an indexed column relative '
                                                'to the total number of rows',
                                                'The physical byte size of the index',
                                                'The number of levels in the B-Tree',
                                                'The creation date of the index'],
                                    'question': 'What is Index Cardinality?'},
                                   {'correct_answer': 'An index built over a subset of rows defined by a WHERE clause '
                                                      "(e.g. WHERE status = 'active')",
                                    'difficulty': 'Medium',
                                    'explanation': 'Partial indexes save disk space and update overhead by excluding '
                                                   'irrelevant rows.',
                                    'options': ['An index built over a subset of rows defined by a WHERE clause (e.g. '
                                                "WHERE status = 'active')",
                                                'An index that only indexes half of each string',
                                                'An index that is partially deleted',
                                                'An index with missing leaf nodes'],
                                    'question': 'What is a Partial Index (Filtered Index)?'},
                                   {'correct_answer': 'An index created on the result of an expression or function '
                                                      '(e.g. CREATE INDEX ON table (LOWER(email)))',
                                    'difficulty': 'Medium',
                                    'explanation': 'Functional indexes allow queries using function predicates to '
                                                   'perform index seeks rather than table scans.',
                                    'options': ['An index created on the result of an expression or function (e.g. '
                                                'CREATE INDEX ON table (LOWER(email)))',
                                                'An index that changes its name dynamically',
                                                'An index used only in stored procedures',
                                                'An index with mathematical variables'],
                                    'question': 'What is an Expression-Based (Functional) Index?'},
                                   {'correct_answer': 'When inserting a key into a full B-Tree node page, the engine '
                                                      'splits the page into two and promotes the middle key to parent',
                                    'difficulty': 'Medium',
                                    'explanation': 'Random insertions into full pages cause page splits, introducing '
                                                   'physical fragmentation.',
                                    'options': ['When inserting a key into a full B-Tree node page, the engine splits '
                                                'the page into two and promotes the middle key to parent',
                                                'Deleting too many rows',
                                                'A hard drive sector crash',
                                                'Running database backups'],
                                    'question': 'What is B-Tree Page Splitting and what causes it?'},
                                   {'correct_answer': 'The percentage of space on each leaf page reserved for data vs '
                                                      'free space left for future inserts (e.g. 80%)',
                                    'difficulty': 'Medium',
                                    'explanation': 'Lowering fill factor leaves headroom for inserts, reducing '
                                                   'expensive page splits on write-heavy tables.',
                                    'options': ['The percentage of space on each leaf page reserved for data vs free '
                                                'space left for future inserts (e.g. 80%)',
                                                'The ratio of index size to table size',
                                                'The percentage of RAM allocated to indexing',
                                                'The total count of indexed columns'],
                                    'question': 'What is the fill factor of a B-Tree index?'},
                                   {'correct_answer': 'If the query condition matches a large percentage of total rows '
                                                      '(low selectivity, >15-20%), sequential I/O is faster than '
                                                      'random index lookups',
                                    'difficulty': 'Medium',
                                    'explanation': 'Sequential block reads outperform millions of scattered random '
                                                   'disk head seeks when retrieving broad subsets.',
                                    'options': ['If the query condition matches a large percentage of total rows (low '
                                                'selectivity, >15-20%), sequential I/O is faster than random index '
                                                'lookups',
                                                'Because the optimizer is disabled',
                                                'Because indexes can only be used once per day',
                                                'Because table scans use zero CPU'],
                                    'question': 'Why might the query optimizer choose a Full Table Scan even when a '
                                                'valid index exists on the filtered column?'},
                                   {'correct_answer': 'Leaf nodes form a doubly linked list containing all table '
                                                      'data/keys, allowing sequential range traversal without '
                                                      're-visiting internal nodes',
                                    'difficulty': 'Hard',
                                    'explanation': 'B+ Trees store records exclusively at leaves, linked sequentially '
                                                   'for high-throughput range scans.',
                                    'options': ['Leaf nodes form a doubly linked list containing all table data/keys, '
                                                'allowing sequential range traversal without re-visiting internal '
                                                'nodes',
                                                'Leaf nodes are stored in a hash table',
                                                'Internal nodes store all data records',
                                                'Leaf nodes have no parent pointers'],
                                    'question': 'What is the B+ Tree structure in databases and how does its leaf-node '
                                                'linking optimize range queries?'},
                                   {'correct_answer': 'It appends all writes sequentially to memory (MemTable) and '
                                                      'flushes immutable SSTables to disk, eliminating random disk I/O '
                                                      'bottlenecks',
                                    'difficulty': 'Hard',
                                    'explanation': 'LSM-Trees convert random writes into sequential appends, offering '
                                                   'immense write throughput.',
                                    'options': ['It appends all writes sequentially to memory (MemTable) and flushes '
                                                'immutable SSTables to disk, eliminating random disk I/O bottlenecks',
                                                'It stores data in binary search trees',
                                                'It prevents all disk writes',
                                                'It uses magnetic tape memory exclusively'],
                                    'question': 'What is an LSM-Tree (Log-Structured Merge-Tree) and why is it '
                                                'preferred over B-Trees for write-intensive databases (Cassandra, '
                                                'RocksDB)?'},
                                   {'correct_answer': 'Compaction merges overlapping SSTables, removes deleted '
                                                      'tombstones, and re-sorts data to control read amplification and '
                                                      'disk usage',
                                    'difficulty': 'Hard',
                                    'explanation': 'Compaction bounds space amplification and search latency across '
                                                   'layered immutable files.',
                                    'options': ['Compaction merges overlapping SSTables, removes deleted tombstones, '
                                                'and re-sorts data to control read amplification and disk usage',
                                                'Compacting database memory using gzip',
                                                'Compressing column names in schemas',
                                                'Deleting old databases'],
                                    'question': 'What are Compaction strategies in LSM-Trees (Size-Tiered vs Leveled '
                                                'Compaction)?'},
                                   {'correct_answer': 'An extensible balanced tree template that indexes non-scalar '
                                                      'spatial, geometric, and range data (used by PostGIS)',
                                    'difficulty': 'Hard',
                                    'explanation': 'GiST allows custom data types to implement tree indexing for '
                                                   'multidimensional and geometric queries.',
                                    'options': ['An extensible balanced tree template that indexes non-scalar spatial, '
                                                'geometric, and range data (used by PostGIS)',
                                                'A hash table of text keys',
                                                'A binary heap in memory',
                                                'A tool for full-text translation'],
                                    'question': 'What is a GiST (Generalized Search Tree) index in PostgreSQL?'},
                                   {'correct_answer': 'An inverted index that maps elements (e.g. JSON keys, array '
                                                      'elements, text lexemes) to lists of matching row IDs',
                                    'difficulty': 'Hard',
                                    'explanation': 'GIN indexes document tokens and array items, enabling ultra-fast '
                                                   'full-text and JSONB containment queries.',
                                    'options': ['An inverted index that maps elements (e.g. JSON keys, array elements, '
                                                'text lexemes) to lists of matching row IDs',
                                                'A geographic index for maps',
                                                'A clustered primary index',
                                                'An encryption algorithm'],
                                    'question': 'What is a GIN (Generalized Inverted Index) in PostgreSQL?'},
                                   {'correct_answer': 'An index storing minimum and maximum values for physical block '
                                                      'ranges; optimal for multi-billion row tables physically sorted '
                                                      'by timestamp/ID',
                                    'difficulty': 'Hard',
                                    'explanation': 'BRIN indexes occupy negligible disk space (kilobytes for gigabytes '
                                                   'of data) on naturally ordered data.',
                                    'options': ['An index storing minimum and maximum values for physical block '
                                                'ranges; optimal for multi-billion row tables physically sorted by '
                                                'timestamp/ID',
                                                'An index that runs on GPU memory',
                                                'A hash index for UUIDs',
                                                'A tree with 100 levels'],
                                    'question': 'What is a BRIN (Block Range Index) in PostgreSQL and when is it '
                                                'optimal?'},
                                   {'correct_answer': 'Dead tuple references accumulate in index pages due to MVCC '
                                                      "updates; resolved using 'REINDEX CONCURRENTLY'",
                                    'difficulty': 'Hard',
                                    'explanation': 'MVCC updates produce orphaned index versions that inflate page '
                                                   'counts until reindexed concurrently.',
                                    'options': ['Dead tuple references accumulate in index pages due to MVCC updates; '
                                                "resolved using 'REINDEX CONCURRENTLY'",
                                                'Indexes becoming corrupted by power outages',
                                                'Indexes growing larger than the hard drive',
                                                'An error during table creation'],
                                    'question': 'What is Index Bloat in PostgreSQL B-Trees and how is it resolved '
                                                'without downtime?'},
                                   {'correct_answer': 'Write/Read amplification is bytes written/read per logical '
                                                      'byte; Space amplification is total physical storage vs logical '
                                                      'data size',
                                    'difficulty': 'Hard',
                                    'explanation': 'The RUM Conjecture proves storage engines cannot optimize Read, '
                                                   'Update, and Memory amplification simultaneously.',
                                    'options': ['Write/Read amplification is bytes written/read per logical byte; '
                                                'Space amplification is total physical storage vs logical data size',
                                                'They are metrics measuring CPU clock cycles',
                                                'They measure network bandwidth only',
                                                'They are compiler profiling flags'],
                                    'question': 'What is the difference between Write Amplification, Read '
                                                'Amplification, and Space Amplification in storage engines?'},
                                   {'correct_answer': 'It truncates distinguishing separator keys in internal branch '
                                                      'nodes to minimal prefixes, fitting more keys per page and '
                                                      'reducing tree height',
                                    'difficulty': 'Hard',
                                    'explanation': 'Shorter router keys allow higher fanout, making the B-Tree '
                                                   'shallower and faster.',
                                    'options': ['It truncates distinguishing separator keys in internal branch nodes '
                                                'to minimal prefixes, fitting more keys per page and reducing tree '
                                                'height',
                                                'It compresses strings with LZW',
                                                'It deletes duplicate keys from the database',
                                                'It converts numbers to 16-bit integers'],
                                    'question': 'How does Prefix Compression (Suffix Truncation) in B-Tree internal '
                                                'nodes increase tree fanout?'},
                                   {'correct_answer': 'Traversing threads acquire a latch on a child node before '
                                                      'releasing the latch on the parent node, ensuring safe '
                                                      'concurrent navigation',
                                    'difficulty': 'Hard',
                                    'explanation': 'Latch crabbing prevents concurrent structural modifications from '
                                                   'disrupting in-flight search paths.',
                                    'options': ['Traversing threads acquire a latch on a child node before releasing '
                                                'the latch on the parent node, ensuring safe concurrent navigation',
                                                'A deadlocked thread state',
                                                'A hardware fault in memory buses',
                                                'An index rebalancing algorithm'],
                                    'question': 'What is B-Tree Latch Crabbing (Lock Crabbing) during concurrent tree '
                                                'traversal?'}],
 'Database Integrity Constraints': [{'correct_answer': 'A formal declarative rule enforced by the DBMS to guarantee '
                                                       'accuracy, consistency, and validity of data',
                                     'difficulty': 'Easy',
                                     'explanation': 'Constraints prevent invalid data from ever being committed to the '
                                                    'database.',
                                     'options': ['A formal declarative rule enforced by the DBMS to guarantee '
                                                 'accuracy, consistency, and validity of data',
                                                 'A password requirement for database users',
                                                 'A physical limit on hard disk drive size',
                                                 'A backup scheduling policy'],
                                     'question': 'What is a database integrity constraint?'},
                                    {'correct_answer': 'Ensures that a column cannot store NULL (missing or undefined) '
                                                       'values',
                                     'difficulty': 'Easy',
                                     'explanation': 'NOT NULL mandates that a value must always be provided for that '
                                                    'attribute.',
                                     'options': ['Ensures that a column cannot store NULL (missing or undefined) '
                                                 'values',
                                                 'Ensures that all numbers are positive',
                                                 'Ensures that values are unique',
                                                 'Ensures strings are capitalized'],
                                     'question': 'What does the NOT NULL constraint enforce?'},
                                    {'correct_answer': 'Ensures that all non-null values in a column (or set of '
                                                       'columns) are distinct across all rows',
                                     'difficulty': 'Easy',
                                     'explanation': 'UNIQUE prevents duplicate values while permitting NULLs (subject '
                                                    'to SQL engine rules).',
                                     'options': ['Ensures that all non-null values in a column (or set of columns) are '
                                                 'distinct across all rows',
                                                 'Ensures values cannot be modified',
                                                 'Ensures values are greater than zero',
                                                 'Ensures the table has only one row'],
                                     'question': 'What does the UNIQUE constraint enforce?'},
                                    {'correct_answer': 'Both UNIQUE and NOT NULL constraints on the designated '
                                                       'column(s)',
                                     'difficulty': 'Easy',
                                     'explanation': 'A primary key inherently requires non-null, uniquely distinct '
                                                    'values for every tuple.',
                                     'options': ['Both UNIQUE and NOT NULL constraints on the designated column(s)',
                                                 'CHECK and DEFAULT constraints',
                                                 'FOREIGN KEY and CASCADE constraints',
                                                 'AUTO_INCREMENT and INDEX constraints'],
                                     'question': 'What does the PRIMARY KEY constraint combine?'},
                                    {'correct_answer': 'Validates that attribute values satisfy a specified boolean '
                                                       'predicate condition before insertion or update',
                                     'difficulty': 'Easy',
                                     'explanation': 'CHECK (e.g., CHECK (age >= 18)) rejects transactions that violate '
                                                    'the condition.',
                                     'options': ['Validates that attribute values satisfy a specified boolean '
                                                 'predicate condition before insertion or update',
                                                 'Checks if the database server has internet access',
                                                 'Checks user passwords for expiration',
                                                 'Verifies hard drive temperatures'],
                                     'question': 'What does a CHECK constraint do?'},
                                    {'correct_answer': 'Specifies a fallback default value to be inserted into a '
                                                       'column if no explicit value is provided',
                                     'difficulty': 'Easy',
                                     'explanation': 'DEFAULT supplies standard values (e.g. DEFAULT CURRENT_TIMESTAMP) '
                                                    'automatically.',
                                     'options': ['Specifies a fallback default value to be inserted into a column if '
                                                 'no explicit value is provided',
                                                 'Resets the database to factory settings',
                                                 'Restores deleted tables',
                                                 'Deletes default user accounts'],
                                     'question': 'What does the DEFAULT constraint do?'},
                                    {'correct_answer': 'Every table must have a primary key and that primary key must '
                                                       'be unique and non-null',
                                     'difficulty': 'Easy',
                                     'explanation': 'Entity integrity ensures individual real-world objects can be '
                                                    'uniquely distinguished.',
                                     'options': ['Every table must have a primary key and that primary key must be '
                                                 'unique and non-null',
                                                 'Entities must be stored on separate servers',
                                                 'Entities must have passwords',
                                                 'Tables must have at least 10 columns'],
                                     'question': 'What is Entity Integrity in the relational model?'},
                                    {'correct_answer': 'Foreign key values in a child table must match an existing '
                                                       'primary key value in the referenced parent table (or be null)',
                                     'difficulty': 'Easy',
                                     'explanation': 'Referential integrity prevents orphan records in dependent child '
                                                    'tables.',
                                     'options': ['Foreign key values in a child table must match an existing primary '
                                                 'key value in the referenced parent table (or be null)',
                                                 'All tables must have identical schemas',
                                                 'All users must have matching permissions',
                                                 'References must be encrypted'],
                                     'question': 'What is Referential Integrity in relational databases?'},
                                    {'correct_answer': 'The DBMS rejects the transaction and raises a constraint '
                                                       'violation error',
                                     'difficulty': 'Easy',
                                     'explanation': 'Violating constraints causes immediate transaction abort or '
                                                    'statement failure.',
                                     'options': ['The DBMS rejects the transaction and raises a constraint violation '
                                                 'error',
                                                 'The value is silently converted to null',
                                                 'The database creates a backup',
                                                 'The table is dropped'],
                                     'question': 'What happens when you attempt to insert data that violates a CHECK '
                                                 'constraint?'},
                                    {'correct_answer': 'Yes, a table can have multiple distinct UNIQUE constraints '
                                                       'across different columns',
                                     'difficulty': 'Easy',
                                     'explanation': 'Multiple candidate keys can each be protected with their own '
                                                    'UNIQUE constraints.',
                                     'options': ['Yes, a table can have multiple distinct UNIQUE constraints across '
                                                 'different columns',
                                                 'No, only one UNIQUE constraint per table is allowed',
                                                 'Only if the table has no primary key',
                                                 'Only in NoSQL databases'],
                                     'question': 'Can a table have multiple UNIQUE constraints?'},
                                    {'correct_answer': 'Automatically deletes all child records when the referenced '
                                                       'parent record is deleted',
                                     'difficulty': 'Medium',
                                     'explanation': 'CASCADE propagates deletions down the foreign key relationship '
                                                    'chain automatically.',
                                     'options': ['Automatically deletes all child records when the referenced parent '
                                                 'record is deleted',
                                                 'Prevents the parent record from being deleted',
                                                 'Sets the child foreign key column to NULL',
                                                 'Sends a notification email to the DBA'],
                                     'question': "What does the 'ON DELETE CASCADE' foreign key action do?"},
                                    {'correct_answer': 'Sets the foreign key column in all matching child rows to NULL '
                                                       'when the parent record is deleted',
                                     'difficulty': 'Medium',
                                     'explanation': 'SET NULL disassociates child records from the deleted parent '
                                                    'while preserving the child data.',
                                     'options': ['Sets the foreign key column in all matching child rows to NULL when '
                                                 'the parent record is deleted',
                                                 'Deletes the child records',
                                                 'Prevents parent deletion',
                                                 'Sets the child column to 0'],
                                     'question': "What does the 'ON DELETE SET NULL' foreign key action do?"},
                                    {'correct_answer': 'Rejects and blocks deletion of the parent record if any '
                                                       'matching child records exist',
                                     'difficulty': 'Medium',
                                     'explanation': 'RESTRICT prevents deletion of parents while dependent children '
                                                    'still reference them.',
                                     'options': ['Rejects and blocks deletion of the parent record if any matching '
                                                 'child records exist',
                                                 'Deletes all child records silently',
                                                 'Moves child records to an archive table',
                                                 'Converts the parent table to read-only'],
                                     'question': "What does the 'ON DELETE RESTRICT' (or 'ON DELETE NO ACTION') action "
                                                 'do?'},
                                    {'correct_answer': 'Enforces that all entries in a given column conform to the '
                                                       'defined data type, format, and valid range of values',
                                     'difficulty': 'Medium',
                                     'explanation': 'Domain integrity ensures data type compliance, length '
                                                    'restrictions, and value ranges.',
                                     'options': ['Enforces that all entries in a given column conform to the defined '
                                                 'data type, format, and valid range of values',
                                                 'Restricts database access to registered domain names',
                                                 'Enforces DNS security protocols',
                                                 'Ensures table names are unique'],
                                     'question': 'What is Domain Integrity in database systems?'},
                                    {'correct_answer': 'The composite foreign key columns must match the composite '
                                                       'primary key columns of the parent table in order and data type',
                                     'difficulty': 'Medium',
                                     'explanation': 'Multi-column foreign keys must match the exact multi-column key '
                                                    'of the parent relation.',
                                     'options': ['The composite foreign key columns must match the composite primary '
                                                 'key columns of the parent table in order and data type',
                                                 'By encrypting both columns together',
                                                 'By hashing the columns with MD5',
                                                 'By matching any one of the parent columns'],
                                     'question': 'How does a composite foreign key enforce referential integrity?'},
                                    {'correct_answer': 'A schema-level constraint that can express complex multi-table '
                                                       'integrity conditions independent of any single table',
                                     'difficulty': 'Medium',
                                     'explanation': 'Assertions enforce cross-table business rules across the entire '
                                                    'schema.',
                                     'options': ['A schema-level constraint that can express complex multi-table '
                                                 'integrity conditions independent of any single table',
                                                 'A debugging print statement in SQL',
                                                 'A user authentication token',
                                                 'A temporary check on memory'],
                                     'question': 'What is an Assertion in standard SQL-92 (CREATE ASSERTION)?'},
                                    {'correct_answer': 'Procedural code executed automatically in response to DML '
                                                       'events, used to enforce complex business rules that '
                                                       'declarative constraints cannot express',
                                     'difficulty': 'Medium',
                                     'explanation': 'Triggers enforce custom cross-table validations, audit logging, '
                                                    'and automated updates.',
                                     'options': ['Procedural code executed automatically in response to DML events, '
                                                 'used to enforce complex business rules that declarative constraints '
                                                 'cannot express',
                                                 'A hardware interrupt on disk write',
                                                 'A tool to schedule daily backups',
                                                 'A button on database UI'],
                                     'question': 'What is a database Trigger and how does it relate to integrity '
                                                 'constraints?'},
                                    {'correct_answer': 'No, CHECK constraints can only reference columns within the '
                                                       'same row of the current table (use triggers or assertions for '
                                                       'cross-table)',
                                     'difficulty': 'Medium',
                                     'explanation': 'Most DBMSs forbid subqueries in CHECK constraints to prevent '
                                                    'performance degradation.',
                                     'options': ['No, CHECK constraints can only reference columns within the same row '
                                                 'of the current table (use triggers or assertions for cross-table)',
                                                 'Yes, anytime using subqueries',
                                                 'Only with JOIN keywords',
                                                 'Only if both tables share the same schema'],
                                     'question': 'Can a CHECK constraint reference columns from other tables in '
                                                 'standard SQL implementations?'},
                                    {'correct_answer': 'Permitted, because each NULL represents an unknown value, so '
                                                       'NULL is not considered equal to another NULL',
                                     'difficulty': 'Medium',
                                     'explanation': 'SQL standards allow multiple NULLs in UNIQUE columns unless '
                                                    'UNIQUE NULLS NOT DISTINCT is specified.',
                                     'options': ['Permitted, because each NULL represents an unknown value, so NULL is '
                                                 'not considered equal to another NULL',
                                                 'Rejected as duplicate key violation',
                                                 'All converted to empty strings',
                                                 'The table automatically creates an index'],
                                     'question': 'What happens when multiple NULL values are inserted into a column '
                                                 'with a UNIQUE constraint in PostgreSQL/MySQL?'},
                                    {'correct_answer': 'Column-level applies to one specific column; table-level is '
                                                       'declared after columns and can span multiple composite columns',
                                     'difficulty': 'Medium',
                                     'explanation': 'Table-level syntax is required for composite keys and '
                                                    'multi-column constraints.',
                                     'options': ['Column-level applies to one specific column; table-level is declared '
                                                 'after columns and can span multiple composite columns',
                                                 'Column-level is faster',
                                                 'Table-level constraints are deprecated',
                                                 'Column-level only applies to numbers'],
                                     'question': 'What is the difference between table-level constraints and '
                                                 'column-level constraints?'},
                                    {'correct_answer': 'Constraints whose enforcement is postponed until the '
                                                       'transaction COMMIT rather than checked after each individual '
                                                       'SQL statement',
                                     'difficulty': 'Hard',
                                     'explanation': 'Deferred constraints allow mutually referencing circular foreign '
                                                    'keys to be inserted within a transaction.',
                                     'options': ['Constraints whose enforcement is postponed until the transaction '
                                                 'COMMIT rather than checked after each individual SQL statement',
                                                 'Constraints that can be deleted by users',
                                                 'Constraints evaluated in background threads',
                                                 'Constraints that only apply on weekends'],
                                     'question': 'What are Deferrable Constraints (DEFERRABLE INITIALLY DEFERRED) in '
                                                 'databases like PostgreSQL and Oracle?'},
                                    {'correct_answer': 'Both records can be inserted with temporary invalid foreign '
                                                       'keys because the constraint check is delayed until COMMIT',
                                     'difficulty': 'Hard',
                                     'explanation': 'Deferring foreign key checks allows interrelated records to be '
                                                    'committed together safely.',
                                     'options': ['Both records can be inserted with temporary invalid foreign keys '
                                                 'because the constraint check is delayed until COMMIT',
                                                 'By deleting one table temporarily',
                                                 'By running both inserts in separate databases',
                                                 'By converting foreign keys to text'],
                                     'question': 'How do deferrable constraints resolve the chicken-and-egg insertion '
                                                 'problem between mutually dependent foreign keys?'},
                                    {'correct_answer': 'A generalized constraint ensuring that no two rows have '
                                                       'overlapping values according to specified comparison operators '
                                                       '(e.g. no overlapping time ranges)',
                                     'difficulty': 'Hard',
                                     'explanation': 'Exclusion constraints prevent temporal overlaps and spatial '
                                                    'collisions using GiST index operators.',
                                     'options': ['A generalized constraint ensuring that no two rows have overlapping '
                                                 'values according to specified comparison operators (e.g. no '
                                                 'overlapping time ranges)',
                                                 'A constraint that excludes users from accessing tables',
                                                 'A rule that deletes excluded columns',
                                                 'A constraint forbidding foreign keys'],
                                     'question': 'What is an Exclusion Constraint in PostgreSQL (CREATE TABLE ... '
                                                 'EXCLUDE USING gist)?'},
                                    {'correct_answer': 'Constraints are checked directly by the engine kernel, are '
                                                       'optimized by query planners, and avoid procedural overhead and '
                                                       'concurrency race conditions',
                                     'difficulty': 'Hard',
                                     'explanation': 'Declarative constraints are atomic, faster, and inform optimizer '
                                                    'cardinality estimations.',
                                     'options': ['Constraints are checked directly by the engine kernel, are optimized '
                                                 'by query planners, and avoid procedural overhead and concurrency '
                                                 'race conditions',
                                                 'Triggers cannot modify data',
                                                 'Constraints use zero CPU',
                                                 'Triggers are deprecated in SQL:2016'],
                                     'question': 'Why are Declarative Constraints generally preferred over Database '
                                                 'Triggers for enforcing data integrity?'},
                                    {'correct_answer': 'The engine must perform full table scans or lock the entire '
                                                       'child table to verify referential integrity, creating '
                                                       'catastrophic lock contention',
                                     'difficulty': 'Hard',
                                     'explanation': 'Modifying parent keys locks child tables if foreign keys lack '
                                                    'indexes, destroying concurrency.',
                                     'options': ['The engine must perform full table scans or lock the entire child '
                                                 'table to verify referential integrity, creating catastrophic lock '
                                                 'contention',
                                                 'It deletes child records automatically',
                                                 'It permanently disables foreign keys',
                                                 'It crashes the database server'],
                                     'question': 'How does foreign key validation without an index on the referencing '
                                                 'child column cause severe deadlocks during parent table updates?'},
                                    {'correct_answer': 'INITIALLY IMMEDIATE checks constraints immediately after every '
                                                       'statement; INITIALLY DEFERRED waits until COMMIT',
                                     'difficulty': 'Hard',
                                     'explanation': 'Immediate constraints fail the active statement; deferred '
                                                    'constraints fail the final commit.',
                                     'options': ['INITIALLY IMMEDIATE checks constraints immediately after every '
                                                 'statement; INITIALLY DEFERRED waits until COMMIT',
                                                 'INITIALLY IMMEDIATE runs on startup',
                                                 'INITIALLY DEFERRED runs only on rollbacks',
                                                 'They are identical in timing'],
                                     'question': 'What is the difference between INITIALLY IMMEDIATE and INITIALLY '
                                                 'DEFERRED constraints?'},
                                    {'correct_answer': 'They require distributed two-phase commit (2PC) transactions '
                                                       'and network round-trips across remote nodes to verify key '
                                                       'presence',
                                     'difficulty': 'Hard',
                                     'explanation': 'Validating cross-shard references across distinct network '
                                                    'partitions adds latency to mutations.',
                                     'options': ['They require distributed two-phase commit (2PC) transactions and '
                                                 'network round-trips across remote nodes to verify key presence',
                                                 'They disable network encryption',
                                                 'They require manual replication by users',
                                                 'Distributed databases cannot support foreign keys'],
                                     'question': 'In distributed databases (e.g. Google Spanner, CockroachDB), why are '
                                                 'cross-table foreign key constraints significantly more expensive?'},
                                    {'correct_answer': 'A record in a child table whose foreign key value no longer '
                                                       'references any valid record in the parent table',
                                     'difficulty': 'Hard',
                                     'explanation': 'Orphans result from unconstrained deletions or disabling foreign '
                                                    'key validation.',
                                     'options': ['A record in a child table whose foreign key value no longer '
                                                 'references any valid record in the parent table',
                                                 'A table with no name',
                                                 'A database without an administrator',
                                                 'An unused index on disk'],
                                     'question': 'What is an Orphan Record in a relational database?'},
                                    {'correct_answer': 'Allows adding constraints instantaneously without validating '
                                                       'existing millions of rows, then validating asynchronously '
                                                       'without write locks',
                                     'difficulty': 'Hard',
                                     'explanation': 'Splitting addition and validation prevents blocking production '
                                                    'writes during multi-hour table scans.',
                                     'options': ['Allows adding constraints instantaneously without validating '
                                                 'existing millions of rows, then validating asynchronously without '
                                                 'write locks',
                                                 'Validates constraints on backup files',
                                                 'Validates constraint spelling',
                                                 'Deletes invalid rows automatically'],
                                     'question': "What does 'VALIDATE CONSTRAINT' vs 'ADD CONSTRAINT ... NOT VALID' do "
                                                 'in PostgreSQL/Oracle for huge tables?'},
                                    {'correct_answer': 'The DBMS creates a unique B-Tree index underneath; inserting a '
                                                       'new key attempts an index insert that immediately detects '
                                                       'duplicate keys',
                                     'difficulty': 'Hard',
                                     'explanation': 'Under the hood, UNIQUE constraints are enforced in O(log n) time '
                                                    'by underlying unique B-Tree indexes.',
                                     'options': ['The DBMS creates a unique B-Tree index underneath; inserting a new '
                                                 'key attempts an index insert that immediately detects duplicate keys',
                                                 'By scanning the entire table on every insert',
                                                 'By hashing table rows to disk files',
                                                 'By running an asynchronous checking thread'],
                                     'question': 'How do unique constraints rely on physical index structures for '
                                                 'enforcement in RDBMS?'}],
 'Database Normalization (1NF, 2NF, 3NF)': [{'correct_answer': 'A systematic process of structuring database schemas '
                                                               'to minimize data redundancy and eliminate anomalies',
                                             'difficulty': 'Easy',
                                             'explanation': 'Normalization organizes fields and relationships into '
                                                            'normal forms to preserve consistency.',
                                             'options': ['A systematic process of structuring database schemas to '
                                                         'minimize data redundancy and eliminate anomalies',
                                                         'Compressing tables to save disk space',
                                                         'Converting tables to JSON format',
                                                         'Backing up data to remote servers'],
                                             'question': 'What is Database Normalization?'},
                                            {'correct_answer': 'Insertion anomaly, Deletion anomaly, and Update '
                                                               'anomaly',
                                             'difficulty': 'Easy',
                                             'explanation': 'Redundancy causes anomalies where deleting or inserting '
                                                            'records creates unintentional side-effects.',
                                             'options': ['Insertion anomaly, Deletion anomaly, and Update anomaly',
                                                         'Network anomaly, CPU anomaly, RAM anomaly',
                                                         'Syntax anomaly, Compiler anomaly, Linker anomaly',
                                                         'Read anomaly, Write anomaly, Execute anomaly'],
                                             'question': 'What are the three primary database modification anomalies '
                                                         'prevented by normalization?'},
                                            {'correct_answer': 'Inconsistent data occurs when modifying a value in one '
                                                               'place requires updating redundant copies across '
                                                               'multiple rows',
                                             'difficulty': 'Easy',
                                             'explanation': 'If redundant copies are not updated simultaneously, the '
                                                            'database enters an inconsistent state.',
                                             'options': ['Inconsistent data occurs when modifying a value in one place '
                                                         'requires updating redundant copies across multiple rows',
                                                         'A failure to download software updates',
                                                         'An error during database reboot',
                                                         'A crash when creating new tables'],
                                             'question': 'What is an Update Anomaly?'},
                                            {'correct_answer': 'Deleting one piece of information unintentionally '
                                                               'causes the unintended loss of other unrelated '
                                                               'information',
                                             'difficulty': 'Easy',
                                             'explanation': 'Un-normalized tables couple disparate concepts so '
                                                            'deleting one record destroys another.',
                                             'options': ['Deleting one piece of information unintentionally causes the '
                                                         'unintended loss of other unrelated information',
                                                         'Accidentally deleting the whole database',
                                                         'Deleting files on the hard drive',
                                                         'A disk sector failure'],
                                             'question': 'What is a Deletion Anomaly?'},
                                            {'correct_answer': 'Inability to insert a record because mandatory '
                                                               'attributes of unrelated entities are not yet known',
                                             'difficulty': 'Easy',
                                             'explanation': 'Coupled designs prevent recording new entities without '
                                                            'dummy or null values for unrelated keys.',
                                             'options': ['Inability to insert a record because mandatory attributes of '
                                                         'unrelated entities are not yet known',
                                                         'A database disk full error',
                                                         'A primary key collision',
                                                         'A syntax error in INSERT INTO'],
                                             'question': 'What is an Insertion Anomaly?'},
                                            {'correct_answer': 'All attributes must contain atomic (indivisible) '
                                                               'values, and there are no repeating groups or arrays',
                                             'difficulty': 'Easy',
                                             'explanation': '1NF forbids multivalued attributes, comma-separated '
                                                            'lists, and repeating column sets.',
                                             'options': ['All attributes must contain atomic (indivisible) values, and '
                                                         'there are no repeating groups or arrays',
                                                         'Every column must be a primary key',
                                                         'The table must have at least 10 rows',
                                                         'All values must be positive integers'],
                                             'question': 'What is the fundamental requirement for a table to be in '
                                                         'First Normal Form (1NF)?'},
                                            {'correct_answer': 'It must be in 1NF and have NO partial functional '
                                                               'dependencies (all non-key attributes fully depend on '
                                                               'the entire primary key)',
                                             'difficulty': 'Easy',
                                             'explanation': '2NF eliminates dependencies on part of a composite '
                                                            'primary key.',
                                             'options': ['It must be in 1NF and have NO partial functional '
                                                         'dependencies (all non-key attributes fully depend on the '
                                                         'entire primary key)',
                                                         'It must have two primary keys',
                                                         'It must be joined with another table',
                                                         'It cannot contain text columns'],
                                             'question': 'What is the requirement for a table to be in Second Normal '
                                                         'Form (2NF)?'},
                                            {'correct_answer': 'No, partial dependencies can only exist when the '
                                                               'primary key is composite (multi-column)',
                                             'difficulty': 'Easy',
                                             'explanation': 'If the primary key is a single attribute, any dependency '
                                                            'on it is inherently full, satisfying 2NF automatically.',
                                             'options': ['No, partial dependencies can only exist when the primary key '
                                                         'is composite (multi-column)',
                                                         'Yes, in all tables',
                                                         'Only if the column is text',
                                                         'Only in foreign tables'],
                                             'question': 'Can partial functional dependencies exist in a table where '
                                                         'the primary key consists of a single column?'},
                                            {'correct_answer': 'It must be in 2NF and have NO transitive functional '
                                                               'dependencies (no non-key attribute depends on another '
                                                               'non-key attribute)',
                                             'difficulty': 'Easy',
                                             'explanation': '3NF ensures non-key attributes depend directly on the '
                                                            'primary key, and nothing but the primary key.',
                                             'options': ['It must be in 2NF and have NO transitive functional '
                                                         'dependencies (no non-key attribute depends on another '
                                                         'non-key attribute)',
                                                         'It must have exactly three tables',
                                                         'It must have three candidate keys',
                                                         'All columns must be numbers'],
                                             'question': 'What is the requirement for a table to be in Third Normal '
                                                         'Form (3NF)?'},
                                            {'correct_answer': 'When non-key attribute X determines non-key attribute '
                                                               'Y, while X depends on primary key PK (PK -> X -> Y)',
                                             'difficulty': 'Easy',
                                             'explanation': "Transitive dependencies create redundancy because Y's "
                                                            'value is repeated for every occurrence of X.',
                                             'options': ['When non-key attribute X determines non-key attribute Y, '
                                                         'while X depends on primary key PK (PK -> X -> Y)',
                                                         'A dependency between two different database servers',
                                                         'A foreign key that points to itself',
                                                         'A cyclic dependency in graphs'],
                                             'question': 'What is a Transitive Dependency?'},
                                            {'correct_answer': 'A stricter version of 3NF where for every functional '
                                                               'dependency X -> Y, X must be a super key',
                                             'difficulty': 'Medium',
                                             'explanation': 'BCNF handles edge cases in 3NF where non-super keys '
                                                            'determine parts of candidate keys.',
                                             'options': ['A stricter version of 3NF where for every functional '
                                                         'dependency X -> Y, X must be a super key',
                                                         'A normal form used exclusively for financial databases',
                                                         'A form requiring 4 tables',
                                                         'A form that forbids foreign keys'],
                                             'question': 'What is Boyce-Codd Normal Form (BCNF)?'},
                                            {'correct_answer': 'A constraint between two sets of attributes such that '
                                                               'whenever two tuples agree on attribute X, they must '
                                                               'also agree on attribute Y',
                                             'difficulty': 'Medium',
                                             'explanation': 'Functional dependencies state that the value of X '
                                                            'uniquely determines the value of Y.',
                                             'options': ['A constraint between two sets of attributes such that '
                                                         'whenever two tuples agree on attribute X, they must also '
                                                         'agree on attribute Y',
                                                         'A mathematical equation in SQL',
                                                         'A function that returns database tables',
                                                         'A procedure that runs on startup'],
                                             'question': 'What is a Functional Dependency (X -> Y)?'},
                                            {'correct_answer': 'A set of sound and complete inference rules '
                                                               '(Reflexivity, Augmentation, Transitivity) used to '
                                                               'derive all valid functional dependencies',
                                             'difficulty': 'Medium',
                                             'explanation': "Armstrong's axioms provide the formal foundation for "
                                                            'computing functional dependency closures.',
                                             'options': ['A set of sound and complete inference rules (Reflexivity, '
                                                         'Augmentation, Transitivity) used to derive all valid '
                                                         'functional dependencies',
                                                         'A set of guidelines for writing C++ code',
                                                         'Hardware rules for disk drives',
                                                         'Rules for naming database tables'],
                                             'question': "What is Armstrong's Axioms in functional dependency theory?"},
                                            {'correct_answer': 'A normal form that eliminates non-trivial Multi-Valued '
                                                               'Dependencies (MVDs) where independent 1:N facts are '
                                                               'packed in one table',
                                             'difficulty': 'Medium',
                                             'explanation': '4NF ensures independent multivalued facts (e.g. Employee '
                                                            'Skills and Employee Languages) are split into separate '
                                                            'tables.',
                                             'options': ['A normal form that eliminates non-trivial Multi-Valued '
                                                         'Dependencies (MVDs) where independent 1:N facts are packed '
                                                         'in one table',
                                                         'A normal form for 4D tables',
                                                         'A form requiring four candidate keys',
                                                         'A form that forbids NULLs completely'],
                                             'question': 'What is Fourth Normal Form (4NF)?'},
                                            {'correct_answer': 'A normal form dealing with cases where a table cannot '
                                                               'be decomposed into smaller tables without join '
                                                               'dependencies',
                                             'difficulty': 'Medium',
                                             'explanation': '5NF guarantees lossless reconstruction when schemas '
                                                            'require decomposition into three or more sub-relations.',
                                             'options': ['A normal form dealing with cases where a table cannot be '
                                                         'decomposed into smaller tables without join dependencies',
                                                         'A form for 5-table schemas',
                                                         'A form used in cloud computing',
                                                         'A deprecated standard'],
                                             'question': 'What is Fifth Normal Form (5NF / Project-Join Normal Form)?'},
                                            {'correct_answer': 'Intentionally introducing redundant data into '
                                                               'normalized schemas to reduce expensive joins and '
                                                               'optimize read query performance',
                                             'difficulty': 'Medium',
                                             'explanation': 'Read-heavy analytical workloads often denormalize schemas '
                                                            'to trade disk space for faster query execution.',
                                             'options': ['Intentionally introducing redundant data into normalized '
                                                         'schemas to reduce expensive joins and optimize read query '
                                                         'performance',
                                                         'Corrupting database schemas',
                                                         'Deleting foreign keys',
                                                         'Converting SQL to NoSQL'],
                                             'question': 'What is Denormalization and why is it used in production '
                                                         'systems?'},
                                            {'correct_answer': 'Faster read queries, but slower writes and increased '
                                                               'risk of data inconsistency and update anomalies',
                                             'difficulty': 'Medium',
                                             'explanation': 'Maintaining duplicated fields requires extra write '
                                                            'operations and careful transactional synchronization.',
                                             'options': ['Faster read queries, but slower writes and increased risk of '
                                                         'data inconsistency and update anomalies',
                                                         'Consumes less disk space',
                                                         'Disables all indexes',
                                                         'Prevents database backups'],
                                             'question': 'What is the trade-off of Denormalization?'},
                                            {'correct_answer': 'Decompose the table: move the partially dependent '
                                                               'attributes and the subset of the key they depend on '
                                                               'into a new separate table',
                                             'difficulty': 'Medium',
                                             'explanation': 'Extracting partial dependencies into dedicated relations '
                                                            'satisfies 2NF.',
                                             'options': ['Decompose the table: move the partially dependent attributes '
                                                         'and the subset of the key they depend on into a new separate '
                                                         'table',
                                                         'Delete the composite key',
                                                         'Make all columns primary keys',
                                                         'Convert all text to integers'],
                                             'question': 'How do you resolve a 2NF violation caused by a partial '
                                                         'dependency?'},
                                            {'correct_answer': 'Create a new table for (A, B) where A is primary key, '
                                                               'and keep A as a foreign key in the original table (PK, '
                                                               'A)',
                                             'difficulty': 'Medium',
                                             'explanation': 'Splitting transitive relationships removes duplicated '
                                                            'A-to-B mappings from the main table.',
                                             'options': ['Create a new table for (A, B) where A is primary key, and '
                                                         'keep A as a foreign key in the original table (PK, A)',
                                                         'Delete column B',
                                                         'Merge PK and B into one column',
                                                         'Drop the database table'],
                                             'question': 'How do you resolve a 3NF violation caused by a transitive '
                                                         'dependency (PK -> A -> B)?'},
                                            {'correct_answer': 'A minimal simplified set of functional dependencies '
                                                               'equivalent to the original set, with no extraneous '
                                                               'attributes or redundant dependencies',
                                             'difficulty': 'Medium',
                                             'explanation': 'Canonical covers provide the standard compact basis for '
                                                            '3NF and BCNF decomposition algorithms.',
                                             'options': ['A minimal simplified set of functional dependencies '
                                                         'equivalent to the original set, with no extraneous '
                                                         'attributes or redundant dependencies',
                                                         'A database backup header',
                                                         'A schema diagram',
                                                         'A cover index in B-Trees'],
                                             'question': 'What is Canonical Cover (Minimal Cover) of a set of '
                                                         'functional dependencies?'},
                                            {'correct_answer': '3NF guarantees both lossless join AND dependency '
                                                               'preservation; BCNF guarantees lossless join but may '
                                                               'lose cross-table dependencies',
                                             'difficulty': 'Hard',
                                             'explanation': 'In rare cases, preserving certain dependencies in BCNF '
                                                            'would re-introduce redundancy, requiring cross-table '
                                                            'assertion checks.',
                                             'options': ['3NF guarantees both lossless join AND dependency '
                                                         'preservation; BCNF guarantees lossless join but may lose '
                                                         'cross-table dependencies',
                                                         'BCNF cannot support candidate keys',
                                                         'BCNF is only theoretical and cannot be implemented',
                                                         '3NF always causes update anomalies'],
                                             'question': 'Why can BCNF decomposition sometimes fail to preserve '
                                                         'functional dependencies, unlike 3NF?'},
                                            {'correct_answer': 'Initialize closure = X; repeatedly add Y to closure if '
                                                               'W is a subset of closure and W -> Y is a functional '
                                                               'dependency until no changes occur',
                                             'difficulty': 'Hard',
                                             'explanation': 'Attribute closure determines all attributes determined by '
                                                            'X, taking polynomial time O(n * |F|).',
                                             'options': ['Initialize closure = X; repeatedly add Y to closure if W is '
                                                         'a subset of closure and W -> Y is a functional dependency '
                                                         'until no changes occur',
                                                         'Sort all attributes alphabetically',
                                                         'Calculate hash of all attributes',
                                                         'Traverse attributes using BFS'],
                                             'question': 'What is the algorithm to compute the Attribute Closure (X+) '
                                                         'of an attribute set under a set of functional dependencies?'},
                                            {'correct_answer': 'A formal algorithmic procedure used to test whether a '
                                                               'schema decomposition is lossless with respect to '
                                                               'functional or join dependencies',
                                             'difficulty': 'Hard',
                                             'explanation': 'The chase algorithm transforms an initial tableau using '
                                                            'dependencies to prove lossless reconstruction.',
                                             'options': ['A formal algorithmic procedure used to test whether a schema '
                                                         'decomposition is lossless with respect to functional or join '
                                                         'dependencies',
                                                         'A performance benchmark measuring query latency',
                                                         'A security penetration test',
                                                         'A deadlock resolution algorithm'],
                                             'question': 'What is the chase test in database theory?'},
                                            {'correct_answer': 'X determines a set of values for Y independently of '
                                                               'all other attributes, forcing Cartesian product '
                                                               'redundancy between independent multivalued attributes',
                                             'difficulty': 'Hard',
                                             'explanation': 'When an entity has two independent multi-valued facts, '
                                                            'mixing them in one table forces all combinations to be '
                                                            'stored.',
                                             'options': ['X determines a set of values for Y independently of all '
                                                         'other attributes, forcing Cartesian product redundancy '
                                                         'between independent multivalued attributes',
                                                         'X depends on multiple databases',
                                                         'X has multiple data types',
                                                         'X is a foreign key with multiple targets'],
                                             'question': 'What is a Multi-Valued Dependency (MVD: X ->-> Y) and how '
                                                         'does it violate 4NF?'},
                                            {'correct_answer': '6NF decomposes relations into irreducible binary '
                                                               'components containing only keys and one attribute; '
                                                               'primarily used in Temporal Databases and Anchor '
                                                               'Modeling',
                                             'difficulty': 'Hard',
                                             'explanation': '6NF simplifies temporal interval changes by isolating '
                                                            'individual attributes with their validity timestamps.',
                                             'options': ['6NF decomposes relations into irreducible binary components '
                                                         'containing only keys and one attribute; primarily used in '
                                                         'Temporal Databases and Anchor Modeling',
                                                         '6NF is for 6-core CPUs',
                                                         '6NF forbids all joins',
                                                         '6NF is used in flat text files'],
                                             'question': 'What is the difference between Sixth Normal Form (6NF) and '
                                                         '5NF, and where is 6NF used?'},
                                            {'correct_answer': 'Surrogate keys simplify joins and 2NF compliance, but '
                                                               'natural keys still require UNIQUE constraints to '
                                                               'prevent duplicate domain records',
                                             'difficulty': 'Hard',
                                             'explanation': 'Using surrogate IDs avoids composite keys but demands '
                                                            'unique constraints on business attributes.',
                                             'options': ['Surrogate keys simplify joins and 2NF compliance, but '
                                                         'natural keys still require UNIQUE constraints to prevent '
                                                         'duplicate domain records',
                                                         'Surrogate keys eliminate all database redundancy',
                                                         'Natural keys are forbidden in SQL',
                                                         'Surrogate keys prevent update anomalies automatically'],
                                             'question': 'How does Surrogate Key design (e.g. auto-increment ID / '
                                                         'UUID) affect normalization vs natural business keys?'},
                                            {'correct_answer': 'Analytical queries require fast aggregations over '
                                                               'millions of rows; 3NF requires dozens of complex joins '
                                                               'that stall analytical query engines',
                                             'difficulty': 'Hard',
                                             'explanation': 'OLAP favors denormalized dimension tables to minimize '
                                                            'join latency during massive table scans.',
                                             'options': ['Analytical queries require fast aggregations over millions '
                                                         'of rows; 3NF requires dozens of complex joins that stall '
                                                         'analytical query engines',
                                                         '3NF is illegal in data warehouses',
                                                         'Star schemas use less memory than 3NF',
                                                         'Snowflake schemas eliminate all primary keys'],
                                             'question': 'In analytical OLAP systems, why are data marts normalized '
                                                         'into Star/Snowflake schemas rather than 3NF transactional '
                                                         'schemas?'},
                                            {'correct_answer': 'Ensures that all functional dependencies in the '
                                                               'original schema can be verified within individual '
                                                               'decomposed tables without computing joins',
                                             'difficulty': 'Hard',
                                             'explanation': 'Dependency preservation ensures updates can be validated '
                                                            'locally in single tables without cross-table join '
                                                            'overhead.',
                                             'options': ['Ensures that all functional dependencies in the original '
                                                         'schema can be verified within individual decomposed tables '
                                                         'without computing joins',
                                                         'Ensures database files are saved to backup media',
                                                         'Ensures foreign keys are encrypted',
                                                         'Ensures primary keys are integers'],
                                             'question': 'What is Dependency Preservation in relational decomposition '
                                                         'and how is it verified?'},
                                            {'correct_answer': 'Testing if removing an attribute from the left-hand or '
                                                               'right-hand side of a dependency changes the overall '
                                                               'closure of F',
                                             'difficulty': 'Hard',
                                             'explanation': 'Removing extraneous attributes produces minimal, '
                                                            'irreducible functional dependency rules.',
                                             'options': ['Testing if removing an attribute from the left-hand or '
                                                         'right-hand side of a dependency changes the overall closure '
                                                         'of F',
                                                         'Deleting unused table columns',
                                                         'Removing null values from rows',
                                                         'Dropping unused indexes'],
                                             'question': 'What is Extraneous Attribute testing during minimal cover '
                                                         'derivation?'},
                                            {'correct_answer': 'Too many fragmented tables require excessive multi-way '
                                                               'JOINs, generating heavy CPU overhead, memory '
                                                               'allocations, and lock contention',
                                             'difficulty': 'Hard',
                                             'explanation': 'Fragmenting data across dozens of normalized tables '
                                                            'increases query latency and execution plan complexity.',
                                             'options': ['Too many fragmented tables require excessive multi-way '
                                                         'JOINs, generating heavy CPU overhead, memory allocations, '
                                                         'and lock contention',
                                                         'It deletes database records automatically',
                                                         'It disables write-ahead logging',
                                                         'It consumes all hard drive sectors'],
                                             'question': 'How does over-normalization degrade performance in '
                                                         'high-throughput transactional OLTP systems?'}],
 'Relational Model and Schemas': [{'correct_answer': 'The relational model representing data in two-dimensional tables '
                                                     'of rows and columns (relations)',
                                   'difficulty': 'Easy',
                                   'explanation': 'Proposed by E.F. Codd, the relational model organizes data into '
                                                  'relations (tables).',
                                   'options': ['The relational model representing data in two-dimensional tables of '
                                               'rows and columns (relations)',
                                               'A hierarchy of linked nodes',
                                               'A graph of vertices and edges',
                                               'Unstructured key-value text files'],
                                   'question': 'What is a relational database based on?'},
                                  {'correct_answer': 'A single row (record) in a relational table',
                                   'difficulty': 'Easy',
                                   'explanation': 'Each row in a table corresponds to an individual tuple of attribute '
                                                  'values.',
                                   'options': ['A single row (record) in a relational table',
                                               'A column header',
                                               'The database name',
                                               'A foreign key constraint'],
                                   'question': "In the relational model, what is a 'tuple'?"},
                                  {'correct_answer': 'A named column representing a characteristic or property of the '
                                                     'entity',
                                   'difficulty': 'Easy',
                                   'explanation': 'Attributes define the properties of the entities stored in a '
                                                  'relation.',
                                   'options': ['A named column representing a characteristic or property of the entity',
                                               'A row record',
                                               'A table index',
                                               'A user account'],
                                   'question': "In the relational model, what is an 'attribute'?"},
                                  {'correct_answer': 'The formal logical structure and blueprint defining tables, '
                                                     'columns, data types, and relationships',
                                   'difficulty': 'Easy',
                                   'explanation': 'A schema outlines the organization of tables, fields, constraints, '
                                                  'and relationships.',
                                   'options': ['The formal logical structure and blueprint defining tables, columns, '
                                               'data types, and relationships',
                                               'The physical hard disk sector layout',
                                               'The database administrative password',
                                               'A temporary table created during search'],
                                   'question': 'What is a database schema?'},
                                  {'correct_answer': 'A column (or set of columns) that uniquely identifies each row '
                                                     'in the table, cannot be null',
                                   'difficulty': 'Easy',
                                   'explanation': 'Primary keys enforce entity integrity by guaranteeing unique '
                                                  'identification of every row.',
                                   'options': ['A column (or set of columns) that uniquely identifies each row in the '
                                               'table, cannot be null',
                                               'A column containing numbers only',
                                               'The first column defined in the CREATE TABLE statement',
                                               'An optional password field'],
                                   'question': 'What is a Primary Key in a relational table?'},
                                  {'correct_answer': 'A column in one table that references the primary key of another '
                                                     'table, establishing a relationship',
                                   'difficulty': 'Easy',
                                   'explanation': 'Foreign keys link related records across tables and enforce '
                                                  'referential integrity.',
                                   'options': ['A column in one table that references the primary key of another '
                                               'table, establishing a relationship',
                                               'A key generated in a foreign country',
                                               'A key that can only store text',
                                               'A column with no constraints'],
                                   'question': 'What is a Foreign Key?'},
                                  {'correct_answer': 'No, primary key columns strictly prohibit NULL values',
                                   'difficulty': 'Easy',
                                   'explanation': 'Entity integrity mandates that primary key fields can never be '
                                                  'NULL.',
                                   'options': ['No, primary key columns strictly prohibit NULL values',
                                               'Yes, up to one NULL value is allowed',
                                               'Yes, if the table is empty',
                                               'Only in foreign tables'],
                                   'question': 'Can a Primary Key column contain NULL values in a relational '
                                               'database?'},
                                  {'correct_answer': 'The number of attributes (columns) in the relation',
                                   'difficulty': 'Easy',
                                   'explanation': 'Degree counts the attributes of the table relation.',
                                   'options': ['The number of attributes (columns) in the relation',
                                               'The number of tuples (rows)',
                                               'The size of the table in megabytes',
                                               'The number of foreign keys'],
                                   'question': 'What is the degree (or arity) of a relation in relational algebra?'},
                                  {'correct_answer': 'The number of tuples (rows) currently stored in the relation',
                                   'difficulty': 'Easy',
                                   'explanation': 'Cardinality denotes the row count of the relation at any given '
                                                  'moment.',
                                   'options': ['The number of tuples (rows) currently stored in the relation',
                                               'The number of columns',
                                               'The maximum allowed table size',
                                               'The number of indexes'],
                                   'question': 'What is the cardinality of a relation in relational algebra?'},
                                  {'correct_answer': 'The set of permissible atomic values that an attribute can hold',
                                   'difficulty': 'Easy',
                                   'explanation': 'Domains define data types and valid value bounds for attributes.',
                                   'options': ['The set of permissible atomic values that an attribute can hold',
                                               'The website address where database is hosted',
                                               'The operating system user group',
                                               'The physical storage folder'],
                                   'question': 'What does a domain refer to in relational database theory?'},
                                  {'correct_answer': 'A primary key composed of two or more columns that together '
                                                     'uniquely identify a record',
                                   'difficulty': 'Medium',
                                   'explanation': 'A composite primary key combines multiple attributes to establish '
                                                  'unique tuple identification.',
                                   'options': ['A primary key composed of two or more columns that together uniquely '
                                               'identify a record',
                                               'A key that combines numbers and text',
                                               'A key that references three different databases',
                                               'An encrypted primary key'],
                                   'question': 'What is a Composite Primary Key?'},
                                  {'correct_answer': 'Any minimal set of attributes that can uniquely identify a tuple '
                                                     'in a relation',
                                   'difficulty': 'Medium',
                                   'explanation': 'A table can have multiple candidate keys; one is selected as the '
                                                  'primary key.',
                                   'options': ['Any minimal set of attributes that can uniquely identify a tuple in a '
                                               'relation',
                                               'A key that might become foreign key',
                                               'A key with temporary values',
                                               'An auto-incrementing integer'],
                                   'question': 'What is a Candidate Key?'},
                                  {'correct_answer': 'A candidate key is a minimal super key with no redundant '
                                                     'attributes',
                                   'difficulty': 'Medium',
                                   'explanation': 'Super keys are any sets of attributes uniquely identifying rows; '
                                                  'candidate keys have no subsets that are super keys.',
                                   'options': ['A candidate key is a minimal super key with no redundant attributes',
                                               'A super key cannot contain primary keys',
                                               'They are identical in every way',
                                               'Candidate keys can contain nulls'],
                                   'question': 'What is the difference between a Candidate Key and a Super Key?'},
                                  {'correct_answer': 'The ability to modify physical storage schemas (indexing, disk '
                                                     'layout) without altering conceptual schemas',
                                   'difficulty': 'Medium',
                                   'explanation': 'Physical data independence isolates logical schema design from '
                                                  'physical disk arrangements.',
                                   'options': ['The ability to modify physical storage schemas (indexing, disk layout) '
                                               'without altering conceptual schemas',
                                               'Storing database on external USB drives',
                                               'Writing code without SQL',
                                               'Running databases without hardware'],
                                   'question': 'What is physical data independence in the ANSI/SPARC 3-tier database '
                                               'architecture?'},
                                  {'correct_answer': 'The ability to modify the conceptual schema without altering '
                                                     'external schemas (user views)',
                                   'difficulty': 'Medium',
                                   'explanation': 'External views remain stable even when conceptual tables or '
                                                  'relationships are adjusted.',
                                   'options': ['The ability to modify the conceptual schema without altering external '
                                               'schemas (user views)',
                                               'Running SQL queries without a CPU',
                                               'Backing up schemas to the cloud',
                                               'Changing programming languages'],
                                   'question': 'What is logical data independence?'},
                                  {'correct_answer': 'A candidate key that was not chosen as the primary key',
                                   'difficulty': 'Medium',
                                   'explanation': 'All candidate keys other than the primary key are termed alternate '
                                                  'keys.',
                                   'options': ['A candidate key that was not chosen as the primary key',
                                               'A foreign key pointing to an external database',
                                               'A secondary database password',
                                               'A backup column'],
                                   'question': 'What is an alternate key in relational database terminology?'},
                                  {'correct_answer': 'Selects a subset of specified columns (attributes) from a '
                                                     'relation, discarding duplicates',
                                   'difficulty': 'Medium',
                                   'explanation': 'Projection (π) filters vertical columns and removes duplicate '
                                                  'resulting tuples.',
                                   'options': ['Selects a subset of specified columns (attributes) from a relation, '
                                               'discarding duplicates',
                                               'Selects rows matching a condition',
                                               'Computes Cartesian product',
                                               'Renames columns'],
                                   'question': 'In relational algebra, what does the Projection operation (symbolized '
                                               'by Greek letter π) do?'},
                                  {'correct_answer': 'Filters rows (tuples) that satisfy a specified predicate '
                                                     'condition',
                                   'difficulty': 'Medium',
                                   'explanation': 'Selection (σ) filters horizontal rows based on boolean conditions.',
                                   'options': ['Filters rows (tuples) that satisfy a specified predicate condition',
                                               'Selects columns from the table',
                                               'Sorts table records',
                                               'Joins two tables'],
                                   'question': 'In relational algebra, what does the Selection operation (symbolized '
                                               'by Greek letter σ) do?'},
                                  {'correct_answer': 'A relation containing 200 rows with all combined attributes of R '
                                                     'and S',
                                   'difficulty': 'Medium',
                                   'explanation': 'Cartesian product pairs every tuple of R with every tuple of S, '
                                                  'yielding |R| * |S| rows.',
                                   'options': ['A relation containing 200 rows with all combined attributes of R and S',
                                               'A relation with 30 rows',
                                               'A relation with 10 rows',
                                               'An empty relation'],
                                   'question': 'What is the result of a Cartesian Product (Cross Join) between '
                                               'relation R (size 10 rows) and relation S (size 20 rows)?'},
                                  {'correct_answer': 'A virtual table defined by a stored SQL query that does not '
                                                     'physically store data itself (unless materialized)',
                                   'difficulty': 'Medium',
                                   'explanation': 'Standard views dynamically run their underlying query when '
                                                  'accessed, presenting tailored views.',
                                   'options': ['A virtual table defined by a stored SQL query that does not physically '
                                               'store data itself (unless materialized)',
                                               'A screenshot of database tables',
                                               'A physical copy of the database on disk',
                                               'A temporary table deleted after 5 seconds'],
                                   'question': 'What is a database view and what is its primary characteristic?'},
                                  {'correct_answer': 'All information in a relational database is represented '
                                                     'explicitly at the logical level in exactly one way: as values in '
                                                     'tables',
                                   'difficulty': 'Hard',
                                   'explanation': "Codd's fundamental rule mandates uniform representation of data and "
                                                  'metadata inside tables.',
                                   'options': ['All information in a relational database is represented explicitly at '
                                               'the logical level in exactly one way: as values in tables',
                                               'All data must be encrypted with 256-bit keys',
                                               'Databases must support SQL syntax',
                                               'Every database must have a root user'],
                                   'question': "What is Codd's Rule 1 (The Information Rule) in relational database "
                                               'theory?'},
                                  {'correct_answer': 'NULL values must be supported systematically to represent '
                                                     'missing or inapplicable information distinct from zero or empty '
                                                     'strings',
                                   'difficulty': 'Hard',
                                   'explanation': "Null represents 'unknown' or 'inapplicable' values consistently "
                                                  'across data types.',
                                   'options': ['NULL values must be supported systematically to represent missing or '
                                               'inapplicable information distinct from zero or empty strings',
                                               'NULL must be treated as integer 0',
                                               'NULL is forbidden in relational databases',
                                               'NULL must only appear in text columns'],
                                   'question': "What is Codd's Rule 3 (Systematic Treatment of Null Values)?"},
                                  {'correct_answer': 'Logical evaluations yield TRUE, FALSE, or UNKNOWN (e.g. NULL = '
                                                     'NULL evaluates to UNKNOWN, not TRUE)',
                                   'difficulty': 'Hard',
                                   'explanation': 'Comparisons involving NULL evaluate to UNKNOWN, requiring IS NULL '
                                                  'for testing.',
                                   'options': ['Logical evaluations yield TRUE, FALSE, or UNKNOWN (e.g. NULL = NULL '
                                               'evaluates to UNKNOWN, not TRUE)',
                                               'True, False, or Error',
                                               'Binary logic with floating point tolerances',
                                               'Quantum bit superposition'],
                                   'question': 'What is Three-Valued Logic (3VL) in the relational model due to NULL '
                                               'values?'},
                                  {'correct_answer': 'A materialized view stores the precomputed query result '
                                                     'physically on disk and must be refreshed when underlying data '
                                                     'changes',
                                   'difficulty': 'Hard',
                                   'explanation': 'Materialized views trade storage and refresh costs for ultra-fast '
                                                  'query execution on complex aggregations.',
                                   'options': ['A materialized view stores the precomputed query result physically on '
                                               'disk and must be refreshed when underlying data changes',
                                               'A materialized view cannot be queried with SELECT',
                                               'A materialized view deletes base tables',
                                               'Materialized views only exist in RAM'],
                                   'question': 'What is a Materialized View and how does it differ from a standard '
                                               'virtual view?'},
                                  {'correct_answer': 'A language is relationally complete if it can express any query '
                                                     'expressible in relational algebra or relational calculus',
                                   'difficulty': 'Hard',
                                   'explanation': 'Relational completeness benchmark ensures a query language provides '
                                                  'core relational operations.',
                                   'options': ['A language is relationally complete if it can express any query '
                                               'expressible in relational algebra or relational calculus',
                                               'A language that supports all SQL keywords',
                                               'A database that has zero NULL values',
                                               'A system that never crashes'],
                                   'question': 'What is relational completeness in query language evaluation?'},
                                  {'correct_answer': 'TRC variables range over tuples (rows); DRC variables range over '
                                                     'individual attribute domain values',
                                   'difficulty': 'Hard',
                                   'explanation': 'Both are non-procedural formalisms differing in variable binding '
                                                  'granularity.',
                                   'options': ['TRC variables range over tuples (rows); DRC variables range over '
                                               'individual attribute domain values',
                                               'TRC uses SQL; DRC uses C++',
                                               'TRC cannot express joins',
                                               'DRC is procedural; TRC is declarative'],
                                   'question': 'What is the difference between Tuple Relational Calculus (TRC) and '
                                               'Domain Relational Calculus (DRC)?'},
                                  {'correct_answer': 'Lossless-join guarantees natural join of decomposed relations '
                                                     'reconstructs the original relation without spurious tuples',
                                   'difficulty': 'Hard',
                                   'explanation': 'Lossless decomposition ensures no fake or extraneous records appear '
                                                  'upon recombining split tables.',
                                   'options': ['Lossless-join guarantees natural join of decomposed relations '
                                               'reconstructs the original relation without spurious tuples',
                                               'Lossless decomposition compresses table size by 50%',
                                               'Lossy decomposition is required for normalization',
                                               'Lossless decomposition only works with numbers'],
                                   'question': 'What is lossy vs lossless-join decomposition in relational schema '
                                               'design?'},
                                  {'correct_answer': 'Representing inheritance (e.g. Employee with subtypes '
                                                     'Hourly/Salaried) via single-table, class-per-table, or '
                                                     'shared-primary-key schemas',
                                   'difficulty': 'Hard',
                                   'explanation': 'EER inheritance models specialize common attributes in supertypes '
                                                  'while mapping subtypes cleanly.',
                                   'options': ['Representing inheritance (e.g. Employee with subtypes Hourly/Salaried) '
                                               'via single-table, class-per-table, or shared-primary-key schemas',
                                               'A hierarchy of database administrative roles',
                                               'A tree of foreign keys',
                                               'A master-slave database replication structure'],
                                   'question': 'What is an entity subtype and supertype hierarchy (EER model) and its '
                                               'translation to relational schemas?'},
                                  {'correct_answer': 'Altering column definitions, constraints, or table layouts on '
                                                     'live petabyte-scale databases without downtime or lock '
                                                     'contention',
                                   'difficulty': 'Hard',
                                   'explanation': 'Online DDL (e.g. pt-online-schema-change, gh-ost) mutates schemas '
                                                  'via shadow tables without locking writes.',
                                   'options': ['Altering column definitions, constraints, or table layouts on live '
                                               'petabyte-scale databases without downtime or lock contention',
                                               'Updating database software versions',
                                               'Migrating from SQL to NoSQL',
                                               'Changing database user passwords'],
                                   'question': 'What is schema evolution and how do forward/backward compatibility '
                                               'challenges manifest in production RDBMS?'},
                                  {'correct_answer': "Answering queries containing the universal quantifier 'FOR ALL' "
                                                     '(e.g., find students who enrolled in ALL courses)',
                                   'difficulty': 'Hard',
                                   'explanation': 'Division identifies tuples in R that match every corresponding '
                                                  'tuple in S.',
                                   'options': ["Answering queries containing the universal quantifier 'FOR ALL' (e.g., "
                                               'find students who enrolled in ALL courses)',
                                               'Dividing numerical values in columns',
                                               'Splitting a table into two equal parts',
                                               'Calculating average values'],
                                   'question': 'In relational algebra, what is the Division operation (R ÷ S) used '
                                               'for?'}],
 'SQL Joins and Relationships': [{'correct_answer': 'To combine columns from two or more tables based on a related '
                                                    'column between them',
                                  'difficulty': 'Easy',
                                  'explanation': 'JOIN clauses combine tuples from multiple tables sharing related '
                                                 'keys.',
                                  'options': ['To combine columns from two or more tables based on a related column '
                                              'between them',
                                              'To merge two database files into one',
                                              'To sort records alphabetically',
                                              'To delete duplicate records across tables'],
                                  'question': 'What is the purpose of an SQL JOIN operation?'},
                                 {'correct_answer': 'Only rows that have matching values in both joined tables',
                                  'difficulty': 'Easy',
                                  'explanation': 'INNER JOIN produces the intersection: records with corresponding '
                                                 'matches on both sides.',
                                  'options': ['Only rows that have matching values in both joined tables',
                                              'All rows from both tables regardless of match',
                                              'All rows from the left table and matching from the right',
                                              'Rows with NULL values only'],
                                  'question': 'What does an INNER JOIN return?'},
                                 {'correct_answer': 'All rows from the left table, plus matched rows from the right '
                                                    'table (NULLs for unmatched right rows)',
                                  'difficulty': 'Easy',
                                  'explanation': 'LEFT JOIN preserves all left table records, filling missing right '
                                                 'table attributes with NULL.',
                                  'options': ['All rows from the left table, plus matched rows from the right table '
                                              '(NULLs for unmatched right rows)',
                                              'All rows from the right table only',
                                              'Only matching rows from both tables',
                                              'All rows from both tables combined with duplicates'],
                                  'question': 'What does a LEFT (OUTER) JOIN return?'},
                                 {'correct_answer': 'All rows from the right table, plus matched rows from the left '
                                                    'table (NULLs for unmatched left rows)',
                                  'difficulty': 'Easy',
                                  'explanation': 'RIGHT JOIN preserves all right table records, filling missing left '
                                                 'table attributes with NULL.',
                                  'options': ['All rows from the right table, plus matched rows from the left table '
                                              '(NULLs for unmatched left rows)',
                                              'All rows from the left table only',
                                              'Only matching rows',
                                              'A Cartesian product'],
                                  'question': 'What does a RIGHT (OUTER) JOIN return?'},
                                 {'correct_answer': 'All rows when there is a match in either left or right table '
                                                    '(NULLs where either side lacks a match)',
                                  'difficulty': 'Easy',
                                  'explanation': 'FULL OUTER JOIN unions the left outer and right outer join results.',
                                  'options': ['All rows when there is a match in either left or right table (NULLs '
                                              'where either side lacks a match)',
                                              'Only rows that have matches in both tables',
                                              'A cross product of all rows',
                                              'An error in standard SQL'],
                                  'question': 'What does a FULL (OUTER) JOIN return?'},
                                 {'correct_answer': 'The Cartesian product of both tables (every row of table A paired '
                                                    'with every row of table B)',
                                  'difficulty': 'Easy',
                                  'explanation': 'CROSS JOIN multiplies all rows: |A| * |B| records without join '
                                                 'conditions.',
                                  'options': ['The Cartesian product of both tables (every row of table A paired with '
                                              'every row of table B)',
                                              'Only rows with identical primary keys',
                                              'An empty result set',
                                              'A table sorted by date'],
                                  'question': 'What does a CROSS JOIN produce?'},
                                 {'correct_answer': 'A regular join in which a table is joined with itself using '
                                                    'distinct table aliases',
                                  'difficulty': 'Easy',
                                  'explanation': 'Self-joins compare rows within the same table (e.g. '
                                                 'employee.manager_id = manager.employee_id).',
                                  'options': ['A regular join in which a table is joined with itself using distinct '
                                              'table aliases',
                                              'A join that runs automatically without a query',
                                              'A join that connects two identical databases',
                                              'A join on a primary key only'],
                                  'question': 'What is a Self-Join in SQL?'},
                                 {'correct_answer': 'ON (or USING)',
                                  'difficulty': 'Easy',
                                  'explanation': 'The ON clause defines the matching criteria linking joined tables.',
                                  'options': ['ON (or USING)', 'WHERE only', 'GROUP BY', 'HAVING'],
                                  'question': 'Which clause specifies the joining condition between two tables?'},
                                 {'correct_answer': 'ON specifies full equality expression (ON a.id = b.id); USING '
                                                    'specifies shared column name in parentheses (USING (id))',
                                  'difficulty': 'Easy',
                                  'explanation': 'USING(id) is a shorthand for ON a.id = b.id when both tables share '
                                                 'the identical column name.',
                                  'options': ['ON specifies full equality expression (ON a.id = b.id); USING specifies '
                                              'shared column name in parentheses (USING (id))',
                                              'ON is for inner joins; USING is for outer joins',
                                              'USING is deprecated in SQL',
                                              'They are identical in syntax'],
                                  'question': 'What is the difference between ON and USING in SQL joins?'},
                                 {'correct_answer': 'A join that automatically joins tables based on all columns '
                                                    'having identical names and data types in both tables',
                                  'difficulty': 'Easy',
                                  'explanation': 'Natural joins match on all common attribute names implicitly, though '
                                                 'risky if schemas evolve.',
                                  'options': ['A join that automatically joins tables based on all columns having '
                                              'identical names and data types in both tables',
                                              'A join that does not use memory',
                                              'A join on physical disk sectors',
                                              'A join created by nature'],
                                  'question': 'What is a Natural Join in SQL?'},
                                 {'correct_answer': 'Equi-join uses the equality operator (=) in the join condition; '
                                                    'non-equi-join uses comparison operators (<, >, BETWEEN)',
                                  'difficulty': 'Medium',
                                  'explanation': 'Non-equi-joins match on ranges or inequality predicates rather than '
                                                 'exact equality.',
                                  'options': ['Equi-join uses the equality operator (=) in the join condition; '
                                              'non-equi-join uses comparison operators (<, >, BETWEEN)',
                                              'Equi-join joins equal number of rows',
                                              'Non-equi-join cannot use indexes',
                                              'Equi-join is only between primary keys'],
                                  'question': 'What is an Equi-Join vs a Non-Equi-Join?'},
                                 {'correct_answer': "Perform a LEFT JOIN from A to B and add 'WHERE B.id IS NULL'",
                                  'difficulty': 'Medium',
                                  'explanation': 'An anti-join filters out matched rows by testing for NULL on the '
                                                 'preserved right-hand side.',
                                  'options': ["Perform a LEFT JOIN from A to B and add 'WHERE B.id IS NULL'",
                                              'Perform an INNER JOIN with != operator',
                                              'Use a CROSS JOIN with LIMIT 0',
                                              'Perform a RIGHT JOIN without ON clause'],
                                  'question': 'How do you find rows in Table A that have NO matching record in Table B '
                                              'using a JOIN?'},
                                 {'correct_answer': 'Returns rows from the first table that have at least one match in '
                                                    'the second table, without duplicating rows or returning second '
                                                    'table columns',
                                  'difficulty': 'Medium',
                                  'explanation': 'Semi-joins (often produced from EXISTS subqueries) return unique '
                                                 'left tuples with matching right records.',
                                  'options': ['Returns rows from the first table that have at least one match in the '
                                              'second table, without duplicating rows or returning second table '
                                              'columns',
                                              'A join that joins half of the rows',
                                              'A join that divides numbers by 2',
                                              'A join on partial strings'],
                                  'question': 'What is a Semi-Join in relational query processing?'},
                                 {'correct_answer': 'Returns rows from the first table that have NO matching rows in '
                                                    'the second table (e.g. NOT EXISTS)',
                                  'difficulty': 'Medium',
                                  'explanation': 'Anti-semi-joins select left records that lack any corresponding '
                                                 'match in the right table.',
                                  'options': ['Returns rows from the first table that have NO matching rows in the '
                                              'second table (e.g. NOT EXISTS)',
                                              'A join that deletes matching rows',
                                              'A join on negative numbers',
                                              'An invalid SQL query'],
                                  'question': 'What is an Anti-Semi-Join?'},
                                 {'correct_answer': 'Non-indexed joins require full table scans or temporary hash '
                                                    'tables; indexed joins use fast B-Tree index seeks',
                                  'difficulty': 'Medium',
                                  'explanation': 'Indexes allow the optimizer to perform index lookups on the inner '
                                                 'table for each outer row.',
                                  'options': ['Non-indexed joins require full table scans or temporary hash tables; '
                                              'indexed joins use fast B-Tree index seeks',
                                              'Non-indexed joins throw a runtime error',
                                              'Indexed joins return fewer rows',
                                              'Indexing has no effect on joins'],
                                  'question': 'What happens when joining two tables on a non-indexed column compared '
                                              'to an indexed column?'},
                                 {'correct_answer': 'One parent record relates to multiple child records; implemented '
                                                    "by placing parent's primary key as a foreign key in the child "
                                                    'table',
                                  'difficulty': 'Medium',
                                  'explanation': "The foreign key in the 'many' table points to the primary key of the "
                                                 "'one' table.",
                                  'options': ['One parent record relates to multiple child records; implemented by '
                                              "placing parent's primary key as a foreign key in the child table",
                                              'Both tables share identical primary keys',
                                              'A junction table is mandatory',
                                              'Implemented via multi-threading'],
                                  'question': 'What is a One-to-Many (1:N) relationship and how is it implemented in '
                                              'relational tables?'},
                                 {'correct_answer': 'Requires an associative bridge table (junction / link table) '
                                                    'containing foreign keys referencing both participating tables',
                                  'difficulty': 'Medium',
                                  'explanation': 'Junction tables break M:N relationships into two clean 1:N foreign '
                                                 'key associations.',
                                  'options': ['Requires an associative bridge table (junction / link table) containing '
                                              'foreign keys referencing both participating tables',
                                              'Implemented by storing comma-separated IDs in a single text column',
                                              'Implemented using multiple primary keys in one table',
                                              'M:N is forbidden in relational databases'],
                                  'question': 'What is a Many-to-Many (M:N) relationship and how is it implemented in '
                                              'relational databases?'},
                                 {'correct_answer': 'Placing a foreign key in either table with a UNIQUE constraint '
                                                    'placed on that foreign key column',
                                  'difficulty': 'Medium',
                                  'explanation': 'A UNIQUE constraint on the foreign key column restricts occurrences '
                                                 'to at most 1.',
                                  'options': ['Placing a foreign key in either table with a UNIQUE constraint placed '
                                              'on that foreign key column',
                                              'Using the same table name twice',
                                              'Using composite primary keys with 5 columns',
                                              'Setting table size limit to 1'],
                                  'question': 'What is a One-to-One (1:1) relationship and how is it enforced in '
                                              'relational schemas?'},
                                 {'correct_answer': 'It accidentally converts the LEFT JOIN into an INNER JOIN because '
                                                    'NULL rows fail the status = 1 filter',
                                  'difficulty': 'Medium',
                                  'explanation': 'Filtering the optional right table in WHERE discards rows where '
                                                 'b.status IS NULL; place it in the ON clause instead.',
                                  'options': ['It accidentally converts the LEFT JOIN into an INNER JOIN because NULL '
                                              'rows fail the status = 1 filter',
                                              'The query runs twice as fast',
                                              'The query syntax fails',
                                              'Unmatched rows are still returned with nulls'],
                                  'question': 'What happens if you filter a right-table column in the WHERE clause of '
                                              "a LEFT JOIN query (e.g. 'WHERE b.status = 1')?"},
                                 {'correct_answer': 'Allows a subquery or joined table on the right side to reference '
                                                    'columns provided by previous tables in the FROM clause',
                                  'difficulty': 'Medium',
                                  'explanation': 'LATERAL acts like a correlated subquery in the FROM clause, '
                                                 'executing per row of the left table.',
                                  'options': ['Allows a subquery or joined table on the right side to reference '
                                              'columns provided by previous tables in the FROM clause',
                                              'A join that sorts columns horizontally',
                                              'A join between two databases on different servers',
                                              'A join without foreign keys'],
                                  'question': 'What is a Lateral Join (LATERAL in PostgreSQL / CROSS APPLY in SQL '
                                              'Server)?'},
                                 {'correct_answer': 'Nested Loop Join, Hash Join, and Sort-Merge Join',
                                  'difficulty': 'Hard',
                                  'explanation': 'Query optimizers choose among Nested Loop, Hash, and Sort-Merge '
                                                 'joins based on cardinality, indexes, and sort order.',
                                  'options': ['Nested Loop Join, Hash Join, and Sort-Merge Join',
                                              'Bubble Join, Quick Join, Heap Join',
                                              'Linear Join, Binary Join, Tree Join',
                                              'Static Join, Dynamic Join, Virtual Join'],
                                  'question': 'What are the three core physical join algorithms implemented inside '
                                              'RDBMS query engines?'},
                                 {'correct_answer': 'When the outer table is small and the inner table has an index on '
                                                    'the join key (Index Nested Loop)',
                                  'difficulty': 'Hard',
                                  'explanation': 'Iterating over a few outer rows and seeking into an index on the '
                                                 'inner table is extremely fast.',
                                  'options': ['When the outer table is small and the inner table has an index on the '
                                              'join key (Index Nested Loop)',
                                              'When both tables have 100 million rows and no indexes',
                                              'When all columns are text',
                                              'When memory is exhausted'],
                                  'question': 'When does a query optimizer choose a Nested Loop Join?'},
                                 {'correct_answer': 'Builds an in-memory hash table on the smaller (build) input, then '
                                                    'streams through the larger (probe) input to match keys',
                                  'difficulty': 'Hard',
                                  'explanation': "Hash join requires enough memory to hold the build input's hash "
                                                 'table, running in O(N + M) time.',
                                  'options': ['Builds an in-memory hash table on the smaller (build) input, then '
                                              'streams through the larger (probe) input to match keys',
                                              'Sorts both tables and scans them linearly',
                                              'Compares all rows against all rows taking O(N^2)',
                                              'Requires zero memory by reading directly from tape'],
                                  'question': 'How does a Hash Join execute and what are its memory requirements?'},
                                 {'correct_answer': 'When both inputs are already sorted on the join key (e.g. from '
                                                    'B-Tree index scans) or when non-equi joins are performed',
                                  'difficulty': 'Hard',
                                  'explanation': 'Pre-sorted inputs merge in a single linear pass O(N + M) with '
                                                 'minimal memory overhead.',
                                  'options': ['When both inputs are already sorted on the join key (e.g. from B-Tree '
                                              'index scans) or when non-equi joins are performed',
                                              'When inputs are small unsorted tables',
                                              'When memory is unlimited',
                                              'When tables contain only UUIDs'],
                                  'question': 'When is a Sort-Merge Join superior to a Hash Join?'},
                                 {'correct_answer': 'It hashes both inputs into corresponding partition files on disk, '
                                                    'then performs independent hash joins on matching partition pairs',
                                  'difficulty': 'Hard',
                                  'explanation': 'Grace hash join breaks massive datasets into smaller disk-spilled '
                                                 'buckets that fit into memory one by one.',
                                  'options': ['It hashes both inputs into corresponding partition files on disk, then '
                                              'performs independent hash joins on matching partition pairs',
                                              'It aborts the query with an out of memory error',
                                              'It switches to an unindexed nested loop join',
                                              'It compresses the tables using gzip in memory'],
                                  'question': 'What is Grace Hash Join and how does it handle build inputs that exceed '
                                              'available RAM (work_mem)?'},
                                 {'correct_answer': 'A central fact table containing numerical measurements surrounded '
                                                    'by denormalized dimension tables, enabling fast star-joins',
                                  'difficulty': 'Hard',
                                  'explanation': 'Star schemas simplify complex reporting queries into single-level '
                                                 'joins between facts and dimensions.',
                                  'options': ['A central fact table containing numerical measurements surrounded by '
                                              'denormalized dimension tables, enabling fast star-joins',
                                              'A schema shaped like a circle',
                                              'A schema with no primary keys',
                                              'A schema where every table connects to every other table'],
                                  'question': 'What is a Star Schema in Data Warehousing and how does it optimize '
                                              'analytical joins?'},
                                 {'correct_answer': 'Dimension tables are normalized into sub-dimension hierarchies, '
                                                    'reducing redundancy at the cost of more joins',
                                  'difficulty': 'Hard',
                                  'explanation': 'Snowflake normalizes dimensions, trading storage efficiency for '
                                                 'additional join complexity.',
                                  'options': ['Dimension tables are normalized into sub-dimension hierarchies, '
                                              'reducing redundancy at the cost of more joins',
                                              'Snowflake tables are read-only',
                                              'Snowflake schemas store data in cold storage',
                                              'Snowflake schemas have no fact tables'],
                                  'question': 'What is a Snowflake Schema and how does it differ from a Star Schema?'},
                                 {'correct_answer': 'The search space of join order trees grows factorially ((2n-2)! / '
                                                    '(n-1)!), requiring Genetic Algorithms or dynamic programming '
                                                    '(System R) to find optimal plans',
                                  'difficulty': 'Hard',
                                  'explanation': 'Picking an inefficient join order can make a query run hours instead '
                                                 'of milliseconds.',
                                  'options': ['The search space of join order trees grows factorially ((2n-2)! / '
                                              '(n-1)!), requiring Genetic Algorithms or dynamic programming (System R) '
                                              'to find optimal plans',
                                              'Join order has zero impact on performance',
                                              'Tables are always joined in the exact order written in SQL',
                                              'The engine runs all possible join orders simultaneously'],
                                  'question': 'How does Join Order Selection impact query optimization in queries with '
                                              '10+ joined tables?'},
                                 {'correct_answer': 'The coordinator builds a compact Bloom filter of join keys from '
                                                    'one node and sends it to the other node to filter rows before '
                                                    'network transfer',
                                  'difficulty': 'Hard',
                                  'explanation': 'Bloom filters drastically reduce network traffic across distributed '
                                                 'database nodes by pre-filtering non-matching records.',
                                  'options': ['The coordinator builds a compact Bloom filter of join keys from one '
                                              'node and sends it to the other node to filter rows before network '
                                              'transfer',
                                              'A join that encrypts network traffic',
                                              'A join on flower catalog databases',
                                              'A join that runs in GPU memory'],
                                  'question': 'What is a Bloom Join (Distributed Hash Join Optimization)?'},
                                 {'correct_answer': 'The optimizer detects foreign key constraints and proves a joined '
                                                    'table contributes no columns or filters, removing the join '
                                                    'entirely from the plan',
                                  'difficulty': 'Hard',
                                  'explanation': 'If integrity constraints guarantee 1:1 match and joined columns are '
                                                 'unused, the optimizer prunes the join.',
                                  'options': ['The optimizer detects foreign key constraints and proves a joined table '
                                              'contributes no columns or filters, removing the join entirely from the '
                                              'plan',
                                              'Deleting tables from the database',
                                              'Removing the WHERE clause',
                                              'Banning joins in production'],
                                  'question': 'What is Join Elimination in advanced SQL query optimizers?'}],
 'Subqueries and Nested Queries': [{'correct_answer': 'A query nested inside another SELECT, INSERT, UPDATE, or DELETE '
                                                      'statement enclosed in parentheses',
                                    'difficulty': 'Easy',
                                    'explanation': 'Subqueries pass their results to an outer enclosing statement.',
                                    'options': ['A query nested inside another SELECT, INSERT, UPDATE, or DELETE '
                                                'statement enclosed in parentheses',
                                                'A query running on a secondary computer',
                                                'A temporary database table',
                                                'An SQL syntax error'],
                                    'question': 'What is a subquery in SQL?'},
                                   {'correct_answer': 'A subquery that returns exactly one single value (one row and '
                                                      'one column)',
                                    'difficulty': 'Easy',
                                    'explanation': 'Scalar subqueries evaluate to a single atomic value usable '
                                                   'wherever an expression is allowed.',
                                    'options': ['A subquery that returns exactly one single value (one row and one '
                                                'column)',
                                                'A subquery that returns a whole table',
                                                'A subquery that cannot contain numbers',
                                                'A subquery running in parallel'],
                                    'question': 'What is a scalar subquery?'},
                                   {'correct_answer': 'In the SELECT list, FROM clause, WHERE clause, and HAVING '
                                                      'clause',
                                    'difficulty': 'Easy',
                                    'explanation': 'SQL allows nested subqueries in almost any query clause.',
                                    'options': ['In the SELECT list, FROM clause, WHERE clause, and HAVING clause',
                                                'Only in the WHERE clause',
                                                'Only in the FROM clause',
                                                'Only in the ORDER BY clause'],
                                    'question': 'Where can a subquery appear in a SQL SELECT statement?'},
                                   {'correct_answer': 'A subquery located in the FROM clause that acts as a temporary '
                                                      'virtual table for the outer query',
                                    'difficulty': 'Easy',
                                    'explanation': 'Subqueries in the FROM clause are treated as derived tables and '
                                                   'require a table alias.',
                                    'options': ['A subquery located in the FROM clause that acts as a temporary '
                                                'virtual table for the outer query',
                                                'A view saved permanently in the catalog',
                                                'A view visible to the public internet',
                                                'A screenshot of a query result'],
                                    'question': 'What is an inline view (derived table)?'},
                                   {'correct_answer': 'EXISTS',
                                    'difficulty': 'Easy',
                                    'explanation': 'EXISTS returns TRUE if the subquery returns at least one row, '
                                                   'stopping evaluation immediately.',
                                    'options': ['EXISTS', 'IN', 'BETWEEN', 'LIKE'],
                                    'question': 'Which operator tests if a subquery returns ANY rows at all?'},
                                   {'correct_answer': 'TRUE',
                                    'difficulty': 'Easy',
                                    'explanation': 'NOT EXISTS evaluates to TRUE when the nested query produces zero '
                                                   'matching rows.',
                                    'options': ['TRUE', 'FALSE', 'NULL', 'UNKNOWN'],
                                    'question': "What does 'NOT EXISTS' evaluate to when the subquery returns an empty "
                                                'result set?'},
                                   {'correct_answer': 'A subquery that references one or more columns from the outer '
                                                      'query and must be evaluated for each outer row',
                                    'difficulty': 'Easy',
                                    'explanation': 'Correlated subqueries depend on values supplied dynamically by the '
                                                   'enclosing row.',
                                    'options': ['A subquery that references one or more columns from the outer query '
                                                'and must be evaluated for each outer row',
                                                'A subquery that runs on a separate database',
                                                'A subquery that does not use parentheses',
                                                'A subquery that contains no WHERE clause'],
                                    'question': 'What is a correlated subquery?'},
                                   {'correct_answer': '> ANY (or > SOME)',
                                    'difficulty': 'Easy',
                                    'explanation': 'col > ANY (subquery) is TRUE if col is greater than the smallest '
                                                   'value in the subquery result.',
                                    'options': ['> ANY (or > SOME)', '> ALL', '> MAX', '> IN'],
                                    'question': 'Which operator tests whether a value is greater than AT LEAST ONE '
                                                'value returned by a subquery?'},
                                   {'correct_answer': '> ALL',
                                    'difficulty': 'Easy',
                                    'explanation': 'col > ALL (subquery) is TRUE only if col exceeds the maximum value '
                                                   'in the subquery result.',
                                    'options': ['> ALL', '> ANY', '> SOME', '> IN'],
                                    'question': 'Which operator tests whether a value is greater than EVERY value '
                                                'returned by a subquery?'},
                                   {'correct_answer': 'A runtime execution error is thrown (e.g. Subquery returned '
                                                      'more than 1 value)',
                                    'difficulty': 'Easy',
                                    'explanation': 'Scalar contexts require strictly <= 1 row; returning multiple rows '
                                                   'violates the scalar contract.',
                                    'options': ['A runtime execution error is thrown (e.g. Subquery returned more than '
                                                '1 value)',
                                                'The engine selects the first row silently',
                                                'The engine averages the rows',
                                                'The query returns NULL'],
                                    'question': 'What happens if a scalar subquery in a SELECT list returns MORE THAN '
                                                'ONE row at runtime?'},
                                   {'correct_answer': 'A named temporary result set defined using the WITH clause that '
                                                      'can be referenced within the main query',
                                    'difficulty': 'Medium',
                                    'explanation': 'CTEs (WITH name AS (SELECT ...)) improve query modularity and '
                                                   'readability over nested subqueries.',
                                    'options': ['A named temporary result set defined using the WITH clause that can '
                                                'be referenced within the main query',
                                                'A permanent database table shared by all users',
                                                'A table stored in RAM only',
                                                'A table created by compilers'],
                                    'question': 'What is a Common Table Expression (CTE) in SQL?'},
                                   {'correct_answer': 'A CTE that references itself to traverse hierarchical or '
                                                      'tree-structured data (e.g., org charts, bill of materials)',
                                    'difficulty': 'Medium',
                                    'explanation': 'Recursive CTEs have an anchor member and a recursive member '
                                                   'unioned together to traverse graphs.',
                                    'options': ['A CTE that references itself to traverse hierarchical or '
                                                'tree-structured data (e.g., org charts, bill of materials)',
                                                'A CTE that causes an infinite loop and crashes',
                                                'A CTE that deletes rows recursively',
                                                'A CTE used only for calculating factorials'],
                                    'question': 'What is a Recursive CTE and what is its primary use case?'},
                                   {'correct_answer': 'The optimizer converts a subquery into an equivalent JOIN or '
                                                      'semi-join to explore more efficient join orderings',
                                    'difficulty': 'Medium',
                                    'explanation': 'Unnesting allows the optimizer to apply index lookups and join '
                                                   'algorithms rather than running nested loops.',
                                    'options': ['The optimizer converts a subquery into an equivalent JOIN or '
                                                'semi-join to explore more efficient join orderings',
                                                'Flattening multidimensional arrays',
                                                'Deleting subqueries from queries',
                                                'Converting SQL to JSON'],
                                    'question': 'What is Subquery Unnesting / Flattening in query optimization?'},
                                   {'correct_answer': "If the subquery returns even a single NULL, 'col NOT IN "
                                                      "(subquery)' evaluates to UNKNOWN/FALSE for all rows, returning "
                                                      'empty set',
                                    'difficulty': 'Medium',
                                    'explanation': 'In 3VL, comparing against NULL yields UNKNOWN; NOT (UNKNOWN) is '
                                                   'UNKNOWN, discarding all rows.',
                                    'options': ["If the subquery returns even a single NULL, 'col NOT IN (subquery)' "
                                                'evaluates to UNKNOWN/FALSE for all rows, returning empty set',
                                                'It causes database crashes',
                                                'It deletes NULL rows from the table',
                                                'It changes NULL to zero'],
                                    'question': "Why is 'NOT IN' with a subquery dangerous when the subquery can "
                                                'return NULL values?'},
                                   {'correct_answer': 'NOT EXISTS is immune to NULL value traps and can short-circuit '
                                                      'upon finding the first match using indexes',
                                    'difficulty': 'Medium',
                                    'explanation': 'NOT EXISTS evaluates existence rather than value matching, '
                                                   'avoiding 3VL null pitfalls.',
                                    'options': ['NOT EXISTS is immune to NULL value traps and can short-circuit upon '
                                                'finding the first match using indexes',
                                                'NOT EXISTS uses less memory',
                                                'NOT IN is deprecated in SQL',
                                                'NOT EXISTS works on unindexed tables only'],
                                    'question': "Why is 'NOT EXISTS' safer and often faster than 'NOT IN' when "
                                                'checking for missing child records?'},
                                   {'correct_answer': 'Yes, subqueries can provide computed update values in SET or '
                                                      'filter target rows in WHERE',
                                    'difficulty': 'Medium',
                                    'explanation': 'Subqueries are frequently used in UPDATE statements to pull values '
                                                   'from related tables.',
                                    'options': ['Yes, subqueries can provide computed update values in SET or filter '
                                                'target rows in WHERE',
                                                'No, subqueries are forbidden in UPDATE statements',
                                                'Only in the WHERE clause',
                                                'Only in MySQL'],
                                    'question': 'Can an UPDATE statement contain a subquery in its SET clause or WHERE '
                                                'clause?'},
                                   {'correct_answer': 'An independent subquery executes once and its result is cached; '
                                                      'a correlated subquery conceptually executes once per outer row',
                                    'difficulty': 'Medium',
                                    'explanation': 'Independent subqueries evaluate as constants; correlated '
                                                   'subqueries require parameters from outer rows.',
                                    'options': ['An independent subquery executes once and its result is cached; a '
                                                'correlated subquery conceptually executes once per outer row',
                                                'Independent subqueries run on different servers',
                                                'Correlated subqueries cannot use indexes',
                                                'There is no execution difference'],
                                    'question': 'What is the difference between an independent (non-correlated) '
                                                'subquery and a correlated subquery in terms of execution?'},
                                   {'correct_answer': 'SELECT MAX(salary) FROM employees WHERE salary < (SELECT '
                                                      'MAX(salary) FROM employees)',
                                    'difficulty': 'Medium',
                                    'explanation': 'Filtering out the absolute maximum allows the inner subquery to '
                                                   'identify the second highest value.',
                                    'options': ['SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) '
                                                'FROM employees)',
                                                'SELECT salary FROM employees ORDER BY salary LIMIT 2',
                                                'SELECT MIN(salary) FROM employees',
                                                'SELECT salary / 2 FROM employees'],
                                    'question': 'How can you write a query to find the employee with the second '
                                                'highest salary using a subquery?'},
                                   {'correct_answer': 'When the recursive member returns an empty result set (zero '
                                                      'rows)',
                                    'difficulty': 'Medium',
                                    'explanation': 'Recursive execution loops until the recursive query produces zero '
                                                   'new rows to add.',
                                    'options': ['When the recursive member returns an empty result set (zero rows)',
                                                'A LIMIT 10 clause',
                                                'When memory is exhausted',
                                                'A timeout timer'],
                                    'question': 'In a Recursive CTE, what terminates the recursion?'},
                                   {'correct_answer': 'Yes, PostgreSQL allows WITH queries to perform DML and return '
                                                      'results via RETURNING to the main query',
                                    'difficulty': 'Medium',
                                    'explanation': 'Writable CTEs allow chaining mutations (e.g. moving rows between '
                                                   'tables) in a single atomic transaction.',
                                    'options': ['Yes, PostgreSQL allows WITH queries to perform DML and return results '
                                                'via RETURNING to the main query',
                                                'No, CTEs are strictly read-only in all databases',
                                                'Only in Oracle',
                                                'Only on temporary tables'],
                                    'question': 'Can a CTE be modified using INSERT, UPDATE, or DELETE in PostgreSQL '
                                                '(Data-Modifying CTE)?'},
                                   {'correct_answer': 'Transforming complex correlated subqueries with aggregations '
                                                      'into joins with GROUP BY over correlation keys',
                                    'difficulty': 'Hard',
                                    'explanation': 'Decorrelation allows cost-based optimizers to avoid quadratic '
                                                   'nested loop execution.',
                                    'options': ['Transforming complex correlated subqueries with aggregations into '
                                                'joins with GROUP BY over correlation keys',
                                                'Deleting correlated subqueries',
                                                'Converting SQL into C++ code',
                                                'Running subqueries in isolated transactions'],
                                    'question': 'What is Subquery Decorrelation (Magic Decorrelation) in advanced '
                                                'database query optimizers?'},
                                   {'correct_answer': 'Materialized CTE acts as an optimization fence (computed once, '
                                                      'stored in memory); Non-materialized is inlined into the main '
                                                      'query plan',
                                    'difficulty': 'Hard',
                                    'explanation': 'PostgreSQL 12 allows the optimizer to inline CTEs by default '
                                                   'unless explicitly marked AS MATERIALIZED.',
                                    'options': ['Materialized CTE acts as an optimization fence (computed once, stored '
                                                'in memory); Non-materialized is inlined into the main query plan',
                                                'Materialized CTE is written to disk permanently',
                                                'Non-materialized CTE is deleted after compilation',
                                                'Materialized CTE cannot contain joins'],
                                    'question': 'What is a Materialized vs Non-Materialized CTE in query planning '
                                                '(e.g. PostgreSQL 12+ AS MATERIALIZED)?'},
                                   {'correct_answer': 'Pushes outer WHERE filter predicates into the subquery or view '
                                                      'before aggregation/joins are executed',
                                    'difficulty': 'Hard',
                                    'explanation': 'Predicate pushdown drastically reduces the intermediate row count '
                                                   'processed by subqueries.',
                                    'options': ['Pushes outer WHERE filter predicates into the subquery or view before '
                                                'aggregation/joins are executed',
                                                'Moves subqueries to background threads',
                                                'Pushes subqueries to client browsers',
                                                'Delays subquery execution until commit'],
                                    'question': 'How does Subquery Pushdown optimize query execution plans?'},
                                   {'correct_answer': 'col = ANY (empty) is FALSE; col = ALL (empty) is vacuously TRUE '
                                                      'for all values',
                                    'difficulty': 'Hard',
                                    'explanation': 'By mathematical logic, a condition holds for ALL elements of an '
                                                   'empty set vacuously.',
                                    'options': ['col = ANY (empty) is FALSE; col = ALL (empty) is vacuously TRUE for '
                                                'all values',
                                                'Both are NULL',
                                                'Both are FALSE',
                                                'Both throw runtime exceptions'],
                                    'question': 'What is the operational difference between ALL and ANY when applied '
                                                'to an empty subquery result set?'},
                                   {'correct_answer': 'The inner table evaluates as a parameterized loop per outer row '
                                                      '(like nested loop), but can use outer column values in index '
                                                      'scans',
                                    'difficulty': 'Hard',
                                    'explanation': 'LATERAL passes outer values into the inner subquery, enabling '
                                                   'index-driven sub-computations per row.',
                                    'options': ['The inner table evaluates as a parameterized loop per outer row (like '
                                                'nested loop), but can use outer column values in index scans',
                                                'It executes once globally',
                                                'It runs using hash joins exclusively',
                                                'It uses map-reduce on disk'],
                                    'question': 'What is Lateral Derived Table correlation and how does the optimizer '
                                                'execute it?'},
                                   {'correct_answer': 'It treats (a, b) as a composite tuple, performing a '
                                                      'multi-column semi-join or hashing multi-column keys',
                                    'difficulty': 'Hard',
                                    'explanation': 'Tuple comparisons evaluate multi-attribute equality atomically via '
                                                   'hash or index lookups.',
                                    'options': ['It treats (a, b) as a composite tuple, performing a multi-column '
                                                'semi-join or hashing multi-column keys',
                                                'It concatenates a and b as strings',
                                                'It converts the query to two independent subqueries',
                                                'Row value constructors are invalid SQL'],
                                    'question': "How does the optimizer handle 'WHERE (a, b) IN (SELECT x, y FROM "
                                                "...)' (Row Value Constructors)?"},
                                   {'correct_answer': 'By tracking an array of visited node IDs (e.g. '
                                                      "array_append(path, node_id)) and adding 'WHERE NOT (node_id = "
                                                      "ANY(path))'",
                                    'difficulty': 'Hard',
                                    'explanation': 'Accumulating the traversal path in an array allows cycle detection '
                                                   'to terminate looping branches.',
                                    'options': ['By tracking an array of visited node IDs (e.g. array_append(path, '
                                                "node_id)) and adding 'WHERE NOT (node_id = ANY(path))'",
                                                'By limiting query execution to 1 second',
                                                'By removing cycles from the database',
                                                'By setting database isolation to SERIALIZABLE'],
                                    'question': 'In recursive graph queries, how do you prevent infinite loops in '
                                                'cyclic graphs using Recursive CTEs?'},
                                   {'correct_answer': 'Scalar subquery cache memorizes the output of correlated '
                                                      'subqueries for recent input parameter values within the same '
                                                      'query execution',
                                    'difficulty': 'Hard',
                                    'explanation': 'Caching identical parameter calls avoids re-evaluating the '
                                                   'subquery for duplicate outer rows.',
                                    'options': ['Scalar subquery cache memorizes the output of correlated subqueries '
                                                'for recent input parameter values within the same query execution',
                                                'It caches the query text in RAM',
                                                'It caches the entire database',
                                                'It saves queries to disk files'],
                                    'question': 'What is the difference between a scalar subquery cache in '
                                                'Oracle/PostgreSQL and query result caching?'},
                                   {'correct_answer': 'Window functions in subqueries can be filtered by WHERE in the '
                                                      'outer query (e.g. WHERE rn <= 3), which is illegal in the '
                                                      'declaring query',
                                    'difficulty': 'Hard',
                                    'explanation': 'Because WHERE runs before window functions, filtering on window '
                                                   'results requires a subquery or CTE.',
                                    'options': ['Window functions in subqueries can be filtered by WHERE in the outer '
                                                'query (e.g. WHERE rn <= 3), which is illegal in the declaring query',
                                                'Window functions cannot be placed inside subqueries',
                                                'It runs 10x slower',
                                                'It changes the result values to NULL'],
                                    'question': 'What is a Window Function applied inside a subquery vs in the outer '
                                                'query?'},
                                   {'correct_answer': 'Converts EXISTS/IN subqueries into DISTINCT semi-joins, '
                                                      'removing redundant work once the first matching tuple is '
                                                      'located',
                                    'difficulty': 'Hard',
                                    'explanation': 'Semi-join transforms short-circuit on the first match, avoiding '
                                                   'full nested subquery scans.',
                                    'options': ['Converts EXISTS/IN subqueries into DISTINCT semi-joins, removing '
                                                'redundant work once the first matching tuple is located',
                                                'Duplicates all rows',
                                                'Reverses table scan directions',
                                                'Converts queries into recursive procedures'],
                                    'question': 'How does query unrolling handle existential quantification in '
                                                'quantified subqueries?'}],
 'Transactions and ACID Properties': [{'correct_answer': 'A logical unit of work consisting of one or more SQL '
                                                         'operations executed as a single indivisible operation',
                                       'difficulty': 'Easy',
                                       'explanation': 'A transaction bundles operations so that either all succeed or '
                                                      'all fail together.',
                                       'options': ['A logical unit of work consisting of one or more SQL operations '
                                                   'executed as a single indivisible operation',
                                                   'A monetary payment between users',
                                                   'A backup of table records',
                                                   'A connection to a remote database'],
                                       'question': 'What is a database transaction?'},
                                      {'correct_answer': 'Atomicity',
                                       'difficulty': 'Easy',
                                       'explanation': "Atomicity guarantees 'all-or-nothing' execution for all "
                                                      'operations in the transaction.',
                                       'options': ['Atomicity', 'Availability', 'Accuracy', 'Authentication'],
                                       'question': "What does the 'A' in ACID properties stand for?"},
                                      {'correct_answer': 'Consistency',
                                       'difficulty': 'Easy',
                                       'explanation': 'Consistency ensures that a transaction transforms the database '
                                                      'from one valid state to another.',
                                       'options': ['Consistency', 'Concurrency', 'Capacity', 'Compatibility'],
                                       'question': "What does the 'C' in ACID properties stand for?"},
                                      {'correct_answer': 'Isolation',
                                       'difficulty': 'Easy',
                                       'explanation': 'Isolation guarantees that concurrent transactions execute '
                                                      'without interfering with one another.',
                                       'options': ['Isolation', 'Integrity', 'Indexing', 'Interoperability'],
                                       'question': "What does the 'I' in ACID properties stand for?"},
                                      {'correct_answer': 'Durability',
                                       'difficulty': 'Easy',
                                       'explanation': 'Durability ensures committed changes survive permanent system '
                                                      'crashes and power failures.',
                                       'options': ['Durability', 'Decoupling', 'Distribution', 'Dependability'],
                                       'question': "What does the 'D' in ACID properties stand for?"},
                                      {'correct_answer': 'COMMIT',
                                       'difficulty': 'Easy',
                                       'explanation': 'COMMIT finalizes changes and makes them visible to other '
                                                      'transactions permanently.',
                                       'options': ['COMMIT', 'SAVE', 'STORE', 'APPLY'],
                                       'question': 'Which SQL statement saves all transaction changes permanently to '
                                                   'the database?'},
                                      {'correct_answer': 'ROLLBACK',
                                       'difficulty': 'Easy',
                                       'explanation': 'ROLLBACK aborts the transaction and restores data to the '
                                                      'pre-transaction state.',
                                       'options': ['ROLLBACK', 'UNDO', 'REVERT', 'DISCARD'],
                                       'question': 'Which SQL statement undoes all uncommitted changes made in the '
                                                   'current transaction?'},
                                      {'correct_answer': 'A marker within a transaction allowing partial rollback to '
                                                         'that specific point without aborting the entire transaction',
                                       'difficulty': 'Easy',
                                       'explanation': 'SAVEPOINT name and ROLLBACK TO name permit granular '
                                                      'sub-transaction recovery.',
                                       'options': ['A marker within a transaction allowing partial rollback to that '
                                                   'specific point without aborting the entire transaction',
                                                   'A snapshot of the entire hard drive',
                                                   'A cloud backup schedule',
                                                   'A permanent database commit'],
                                       'question': 'What is a Savepoint in SQL transactions?'},
                                      {'correct_answer': 'A transaction reads uncommitted data written by another '
                                                         'concurrent transaction that might later be rolled back',
                                       'difficulty': 'Easy',
                                       'explanation': 'Dirty reads expose uncommitted, temporary state that may '
                                                      'subsequently be discarded.',
                                       'options': ['A transaction reads uncommitted data written by another concurrent '
                                                   'transaction that might later be rolled back',
                                                   'Reading corrupted hard drive sectors',
                                                   'Reading data over an unencrypted connection',
                                                   'Reading deleted files'],
                                       'question': 'What is a Dirty Read phenomenon in database concurrency?'},
                                      {'correct_answer': 'A transaction re-reads the same row and discovers that its '
                                                         'data has been modified by another committed transaction',
                                       'difficulty': 'Easy',
                                       'explanation': 'Non-repeatable reads occur when committed updates alter row '
                                                      'values between consecutive reads.',
                                       'options': ['A transaction re-reads the same row and discovers that its data '
                                                   'has been modified by another committed transaction',
                                                   'A query that fails to execute twice',
                                                   'A query that returns random data',
                                                   'A hard drive read error'],
                                       'question': 'What is a Non-Repeatable Read (Fuzzy Read)?'},
                                      {'correct_answer': 'A transaction re-executes a range query and discovers new '
                                                         "'phantom' rows inserted or deleted by another committed "
                                                         'transaction',
                                       'difficulty': 'Medium',
                                       'explanation': 'Phantom reads affect range queries when newly committed tuples '
                                                      'satisfy the search predicate.',
                                       'options': ['A transaction re-executes a range query and discovers new '
                                                   "'phantom' rows inserted or deleted by another committed "
                                                   'transaction',
                                                   'A ghost record in memory',
                                                   'A deleted table appearing in catalog',
                                                   'A hardware glitch in RAM'],
                                       'question': 'What is a Phantom Read phenomenon?'},
                                      {'correct_answer': 'READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, '
                                                         'SERIALIZABLE',
                                       'difficulty': 'Medium',
                                       'explanation': 'ANSI SQL defines 4 isolation levels balancing concurrency '
                                                      'throughput against isolation anomalies.',
                                       'options': ['READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE',
                                                   'LOW, MEDIUM, HIGH, MAXIMUM',
                                                   'SNAPSHOT, ISOLATED, SHARED, EXCLUSIVE',
                                                   'LEVEL 1, LEVEL 2, LEVEL 3, LEVEL 4'],
                                       'question': 'What are the four standard ANSI SQL transaction isolation levels '
                                                   'in order from least to most strict?'},
                                      {'correct_answer': 'READ UNCOMMITTED',
                                       'difficulty': 'Medium',
                                       'explanation': 'READ UNCOMMITTED allows reading dirty, uncommitted rows from '
                                                      'active transactions.',
                                       'options': ['READ UNCOMMITTED',
                                                   'READ COMMITTED',
                                                   'REPEATABLE READ',
                                                   'SERIALIZABLE'],
                                       'question': 'Which isolation level permits Dirty Reads?'},
                                      {'correct_answer': 'READ COMMITTED',
                                       'difficulty': 'Medium',
                                       'explanation': 'READ COMMITTED guarantees that queries only see data committed '
                                                      'before the query began.',
                                       'options': ['READ COMMITTED',
                                                   'READ UNCOMMITTED',
                                                   'REPEATABLE READ',
                                                   'SERIALIZABLE'],
                                       'question': 'What is the default transaction isolation level in PostgreSQL and '
                                                   'Oracle?'},
                                      {'correct_answer': 'REPEATABLE READ',
                                       'difficulty': 'Medium',
                                       'explanation': 'MySQL InnoDB defaults to REPEATABLE READ using MVCC and '
                                                      'next-key locking.',
                                       'options': ['REPEATABLE READ',
                                                   'READ COMMITTED',
                                                   'SERIALIZABLE',
                                                   'READ UNCOMMITTED'],
                                       'question': 'What is the default transaction isolation level in MySQL InnoDB?'},
                                      {'correct_answer': 'SERIALIZABLE',
                                       'difficulty': 'Medium',
                                       'explanation': 'SERIALIZABLE guarantees that execution produces results '
                                                      'identical to some serial ordering.',
                                       'options': ['SERIALIZABLE',
                                                   'REPEATABLE READ',
                                                   'READ COMMITTED',
                                                   'READ UNCOMMITTED'],
                                       'question': 'Which isolation level completely prevents all concurrency '
                                                   'anomalies including Dirty Reads, Non-Repeatable Reads, and Phantom '
                                                   'Reads?'},
                                      {'correct_answer': 'Changes are written sequentially to a durable log file on '
                                                         'disk BEFORE modifying data pages in memory or data files',
                                       'difficulty': 'Medium',
                                       'explanation': 'WAL ensures changes can be replayed (REDO) or undone (UNDO) '
                                                      'upon crash recovery.',
                                       'options': ['Changes are written sequentially to a durable log file on disk '
                                                   'BEFORE modifying data pages in memory or data files',
                                                   'Data is saved to cloud storage before write',
                                                   'Transactions are written to RAM only',
                                                   'Logs are written after commit completes'],
                                       'question': 'What is Write-Ahead Logging (WAL) and how does it guarantee '
                                                   'Atomicity and Durability?'},
                                      {'correct_answer': 'A point where all modified dirty data pages in memory buffer '
                                                         'pools are flushed to disk, allowing older WAL logs to be '
                                                         'safely purged',
                                       'difficulty': 'Medium',
                                       'explanation': 'Checkpoints bound crash recovery time by flushing dirty buffers '
                                                      'to data files.',
                                       'options': ['A point where all modified dirty data pages in memory buffer pools '
                                                   'are flushed to disk, allowing older WAL logs to be safely purged',
                                                   'A pause in database query processing',
                                                   'A user login point',
                                                   'A backup marker'],
                                       'question': 'What is a Checkpoint in database WAL systems?'},
                                      {'correct_answer': 'Every single individual SQL statement is automatically '
                                                         'executed as its own independent committed transaction',
                                       'difficulty': 'Medium',
                                       'explanation': 'In autocommit mode, each SQL statement commits immediately upon '
                                                      'successful execution.',
                                       'options': ['Every single individual SQL statement is automatically executed as '
                                                   'its own independent committed transaction',
                                                   'The database automatically creates indexes',
                                                   'Transactions commit every midnight',
                                                   'The database commits changes to GitHub'],
                                       'question': 'What is Autocommit mode in database connections?'},
                                      {'correct_answer': 'An explicit transaction that reverses the business effects '
                                                         'of a previously committed transaction in long-running '
                                                         'workflows',
                                       'difficulty': 'Medium',
                                       'explanation': 'Sagas use compensating actions (e.g. refunding a payment) to '
                                                      'handle failures across distributed microservices.',
                                       'options': ['An explicit transaction that reverses the business effects of a '
                                                   'previously committed transaction in long-running workflows',
                                                   'A transaction that pays database licensing fees',
                                                   'A query that fixes syntax errors',
                                                   'A backup transaction'],
                                       'question': 'What is a Compensating Transaction in distributed saga patterns?'},
                                      {'correct_answer': 'Readers do not block writers and writers do not block '
                                                         'readers; the engine maintains multiple row versions with '
                                                         'transaction timestamps',
                                       'difficulty': 'Hard',
                                       'explanation': 'MVCC provides non-blocking point-in-time snapshots, maximizing '
                                                      'concurrent query throughput.',
                                       'options': ['Readers do not block writers and writers do not block readers; the '
                                                   'engine maintains multiple row versions with transaction timestamps',
                                                   'It allows multiple versions of the database software to run '
                                                   'simultaneously',
                                                   'It creates multiple copies of tables on disk',
                                                   'It disables locking across all transactions'],
                                       'question': 'What is Multi-Version Concurrency Control (MVCC) and what is its '
                                                   'primary benefit?'},
                                      {'correct_answer': 'Two concurrent transactions read overlapping data, perform '
                                                         'disjoint writes that violate a cross-row constraint; occurs '
                                                         'in Snapshot Isolation',
                                       'difficulty': 'Hard',
                                       'explanation': 'Snapshot Isolation prevents dirty and non-repeatable reads but '
                                                      'remains vulnerable to write skew.',
                                       'options': ['Two concurrent transactions read overlapping data, perform '
                                                   'disjoint writes that violate a cross-row constraint; occurs in '
                                                   'Snapshot Isolation',
                                                   'A hard drive head failure during write',
                                                   'A corrupted index write',
                                                   'Occurs only in READ UNCOMMITTED'],
                                       'question': 'What is Write Skew anomaly and at what isolation level can it '
                                                   'occur?'},
                                      {'correct_answer': 'A 3-phase recovery algorithm: Analysis (scans WAL from '
                                                         'checkpoint), REDO (repeats history to recover state), and '
                                                         'UNDO (rolls back active transactions)',
                                       'difficulty': 'Hard',
                                       'explanation': 'ARIES is the classic recovery model ensuring physiological '
                                                      'logging and repeatable history.',
                                       'options': ['A 3-phase recovery algorithm: Analysis (scans WAL from '
                                                   'checkpoint), REDO (repeats history to recover state), and UNDO '
                                                   '(rolls back active transactions)',
                                                   'A database encryption standard',
                                                   'A query optimization algorithm',
                                                   'A distributed consensus protocol'],
                                       'question': 'What is the ARIES (Algorithms for Recovery and Isolation '
                                                   'Exploiting Semantics) recovery algorithm?'},
                                      {'correct_answer': 'An optimistic lock-free algorithm that detects '
                                                         'rw-antidependency cycles at runtime and aborts conflicting '
                                                         'transactions to achieve true serializability',
                                       'difficulty': 'Hard',
                                       'explanation': 'SSI provides true serializability without coarse-grained read '
                                                      'locking by tracking SIREAD lock conflicts.',
                                       'options': ['An optimistic lock-free algorithm that detects rw-antidependency '
                                                   'cycles at runtime and aborts conflicting transactions to achieve '
                                                   'true serializability',
                                                   'A pessimistic table-locking mechanism',
                                                   'A distributed backup scheduler',
                                                   'A tool for snapshotting virtual machines'],
                                       'question': 'What is Serializable Snapshot Isolation (SSI) in PostgreSQL?'},
                                      {'correct_answer': 'A distributed atomic commitment protocol with Prepare Phase '
                                                         '(nodes vote yes/no) and Commit Phase (coordinator '
                                                         'commits/aborts all)',
                                       'difficulty': 'Hard',
                                       'explanation': '2PC guarantees distributed atomicity across multiple remote '
                                                      'database shards.',
                                       'options': ['A distributed atomic commitment protocol with Prepare Phase (nodes '
                                                   'vote yes/no) and Commit Phase (coordinator commits/aborts all)',
                                                   'Running transactions twice to verify accuracy',
                                                   'A protocol that commits every two seconds',
                                                   'A backup protocol'],
                                       'question': 'What is the Two-Phase Commit (2PC) protocol in distributed '
                                                   'transactions?'},
                                      {'correct_answer': 'It is a blocking protocol: if the coordinator crashes during '
                                                         'the prepare phase, participating nodes are left blocked '
                                                         'indefinitely',
                                       'difficulty': 'Hard',
                                       'explanation': 'Participant nodes holding locks cannot unilaterally decide to '
                                                      'commit or abort if the coordinator dies.',
                                       'options': ['It is a blocking protocol: if the coordinator crashes during the '
                                                   'prepare phase, participating nodes are left blocked indefinitely',
                                                   'It cannot support transactions',
                                                   'It causes data corruption on every commit',
                                                   'It only works with text data'],
                                       'question': 'What is the primary vulnerability of the basic Two-Phase Commit '
                                                   'protocol?'},
                                      {'correct_answer': '32-bit transaction IDs (XIDs) wrap around after 2 billion '
                                                         'transactions; VACUUM must freeze older XIDs to prevent past '
                                                         'data from appearing in the future',
                                       'difficulty': 'Hard',
                                       'explanation': 'Without vacuum freezing, circular 32-bit modulo arithmetic '
                                                      'causes historical tuples to become invisible.',
                                       'options': ['32-bit transaction IDs (XIDs) wrap around after 2 billion '
                                                   'transactions; VACUUM must freeze older XIDs to prevent past data '
                                                   'from appearing in the future',
                                                   'Transaction IDs exceed 64 bits',
                                                   'A stack overflow in database memory',
                                                   'A corruption of database passwords'],
                                       'question': 'What is a Transaction ID Wraparound (vacuum freeze) issue in '
                                                   'PostgreSQL?'},
                                      {'correct_answer': 'Calling fsync() forces the OS disk controller cache to flush '
                                                         'dirty pages to physical non-volatile storage, adding '
                                                         'rotational/SSD latency',
                                       'difficulty': 'Hard',
                                       'explanation': 'Group commit batches multiple transactions into a single '
                                                      'fsync() call to overcome physical disk latency.',
                                       'options': ['Calling fsync() forces the OS disk controller cache to flush dirty '
                                                   'pages to physical non-volatile storage, adding rotational/SSD '
                                                   'latency',
                                                   'fsync() disables writes to disk',
                                                   'fsync() compresses data files',
                                                   'fsync() runs queries on GPU'],
                                       'question': 'How does fsync() flushing affect database transaction commit '
                                                   'throughput and durability?'},
                                      {'correct_answer': 'A distributed system can guarantee at most two out of '
                                                         'Consistency, Availability, and Partition Tolerance '
                                                         'simultaneously',
                                       'difficulty': 'Hard',
                                       'explanation': 'During network partitions (P), distributed architectures must '
                                                      'choose between strong consistency (C) or availability (A).',
                                       'options': ['A distributed system can guarantee at most two out of Consistency, '
                                                   'Availability, and Partition Tolerance simultaneously',
                                                   'All systems must guarantee CPU, Allocation, and Power',
                                                   'Compression, Analytics, and Persistence',
                                                   'Calculus, Algebra, and Probability'],
                                       'question': 'What is the CAP Theorem in distributed data systems?'},
                                      {'correct_answer': 'If Partitioned (P): choose Availability (A) or Consistency '
                                                         '(C); Else (E): choose Latency (L) or Consistency (C)',
                                       'difficulty': 'Hard',
                                       'explanation': 'PACELC explicitly models the latency vs consistency trade-off '
                                                      'during normal non-partitioned operation.',
                                       'options': ['If Partitioned (P): choose Availability (A) or Consistency (C); '
                                                   'Else (E): choose Latency (L) or Consistency (C)',
                                                   'A theorem for packet delivery',
                                                   'An encryption framework for databases',
                                                   'A protocol for cloud scaling'],
                                       'question': 'What is PACELC theorem as an extension of CAP theorem?'}]}

