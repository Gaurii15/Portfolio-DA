import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change .hero align-items
content = re.sub(
    r'\.hero\s*\{[^}]*align-items:\s*center;',
    lambda m: m.group(0).replace('align-items: center;', 'align-items: flex-start;'),
    content
)

# 2. Change .hero padding bottom to 20px (from 50px 0)
content = re.sub(
    r'(\.hero\s*\{[^}]*padding:\s*)50px 0;',
    r'\1 50px 0 20px 0;',
    content
)

# 3. Change .hero-text h1 font-size
content = re.sub(
    r'(\.hero-text h1\s*\{[^}]*font-size:\s*)4\.5rem;',
    r'\g<1>3.8rem;',
    content
)

# 4. Change media query h1 font-size
content = re.sub(
    r'(\.hero-text h1\s*\{[^}]*font-size:\s*)3\.5rem;',
    r'\g<1>3.0rem;',
    content
)

# 5. Change .hero-img-col align-items to flex-start and add padding-top
content = re.sub(
    r'(\.hero-img-col\s*\{[^}]*align-items:\s*)center;',
    r'\g<1>flex-start;\n      padding-top: 45px;',
    content
)

# 6. Change .achievements-container margin-top
content = re.sub(
    r'(\.achievements-container\s*\{[^}]*margin-top:\s*)50px;',
    r'\g<1>20px;\n      margin-bottom: 50px;',
    content
)

# 7. Move achievements-container outside of .hero
# First extract the HTML block
achievements_pattern = r'(\s*<div class="achievements-container reveal".*?</div>\s*</div>)'
match = re.search(achievements_pattern, content, flags=re.DOTALL)
if match:
    achievements_html = match.group(1)
    
    # Remove from original location
    content = content.replace(achievements_html, '')
    
    # Insert after </section> <!-- End of hero -->
    content = content.replace('</section>', '</section>' + achievements_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
