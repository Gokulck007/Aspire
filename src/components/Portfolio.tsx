'use client';

import { motion } from 'framer-motion';
import Image from 'next/image';

const works = [
  {
    title: "Cinematic Brand Motion",
    category: "AI Video",
    image: "/hero.png",
    span: "col-span-2 row-span-2"
  },
  {
    title: "Luxury Identity System",
    category: "Graphic Design",
    image: "/branding.png",
    span: "col-span-1 row-span-1"
  },
  {
    title: "Future of E-Commerce",
    category: "Web Development",
    image: "/web-dev.png",
    span: "col-span-1 row-span-1"
  }
];

export default function Portfolio() {
  return (
    <section id="portfolio" className="py-24 bg-[#0A0A0A] px-6">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
          <div>
            <h2 className="text-4xl md:text-6xl font-bold font-heading mb-4">Selected Works</h2>
            <p className="text-gray-400 text-xl max-w-xl">
              A curated collection of visual experiences and strategic identities.
            </p>
          </div>
          <div className="flex gap-4">
            <span className="px-4 py-2 rounded-full border border-white/10 text-sm font-medium text-white/60 hover:text-[#FF4D00] transition-colors cursor-pointer">All</span>
            <span className="px-4 py-2 rounded-full border border-white/10 text-sm font-medium text-white/60 hover:text-[#FF4D00] transition-colors cursor-pointer">Design</span>
            <span className="px-4 py-2 rounded-full border border-white/10 text-sm font-medium text-white/60 hover:text-[#FF4D00] transition-colors cursor-pointer">Video</span>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-[300px]">
          {works.map((work, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.2 }}
              className={`group relative overflow-hidden rounded-2xl glass ${work.span}`}
            >
              <Image 
                src={work.image} 
                alt={work.title}
                fill
                className="object-cover transition-transform duration-700 group-hover:scale-110 opacity-60 group-hover:opacity-100"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex flex-col justify-end p-8">
                <span className="text-[#FF4D00] font-bold text-sm uppercase tracking-widest mb-2">{work.category}</span>
                <h3 className="text-2xl font-bold text-white">{work.title}</h3>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
