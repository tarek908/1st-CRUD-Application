#Django CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application built with Django. It allows users to insert, view, edit, and delete user details, and comes with API integration for public data fetching. Below are the core features and functionalities of the application.

Features:

Insert User Details: A form allows users to insert their profile image, name, occupation (title), email, and a short description.

Public Data Fetching: The data entered by the user is fetched from the database and displayed publicly through an API, ensuring real-time access to updated information.

##Edit Functionality:

A button on the public data page allows users to edit the data.

It opens a pre-filled form with the existing data, allowing users to modify and update their information easily.


##Delete Functionality:

There is a delete button to remove all user data from the database.

Before deletion, a confirmation pop-up is shown to ensure accidental deletion is avoided.

##Technologies Used:

Django: Backend framework

HTML/CSS/Bootstrap: Frontend styling

SQLite: Default database (easily switchable to other databases like MySQL/PostgreSQL)

Django REST Framework: For building the API

