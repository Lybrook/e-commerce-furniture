import { useState, useEffect } from "react";

const OrderList = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetch("/api/orders")
      .then((res) => res.json())
      .then((data) => setOrders(data))
      .catch((error) => console.error("Error fetching orders:", error));
  }, []);

  return (
    <div className="p-10">
      <h2 className="text-2xl font-bold mb-4">Order List</h2>
      <ul className="list-disc pl-5">
        {orders.length > 0 ? (
          orders.map((order) => (
            <li key={order.id} className="p-2 border-b">
              Order #{order.id} - <span className="font-bold">${order.total_cost}</span>
            </li>
          ))
        ) : (
          <p>No orders placed yet.</p>
        )}
      </ul>
    </div>
  );
};

export default OrderList;
