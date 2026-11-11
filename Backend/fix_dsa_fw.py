with open('Backend/create_dsa_bank.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "What is the Floyd-Warshall algorithm and what is its time complexity?" in line:
        new_lines.append("""    make_q("What is the Floyd-Warshall algorithm and what is its time complexity?", ["A dynamic programming algorithm that finds all-pairs shortest paths in O(V^3) time", "A single-source shortest path algorithm in O(V log V)", "A flow network algorithm in O(V^2 E)", "A topological sorting algorithm in O(V + E)"], "A dynamic programming algorithm that finds all-pairs shortest paths in O(V^3) time", "Floyd-Warshall computes shortest paths between all pairs of vertices in O(V^3) time using dynamic programming.", "Hard"),\n""")
    else:
        new_lines.append(line)

with open('Backend/create_dsa_bank.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed Floyd-Warshall line in create_dsa_bank.py")

