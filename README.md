#  Mobile Repair API

A simple REST API built with **Flask** and **SQLite** to manage mobile repair records.

## Features

* Add Repair
* View All Repairs
* Update Repair
* Delete Repair

## Technologies

* Python 3
* Flask
* SQLite3

## Project Structure

```text
mobile-repair-api/
│
├── app.py
├── repair.db
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install flask
```

Run:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint        |
| ------ | --------------- |
| POST   | `/repairs`      |
| GET    | `/repairs`      |
| PUT    | `/repairs/<id>` |
| DELETE | `/repairs/<id>` |

## Sample JSON

```json
{
    "customer_name": "Maheen",
    "mobile_model": "Samsung A52",
    "problem": "Screen Damage",
    "repair_cost": 5000
}
```

## Database

```sql
CREATE TABLE repairs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    mobile_model TEXT,
    problem TEXT,
    repair_cost REAL
);
```

## Requirements

```text
Flask==3.1.0
```

# Authur:
MAHEEN ASAD
