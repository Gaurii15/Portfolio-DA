import os
import re

directory = '.'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
links = set()

for filename in html_files:
    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
        content = f.read()
        matches = re.findall(r'href=[\"\'](.*?)[\"\']', content)
        for m in matches:
            links.add((filename, m))

print("Checking external links...")
for filename, link in sorted(links):
    if link.startswith('http') or link.startswith('mailto'):
        print(f"{filename}: {link}")
