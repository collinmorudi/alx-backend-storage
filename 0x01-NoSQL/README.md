# NoSQL and MongoDB Project

## Overview
This project focuses on understanding NoSQL databases, specifically MongoDB, and how to interact with them using both MongoDB commands and Python scripts with PyMongo.

## Learning Objectives
- What NoSQL means
- The difference between SQL and NoSQL
- What ACID is
- What document storage is
- Types of NoSQL databases
- Benefits of NoSQL databases
- How to query, insert, update, and delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File
- **Environment**: Ubuntu 18.04 LTS using MongoDB (version 4.2)
- **File Format**: All files should end with a new line and start with a comment: `// my comment`
- **README.md**: A `README.md` file is mandatory at the root of the project folder.
- **File Length**: The length of files will be tested using `wc`.

### Python Scripts
- **Environment**: Ubuntu 18.04 LTS using Python 3.7 and PyMongo (version 3.10)
- **File Format**: All files should end with a new line and start with `#!/usr/bin/env python3`
- **Coding Style**: Code should use the pycodestyle style (version 2.5.*)
- **Documentation**: All modules and functions should have documentation.
- **Execution**: Code should not be executed when imported (use `if __name__ == "__main__":`).

## Installing MongoDB and PyMongo

### MongoDB Installation
To install MongoDB 4.2 on Ubuntu 18.04, follow these steps:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod start
$ mongo --version
```

Ensure the data directory exists:
```bash
$ sudo mkdir -p /data/db
```

### PyMongo Installation
To install PyMongo, use:
```bash
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

## Running MongoDB

### Using Container-on-Demand
To run MongoDB using a container-on-demand:

- Ask for a container with Ubuntu 18.04 - MongoDB.
- Connect via SSH or WebTerminal.
- Start MongoDB:
  ```bash
  $ service mongod start
  * Starting database mongod                                              [ OK ]
  ```

## Tasks

### Example Commands and Scripts

#### Listing Databases
To list databases using a MongoDB command file:
```bash
$ cat 0-list_databases | mongo
```

#### Interacting with MongoDB using Python
Here is an example of a Python script to interact with MongoDB:

```python
#!/usr/bin/env python3
"""
Main script to interact with MongoDB.
"""

from pymongo import MongoClient

def list_databases():
    """
    List all databases in the MongoDB instance.
    """
    client = MongoClient('mongodb://localhost:27017/')
    databases = client.list_database_names()
    print(databases)
    client.close()

if __name__ == "__main__":
    list_databases()
```

## Repository
- **GitHub repository**: alx-backend-storage
- **Directory**: 0x00-NoSQL_MongoDB
- **Files**:
  - `0-list_databases` (MongoDB command file)
  - `1-python_script.py` (Python script using PyMongo)

## Contributing
Contributions are welcome. Ensure all code adheres to the specified guidelines and includes proper documentation.

## License
This project is licensed under the terms of the MIT License. See the LICENSE file for details.
