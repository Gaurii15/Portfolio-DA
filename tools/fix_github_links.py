import os
import re

directory = '.'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

count = 0

def add_target_blank(match):
    full_tag = match.group(0)
    if 'target="_blank"' not in full_tag and "target='_blank'" not in full_tag:
        # Insert target="_blank" before the closing ">"
        # Be careful if there are spaces before ">"
        full_tag = re.sub(r'\s*>$', ' target="_blank">', full_tag)
    return full_tag

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all anchor tags that have href containing "github.com"
    # Using a negative lookahead to prevent matching if already has target="_blank"?
    # Actually, the function handles checking.
    new_content = re.sub(r'<a\s+[^>]*href=[\'"][^\'"]*github\.com[^\'"]*[\'"][^>]*>', add_target_blank, content, flags=re.IGNORECASE)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed GitHub links in {filename}")
        count += 1

print(f"Total files updated: {count}")
