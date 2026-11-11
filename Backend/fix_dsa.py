with open('Backend/create_dsa_bank.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "What is a Persistent Stack (Purely Functional Stack)?" in line:
        new_lines.append("""    make_q("What is a Persistent Stack (Purely Functional Stack)?", ["A stack where push and pop operations return a new stack reference while preserving the previous version via structural sharing", "A stack saved to an SQL database", "A stack that cannot be popped", "A stack stored in non-volatile NVRAM"], "A stack where push and pop operations return a new stack reference while preserving the previous version via structural sharing", "A persistent stack shares its tail node with previous versions, allowing time-traveling without copying.", "Hard"),\n""")
    else:
        new_lines.append(line)

with open('Backend/create_dsa_bank.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed create_dsa_bank.py")

