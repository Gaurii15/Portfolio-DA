import os
import re

directory = '.'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

count = 0
for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert `<article class="achievement-card">` etc. back to `<div class="achievement-card">`
    # because the closing tags are `</div>`, which broke the layout.
    new_content = re.sub(r'<article class="(card|project-card|blog-card|service-card|achievement-card)([^"]*)">', r'<div class="\1\2">', content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed layout for {filename}")
        count += 1

print(f"Total files fixed: {count}")
