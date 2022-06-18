import React, { useEffect, useState } from "react";
import axios from "../../axios";
import {Link} from 'react-router-dom'

function Courses() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get("/api/courses/").then((response) => setCourses(response.data));
  }, []);

  return (
    <section id="popular-courses" className="courses">
      <div className="container" data-aos="fade-up">
        <div className="section-title">
          <p className="lng-kurser">Կուրսեր</p>
        </div>

        <div className="row ellen" data-aos="zoom-in" data-aos-delay="100">
          {courses.map((item) => {
            return (
              <div className="col-lg-3 col-md-6 d-flex align-items-stretch" key={item.id}>
                <div className="course-item">
                  <div className='cours-item-image'>
                    <Link to='/courses'>
                    <img src={item.image} className="img-fluid-courses" alt="..." />
                    </Link>
                  </div>
                  
                  <div className="course-content">
                    <div className="d-flex justify-content-between align-items-center mb-3">
                      <h4>{item.title}</h4>
                      <p className="price">$169</p>
                    </div>
                    <div className='short_description'>
                      <p>{item.short_description}</p>
                    </div>
                    

                    <div className='d-flex justify-content-end align-self-end'>
                      <Link className="btn btn-primary courses-button" to="/register" role="button">Գրանցվել հիմա</Link>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}


        </div>
      </div>
    </section>
  );
}

export default Courses;
