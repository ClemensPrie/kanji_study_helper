import base64

# Read the updated template
with open('app_template.html', 'rb') as f:
    content = f.read()

# Encode to Base64
encoded = base64.b64encode(content).decode()

# Create write_template.py with the encoded template
write_template_code = f'''import base64
t = base64.b64decode("""{encoded}""").decode("utf-8")
with open("app_template.html", "w", encoding="utf-8") as f:
    f.write(t)
print("Template written to app_template.html")
'''

# Write to write_template.py
import os
write_template_path = os.path.join(
    os.path.dirname(__file__),
    '..',
    '..',
    'Masterarbeit_Clemens_P',
    'write_template.py'
)

# Try to find write_template.py in the workspace
possible_paths = [
    'c:\\Users\\cprie\\Documents\\Masterarbeit_Clemens_P\\write_template.py',
    'c:\\Users\\cprie\\Documents\\Masterarbeit_Clemens_P\\scripts\\write_template.py',
]

target_path = None
for p in possible_paths:
    if os.path.exists(p):
        target_path = p
        break

if target_path:
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(write_template_code)
    print(f"Updated {target_path}")
else:
    # Write to current directory as fallback
    with open('write_template.py', 'w', encoding='utf-8') as f:
        f.write(write_template_code)
    print("Updated write_template.py in current directory")

print(f"Encoded template size: {len(encoded)} characters")
print(f"Original template size: {len(content)} bytes")
