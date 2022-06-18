import React from 'react'
import Main from '../components/Main/Main'

import About from '../components/About/About';

import Count from '../components/Count/Count';
import Courses from '../components/Courses/Courses';
import Trainers from '../components/Trainers/Trainers';



function HomePage() {
  return (
    <>
      <Main />
      <About />
      <Count/>
      <Courses/>
      <Trainers/>
    </>
  )
}

export default HomePage