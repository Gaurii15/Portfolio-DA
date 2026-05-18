import os
import re

directory = '.'

# The previous script accidentally replaced the <p> tag with P due to octal evaluation \120
# We need to replace the corrupted text with a proper opening <p> tag, effectively removing the copyright text
footer_pattern = re.compile(r'P24\s*&copy;\s*Gauri\s*Borse\.\s*All\s*Rights\s*Reserved\.<br>', re.IGNORECASE)

replacement = r'<p style="text-align:center; opacity:0.5; font-size:0.8rem; margin:20px 0;">'

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = footer_pattern.sub(replacement, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {filename}")
            count += 1

print(f"Total files fixed: {count}")
