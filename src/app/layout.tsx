import type { Metadata } from "next";
import { Inter, Montserrat } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const montserrat = Montserrat({ subsets: ["latin"], variable: "--font-montserrat" });

export const metadata: Metadata = {
  title: "Aspire | Design. Strategize. Elevate.",
  description: "High-end creative agency specializing in Graphic Design, AI Video, Marketing Strategy, and Web Development. We elevate brands through cutting-edge technology and data-driven growth.",
  keywords: ["Creative Agency", "Design", "AI Video", "Marketing Strategy", "SEO", "Web Development", "Aspire"],
  openGraph: {
    title: "Aspire | Design. Strategize. Elevate.",
    description: "Elevate your brand with Aspire's expert design and strategy.",
    url: "https://aspire.agency",
    siteName: "Aspire",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Aspire | Design. Strategize. Elevate.",
    description: "Elevate your brand with Aspire's expert design and strategy.",
    images: ["/og-image.png"],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${montserrat.variable} scroll-smooth`}>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "CreativeBusiness",
              "name": "Aspire",
              "url": "https://aspire.agency",
              "logo": "https://aspire.agency/logo.png",
              "description": "Premium creative agency specializing in Design, AI Video, and Growth Strategy.",
              "address": {
                "@type": "PostalAddress",
                "addressCountry": "US"
              },
              "serviceType": ["Graphic Design", "AI Video", "Marketing", "Web Development"]
            }),
          }}
        />
      </head>
      <body className="antialiased bg-[#0A0A0A] text-white">
        {children}
      </body>
    </html>
  );
}
