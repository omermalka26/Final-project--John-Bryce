# 🏖️ Vacation Booking - Vite React App

A modern vacation booking application built with React 18 and Vite for lightning-fast development.

## Features

- **React 18** with modern hooks and features
- **Vite** for blazing fast development and builds
- **React Router DOM** for client-side routing
- **User Authentication** with JWT tokens
- **Admin Dashboard** for vacation management
- **Responsive Design** with modern CSS

## Prerequisites

- Node.js (v16 or higher)
- Flask backend running on http://localhost:5000

## Available Scripts

### `npm run dev`

Runs the app in development mode with Vite.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page reloads instantly when you make changes.\
You'll see lint errors and warnings in the console.

### `npm run build`

Builds the app for production to the `dist` folder.\
The build is optimized and includes tree-shaking and minification.

### `npm run preview`

Preview the production build locally.

## Environment Variables

Create a `.env` file in the root directory:

```
VITE_API_BASE_URL=http://localhost:5000
```

## Backend Setup

Make sure your Flask backend is running on `http://localhost:5000` with the following endpoints:

- `POST /login` - User authentication
- `POST /register` - User registration  
- `GET /vacations` - Get all vacations
- `GET /countries` - Get all countries
- And more...

## Project Structure

```
src/
├── api/           # API communication functions
├── components/    # Reusable React components
├── contexts/      # React Context providers
├── pages/         # Page components for routing
├── App.jsx        # Main application component
└── index.jsx      # Application entry point
```

## Migration from Create React App

This project was successfully migrated from Create React App to Vite for:
- ⚡ **Faster builds** (2-10x speed improvement)
- 🔥 **Instant HMR** (Hot Module Replacement)
- 📦 **Smaller bundle size** 
- 🛠️ **Better development experience**

## Learn More

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://reactjs.org/)
- [React Router](https://reactrouter.com/)
