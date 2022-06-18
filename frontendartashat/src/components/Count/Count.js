import React from "react";
import './count.css'
import axios from '../../axios.js'
import {useEffect, useState} from "react"

function Count() {

  const [count, setCount] = useState({})

  useEffect(() => {
    axios.get('/api/total-info/')
      .then(response => setCount(response.data))
  }, [])



  return (
    <section id="counts" className="counts section-bg">
      <div className="container">
        <div className="row counters">
          <div className="col-lg-3 col-6 text-center">
            <span
              data-purecounter-start="0"
              data-purecounter-end="160"
              data-purecounter-duration="1"
              className="purecounter"
            ></span>
            <span>{count.students}</span>
            <p>ՈԻսանող</p>
          </div>

          <div className="col-lg-3 col-6 text-center">
            <span
              data-purecounter-start="0"
              data-purecounter-end="5"
              data-purecounter-duration="1"
              className="purecounter"
            ></span>
            <span>{count.courses}</span>
            <p>Կուրսեր</p>
          </div>

          <div className="col-lg-3 col-6 text-center">
            <span
              data-purecounter-start="0"
              data-purecounter-end="17"
              data-purecounter-duration="1"
              className="purecounter"
            ></span>
            <span>{count.events}</span>
            <p>Միջոցառումներ</p>
            
          </div>

          <div className="col-lg-3 col-6 text-center">
            <span
              data-purecounter-start="0"
              data-purecounter-end="4"
              data-purecounter-duration="1"
              className="purecounter"
            ></span>
            <span>{count.teachers}</span>
            <p>Դասավանդողներ</p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Count;
