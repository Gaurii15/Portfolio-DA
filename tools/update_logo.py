import glob, os, re

new_logo = """    <a href="index.html" class="logo">GB</a>"""

# We'll use a regex to match the entire <a> tag that contains class="logo"
# The regex should span multiple lines
pattern = re.compile(r'<a href="index\.html" class="logo">.*?</a>', re.DOTALL)

updated_files = []
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'class="logo"' in content:
        new_content = pattern.sub(new_logo, content)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.append(file)

print('Updated files:', updated_files)
