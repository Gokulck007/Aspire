'use client';

import { motion } from 'framer-motion';
import { Code2, Cpu, Globe, Zap } from 'lucide-react';

export default function Development() {
  return (
    <section className="py-24 bg-[#050505] px-6">
      <div className="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-16">
        <div className="lg:w-1/2">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            className="relative rounded-3xl overflow-hidden glass p-4"
          >
            <div className="bg-black/90 rounded-2xl p-6 aspect-video font-mono text-sm text-gray-400 overflow-hidden">
              <div className="flex gap-2 mb-4">
                <div className="w-3 h-3 rounded-full bg-red-500" />
                <div className="w-3 h-3 rounded-full bg-yellow-500" />
                <div className="w-3 h-3 rounded-full bg-green-500" />
              </div>
              <p className="text-[#FF4D00]">class AspireEngine {"{"}</p>
              <p className="pl-4">constructor() {"{"}</p>
              <p className="pl-8 text-white">this.vision = "Design. Strategize. Elevate.";</p>
              <p className="pl-8 text-white">this.performance = 100;</p>
              <p className="pl-4">{"}"}</p>
              <p className="pl-4 text-gray-600">// Optimizing for 2026 AI-Search...</p>
              <p className="pl-4">async deploy() {"{"}</p>
              <p className="pl-8 text-green-400">return await ignite(this.vision);</p>
              <p className="pl-4">{"}"}</p>
              <p className="text-[#FF4D00]">{"}"}</p>
            </div>
            {/* Floating Element */}
            <motion.div 
              animate={{ y: [0, -10, 0] }}
              transition={{ repeat: Infinity, duration: 4 }}
              className="absolute -top-6 -right-6 p-6 glass rounded-2xl border-[#FF4D00]/30"
            >
              <Cpu size={32} className="text-[#FF4D00]" />
            </motion.div>
          </motion.div>
        </div>

        <div className="lg:w-1/2">
          <h2 className="text-4xl md:text-6xl font-bold font-heading mb-8">Technical Mastery</h2>
          <p className="text-gray-400 text-xl mb-10">
            We don't just build websites; we engineer digital fortresses. Fast, secure, and optimized for the next generation of search.
          </p>
          
          <div className="space-y-6">
            {[
              { icon: Zap, text: "Ultra-fast performance with Next.js 15" },
              { icon: Globe, text: "Global edge deployment" },
              { icon: Code2, text: "Clean, scalable architecture" }
            ].map((item, idx) => (
              <div key={idx} className="flex items-center gap-4 text-lg font-medium text-white/80">
                <div className="p-2 rounded-lg bg-[#FF4D00]/20">
                  <item.icon size={20} className="text-[#FF4D00]" />
                </div>
                {item.text}
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
