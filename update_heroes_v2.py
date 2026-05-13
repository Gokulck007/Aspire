import os
import re

# Pages with successful new images
v2_pages = ['about.html', 'services.html', 'portfolio.html', 'contact.html']

# Pages to revert to gradient heroes (until quota resets)
gradient_pages = ['design.html', 'ai-video.html', 'growth.html', 'web-dev.html']

for filename in v2_pages + gradient_pages:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if filename in gradient_pages:
            # Replace img with a premium gradient placeholder
            placeholder = """<div class="relative z-10 w-full aspect-square rounded-3xl glass float flex items-center justify-center bg-gradient-to-br from-[#FF4D00]/20 to-transparent border border-white/10">
                <div class="w-1/2 h-1/2 bg-[#FF4D00]/10 blur-[60px] rounded-full"></div>
            </div>"""
            content = re.sub(r'<img src="[^"]+" alt="[^"]+" class="relative z-10 w-full h-auto rounded-3xl glass float">', placeholder, content)
        else:
            # Just ensure alt tags are clean (already done by previous script but good to be safe)
            pass

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Refined hero for {filename}")

print("Done.")
