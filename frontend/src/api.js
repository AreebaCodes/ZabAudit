import axios from "axios"  //HELPS IN CONNECTING FRONTEND AND BACKEND
//CREATING CONNECTION
const api=axios.create({
    baseURL:"http://localhost:8000",
});
//EXPORTING
export default api;
