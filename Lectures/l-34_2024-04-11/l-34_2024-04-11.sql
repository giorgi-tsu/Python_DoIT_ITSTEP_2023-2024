#One to One Relationship
#https://dotnettutorials.net/lesson/database-relationships-in-mysql/#google_vignette
 
-- Create Students Table
CREATE TABLE Students (
     Id INT PRIMARY KEY,
     Name VARCHAR(40) NOT NULL,
     Class VARCHAR(20),
     Age INT
);
 
-- Populate the Students Table with test data
INSERT INTO Students VALUES 
(1,'John', 'First', 5),
(2, 'Mary', 'Third', 7),
(3, 'Mike', 'Second', 6),
(4, 'Linda', 'Third', 7)
;

-- Create Addresses Table
CREATE TABLE Addresses (
     AddressId INT PRIMARY KEY, 
     Address VARCHAR(100) NOT NULL,
     StudentId INT NOT NULL UNIQUE,
     FOREIGN KEY (StudentId) REFERENCES Students(Id)
);
 
-- Populate the Addresses Table with test data
INSERT INTO Addresses VALUES
(1001, 'Mumbai', 1),
(1002, 'Delhi', 2),
(1003, 'BBSR', 3),
(1004, 'Hyderabad', 4)
;
 
-- INSERT INTO Addresses VALUES (1004, 'Hyderabad', 1);
 
SELECT * FROM Addresses;
 
 
 
 
#One-to-Many Relationship
#https://dev.to/elhamnajeebullah/mysql-how-to-create-one-to-many-relationship-4gph
/*The "customers" table stores information about the website's customers, including their first and last name, email, and password.*/
 
CREATE TABLE categories (
    categoryID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
 
/*The "products" table stores information about the products available for purchase on the website, including their name, price, and the category they belong to.*/
CREATE TABLE products (
    productID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    categoryID INT NOT NULL,
    FOREIGN KEY (categoryID) REFERENCES categories(categoryID)
);
 
 
INSERT INTO categories (name) 
VALUES 
('Electronics'),
('Food')
;
 
INSERT INTO products (name, price, categoryID) 
VALUES 
('Laptop', 999.99, 1),
('Milk', 0.99, 2)
;
 
INSERT INTO products (name, price, categoryID) 
VALUES 
('TV', 999.99, 1)
;
 
 
 
#Creating a many-to-many relationship
#Here is an example of how to create a many-to-many relationship between a "products" table and a "orders" table using a "orderDetails" table:
 
CREATE TABLE orders (
    orderID INT AUTO_INCREMENT PRIMARY KEY,
    studentID INT NOT NULL,
    orderDate DATE NOT NULL,
    FOREIGN KEY (studentID) REFERENCES students(Id)
);
 
CREATE TABLE orderDetails (
  orderID INT NOT NULL,
  productID INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (orderID, productID),
  FOREIGN KEY (orderID) REFERENCES orders(orderID),
  FOREIGN KEY (productID) REFERENCES products(productID)
);
 
 
INSERT INTO orders (studentID, orderDate) 
VALUES (1, '2022-01-01');
 
INSERT INTO orders (studentID, orderDate) 
VALUES 
(4, '2023-05-02'),
(3, '2024-07-03')


