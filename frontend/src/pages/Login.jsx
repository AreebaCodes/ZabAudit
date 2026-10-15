import { useState } from "react";
import api from '../api'
function Login(){
    //INTIALIZING VARIABLES FOR FORM (UI)
    const[email,setEmail]=useState("") //DEFAULT VALUE EMPTY STRING
    const[password,setPassword]=useState("") //DEFAULT VALUE EMPTY STRING
    const [role,setRole]=useState("PM")  //PROGRAM MANAGER IS DEFAULT ROLE

    //CREATING HANDLE FUNCTION FOR BACKEND LOGIC WHEN USERS SUBMITS DATA
    async function handleSubmit(e){
        e.preventDefault()  //TO PREVENT DEFAULT FORM SUBMISSION 
        //DIFFERENT ENDPOINTS FOR DIFFERENT ROLES THAT' WHY  THERE IS A CONDITION IN ROLE
        const route=role=="PM"? "/pm/login": "/student/login"  //ROLE IS CHECKEDTHERE
        
        try{
        const response=await api.post(route,{email,password})
        console.log(response.data)  //JUST FOR TESTING PURPOSE
        }catch(error){
        console.log(error)
        }
    }
    return(
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
        
        <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md border-t-4 border-gold">
            
            <h1 className="text-2xl font-bold text-navy mb-1"> Login </h1>
            <p className="text-gray-500 text-sm mb-6">Sign in to access your Dashboard</p>
            <div className="flex gap-2 mb-6">
            <button type="button" onClick={()=>setRole("PM")} className={`flex-1 py-2 rounded-md font-semibold text-sm transition ${role === "PM" ? "bg-navy text-white" : "bg-gray-100 text-gray-500"}`} >Program Manager</button>
            <button type="button" onClick={()=>setRole("Student")} className={`flex-1 py-2 rounded-md font-semibold text-sm transition ${role === "Student" ? "bg-navy text-white" : "bg-gray-100 text-gray-500"}`}>Student</button>
            </div>
            <label htmlFor="email" className="block text-sm font-semibold text-navy mb-1">Enter your Email</label> 
            <input type="text" id="email" name="email" value={email} onChange={(e)=>setEmail(e.target.value)} className="w-full border border-gray-300 rounded-md px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-navy"></input> 
            <label htmlFor="password" className="block text-sm font-semibold text-navy mb-1">Enter your Password</label> 
            <input type="password" id="password" name="password" value={password} onChange={(e)=>setPassword(e.target.value)} className="w-full border border-gray-300 rounded-md px-3 py-2 mb-4 focus:outline-none focus:ring-2 focus:ring-navy"></input> 
            <button type="submit" className="w-full bg-navy text-white font-bold py-2 rounded-md hover:opacity-90 transition">Login</button>  
        </form>
        </div>
    )
}

export default Login;