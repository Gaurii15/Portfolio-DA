import glob, os, re

new_logo = """    <a href="index.html" class="logo">
      <div class="logo-img">
        <svg viewBox="0 0 100 100" fill="var(--gradient-btn)">
          <circle cx="50" cy="50" r="40" stroke="url(#grad1)" stroke-width="8" fill="none" />
          <rect x="28" y="45" width="10" height="25" rx="3" fill="url(#grad1)" />
          <rect x="45" y="30" width="10" height="40" rx="3" fill="url(#grad1)" />
          <rect x="62" y="15" width="10" height="55" rx="3" fill="url(#grad1)" />
          <defs>
            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" style="stop-color:#8176AF;stop-opacity:1" />
              <stop offset="100%" style="stop-color:#C0B7E8;stop-opacity:1" />
            </linearGradient>
          </defs>
        </svg>
      </div> GB
    </a>"""

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
