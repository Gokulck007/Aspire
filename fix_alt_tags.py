import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find alt="..." and remove any HTML tags inside the quotes
    def clean_alt(match):
        alt_content = match.group(1)
        # Remove anything between < and >
        clean_content = re.sub(r'<[^>]+>', '', alt_content)
        return f'alt="{clean_content}"'

    content = re.sub(r'alt="([^"]*)"', clean_alt, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Cleaned alt tags in {len(html_files)} files.")
