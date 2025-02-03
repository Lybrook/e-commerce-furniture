import { useState, useEffect } from "react";

const Products = () => {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);
  const [editProduct, setEditProduct] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch("https://e-comm-wkqo.onrender.com/products", {
          headers: {
            Accept: "application/json",
          },
        });
        if (!response.ok) {
          throw new Error("Failed to fetch products");
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
    return <div className="flex justify-center items-center h-screen">Loading...</div>;
  }

  if (error) {
    return <div className="flex justify-center items-center h-screen text-red-600">{error}</div>;
  }

  return (
    <div className="p-10">
      <h2 className="text-3xl font-bold mb-6 text-center text-gray-800">Our Products</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {products.map((product) => (
          <div key={product.id} className="bg-white p-6 border rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
            <img src={product.image_url} alt={product.name} className="w-full h-48 object-cover rounded-t-lg mb-4" />
            <h3 className="text-xl font-bold mb-2">{product.name}</h3>
            <p className="text-gray-600 mb-4">{product.description}</p>
            <p className="text-blue-600 font-bold text-lg mb-4">${product.price.toFixed(2)}</p>
            <div className="flex justify-between">
              <button
                className="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded transition duration-300"
                onClick={() => setEditProduct(product)}
              >
                Update
              </button>
              <button
                className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300"
                onClick={() => handleDelete(product.id)}
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
      {editProduct && (
        <div className="mt-10 p-6 bg-white border rounded-lg shadow-md">
          <h3 className="text-2xl font-bold mb-4">Edit Product</h3>
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleUpdate(editProduct);
              setEditProduct(null);
            }}
          >
            <div className="grid grid-cols-1 gap-4">
              <input
                type="text"
                value={editProduct.name}
                onChange={(e) => setEditProduct({ ...editProduct, name: e.target.value })}
                className="border p-2 rounded"
                placeholder="Name"
              />
              <input
                type="text"
                value={editProduct.description}
                onChange={(e) => setEditProduct({ ...editProduct, description: e.target.value })}
                className="border p-2 rounded"
                placeholder="Description"
              />
              <input
                type="number"
                value={editProduct.price}
                onChange={(e) => setEditProduct({ ...editProduct, price: parseFloat(e.target.value) })}
                className="border p-2 rounded"
                placeholder="Price"
              />
              <input
                type="text"
                value={editProduct.category}
                onChange={(e) => setEditProduct({ ...editProduct, category: e.target.value })}
                className="border p-2 rounded"
                placeholder="Category"
              />
              <input
                type="text"
                value={editProduct.image_url}
                onChange={(e) => setEditProduct({ ...editProduct, image_url: e.target.value })}
                className="border p-2 rounded"
                placeholder="Image URL"
              />
              <button type="submit" className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Save
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
};

export default Products;