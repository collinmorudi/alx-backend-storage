# MySQL Advanced Project

## Overview
This project focuses on advanced MySQL concepts, including creating tables with constraints, optimizing queries with indexes, and implementing stored procedures, functions, views, and triggers. Here, we will cover the specific tasks related to creating tables, ranking data, and querying databases.

## Learning Objectives
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements
### General
- **Environment**: Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- **File Format**: All files should end with a new line and start with a comment describing the task.
- **SQL Keywords**: All SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`).
- **Comments**: SQL queries should have a comment just before them.
- **README.md**: A `README.md` file is mandatory at the root of the project folder.
- **File Length**: The length of files will be tested using `wc`.
- **Container-on-Demand**: Use “container-on-demand” to run MySQL with Ubuntu 18.04 - Python 3.7.

### Running MySQL
To start MySQL in the container:
```bash
$ service mysql start
 * MySQL Community Server 5.7.30 is started
```
Credentials in the container: `root/root`.

### Importing SQL Dump
To import a SQL dump:
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

## Tasks

### 0. We are all unique!
- **File**: `0-uniq_users.sql`
- **Description**: Create a table `users` with the following attributes:
  - `id`: integer, never null, auto increment, and primary key
  - `email`: string (255 characters), never null and unique
  - `name`: string (255 characters)
- **Example**:
  ```sql
  -- Create users table if it does not exist
  CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      name VARCHAR(255)
  );
  ```

### 1. In and not out
- **File**: `1-country_users.sql`
- **Description**: Create a table `users` with the following attributes:
  - `id`: integer, never null, auto increment, and primary key
  - `email`: string (255 characters), never null and unique
  - `name`: string (255 characters)
  - `country`: enumeration of countries (US, CO, TN), never null (default is US)
- **Example**:
  ```sql
  -- Create users table if it does not exist
  CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      name VARCHAR(255),
      country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
  );
  ```

### 2. Best band ever!
- **File**: `2-fans.sql`
- **Description**: Rank country origins of bands by the number of fans.
  - Import the `metal_bands.sql` dump.
  - Column names must be `origin` and `nb_fans`.
- **Example**:
  ```sql
  -- Rank country origins by the number of fans
  SELECT origin, COUNT(*) AS nb_fans
  FROM metal_bands
  GROUP BY origin
  ORDER BY nb_fans DESC;
  ```

### 3. Old school band
- **File**: `3-glam_rock.sql`
- **Description**: List all bands with Glam rock as their main style, ranked by their longevity.
  - Import the `metal_bands.sql` dump.
  - Column names must be `band_name` and `lifespan` (in years until 2022).
- **Example**:
  ```sql
  -- List bands with Glam rock style, ranked by longevity
  SELECT band_name, 2022 - formed AS lifespan
  FROM metal_bands
  WHERE style = 'Glam rock'
  ORDER BY lifespan DESC;
  ```

## Repository
- **GitHub repository**: alx-backend-storage
- **Directory**: 0x00-MySQL_Advanced
- **Files**:
  - `0-uniq_users.sql`
  - `1-country_users.sql`
  - `2-fans.sql`
  - `3-glam_rock.sql`

## Contributing
Contributions are welcome. Ensure all SQL queries follow the specified guidelines and include comments.
