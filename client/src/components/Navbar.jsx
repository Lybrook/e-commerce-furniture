import { Link } from "react-router-dom";

const Navbar = () => {
  const navLinks = [
    { id: 1, to: "/", text: "Home" },
    { id: 2, to: "/products", text: "Products" },
    { id: 3, to: "/orders", text: "Orders" },
  ];

  return (
    <nav className="bg-blue-600 text-white p-4 flex justify-between">
      <h1 className="text-xl font-bold">E-Commerce</h1>
      <ul className="space-x-4">
        {navLinks.map((link) => (
          <li key={link.id}>
            <Link to={link.to} className="hover:underline">
              {link.text}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Navbar;