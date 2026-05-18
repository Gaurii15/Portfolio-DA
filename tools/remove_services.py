import glob
import os

target_strings = [
    '        <li><a href="services.html">Services</a></li>\n',
    '        <li><a href="services.html" class="active">Services</a></li>\n',
    '        <li><a href="services.html" class="active\\">Services</a></li>\n',
    '<li><a href="services.html">Services</a></li>',
    '<li><a href="services.html" class="active">Services</a></li>',
    '<li><a href="services.html" class="active\\">Services</a></li>'
]

updated_files = []

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for target in target_strings:
        if target in content:
            content = content.replace(target, '')
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_files.append(filepath)

print(f"Successfully updated navigation in {len(updated_files)} files: {updated_files}")

# Remove services.html file
if os.path.exists('services.html'):
    try:
        os.remove('services.html')
        print("Successfully deleted services.html locally.")
    except Exception as e:
        print(f"Error deleting services.html: {e}")
