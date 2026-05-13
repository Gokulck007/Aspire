'use client';

import { motion } from 'framer-motion';
import Image from 'next/image';

export default function Hero() {
  return (
    <section className="relative h-screen flex flex-col items-center justify-center overflow-hidden bg-[#0A0A0A]">
      {/* Background Glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-[#FF4D00]/20 blur-[120px] rounded-full pointer-events-none" />
      
      {/* Content */}
      <div className="relative z-10 flex flex-col items-center text-center px-4">
        <motion.div
          initial={{ opacity: 0, scale: 0.8, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          transition={{ duration: 1, ease: "easeOut" }}
          className="mb-8"
        >
          {/* Logo Placeholder - In a real app, this would be an SVG or Image */}
          <div className="relative w-32 h-32 md:w-48 md:h-48 float">
            <svg viewBox="0 0 100 100" className="w-full h-full">
              <rect x="10" y="10" width="80" height="80" fill="none" stroke="white" strokeWidth="4" />
              <path d="M50 20 L80 80 L20 80 Z" fill="#FF4D00" />
              <rect x="35" y="55" width="30" height="25" fill="white" />
            </svg>
          </div>
        </motion.div>

        <motion.h1 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5, duration: 0.8 }}
          className="text-5xl md:text-8xl font-bold font-heading mb-6 tracking-tight"
        >
          <span className="text-white">Design. </span>
          <span className="text-[#FF4D00]">Strategize. </span>
          <span className="text-white">Elevate.</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1, duration: 1 }}
          className="text-gray-400 text-lg md:text-2xl max-w-2xl mb-10 font-sans"
        >
          We are <span className="text-white font-semibold">Aspire</span>. A premium creative engine dedicated to scaling high-trust brands through elite design and AI-driven video.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1.2, duration: 0.8 }}
        >
          <button className="btn-primary">
            Elevate Your Brand
          </button>
        </motion.div>
      </div>

      {/* Scroll Indicator */}
      <motion.div
        animate={{ y: [0, 10, 0] }}
        transition={{ repeat: Infinity, duration: 2 }}
        className="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-50"
      >
        <span className="text-xs uppercase tracking-widest text-white/50">Scroll to Explore</span>
        <div className="w-[1px] h-12 bg-gradient-to-b from-white/50 to-transparent" />
      </motion.div>
    </section>
  );
}
