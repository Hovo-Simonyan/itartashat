import React from "react";
import logo from "./logo.png";
import drosh1 from "./drosh1.png"
import drosh2 from "./drosh2.jpg"
import { Link } from "react-router-dom";

function Header() {
  return (
    <header id="header" className="fixed-top">
      <div className="container-fluid d-flex align-items-center justify-content-around w-100">
        <div>
          <h1 className="logo me-auto">
            <Link to="/">
              <div className="logoDiv">
                <img className="imImg" src={logo} alt="" />
              </div>
            </Link>
          </h1>
        </div>

        <div className="d-flex">
          <nav id="navbar" className="navbar order-last order-lg-0">
            <ul>
              <li>
                <Link to="/about" className="lng-masin">
                  Մեր մասին
                </Link>
              </li>

              
              <li>
                <Link to="/events" className="lng-mijocarum">
                  Միջոցառումները
                </Link>
              </li>

              <li>
                <Link
                  to="/courses"
                  className="lng-nviraberel"
                >
                  Կուրսեր
                </Link>
              </li>
              <li>
                <Link to="/materials" className="lng-kap">
                Դասեր
                </Link>
              </li>
              <li>
                <Link to="/register" className="lng-kap">
                Գրացվել
                </Link>
              </li>
            </ul>
            <i className="bi bi-list mobile-nav-toggle"></i>
          </nav>
          {/* <Link to="/register" className="get-started-btn lng-mianal">
            Միանալ Հիմա
          </Link> */}
          <Link to="/login" className="get-started-btn lng-mianal">
            Մուտք գործել
          </Link>
        </div>

        <div className="obsh">
          <div className="drosh1">
            <a href="#something">
              <img src={drosh1} alt="" />
            </a>
          </div>
          <div className="drosh2">
            <a href="#something">
              <img src={drosh2} alt="" />
            </a>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;
