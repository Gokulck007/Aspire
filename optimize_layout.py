import os
import glob
import re

html_files = glob.glob('*.html')

# Master components from index.html (cleaned up)
master_style = """    <style>
        :root {
            --brand-primary: #0A0A0A;
            --brand-accent: #FF4D00;
            --brand-secondary: #FFFFFF;
        }
        
        body {
            background-color: var(--brand-primary);
            color: var(--brand-secondary);
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }

        .font-heading { font-family: 'Montserrat', sans-serif; }

        .glass {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .glass-dark {
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .float {
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        .btn-primary {
            background-color: var(--brand-accent);
            padding: 1rem 2.5rem;
            border-radius: 9999px;
            font-weight: 700;
            transition: all 0.3s;
            box-shadow: 0 0 20px rgba(255, 77, 0, 0.3);
        }

        .btn-primary:hover {
            transform: scale(1.05);
            box-shadow: 0 0 40px rgba(255, 77, 0, 0.5);
        }

        .text-gradient {
            background: linear-gradient(to right, #fff, #888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Portfolio Grid Overlays */
        .portfolio-item:hover .overlay {
            opacity: 1;
        }
    </style>"""

master_header = """    <!-- Navigation Header -->
    <header class="fixed top-0 left-0 right-0 z-50 transition-all duration-300" id="main-header">
        <nav class="p-6 flex justify-between items-center max-w-7xl mx-auto">
            <a href="index.html" class="flex items-center gap-4">
                <img src="logo.png" alt="Adspire Logo" class="h-10 w-auto">
                <span class="text-2xl font-heading font-extrabold tracking-tighter text-white">ADSPIRE</span>
            </a>
            <div class="hidden md:flex items-center gap-10 text-sm font-bold uppercase tracking-widest text-gray-400">
                <a href="index.html" class="hover:text-white transition-colors">Home</a>
                <a href="about.html" class="hover:text-white transition-colors">About</a>
                <a href="services.html" class="hover:text-white transition-colors">Services</a>
                <a href="portfolio.html" class="hover:text-white transition-colors">Portfolio</a>
                <a href="contact.html" class="hover:text-white transition-colors">Contact</a>
                <a href="contact.html" class="bg-[#FF4D00] text-white px-6 py-2 rounded-full hover:scale-105 transition-all shadow-[0_0_20px_rgba(255,77,0,0.3)]">Get Started</a>
            </div>
            <!-- Mobile Menu Toggle -->
            <button class="md:hidden text-white" id="mobile-toggle">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            </button>
        </nav>
        <!-- Mobile Menu Overlay -->
        <div id="mobile-menu" class="fixed inset-0 z-50 flex flex-col items-center justify-center gap-8 text-2xl font-bold uppercase tracking-widest transition-all duration-500 opacity-0 pointer-events-none bg-black/95 backdrop-blur-xl">
            <button class="absolute top-6 right-6 text-white" id="mobile-close">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
            <a href="index.html" class="hover:text-[#FF4D00]">Home</a>
            <a href="about.html" class="hover:text-[#FF4D00]">About</a>
            <a href="services.html" class="hover:text-[#FF4D00]">Services</a>
            <a href="portfolio.html" class="hover:text-[#FF4D00]">Portfolio</a>
            <a href="contact.html" class="hover:text-[#FF4D00]">Contact</a>
        </div>
    </header>"""

master_script = """    <script>
        const header = document.getElementById('main-header');
        const mobileToggle = document.getElementById('mobile-toggle');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileClose = document.getElementById('mobile-close');

        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('glass', 'py-2');
            } else {
                header.classList.remove('glass', 'py-2');
            }
        });

        mobileToggle.addEventListener('click', () => {
            mobileMenu.classList.remove('opacity-0', 'pointer-events-none');
            document.body.style.overflow = 'hidden';
        });
        mobileClose.addEventListener('click', () => {
            mobileMenu.classList.add('opacity-0', 'pointer-events-none');
            document.body.style.overflow = '';
        });
    </script>"""

master_footer = """    <!-- Footer -->
    <footer class="py-20 px-6 border-t border-white/5">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
            <div class="text-2xl font-heading font-extrabold tracking-tighter">
                <span class="text-[#FF4D00]">AD</span>SPIRE
            </div>
            <div class="flex gap-10 text-sm text-gray-500 font-bold uppercase tracking-widest">
                <a href="design.html" class="hover:text-white transition-colors">Design</a>
                <a href="services.html" class="hover:text-white transition-colors">Services</a>
                <a href="contact.html" class="hover:text-white transition-colors">Contact</a>
            </div>
            <div class="text-gray-600 text-sm">
                © 2026 Adspire Creative Agency.
            </div>
        </div>
    </footer>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace Header
    content = re.sub(r'<!-- Navigation Header -->.*?<!-- Mobile Menu Overlay -->.*?</div>\s*</header>', master_header, content, flags=re.DOTALL)
    # 2. Replace Footer
    content = re.sub(r'<!-- Footer -->.*?</footer>', master_footer, content, flags=re.DOTALL)
    # 3. Replace Script
    content = re.sub(r'<script>\s*const header = document\.getElementById\(.main-header.\);.*?</script>', master_script, content, flags=re.DOTALL)
    # 4. Replace Style
    content = re.sub(r'<style>.*?</style>', master_style, content, flags=re.DOTALL)

    # 5. Typography Optimizations
    # Add tracking-tight to headings if not present
    content = re.sub(r'(<h[123][^>]*class="[^"]*font-heading[^"]*)(")', r'\1 tracking-tight\2', content)
    # Ensure paragraphs have leading-relaxed and text-gray-400
    content = re.sub(r'(<p[^>]*class="[^"]*)(text-gray-400[^"]*|text-gray-300[^"]*)(")', r'\1leading-relaxed text-gray-400\3', content)
    # Cap long paragraph containers at max-w-3xl for better readability
    content = content.replace('max-w-4xl mx-auto text-gray-300', 'max-w-3xl mx-auto text-gray-400')

    # 6. Global Branding fix
    content = content.replace("ADADSPIRE", "ADSPIRE")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully optimized and unified {len(html_files)} HTML files.")
