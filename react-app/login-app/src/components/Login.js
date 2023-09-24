import React, { useState } from 'react';
import './Login.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Username: ${username}, Password: ${password}`);
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      <label>
        Username:
        <input type="text" value={username} onChange={(event) => setUsername(event.target.value)} />
      </label>
      <label>
        Password:
        <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      </label>
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;