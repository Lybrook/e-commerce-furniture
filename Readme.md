# Inventory Furniture Store

This is a full-stack Inventory application for keeping records of furniture. The backend is built using Flask, while the frontend is developed with React.

##Links
https://e-commerce-furniture-six.vercel.app/
https://e-commerce-furniture-uepv.onrender.com

## Features

### Backend (Flask API)
- Built with Flask.
- Uses a Pipfile for dependency management.
- At least three models, including:
  - Two one-to-many relationships.
  - One reciprocal many-to-many relationship with an additional user-submittable attribute.
- Full CRUD actions for at least one resource.
- Create and read actions for each resource.
- Form validation using Formik.
- Data type validation and string/number format validation.
- Authentication implemented.
- Connected to a React frontend via fetch requests.
- Deployment on Render.

### Frontend (React)
- Built with React and React Router.
- Uses Tailwind CSS for styling.
- At least three client-side routes.
- Navigation UI for seamless route switching.
- Fetch requests to connect with the backend API.
- Five core components:
  - `App.jsx`
  - `Home.jsx`
  - `Navbar.jsx`
  - Two additional components for specific features.
- Persistent cart functionality.

## Project Structure

```
E-Commerce-Furniture-Store/
│-- backend/                # Flask backend
│   ├── models.py           # Database models
│   ├── routes.py           # API routes
│   ├── app.py              # Main Flask app
│   ├── Pipfile             # Dependencies
│-- frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   ├── App.jsx         # Main app component
│   │   ├── index.js        # Entry point
│   │   ├── index.css       # Tailwind CSS styles
│   ├── package.json        # Frontend dependencies
│-- README.md               # Documentation
```

## Installation & Setup

### Backend Setup (Flask)
1. Clone the repository and navigate to the backend folder:
   ```bash
   git clone https://github.com/Lybrook/e-commerce-furniture
   cd backend
   ```
2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```
3. Run the Flask app:
   ```bash
   pipenv run flask run
   ```

### Frontend Setup (React)
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```

## Deployment
- Backend is deployed on **Render**.
- Frontend can be deployed on **Vercel** or **Netlify**.

## Contributing
Feel free to fork the repository and create pull requests with enhancements or bug fixes.

## License
This project is licensed under the MIT License.

