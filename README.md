# Automated-Price-Tracker-Analysis-Pipeline-mini-Project-3

## Project Overview

This project is a complete data engineering pipeline that tracks product prices from an e-commerce website, stores historical data, and analyzes price changes over time.

The system demonstrates end-to-end data workflow, including:

Web scraping

Data storage

Database management

Price trend analysis

It is designed following industry-level practices for building scalable and maintainable data pipelines.

## Business Objective

### The purpose of this project is to:

### Monitor product price changes over time

### Store historical pricing data

### Identify price fluctuations and trends

### Support use cases like:

          Price comparison tools

          Market analysis

          Automated alerts for price drops

## Key Features

✔ Automated web scraping of product data

✔ Extracts:

Product Title

Price

Timestamp

✔ Stores data in SQLite database

✔ Ensures data uniqueness (no duplicates)

✔ Tracks historical price changes

✔ Performs price analysis using aggregation

## Technologies Used

Python

Requests

BeautifulSoup

Pandas

SQLAlchemy

SQLite

## Project Structure

price-tracker-pipeline/

│
├── data/

│
├── database/

│   └── price_tracker.db

│
├── scripts/

│   ├── scraper.py

│   ├── database.py

│   └── analyzer.py

│
├── README.md

└── requirements.txt

## Pipeline Architecture

### 1️⃣ Data Collection (Scraper)

Scrapes product data from an online store

Extracts:

Title

Price

Current timestamp

Uses BeautifulSoup for HTML parsing

Cleans price using regex

👉 Implemented in scraper.py

### 2️⃣ Data Storage (Database Layer)

Creates a structured database table

Enforces uniqueness using:

title + date constraint

Saves data using SQLAlchemy

👉 Implemented in database.py

### 3️⃣ Data Analysis

Reads stored data from database

Groups data by product title

Calculates:

Minimum price

Maximum price

👉 Implemented in analyzer.py

## How to Run the Project

### Step 1: Clone Repository

git clone https://github.com/yourusername/price-tracker-pipeline.git

cd price-tracker-pipeline

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Run Scraper

python scraper.py

This will:

Scrape product data

Store it in the database

### Step 4: Run Analysis
python analyzer.py

This will display:

Min and max prices for each product

## Example Output

Product	    Min Price	    Max Price

Book A	    20.00	        25.00

## Key Insights

Enables tracking of price fluctuations over time

Helps identify pricing patterns

Supports data-driven decision making

## Industry-Level Highlights

### This project demonstrates:

✔ Modular pipeline design (scraper + DB + analysis)

✔ Database integration (very important for data engineering)

✔ Historical data tracking

✔ Clean and scalable architecture

✔ Separation of concerns (each file has a clear role)

## Future Improvements

Add scheduling (Cron / Airflow)

Integrate with cloud databases (AWS RDS, BigQuery)

Build dashboard (Streamlit / Power BI)

Add alert system (email/Telegram for price drops)

Multi-product & multi-site tracking

## Author

### Adeel Khan
### Aspiring Data Engineer
