import { useState } from 'react'
import {Routes,Route} from 'react-router-dom'
import Login from './pages/Login'
import Navbar from './components/Navbar'
import SignUp from './pages/Signup'
import Dashboard from './pages/Dashboard'
import ForgotPassword from './pages/ForgotPassword'
import StudentSignup from './pages/StudentSignup'
function App() {
 // const [count, setCount] = useState(0)

  return (
    <>
    <Navbar/>
    <Routes>
     <Route path="/" element={<Login/>}/>
     <Route path="/signup" element={<SignUp />} />
     <Route path="/student-signup" element={<StudentSignup/>}/>
     <Route path="/dashboard" element={<Dashboard/>}/>
     <Route path="/forgot-password" element={<ForgotPassword />} />
    </Routes>
      
    </>
  )
}

export default App
