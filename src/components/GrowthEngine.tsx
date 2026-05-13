'use client';

import { motion } from 'framer-motion';
import { TrendingUp, Target, Search, BarChart3 } from 'lucide-react';

const stats = [
  { icon: TrendingUp, label: "Marketing Strategy", detail: "Data-driven roadmaps for scaling." },
  { icon: Target, label: "Ad Performance", detail: "High-conversion campaigns that stick." },
  { icon: Search, label: "SEO Mastery", detail: "Dominating AI-search for 2026." },
  { icon: BarChart3, label: "Analytics", detail: "Real-time insights and growth tracking." }
];

export default function GrowthEngine() {
  return (
    <section className="py-24 bg-[#0A0A0A] relative overflow-hidden">
      <div className="absolute top-0 right-0 w-1/2 h-full bg-[#FF4D00]/5 -skew-x-12 translate-x-1/2" />
      
      <div className="max-w-7xl mx-auto px-6 relative z-10">
        <div className="text-center mb-20">
          <h2 className="text-4xl md:text-6xl font-bold font-heading mb-6">Growth Engine</h2>
          <p className="text-gray-400 text-xl max-w-2xl mx-auto">
            Beyond design, we build machines that sell. Our strategic layer ensures your visual excellence translates into market dominance.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {stats.map((item, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: index % 2 === 0 ? -20 : 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="p-8 rounded-3xl glass-dark hover:border-[#FF4D00]/50 transition-all group cursor-default"
            >
              <div className="w-14 h-14 rounded-2xl bg-[#FF4D00]/10 flex items-center justify-center mb-6 group-hover:bg-[#FF4D00] transition-colors">
                <item.icon className="text-[#FF4D00] group-hover:text-white" size={28} />
              </div>
              <h3 className="text-xl font-bold mb-3">{item.label}</h3>
              <p className="text-gray-500 leading-relaxed">{item.detail}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
