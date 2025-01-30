import { useState, useEffect } from "react";

const UserProfile = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch("/api/user");
        if (!response.ok) {
          throw new Error("Failed to fetch user data");
        }
        const data = await response.json();
        setUser(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setIsLoading(false);
      }
    };
    fetchUser();
  }, []);

  if (isLoading) {
    return (
      <div className="p-10">
        <h2 className="text-2xl font-bold mb-4">User Profile</h2>
        <p>Loading...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-10">
        <h2 className="text-2xl font-bold mb-4">User Profile</h2>
        <p>Error: {error}</p>
      </div>
    );
  }

  return (
    <div className="p-10">
      <h2 className="text-2xl font-bold mb-4">User Profile</h2>
      {user ? (
        <div className="border p-4 rounded-lg shadow-md">
          <h3 className="font-bold text-lg">{user.name}</h3>
          <p>Email: {user.email}</p>
          <p>Joined: {new Date(user.created_at).toLocaleDateString()}</p>
        </div>
      ) : (
        <p>No user data available.</p>
      )}
    </div>
  );
};

export default UserProfile;