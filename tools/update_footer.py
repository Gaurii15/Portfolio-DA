import os
import re

directory = '.'

footer_pattern = re.compile(r'(<p[^>]*>)\s*2024\s*©\s*Gauri\s*Borse\.\s*All\s*Rights\s*Reserved\.\s*(</p>)', re.IGNORECASE | re.MULTILINE | re.DOTALL)

replacement = r'\12024 &copy; Gauri Borse. All Rights Reserved.<br><span style="color: var(--primary-light); font-weight: 600; opacity: 1; margin-top: 5px; display: inline-block;">Designed &amp; Coded by Gauri</span>\2'

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

print(f"Total files updated: {count}")
