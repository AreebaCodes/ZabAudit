import { useState } from 'react'
import {Routes,Route} from 'react-router-dom'
import Login from './pages/Login'
import Navbar from './components/Navbar'
function App() {
 // const [count, setCount] = useState(0)

  return (
    <>
    <Navbar/>
    <Routes>
     <Route path="/" element={<Login/>}/>
    </Routes>
      
    </>
  )
}

export default App
