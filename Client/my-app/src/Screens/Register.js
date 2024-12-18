import "./Register.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const navigation = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async () => {
    try {
      const response = await fetch("http://localhost:3000/users/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userName: username, password }),
      });

      const data = await response.json();
      if (response.ok) {
        navigation("/login");
        setError("");
      } else {
        setError(data.message || "Failed to register.");
      }
    } catch (err) {
      setError("An error occurred while registering.");
    }
  };

  return (
    <div className="d-flex align-items-center flex-column change aaaa">
      <h2 className="display-4 mb-5" id="register">
        Register
      </h2>
      <div className="input-group mb-5 w-75">
        <span className="input-group-text">
          <i className="bi bi-person"></i>
        </span>
        <div className="form-floating w-75">
          <input
            type="text"
            className="form-control"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <label>Username</label>
        </div>
      </div>
      <div className="input-group mb-5 w-75">
        <span className="input-group-text">
          <i className="bi bi-lock-fill"></i>
        </span>
        <div className="form-floating w-75">
          <input
            type="password"
            className="form-control"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <label>Password</label>
        </div>
      </div>
      {error && <p className="text-danger">{error}</p>}
      {message && <p className="text-success">{message}</p>}
      <button onClick={handleRegister} className="btn btn-primary mb-5 buttons">
        Register
      </button>
    </div>
  );
};

const Reg = () => {
  return (
    <div className="container">
      <div className="row justify-content-center row-equal-height">
        <div className="col-12 col-md-4 neon-div order-2 order-md-1" id="left">
          <Register />
        </div>
        <div className="col-12 col-md-8 order-1 order-md-2" id="right">
          <img src="/picture1.jpg" alt="ping pong paddles" className="img-fluid full-img" />
        </div>
      </div>
    </div>
  );
};

export { Reg };
