# 🛒 Brain Rot Shop 🤑

**Brain Rot Shop** is a simple e-commerce web application built with Flask.  
It allows users to browse products, add items to their cart, and proceed to checkout.

---

## 🚀 Features

- **Product Listing**: View a list of products with their names, prices, and images.
- **Shopping Cart**: Add, remove, and update quantities of items in the cart.
- **Checkout**: Submit an order with personal and payment details.
- **Contact Page**: View contact information for the shop.

---

## 🧰 Requirements

- Python 3.11  
- Flask 2.3.2  
- Docker (optional, for containerized deployment)

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/leonard2005n/Brain-Rot-Shop
   cd Brain-Rot-Shop
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python server.py
   ```

4. Open your browser and navigate to:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t brain-rot-shop .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 brain-rot-shop
   ```

3. Access the application at:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 🔑 Login

1. Navigate to the login page:  
   [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

2. Use the following credentials to log in:
   - **Username**: `admin`
   - **Password**: `password123`

3. Once logged in, you can browse the shop and manage your cart.

4. To log out, click the **Logout** link in the navigation bar.

---
## 🧑‍💻 Usage

### 🛍️ Product Listing
- View all available products on the homepage.
- Click **"Add to Cart"** to add a product to your shopping cart.

### 🛒 Shopping Cart
- View your cart by clicking the **"Cart"** link in the navigation bar.
- Update item quantities or remove items from the cart.

### 💳 Checkout
- Proceed to checkout by clicking **"Proceed to Checkout"** in the cart.
- Fill out the form with your details and submit your order.

---

## 📁 File Descriptions

- `server.py`: The main Flask application that handles routes and logic.
- `products.py`: Contains the product data used in the application.
- `templates/`: HTML templates for the application.
- `static/`: Static assets like CSS and images.
- `requirements.txt`: Lists the Python dependencies.
- `Dockerfile`: Configuration for containerizing the application.