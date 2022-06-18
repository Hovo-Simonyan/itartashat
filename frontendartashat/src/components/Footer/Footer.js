import axios from "../../axios";
import React, { useEffect, useState } from "react";
import {Link} from 'react-router-dom'

function Footer() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get("/api/courses/").then((response) => setCourses(response.data));
  }, []);

  return (
    <footer id="footer">
      <div className="footer-top">
        <div className="container">
          <div className="row">
            <div className="col-lg-4 col-md-6 footer-contact">
              <h3>IT Artashat</h3>
              <p className="lng-footerP">
                ՀՀ <br />
                Ք․Արտաշատ <br />
                Օգոստոսի 23 115/3 <br />
                <br />
                <strong>Phone number:</strong> +374 94-10-76-94
                <br />
                <strong>Phone number:</strong> +374 33-10-76-94
                <br />
                <strong>Email:</strong> <a href="">itartashat@gmail.com</a>
                <br />
              </p>
            </div>

            <div className="col-lg-4 col-md-6 footer-links">
              <h4 className="lng-kurshxum">Կուրսերի Հղումներ</h4>
              <ul>
              {courses.map((item) => {
                return (
                    <li>
                      <i className="bx bx-chevron-right"></i>
                      <Link to="/courses" className="lng-veebc">
                        {item.title} -- {item.absolute_url}
                      </Link>
                    </li>
                );
              })}
              </ul>
            </div>

            <div className="col-lg-4 col-md-6 footer-newsletter">
              <h4>Բաժանորդագրվել</h4>
              <form action="" method="post">
                <input type="email" name="email" />
                <input type="submit" value="Բաժանորդագրվել" disabled />
              </form>
            </div>
          </div>
        </div>
      </div>

      <div className="container d-md-flex py-4">
        <div className="me-md-auto text-center text-md-start">
          <div className="copyright">
            &copy; Copyright{" "}
            <strong>
              <span>IT Artashat</span>
            </strong>
            . All Rights Reserved
          </div>
          <div className="credits"></div>
        </div>
        <div className="social-links text-center text-md-right pt-3 pt-md-0">
          <a
            href="https://www.facebook.com/ITartashat/"
            className="facebook"
            target="_blank"
          >
            <i className="bx bxl-facebook"></i>
          </a>
          <a
            href="https://www.instagram.com/itartashat/?igshid=YmMyMTA2M2Y="
            className="instagram"
            target="_blank"
          >
            <i className="bx bxl-instagram"></i>
          </a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
