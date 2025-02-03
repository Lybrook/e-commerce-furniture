import { Link } from "react-router-dom";

const Navbar = () => {
  const navLinks = [
    { id: 1, to: "/", text: "Home" },
    { id: 2, to: "/products", text: "Products" },
    { id: 3, to: "/create-product", text: "Create Product" },
  ];

  return (
    <nav className="bg-blue-800 text-white p-4 shadow-lg">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">Furniture Inventory</h1>
        <ul className="flex space-x-6">
          {navLinks.map((link) => (
            <li key={link.id}>
              <Link
                to={link.to}
                className="hover:text-gray-300 transition duration-300"
              >
                {link.text}
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;