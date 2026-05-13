import os
import re

pages = {
    'about.html': {'title': 'The Vision Behind <span class="text-[#FF4D00]">Adspire</span>', 'desc': 'Born at the intersection of design and technology, Adspire is more than a creative agency. We are a growth partner for brands that refuse to settle for the ordinary.', 'img': 'about_hero.png'},
    'services.html': {'title': 'Comprehensive <span class="text-[#FF4D00]">Solutions</span>', 'desc': 'From initial design to global scale, we provide the technical and creative engine to elevate your brand to the next level.', 'img': 'services_hero.png'},
    'portfolio.html': {'title': 'Our <span class="text-[#FF4D00]">Work</span>', 'desc': 'A showcase of visual excellence, strategic branding, and high-performance digital architecture across diverse industries.', 'img': 'portfolio_hero.png'},
    'contact.html': {'title': 'Start Your <span class="text-[#FF4D00]">Journey</span>', 'desc': 'Ready to elevate your brand? Connect with our team of specialists to start building your future today.', 'img': 'contact_hero.png'},
    'design.html': {'title': 'Visual <span class="text-[#FF4D00]">Identity</span>', 'desc': 'Authoritative design systems and logo architectures that command attention and build unshakable market trust.', 'img': 'design_hero.png'},
    'ai-video.html': {'title': 'AI <span class="text-[#FF4D00]">Cinema</span>', 'desc': 'Step into the future of content with cinematic 4K AI video productions that capture the essence of your brand.', 'img': 'ai_video_hero.png'},
    'growth.html': {'title': 'Strategic <span class="text-[#FF4D00]">Scaling</span>', 'desc': 'Data-driven marketing engines designed to turn raw traffic into high-value, long-term brand advocates.', 'img': 'growth_hero.png'},
    'web-dev.html': {'title': 'High-Perf <span class="text-[#FF4D00]">Web</span>', 'desc': 'Modern digital architecture optimized for ultra-fast performance and the 2026 AI-search landscape.', 'img': 'web_dev_hero.png'}
}

hero_template = """    <!-- Hero Section -->
    <section class="relative min-h-[80vh] flex items-center pt-24 px-6 overflow-hidden">
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div class="relative z-10 text-left">
                <h1 class="text-4xl md:text-7xl font-heading font-extrabold mb-6 tracking-tighter">
                    {title}
                </h1>
                <p class="text-xl text-gray-400 max-w-xl mb-10 leading-relaxed">
                    {desc}
                </p>
                <a href="contact.html" class="btn-primary inline-block">Work With Us</a>
            </div>
            <div class="relative">
                <div class="absolute -inset-4 bg-[#FF4D00]/20 blur-3xl rounded-full opacity-20"></div>
                <img src="{img}" alt="{title}" class="relative z-10 w-full h-auto rounded-3xl glass float">
            </div>
        </div>
    </section>"""

for filename, data in pages.items():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the existing Hero Section or the first section after the spacer
        pattern = r'<!-- (?:About|Services|Portfolio|Contact|Hero) Hero -->.*?<section.*?>.*?</section>'
        new_hero = hero_template.format(title=data['title'], desc=data['desc'], img=data['img'])
        
        # If the pattern doesn't match, try finding the first section after the header spacer
        if not re.search(pattern, content, flags=re.DOTALL):
            pattern = r'<div class="h-24"></div>\s*<!--.*?-->\s*<section.*?>.*?</section>'
            new_hero = '<div class="h-24"></div>\n' + new_hero
            
        content = re.sub(pattern, new_hero, content, count=1, flags=re.DOTALL)
        
        # Cleanup extra spacers if any
        content = content.replace('<div class="h-24"></div>\n    <div class="h-24"></div>', '<div class="h-24"></div>')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated hero for {filename}")

print("Done.")
