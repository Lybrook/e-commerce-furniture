import { useState, useEffect } from "react";

const Orders = () => {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await fetch("/api/orders");
        if (!response.ok) {
          throw new Error("Failed to fetch orders");
        }
        const data = await response.json();
        setOrders(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };
    fetchOrders();
  }, []);

  const handleAddProduct = async (orderId, productId) => {
    try {
      const productResponse = await fetch(`/api/products/${productId}`);
      if (!productResponse.ok) {
        throw new Error("Failed to fetch product details");
      }
      const product = await productResponse.json();

      const response = await fetch("/api/order_products", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ order_id: orderId, product_id: productId, quantity: 1 }),
      });
      if (!response.ok) {
        throw new Error("Failed to add product to order");
      }
      const updatedOrder = await response.json();

      setOrders(orders.map((order) => {
        if (order.id === updatedOrder.id) {
          return {
            ...order,
            products: [...(order.products || []), { ...product, quantity: 1 }],
            total_cost: updatedOrder.total_cost,
          };
        }
        return order;
      }));
    } catch (error) {
      setError(error.message);
    }
  };

  if (loading) {
    return <div className="flex justify-center items-center h-screen">Loading...</div>;
  }

  if (error) {
    return <div className="flex justify-center items-center h-screen text-red-600">{error}</div>;
  }

  if (orders.length === 0) {
    return <div className="p-10">No orders found.</div>;
  }

  return (
    <div className="p-10">
      <h2 className="text-2xl font-bold mb-4">Orders</h2>
      <ul className="list-none">
        {orders.map((order) => (
          <li key={order.id} className="mb-4 p-4 border rounded-lg shadow-md">
            <div className="flex justify-between items-center mb-2">
              <div>
                <h3 className="font-bold text-lg">Order #{order.id}</h3>
                <p className="text-gray-600">Total Cost: ${order.total_cost ? order.total_cost.toFixed(2) : '0.00'}</p>
              </div>
              <button
                className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                onClick={() => handleAddProduct(order.id, 1)} // Example product ID
              >
                Add Product
              </button>
            </div>
            <div className="bg-gray-100 p-2 rounded">
              <h4 className="font-semibold mb-2">Products in this order:</h4>
              <ul className="list-disc pl-5">
                {(order.products || []).map((product) => (
                  <li key={product.id} className="ml-4">
                    <span className="font-semibold">{product.name}</span> - ${product.price ? product.price.toFixed(2) : '0.00'} x {product.quantity}
                  </li>
                ))}
              </ul>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Orders;