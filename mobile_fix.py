import os
import glob

html_files = glob.glob('*.html')

old_menu = """        <!-- Mobile Menu Overlay -->
        <div id="mobile-menu" class="hidden fixed inset-0 bg-black z-50 flex flex-col items-center justify-center gap-8 text-2xl font-bold uppercase tracking-widest transition-all">"""

new_menu = """        <!-- Mobile Menu Overlay -->
        <div id="mobile-menu" class="fixed inset-0 z-50 flex flex-col items-center justify-center gap-8 text-2xl font-bold uppercase tracking-widest transition-all duration-500 opacity-0 pointer-events-none bg-black/95 backdrop-blur-xl">"""

old_script = """        mobileToggle.addEventListener('click', () => mobileMenu.classList.remove('hidden'));
        mobileClose.addEventListener('click', () => mobileMenu.classList.add('hidden'));"""

new_script = """        mobileToggle.addEventListener('click', () => {
            mobileMenu.classList.remove('opacity-0', 'pointer-events-none');
            document.body.style.overflow = 'hidden';
        });
        mobileClose.addEventListener('click', () => {
            mobileMenu.classList.add('opacity-0', 'pointer-events-none');
            document.body.style.overflow = '';
        });"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix typo
    content = content.replace("ADADSPIRE", "ADSPIRE")
    
    # Fix typography
    content = content.replace("text-5xl md:text-7xl", "text-4xl md:text-6xl")
    content = content.replace("text-5xl md:text-8xl", "text-4xl md:text-7xl lg:text-8xl")
    content = content.replace("text-4xl md:text-6xl", "text-3xl md:text-5xl")
    
    # Fix menu HTML & JS
    content = content.replace(old_menu, new_menu)
    content = content.replace(old_script, new_script)
    
    # Fix body overflow
    content = content.replace("<body>", '<body class="overflow-x-hidden">')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully processed {len(html_files)} HTML files.")
