import {Link} from 'react-router-dom'
import szabistlogo from '../assets//szabist-logo.png'
function Navbar(){
    return (
        <nav className="bg-navy text-white px-6 py-4 flex items-center justify-between">
             <img 
                    src={szabistlogo} 
                    alt="SZABIST Logo" 
                    className="h-10 w-auto object-contain" 
                />
            <span className="font-bold text-xl">ZABAUDIT</span>
            <div className="flex gap-6">
                <Link to="/">Home</Link>
                <Link to="/">About</Link>
                <Link to="/dashboard">Course Status Dashboard</Link>
                <Link to="/clearance">Clearance Status Generator</Link>
                <Link to="/prereq-tree">Prereq Tree</Link>
                <Link to="/contact">Contact</Link>
            </div>
        </nav>
    )
}

export default Navbar;