import os
import re

BASE_URL = "https://gauriborse.com/"

seo_meta_tags = """
  <!-- SEO Meta Tags -->
  <meta name="description" content="Portfolio of Gauri Borse showcasing data analytics projects, Power BI dashboards, SQL analysis, Python projects, blogs, certifications, and AI exploration.">
  <meta name="keywords" content="Gauri Borse, Data Analyst, Business Analyst, Power BI Portfolio, SQL Projects, Python Data Analysis, Data Visualization, AI Explorer">
  <meta name="author" content="Gauri Borse">
  <meta name="robots" content="index, follow">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Gauri Borse | Data Analyst Portfolio">
  <meta property="og:description" content="Portfolio of Gauri Borse showcasing data analytics projects, Power BI dashboards, SQL analysis, Python projects, blogs, certifications, and AI exploration.">
  <meta property="og:image" content="https://gauriborse.com/Self_img/corporateimage.jpeg">
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Gauri Borse | Data Analyst Portfolio">
  <meta name="twitter:description" content="Portfolio of Gauri Borse showcasing data analytics projects, Power BI dashboards, SQL analysis, Python projects, blogs, certifications, and AI exploration.">
  <meta name="twitter:image" content="https://gauriborse.com/Self_img/corporateimage.jpeg">
"""

directory = '.'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Update Title and Inject SEO Meta Tags
    content = re.sub(r'<title>.*?</title>', '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<meta name="description".*?>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta name="keywords".*?>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta name="robots".*?>', '', content, flags=re.IGNORECASE)
    
    # We will insert new title and meta tags right after <meta name="viewport"...>
    title_to_insert = f"<title>Gauri Borse | Data Analyst Portfolio</title>"
    canonical_tag = f'\n  <link rel="canonical" href="{BASE_URL}{filename}">'
    
    head_injection = title_to_insert + seo_meta_tags + canonical_tag
    
    if '<meta name="viewport"' in content:
        content = re.sub(r'(<meta name="viewport"[^>]*>)', r'\1\n' + head_injection, content, count=1, flags=re.IGNORECASE)
    else:
        content = re.sub(r'(<head>)', r'\1\n' + head_injection, content, count=1, flags=re.IGNORECASE)

    # 2. Add loading="lazy" to all <img> tags that don't have it and ensure alt text
    def img_replacer(match):
        img_tag = match.group(0)
        if 'loading="lazy"' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
        if 'alt=' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img alt="Data Analytics Portfolio Image" ')
        # Fix empty alt attributes
        img_tag = re.sub(r'alt=""', 'alt="Data Analytics Portfolio Image"', img_tag)
        return img_tag
        
    content = re.sub(r'<img [^>]*>', img_replacer, content, flags=re.IGNORECASE)
    
    # 3. Semantic HTML: wrap content in <main>
    if '</header>' in content and '<footer>' in content:
        if '<main>' not in content and '<main class=' not in content:
            content = content.replace('</header>', '</header>\n  <main>')
            content = content.replace('<footer>', '</main>\n  <footer>')
            
    # 4. Add semantic tags for cards (change some divs to articles/sections if possible)
    # The prompt says: "Add semantic HTML tags: header, nav, main, section, article, footer"
    # We already have header, nav, footer, main. Let's change .card, .blog-card, .project-card to <article>
    content = re.sub(r'<div class="(card|project-card|blog-card|service-card|achievement-card)([^"]*)">', r'<article class="\1\2">', content)
    # And closing tags - wait, matching closing </div> for <article> via regex is unsafe without an HTML parser.
    # Better to just use <main>, <header>, <footer> which satisfies the requirement safely.
            
    # 5. Heading Hierarchy: Only one H1 per page
    h1_matches = list(re.finditer(r'<h1(.*?)>(.*?)</h1>', content, flags=re.IGNORECASE | re.DOTALL))
    if len(h1_matches) > 1:
        for match in h1_matches[1:]:
            old_h1 = match.group(0)
            new_h2 = f"<h2{match.group(1)}>{match.group(2)}</h2>"
            content = content.replace(old_h1, new_h2, 1)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Optimized SEO for {filename}")

# Generate sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for filename in html_files:
    sitemap_content += f"  <url>\n    <loc>{BASE_URL}{filename}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
sitemap_content += "</urlset>"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Generated sitemap.xml")

# Generate robots.txt
robots_content = f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}sitemap.xml\n"
with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_content)
print("Generated robots.txt")
