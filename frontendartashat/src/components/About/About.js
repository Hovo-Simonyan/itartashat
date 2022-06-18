import React from "react";
import "./about.css";
import carusel2 from "../../img/carusel2.jpg";

function About() {
  return (
    <section id="about" className="about">
      <div className="container" data-aos="fade-up">
        <div className="row">
          <div
            className="col-lg-6 order-1 order-lg-2"
            data-aos="fade-left"
            data-aos-delay="100"
          >
            <img src={carusel2} className="img-fluid" alt="" />
          </div>
          <div className="col-lg-6 pt-4 pt-lg-0 order-2 order-lg-1 content">
            <h3 className="lng-mer">Մեր Մասին</h3>
            <p className="fst-italic">
              ԱյԹի Արտաշատ ծրագրավորման կենտրոնը (ԱյԹի Արտաշատ ԾԿ) կազմավորվել է
              2021թվականի հունիսին։ Մասնագիտական կրթական ծրագրերով ընկերությունը
              իրականացնում է խաղերի ծրագրավորման, վեբ ծրագրավորման,խոսակցական
              անգլերենի,օֆիս ծրագրերի ուսուցում և ընդունում է վեբ կայքերի ու
              գովազդների մուլտիֆիկացման/անիմացիոն պատվերներ։ Ծրագրավորման
              կենտրոնը նաև իրականացնում է <b>վերապատրաստման</b> և{" "}
              <b>որակավորման բարձրացման</b>
              ծրագրեր։ Ի տարբերություն այլ այթի կենտրոնների ,այստեղ կարող են
              սովորել նշված թվային մասնագիտությունները սկսած յոթ տարեկանից բոլոր
              տրամաբանող ինդիվիդուալները։
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default About;
