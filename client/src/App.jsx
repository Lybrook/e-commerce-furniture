import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Products from "./pages/Products";
// import Orders from "./pages/Orders";
import CreateProduct from "./pages/CreateProduct";
import "./index.css";

export default function App() {
  return (
    <Router>
      <Navbar />
      <div className="container mx-auto p-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<Products />} />
          {/* <Route path="/orders" element={<Orders />} /> */}
          <Route path="/create-product" element={<CreateProduct />} />
        </Routes>
      </div>
    </Router>
  );
}