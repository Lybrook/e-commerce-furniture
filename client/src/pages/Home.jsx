import { Link } from "react-router-dom";

const Home = () => {
  const handleShopNowClick = () => {
    console.log('Shop Now button clicked');
  };

  return (
    <div className="bg-gray-100 min-h-screen flex flex-col items-center justify-center">
      <div className="bg-white shadow-lg rounded-lg p-10 text-center">
        <h2 className="text-4xl font-bold mb-6 text-gray-800">Welcome to Our Furniture Inventory</h2>
        <p className="text-xl mb-8 text-gray-600">Explore our amazing furniture collection.</p>
        <Link to="/products">
        </Link>
      </div>
    </div>
  );
};

export default Home;