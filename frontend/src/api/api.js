import API from "./axios";

export const registerUser = async (data) =>{
    try {
        const response = await API.post("/register",data)
        return response.data
    } catch (error) {
        throw error.response.data
    }
}

export const loginUser = async (data) => {try {
    const response = await API.post("/login",data)
    return response.data
} catch (error) {
    throw error.response.data
}}

