import React, { useState } from 'react';
import { registerUser } from '../api/api';
import './RegisterForm.css';

const RegisterForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(false);

    const handleSubmit = async (e) => {
        const data = {username, password};
        try {
            const response = await registerUser(data);
            console.log("Registration successful",response);
            setSuccess(true);
        } catch (error) {
            setError(error.message);
            console.log("Registration failed",error);
            setSuccess(false);
        }
    }

    return (
        <form className = "form">
                <label>
                    Username
                </label>
                <input type = "text" value = {username} onChange = {(e) => setUsername(e.target.value)}/>

            <label>Password:</label>
            <input type = "password" value = {password} onChange = {(e) => setPassword(e.target.value)}/>
            
            <button type = "submit" onClick = {handleSubmit}>Register</button>
        </form>

    )
}

export default RegisterForm;
