with open('Backend/create_dsa_bank.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'How can a circular buffer achieve lock-free Single-Producer Single-Consumer (SPSC) thread safety?'
lines = text.split('\n')
for i, line in enumerate(lines):
    if target in line:
        lines[i] = line.replace('"Hard")', '"Medium")')
        print(f"Replaced line {i}")

with open('Backend/create_dsa_bank.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Saved create_dsa_bank.py")

