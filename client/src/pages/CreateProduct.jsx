import { useState } from "react";

const CreateProduct = () => {
  const [product, setProduct] = useState({
    name: "",
    description: "",
    price: "",
    category: "",
    image_url: "",
  });
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setProduct({ ...product, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("https://e-commerce-furniture-uepv.onrender.com/products", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(product),
      });
      if (!response.ok) {
        throw new Error("Failed to create product");
      }
      const newProduct = await response.json();
      console.log("Product created:", newProduct);
      setProduct({
        name: "",
        description: "",
        price: "",
        category: "",
        image_url: "",
      });
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="p-10">
      <h2 className="text-3xl font-bold mb-6 text-center text-gray-800">Create Product</h2>
      {error && <div className="text-red-600 mb-4">{error}</div>}
      <form onSubmit={handleSubmit} className="grid grid-cols-1 gap-4">
        <input
          type="text"
          name="name"
          value={product.name}
          onChange={handleChange}
          className="border p-2 rounded"
          placeholder="Name"
        />
        <input
          type="text"
          name="description"
          value={product.description}
          onChange={handleChange}
          className="border p-2 rounded"
          placeholder="Description"
        />
        <input
          type="number"
          name="price"
          value={product.price}
          onChange={handleChange}
          className="border p-2 rounded"
          placeholder="Price"
        />
        <input
          type="text"
          name="category"
          value={product.category}
          onChange={handleChange}
          className="border p-2 rounded"
          placeholder="Category"
        />
        <input
          type="text"
          name="image_url"
          value={product.image_url}
          onChange={handleChange}
          className="border p-2 rounded"
          placeholder="Image URL"
        />
        <button type="submit" className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Create
        </button>
      </form>
    </div>
  );
};

export default CreateProduct;