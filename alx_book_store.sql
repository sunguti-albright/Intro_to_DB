/*
Imagine you’re tasked with designing a MySQL database for an online bookstore. The database should store information about books, authors, customers, orders, and order details. Here’s an overview of the database schema:
*/

-- Database Name: alx_book_store
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;
/*
Authors: Stores information about authors.
author_id (Primary Key)
author_name VARCHAR(215)
*/
CREATE TABLE IF NOT EXISTS Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);
