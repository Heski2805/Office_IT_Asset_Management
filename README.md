# Office IT Asset Management

## Project Description

A Python-based application designed to manage office IT assets, including asset information, stock quantities, status, and location.

This project was initially developed using JSON for data storage and later enhanced by migrating to a MySQL database.

## Project Objectives

- Practice Python programming through a practical project.
- Apply functions, lists, dictionaries, and JSON for data management.
- Understand relational database management using MySQL.
- Integrate Python applications with a MySQL database.
- Build a simple application relevant to office IT asset management.

## Development History

This project was developed in two stages:

### Version 1.0 - JSON-Based Storage

The initial version used JSON as its data storage mechanism. It was developed to practice Python fundamentals, including functions, lists, dictionaries, file handling, and JSON.

#### Features Version 1.0 - JSON-Based Storage
- Add new IT assets.
- Search assets by ID.
- Update asset stock quantities.
- Delete existing assets.
- View all registered assets.
- Store asset data using JSON for data persistence.
- Validate user input to prevent invalid data.

### Version 2.0 - MySQL Database Integration

The application was enhanced by migrating its data storage from JSON to MySQL.

This development introduced SQL queries, database integration, CRUD operations using MySQL, transaction handling, and environment variable management.

The project's development progression can also be explored through its Git commit history.

#### Features Version 2.0 - MySQL Database Integration

- Add new IT assets.
- Search assets by ID.
- Update asset stock quantities.
- Delete existing assets **with confirmation**.
- View all registered assets.
- Store asset data **in a MySQL database**.
- Validate user input to prevent invalid data.
- Handle database errors and transactions.

## Technologies Used

- Python
- MySQL
- MySQL Connector/Python
- python-dotenv
- SQL
- Visual Studio Code
- Git & GitHub

## Project Structure

```text
Office_IT_Asset_Management/
│
├── screenshots/
│   ├── version_1.0/
│   └── version_2.0/
│
├── .gitignore
├── main.py
└── README.md
```

## How to Run

1. Make sure Python and MySQL Server are installed.
2. Make sure the MySQL service is running.
3. Create the database and `assets` table by running the following SQL commands in MySQL:

   ```sql
   CREATE DATABASE latihan_mysql;

   USE latihan_mysql;

   CREATE TABLE assets (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nama VARCHAR(100),
       harga DECIMAL(12,2),
       stok INT,
       status VARCHAR(30),
       lokasi VARCHAR(100)
   );
   ```

4. Open the project folder in Visual Studio Code.
5. Open the terminal and install the required Python packages:

   ```bash
   pip install mysql-connector-python python-dotenv
   ```

6. Create a `.env` file in the project directory and add your MySQL password:

   ```env
   DB_PASSWORD=your_mysql_password
   ```

   Replace `your_mysql_password` with your own MySQL password. Do not share or upload this file.

7. Run the application:

   ```bash
   python main.py
   ```

## Application Preview

### Version 1.0 — JSON-Based Storage

#### 1. Main Menu

![Main Menu](screenshots/version_1.0/01_main_menu.png)

#### 2. View All Assets

![View All Assets - Part 1](screenshots/version_1.0/02_view_assets_1.png)

![View All Assets - Part 2](screenshots/version_1.0/02_view_assets_2.png)

#### 3. Add Asset

![Add Asset](screenshots/version_1.0/03_add_asset.png)

#### 4. Search Asset

![Search Asset](screenshots/version_1.0/04_search_asset.png)

#### 5. Delete Asset

![Delete Asset](screenshots/version_1.0/05_delete_asset.png)

#### 6. Update Asset

![Update Asset](screenshots/version_1.0/06_update_asset.png)

#### 7. View Assets After Deletion

![View Assets After Deletion - Part 1](screenshots/version_1.0/07_view_asset_after_delete_1.png)

![View Assets After Deletion - Part 2](screenshots/version_1.0/07_view_asset_after_delete_2.png)

### Version 2.0 — MySQL Database Integration

#### 1. Main Menu

![Main Menu - Version 2.0](screenshots/version_2.0/01_main_menu.png)

#### 2. Initial Database State

![Initial Database State](screenshots/version_2.0/02_database_initial_state.png)

#### 3. View All Assets

![View All Assets - Part 1](screenshots/version_2.0/02_view_assets_1.png)

![View All Assets - Part 2](screenshots/version_2.0/02_view_assets_2.png)

#### 4. Add Asset

![Add Asset](screenshots/version_2.0/03_add_asset.png)

#### 5. Database After Add

![Database After Add](screenshots/version_2.0/03_database_after_add.png)

#### 6. Search Asset

![Search Asset](screenshots/version_2.0/04_search_asset.png)

#### 7. Update Asset

![Update Asset](screenshots/version_2.0/05_update_asset.png)

#### 8. Database After Update

![Database After Update](screenshots/version_2.0/05_database_after_update.png)

#### 9. Delete Asset

![Delete Asset](screenshots/version_2.0/06_delete_asset.png)

#### 10. Final Database State

![Final Database State](screenshots/version_2.0/07_database_final_state.png)

## Project Status

Version 2.0 - MySQL Database Integration

This project is maintained as a learning project and demonstrates the development of a Python-based IT asset management application, from JSON-based storage to MySQL database integration.
