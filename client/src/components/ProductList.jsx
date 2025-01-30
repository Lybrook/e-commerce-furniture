import { useState, useEffect } from "react";

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch("/api/products");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="p-10">
      <h2 className="text-2xl font-bold mb-4">Product List</h2>
      <div className="grid grid-cols-3 gap-6">
        {products.length > 0 ? (
          products.map((product) => (
            <div key={product.id} className="border p-4 rounded-lg shadow-md">
              <img
                src={product.image_url}
                alt={product.name}
                className="w-full h-32 object-cover rounded-md"
              />
              <h3 className="font-bold text-lg mt-2">{product.name}</h3>
              <p className="text-gray-700">{product.description}</p>
              <p className="text-blue-600 font-bold mt-2">${product.price}</p>
            </div>
          ))
        ) : (
          <p>No products available.</p>
        )}
      </div>
    </div>
  );
};

export default ProductList;