import React from 'react'
import './main.css'
import { Link } from "react-router-dom";

function Main() {
  return (
    <section id="hero" className="d-flex justify-content-center align-items-center">
        <div className="container position-relative" data-aos="zoom-in" data-aos-delay="100">
            <h1 className="lng-sovorir">Սովորի՛ր այսօր,<br />Սովորի՛ր վաղը, <br />Կերտի՛ր ապագադ հիմա</h1>
            <Link to="/register" className="btn-get-started lng-sksenq">Սկսենք հիմա</Link>
        </div>
    </section>
  )
}

export default Main