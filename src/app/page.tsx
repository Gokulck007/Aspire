import Hero from '@/components/Hero';
import Portfolio from '@/components/Portfolio';
import GrowthEngine from '@/components/GrowthEngine';
import Development from '@/components/Development';

export default function Home() {
  return (
    <main className="min-h-screen">
      <Hero />
      <Portfolio />
      <GrowthEngine />
      <Development />
      
      {/* Footer */}
      <footer className="py-20 bg-[#050505] border-t border-white/5 px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-10">
          <div>
            <div className="text-3xl font-bold font-heading mb-4 flex items-center gap-2">
              <span className="text-[#FF4D00]">AD</span>ASPIRE
            </div>
            <p className="text-gray-500 max-w-xs">
              Elevating brands through elite design, strategy, and technical mastery.
            </p>
          </div>
          
          <div className="flex gap-12 text-sm text-gray-400">
            <div className="flex flex-col gap-4">
              <span className="text-white font-bold uppercase tracking-widest text-xs">Services</span>
              <a href="#" className="hover:text-[#FF4D00] transition-colors">Design</a>
              <a href="#" className="hover:text-[#FF4D00] transition-colors">Video</a>
              <a href="#" className="hover:text-[#FF4D00] transition-colors">Strategy</a>
            </div>
            <div className="flex flex-col gap-4">
              <span className="text-white font-bold uppercase tracking-widest text-xs">Company</span>
              <a href="#" className="hover:text-[#FF4D00] transition-colors">About</a>
              <a href="#" className="hover:text-[#FF4D00] transition-colors">Careers</a>
              <a href="#" className="hover:text-[#FF4D00] transition-colors">Contact</a>
            </div>
          </div>
          
          <div className="text-center md:text-right">
            <p className="text-gray-600 text-sm mb-4">© 2026 Aspire Agency. All rights reserved.</p>
            <div className="flex gap-4 justify-center md:justify-end">
              <div className="w-10 h-10 rounded-full glass flex items-center justify-center hover:bg-[#FF4D00] transition-all cursor-pointer">
                <span className="sr-only">LinkedIn</span>
                {/* Icon placeholder */}
              </div>
              <div className="w-10 h-10 rounded-full glass flex items-center justify-center hover:bg-[#FF4D00] transition-all cursor-pointer">
                <span className="sr-only">Twitter</span>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </main>
  );
}
