import os
import re

placeholder_html = """
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(20, 18, 28, 0.95), rgba(33, 30, 46, 0.98)); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border: 2px dashed rgba(192, 183, 232, 0.2); border-radius: var(--border-radius-md); z-index: 2; box-shadow: inset 0 0 50px rgba(0,0,0,0.5);">
            <svg viewBox="0 0 24 24" style="width: 50px; height: 50px; fill: var(--primary-light); margin-bottom: 15px; opacity: 0.8; filter: drop-shadow(0 0 10px rgba(192, 183, 232, 0.5));">
              <path d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm0 18c-4.411 0-8-3.589-8-8s3.589-8 8-8 8 3.589 8 8-3.589 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/>
            </svg>
            <h3 style="font-size: 1.8rem; margin-bottom: 8px; color: var(--text-light); letter-spacing: 1px;">Video Coming Soon</h3>
            <p style="font-size: 1rem; color: var(--text-muted); max-width: 80%; line-height: 1.5;">The detailed video walkthrough for this project is currently in production.</p>
          </div>
"""

directory = '.'
count = 0

# We look for <div class="video-container"> followed by anything up to </iframe>
# And we replace the src attribute with empty string, then append the placeholder
pattern = re.compile(r'(<div class="video-container"[^>]*>)\s*(<iframe.*?src=")(.*?)(".*?>.*?</iframe>)', re.IGNORECASE | re.DOTALL)

for filename in os.listdir(directory):
    if filename.lower().startswith('project-') and filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = pattern.sub(r'\1\n          \2\4' + placeholder_html, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
            count += 1

print(f"Total files updated: {count}")
