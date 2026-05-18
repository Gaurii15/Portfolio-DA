import os
import re

directory = '.'

footer_old_pattern = re.compile(r'<p style="text-align:center; margin:20px 0;"><span style="color: var\(--text-muted\); font-weight: 600; opacity: 0\.9; font-size: 1rem; letter-spacing: 0\.5px;">Designed &amp; Coded by Gauri</span></p>', re.IGNORECASE)

replacement = r'<p style="text-align:center; margin:20px 0;"><span style="color: var(--text-muted); font-weight: 400; opacity: 0.8; font-size: 0.85rem; letter-spacing: 0.5px;">Designed &amp; Coded by <span style="color: var(--primary-light); font-weight: 600;">Gauri</span></span></p>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = footer_old_pattern.sub(replacement, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {filename}")
            count += 1

print(f"Total files updated: {count}")
