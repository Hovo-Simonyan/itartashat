import React, { useEffect, useState } from "react";
import axios from "../../axios";

function Trainers() {
  const [trainers, setTrainers] = useState([]);

  useEffect(() => {
    axios.get("/api/teachers/").then((response) => setTrainers(response.data));
  }, []);

  return (
    <section id="trainers" className="trainers">
      <div className="container" data-aos="fade-up">
        <div className="section-title">
          <p className="lng-kurser">Դասավանդողներ</p>
        </div>
        <div className="row" data-aos="zoom-in" data-aos-delay="100">
          {trainers.map((item) => {
            return (
              <div
                className="col-lg-3 col-md-6 d-flex align-items-stretch"
                key={item.id}
              >
                <div className="member">
                  <img
                    src={"http://127.0.0.1:8000" + item.image}
                    className="img-fluid img-fluid-member"
                    alt=""
                  />
                  <div className="member-content">
                    <h4 className="lng-serin">
                      {item.first_name} {item.last_name}
                    </h4>
                    <span className="lng-webser">{item.position}</span>
                    <p>{item.about_teacher}</p>
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

export default Trainers;
