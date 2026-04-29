# 📚 Scrapy Book Data Extraction & Analysis Project

## 📌 Project Overview

This project demonstrates how to use **Scrapy**, a powerful Python web scraping framework, to extract structured data from a website and perform data analysis with visualization.

The project scrapes book data from an online catalog and transforms it into usable data for analysis, following a simple **ETL (Extract, Transform, Load)** workflow.

---

## 🧠 What is Scrapy?

**Scrapy** is an open-source Python framework designed for web scraping and data extraction.

It allows developers to:

* Crawl websites automatically
* Extract structured data
* Export data into formats like JSON, CSV, etc.

In this project, Scrapy is used as the **data ingestion tool**.

---

## 🎯 Project Goals

* Extract book data (title, price, rating)
* Handle pagination (multiple pages)
* Store data in structured JSON format
* Perform data analysis using Python
* Create meaningful visualizations

---

## ⚙️ Project Structure

```
scrapy_project/
│
├── my_scraper/                 # Scrapy main project
│   ├── spiders/
│   │   └── books.py           # Spider (data extraction logic)
│   ├── items.py               # Data model (default)
│   ├── pipelines.py           # Data processing (optional)
│   ├── middlewares.py         # Scrapy middleware (default)
│   ├── settings.py            # Project settings
│   └── __init__.py
│
├── plots/                     # Generated visualizations
│   ├── price_distribution.png
│   ├── top10_expensive_books.png
│   ├── rating_distribution.png
│   └── avg_price_by_rating.png
│
├── output.json                # Scraped dataset
├── analysis.py                # Data analysis & visualization script
├── scrapy.cfg                 # Scrapy configuration
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

## 🔄 Workflow (ETL Pipeline)

1. **Extract** → Scrapy spider collects data from the website
2. **Transform** → Data cleaned (price converted to numeric, rating parsed)
3. **Load** → Data stored in `output.json`
4. **Analyze** → Python script generates insights and charts

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the scraper

```bash
python -m scrapy crawl books -O output.json
```

### 3. Run analysis

```bash
python analysis.py
```

---

## 📊 Output

### 📁 Data

* `output.json` → Contains scraped book data

### 📈 Visualizations (in `plots/`)

* Price distribution histogram
* Top 10 most expensive books
* Rating distribution
* Average price by rating

---

## 🔍 Where to Look

* `books.py` → scraping logic
* `output.json` → collected data
* `analysis.py` → data processing & visualization
* `plots/` → final graphical outputs

---

## 💡 Key Features

* Multi-page scraping (pagination)
* Data cleaning and transformation
* Visual analytics with matplotlib
* Organized project structure
* Ready for ETL pipeline integration

---

## 🧪 Example Output

* Total books scraped: ~1000
* Average price: ~35 GBP
* Most expensive book identified
* Distribution of prices and ratings visualized

---

## 🤖 AI Usage

This project was developed with the assistance of AI tools (ChatGPT) for guidance, debugging, and code improvement.

---

## 📚 References

* https://scrapy.org/
* https://pandas.pydata.org/
* https://matplotlib.org/

```
```
