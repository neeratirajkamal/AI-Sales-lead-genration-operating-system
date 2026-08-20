import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Vortexen + Plus UAE RevenueOS — AI Lead Generation & Outreach Engine',
  description: 'Signal-to-revenue commercial intelligence & multi-channel outreach engine for Abu Dhabi, UAE & Saudi Arabia.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-[#090d16] text-slate-100 antialiased selection:bg-cyan-500 selection:text-white">
        {children}
      </body>
    </html>
  )
}
