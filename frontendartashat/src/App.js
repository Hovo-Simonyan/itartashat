import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import AboutPage from "./pages/AboutPage";
import EventPage from "./pages/EventPage";
import CoursePage from "./pages/CoursePage";
import MaterialPage from "./pages/MaterialPage";
import RegisterPage from "./pages/RegisterPage";


import "./style.css";
import { Routes, Route } from "react-router-dom";


function App() {
  return (
    <div>
      <Header />

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/materials" element={<MaterialPage />} />
        <Route path="/events" element={<EventPage />} />
        <Route path="/courses" element={<CoursePage />} />
        <Route path="/register" element={<RegisterPage />} />

      </Routes>

      <Footer />
    </div>
  );
}

export default App;
