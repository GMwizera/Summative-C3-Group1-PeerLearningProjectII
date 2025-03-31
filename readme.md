Here’s a detailed README template for your app. You can customize this further depending on your app's specifics.

---

# **Peer Learning Reservation System - README**

## **Table of Contents:**

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation Instructions](#installation-instructions)
5. [App Functionality](#app-functionality)
6. [User Flow](#user-flow)
7. [Database Setup](#database-setup)
8. [How to Use the App](#how-to-use-the-app)
9. [Troubleshooting](#troubleshooting)
10. [License](#license)

---

## **Overview**

The Peer Learning Reservation System is a Python-based command-line application that allows users to:

- Register and log in.
- Search available venues based on their category, price, and rating.
- Reserve seats in venues like concerts, restaurants, parks, etc.
- View their bookings.

This app is designed for users who want to explore available venues, make reservations, and manage their bookings efficiently.

---

## **Features**

- **User Registration & Login**: Allows users to register with a username and email, and log in using their credentials.
- **Venue Search**: Users can search for available venues by category (e.g., restaurants, concerts) and filter by price and rating.
- **Reservation System**: Allows users to reserve a specified number of seats at a venue.
- **Booking Management**: Users can view their bookings and the details of each reservation.

---

## **Technologies Used**

- **Python**: The main programming language used for the app.
- **MySQL**: A relational database to store user data and venue information.
- **Hashlib**: Used to hash user passwords securely before storing them in the database.
- **MySQL Connector**: Used to interact with the MySQL database from the Python script.

---

## **Installation Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/PeerLearning-Reservation-System.git
   cd PeerLearning-Reservation-System
   ```

2. **Install dependencies**:
   Make sure Python 3.7+ is installed, and then install the required Python libraries.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the MySQL Database**:
   - Set up a MySQL database using the instructions below. You can modify the database credentials in the app to connect it to your local or remote MySQL database.

4. **Run the app**:
   - Start the app by running:
     ```bash
     python3 main.py
     ```

---

## **App Functionality**

### **1. User Registration & Login**

- **Registration**: The first time a user interacts with the app, they are asked to register. The app will prompt the user for a `username`, `email`, and `password`. 
    - The password is securely hashed and stored in the database.
    - If a user attempts to register with an existing username, they will be prompted that the username is already taken.
  
- **Login**: Once registered, users can log in using their `username` and `password`. The password is verified against the stored hashed password in the database.

### **2. Venue Search**

- After logging in, users can search for venues by choosing a category (Restaurant, Concert, etc.). 
    - The app filters venues based on user-defined criteria: maximum price and minimum rating (0-5).
    - Available venues are then listed with their respective attributes such as `name`, `category`, `price`, `rating`, and `availability`.

### **3. Reservation System**

- Users can make reservations at available venues by specifying the `Venue ID` and the `number of seats`.
    - After confirming, the reservation is recorded in the database with the corresponding `user_id`, `venue_id`, and the number of `seats_reserved`.

### **4. Booking Management**

- Users can view their reservations by selecting the "View My Bookings" option.
    - The app will display all reservations made by the logged-in user, including details like `venue_name`, `seats_reserved`, and `reservation_time`.

---

## **User Flow**

1. **User Registration**: 
   - User enters username, email, and password.
   - The system checks if the username exists. If not, registration is successful.

2. **Login**:
   - User enters username and password to log in.
   - If credentials match, the user is logged in and redirected to the main menu.

3. **Venue Search**:
   - User selects a category and enters filters (max price and min rating).
   - The app displays a list of matching venues.

4. **Reservation**:
   - User selects a venue and enters the number of seats to reserve.
   - The reservation is recorded, and the user receives confirmation.

5. **View Bookings**:
   - User can view their past and current reservations.

---

## **Database Setup**

1. **Create a MySQL database** for the app, and set up the required tables (`users`, `venues`, `reservations`).

2. **Run the following SQL script to set up the tables**:

   ```sql
   CREATE DATABASE IF NOT EXISTS summative;

   USE summative;

   CREATE TABLE users (
       user_id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) UNIQUE,
       email VARCHAR(100),
       password VARCHAR(255)
   );

   CREATE TABLE venues (
       venue_id INT AUTO_INCREMENT PRIMARY KEY,
       venue_name VARCHAR(100),
       category VARCHAR(50),
       location VARCHAR(100),
       price DECIMAL(10, 2),
       rating INT,
       available_seats INT
   );

   CREATE TABLE reservations (
       reservation_id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT,
       venue_id INT,
       seats_reserved INT,
       reservation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (user_id) REFERENCES users(user_id),
       FOREIGN KEY (venue_id) REFERENCES venues(venue_id)
   );
   ```

3. Modify the database credentials (`db.py`) to connect to your MySQL server.

---

## **How to Use the App**

1. **Run the Application**: 
   - After setting up the database and installing dependencies, run the app by executing `python3 main.py`.

2. **Register**: 
   - If you're a new user, select `R` to register. Provide a username, email, and password.

3. **Log in**: 
   - If you already have an account, select `L` to log in using your username and password.

4. **Search for Venues**: 
   - Once logged in, you can search for venues based on the category, maximum price, and minimum rating.

5. **Make a Reservation**: 
   - Choose a venue and reserve seats. Enter the number of seats to reserve, and the reservation will be saved.

6. **View Bookings**: 
   - Check your past and upcoming reservations by selecting `View My Bookings`.

---

## **Troubleshooting**

- **"Invalid credentials" during login**: 
   - Ensure that the username and password are entered correctly. Passwords are hashed, so verify that you are using the correct password.

- **"Database connection error"**: 
   - Ensure that the MySQL server is running and the database credentials are correct.

- **"No venues found"**: 
   - Ensure that venues have been correctly inserted into the database.

---


