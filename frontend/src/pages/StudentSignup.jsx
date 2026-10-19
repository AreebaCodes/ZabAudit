import { useState } from "react";
import {useNavigate,Link} from "react-router-dom"
import api from "../api"

export default function StudentSignup(){
    //FIELDS ZIADA HOSAKHTI HY EK FORM MEIN TBHI FORM DATA USE KRNA ZIADA BEHTAR HY
    const[formdata,setFormdata]=useState({  
          name:"",
          email:"",
          password:"",
          program:"BSCS", //BY DEFAULT
          reg_no:"2312393" //BY DEFAULT,
         
    })
    //FOR ERROR HANDLING
    const[error,setError]=useState("")

    //FOR INPUT HANDLING FUNCTION
    const handleChange=(e)=>{
        setFormdata({...formdata,[e.target.name]:e.target.value})
    }
    const navigate=useNavigate()
    //FOR SUBMITTING
    async function handleSubmit(e){
          e.preventDefault()
          setError("") //old errors should be removed
          if(!formdata.email.toLowerCase().endsWith("@szabist.pk")){
            setError("Email must end with @szabist.pk")
            return
          }
          try{
            await api.post("/student/signup",{
                ...formdata ,//SPREAD OPERATOR AS FORM DATA IS AN OBJECT
                year:Number(formdata.year) //AS IT IS DEFINED AS INT IN THE BACKEND
            })
            navigate("/") //ON SUCESSS LOGIN PAGE IS OPENED

          }catch(err){
            const detail=err.response?.data?.detail
            if(!detail){
                setError("SERVER DOWN INTERNAL ERROR ")
            }
            else if(Array.isArray(detail)){
                setError(detail[0].msg.replace("Value error, ", ""))
            }
            else{
                setError(detail) //HTTP EXPECTION
            }
          }


    }
    const inputClass = "w-full border border-gray-300 rounded-md px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-navy"
    return (
       <div className="min-h-[calc(100vh-80px)] bg-gray-50 flex items-center justify-center px-4 py-8">
       <div className="bg-white w-full max-w-md rounded-lg shadow-md border-t-4 border-gold p-8">
       <h2 className="text-2xl font-bold text-navy text-center mb-1">Create Student Account</h2>
       <p className="text-sm text-gray-500 text-center mb-6">Use your SZABIST email to register</p>
       <form onSubmit={handleSubmit}>
        <label className="block text-sm font-medium text-navy mb-1">Full Name</label>
        <input type="text" name="name" value={formdata.name} onChange={handleChange} placeholder="Enter your Official Name" className={inputClass} required/>
        <label className="block text-sm font-medium text-navy mb-1">Email</label>
        <input type="email" name="email" value={formdata.email} onChange={handleChange} placeholder="name@szabist.edu.pk" className={inputClass} required/>
        <label className="block text-sm font-medium text-navy mb-1">Password</label>
        <input type="password" name="password" onChange={handleChange} value={formdata.password} minLength={8} maxLength={16} className={inputClass} required/>
        
                <label className="block text-sm font-medium text-navy mb-1">Enter your Program Name</label>
                <select name="program" value={formdata.program} onChange={handleChange} className={inputClass}>
                    <option value="BBA">BBA</option>
                    <option value="BSAF">BSAF</option>
                    <option value="BSCS">BSCS</option>
                    <option value="BSSE">BSSE</option>
                    <option value="BEME">BEME</option>
                    <option value="BSAI">BSAI</option>
                    <option value="BSSS">BSSS</option>
                    <option value="BSASAI">BSASAI</option>
                </select>
           
                <label className="block text-sm font-medium text-navy mb-1">Registration Number</label>
                <input type="text" name="reg_no" value={formdata.reg_no} onChange={handleChange} placeholder="Enter your Szabist Registration ID:" className={inputClass} required/>
            
        {error && <p className="text-red-600 text-sm mb-4">{error}</p>}
        <button type="submit" className="w-full bg-navy text-white font-semibold py-2 rounded-md hover:opacity-90 transition">Sign Up</button>
        </form>
        <p className="text-sm text-center text-gray-500 mt-4">Already have an account?{" "}
        <Link to="/" className="text-navy font-semibold hover:underline">Login</Link>
        </p>
       </div>
       </div>
    )
}