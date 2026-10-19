import szabistlogo from '../assets/szabist-logo.png'

function Navbar() {
  return (
    <nav className="bg-navy text-white px-4 sm:px-6 h-16 md:h-20 flex items-center justify-between gap-4 border-b-4">
      <div className="flex items-center gap-3 min-w-0">
        <div className="bg-white rounded-md p-1 shrink-0">
          <img src={szabistlogo} alt="SZABIST Logo" className="h-10 sm:h-12 md:h-14 w-auto object-contain" />
        </div>
        <div className="hidden sm:block w-0.5 h-8 md:h-10 bg-white/40"></div>
        <div className="text-xl sm:text-2xl md:text-3xl font-extrabold truncate">
          <span className="text-white">ZAB</span><span className="text-gold">AUDIT</span>
        </div>
      </div>

      <div className="hidden lg:flex gap-5 text-sm font-semibold cursor-default">
        <span>Home</span>
        <span>About</span>
        <span>Course Status Dashboard</span>
        <span>Clearance Status Generator</span>
        <span>Prereq Tree</span>
        <span>Contact</span>
      </div>
    </nav>
  )
}

export default Navbar