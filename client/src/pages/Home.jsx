const Home = () => {
  const handleShopNowClick = () => {
    console.log('Shop Now button clicked');
  };

  return (
    <div className="bg-black text-white container mx-auto p-10 text-center flex flex-col items-center">
      <h2 className="text-4xl font-bold mb-6">Welcome to Our Furniture Store</h2>
      <p className="text-xl mb-8">Explore our amazing furniture collection.</p>
      <button 
        className="px-6 py-2 bg-white text-black font-semibold rounded-lg shadow-lg hover:bg-gray-300 transition duration-300"
        onClick={handleShopNowClick}
        type="button"
        aria-label="Shop Now"
      >
        Shop Now
      </button>
    </div>
  );
};

export default Home;