import os
import re

directory = '.'

footer_html = """  <footer>
    <div class="container">
      <p style="text-align:center; margin:20px 0;"><span style="color: var(--text-muted); font-weight: 600; opacity: 0.9; font-size: 1rem; letter-spacing: 0.5px;">Designed &amp; Coded by Gauri</span></p>
    </div>
  </footer>"""

footer_pattern = re.compile(r'<footer[^>]*>.*?</footer>', re.IGNORECASE | re.DOTALL)

count = 0
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if footer_pattern.search(content):
            new_content = footer_pattern.sub(footer_html, content)
        else:
            if '<script src="js/animations.js"></script>' in content:
                new_content = content.replace('<script src="js/animations.js"></script>', f"{footer_html}\n\n  <script src=\"js/animations.js\"></script>")
            else:
                new_content = content.replace('</body>', f"{footer_html}\n</body>")
                
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {filename}")
            count += 1

print(f"Total files updated: {count}")
