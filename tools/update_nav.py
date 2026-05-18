import glob, os

updated = []
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'certifications.html' not in content and 'nav-links' in content:
        content = content.replace('<li><a href="services.html">Services</a></li>', '<li><a href="services.html">Services</a></li>\n        <li><a href="certifications.html">Certificates</a></li>')
        content = content.replace('<li><a href="services.html" class="active">Services</a></li>', '<li><a href="services.html" class="active\">Services</a></li>\n        <li><a href="certifications.html">Certificates</a></li>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(file)

print('Updated files:', updated)
