import { useState, useEffect } from "react";

const Orders = () => {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchOrders = async () => {
      setIsLoading(true);
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
        setIsLoading(false);
      }
    };
    fetchOrders();
  }, []);

  if (isLoading) {
    return (
      <div className="p-10">
        <h2 className="text-xl font-bold">Orders</h2>
        <p>Loading...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-10">
        <h2 className="text-xl font-bold">Orders</h2>
        <p>Error: {error}</p>
      </div>
    );
  }

  if (orders.length === 0) {
    return (
      <div className="p-10">
        <h2 className="text-xl font-bold">Orders</h2>
        <p>No orders found.</p>
      </div>
    );
  }

  return (
    <div className="p-10">
      <h2 className="text-xl font-bold">Orders</h2>
      <ul className="list-disc pl-5">
        {orders.map((order) => (
          <li key={order.id}>
            Order #{order.id} - Total Cost: ${order.total_cost}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Orders;