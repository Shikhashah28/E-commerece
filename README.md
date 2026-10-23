# E-commerce Books Data Analysis

This project collects book listings from [Books to Scrape](https://books.toscrape.com/), cleans the collected data, explores prices, ratings, and availability, and creates charts for analysis. A Power BI report file is also included.

## Project workflow

### 1. Data scraping

[`scraper.py`](./scraper.py) uses `requests` and Beautiful Soup to visit the Books to Scrape catalogue. It follows each page's **next** link until there are no more pages, collecting each book's:

- Title
- Price
- Availability
- Star rating

The scraper checks for unsuccessful HTTP responses, waits one second between pages, and saves the results to `books_data.csv`.

### 2. Data cleaning

[`clean_data.py`](./clean_data.py) reads `books_data.csv` and:

- Reports the original dataset shape, missing values, and duplicate row count.
- Removes duplicate rows.
- Removes the pound sign from prices and converts prices to numeric values.
- Converts word ratings (`One` to `Five`) to numbers (`1` to `5`).
- Drops rows missing a title, price, or rating, and resets the row index.

The cleaned dataset is saved as `books_cleaned.csv`. Availability is retained as collected.

### 3. Exploratory data analysis (EDA)

[`analysis.py`](./analysis.py) reads the cleaned dataset and prints a preview and summary information. It examines price statistics and the average price, identifies the most and least expensive books, and reports book counts by rating and availability.

### 4. Visualisation

[`visualisations.py`](./visualisations.py) uses Matplotlib to create and save three charts from `books_cleaned.csv`:

- `price_distribution.png` — distribution of book prices.
- `rating_distribution.png` — number of books at each rating.
- `average_price_by_rating.png` — average price for each rating.

The script also displays the charts when run in an environment with graphical display support.

### 5. Power BI

`Ecommerce - Intelligence.pbix` is the included Power BI report. Open it with Power BI Desktop to view the report. The prepared `books_cleaned.csv` is the analysis-ready data file for Power BI; if you need to reconnect or refresh the data source, import that CSV and confirm the column types:

- `title`, `availability`: Text
- `price`: Decimal number (GBP)
- `rating`: Whole number (1–5)

After reconnecting the source, refresh the report to load the cleaned data.

## Repository contents

| File | Description |
| --- | --- |
| `scraper.py` | Scrapes book listings and creates `books_data.csv`. |
| `books_data.csv` | Raw scraped book data. |
| `clean_data.py` | Cleans the raw CSV and creates `books_cleaned.csv`. |
| `books_cleaned.csv` | Cleaned data used for analysis and charts. |
| `analysis.py` | Prints exploratory summaries and statistics. |
| `visualisations.py` | Generates the three chart images. |
| `price_distribution.png` | Price distribution chart. |
| `rating_distribution.png` | Book count by rating chart. |
| `average_price_by_rating.png` | Average price by rating chart. |
| `Ecommerce - Intelligence.pbix` | Power BI report. |

## Run the Python workflow

Python 3 is required. From the project directory, install the script dependencies:

```powershell
python -m pip install requests beautifulsoup4 pandas matplotlib
```

Run the scripts in order so each step has the data file produced by the previous one:

```powershell
python scraper.py
python clean_data.py
python analysis.py
python visualisations.py
```

The scraper makes HTTP requests to the public Books to Scrape site. The later steps can be run using the CSV files already in the repository without scraping again.
