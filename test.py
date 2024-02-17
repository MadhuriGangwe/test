import sqlite3

conn = sqlite3.connect('testDb.sqlite')

#We will create all the tables first
print ("Opened database successfully");
conn.execute('''CREATE TABLE `customer` (
  `customer_id` int(11) PRIMARY KEY NOT NULL,
  `age` int(11) NOT NULL
)''')

conn.execute('''CREATE TABLE `items` (
  `item_id` int(11) PRIMARY KEY NOT NULL,
  `item_name` varchar(255) NOT NULL
)''')

conn.execute('''CREATE TABLE `orders` (
  `order_id` int(11) PRIMARY KEY NOT NULL,
  `sales_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
)''')

conn.execute('''CREATE TABLE `sales` (
  `sales_id` int(11) PRIMARY KEY NOT NULL,
  `customer_id` int(11) NOT NULL
)''')
print("tables created successfully")


#insert data into tables

conn.execute('''INSERT INTO `customer` (`customer_id`, `age`) VALUES
(1, 21),
(2, 23),
(3, 35)''')

conn.execute('''INSERT INTO `items` (`item_id`, `item_name`) VALUES
(1, 'x'),
(2, 'y'),
(3, 'z')''')

conn.execute('''INSERT INTO `orders` (`order_id`, `sales_id`, `item_id`, `quantity`) VALUES
(1, 1, 1, 3),
(2, 2, 1, 7),
(3, 3, 1, 1),
(4, 4, 2, 1),
(5, 5, 3, 1),
(6, 6, 3, 1),
(7, 7, 3, 1)''')

conn.execute('''INSERT INTO `sales` (`sales_id`, `customer_id`) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 2),
(6, 3),
(7, 3)''')

queryData = conn.execute('''SELECT cu.customer_id, cu.age, it.item_name, SUM(od.quantity)  FROM customer as cu
             JOIN sales as sa ON sa.customer_id=cu.customer_id
             JOIN orders as od ON od.sales_id =sa.sales_id
             JOIN  items AS it ON it.item_id=od.item_id
             GROUP BY od.item_id, sa.customer_id
             ''')

print(queryData)

for data in queryData:
    print(data)

print("data inserted successfully")

