import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Clean the alt tags aggressively
    content = content.replace('alt="The Vision Behind <span class="text-[#FF4D00]">Adspire</span>"', 'alt="The Vision Behind Adspire"')
    content = content.replace('alt="Comprehensive <span class="text-[#FF4D00]">Solutions</span>"', 'alt="Comprehensive Solutions"')
    content = content.replace('alt="Start Your <span class="text-[#FF4D00]">Journey</span>"', 'alt="Start Your Journey"')
    content = content.replace('alt="Our <span class="text-[#FF4D00]">Work</span>"', 'alt="Our Work"')
    content = content.replace('alt="Visual <span class="text-[#FF4D00]">Identity</span>"', 'alt="Visual Identity"')
    content = content.replace('alt="AI <span class="text-[#FF4D00]">Cinema</span>"', 'alt="AI Cinema"')
    content = content.replace('alt="Strategic <span class="text-[#FF4D00]">Scaling</span>"', 'alt="Strategic Scaling"')
    content = content.replace('alt="High-Perf <span class="text-[#FF4D00]">Web</span>"', 'alt="High-Perf Web"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed broken alt tags.")
