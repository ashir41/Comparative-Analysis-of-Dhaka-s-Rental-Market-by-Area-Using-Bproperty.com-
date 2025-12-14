# Comparative Analysis of Dhaka’s Rental Market

This project analyzes Dhaka’s rental housing market using scraped data. We collected listings for 1–5 bedroom apartments for rent in Dhaka from **Bproperty.com**, a leading Bangladeshi real estate portal. Selenium (Python) was used to automate web browsing and extract listing details from dynamic pages. The scraping script saves raw listings to a CSV file (`dhaka_rental_properties.csv`) in the repository root. The raw CSV is then cleaned and transformed using the included Jupyter notebooks to produce cleaned and transformed Excel files for analysis. Results are presented in an interactive Tableau dashboard (link below) that highlights key metrics and insights.

---

## Data Collection

- **Source:** Rental listings from [Bproperty.com](https://www.bproperty.com/rent/dhaka/residential/1-2-3-4-5-bedroom/) (Dhaka, residential rent, 1–5 bedrooms).  
- **Scraping:** Selenium WebDriver (Chrome) with Python was used to navigate pages and extract fields. The scraper script `scraper.py`:
  - Iterates pages 1	6 (configurable in the script; current code loops pages 1	50).
  - Uses ChromeDriver (ensure ChromeDriver is installed and available in PATH).
  - Opens a browser for each page, waits for dynamic content (the script currently sleeps 30 seconds per page), and collects listing elements.
  - Extracted fields (from the listing HTML/attributes):
    - `location` (full location text)
    - `bedroom number` (from `data-bedrooms` attribute)
    - `bathroom number` (from `data-bathrooms` attribute)
    - `size` (from `data-floor_area`, the script appends " sqft")
    - `rent price` (from `data-price`, formatted in BDT or marked "N/A")
  - Output: `dhaka_rental_properties.csv` saved to the repository root.

  Note: Area and Sub-area are not directly extracted by the scraper; these are derived during the cleaning step (the notebooks split the `location` field into `Sub_area` and `Area`).
- **Volume:** ~1,493 listings were scraped in the project run referenced here (may vary depending on time of scrape and pagination).

---

## Data Processing

- **Cleaning:** The `data_process.ipynb` notebook loads the raw CSV/Excel, splits `location` into `Sub_area` and `Area`, strips units from `size`, and converts `rent price` and `size` to numeric types. It saves the cleaned dataset as `bproperty_rentals_cleaned.xlsx` (note: the notebook contains hard-coded Windows file paths; update these paths before running).
- **Transformation / Feature Engineering:** The `data_process_new.ipynb` notebook computes additional columns:
  - `rent_per_sqft` (rent price / size)
  - `bedroom_category` (Small: 1	2, Medium: 3	4, Large: 5+)
  - `size_category` (<1000 sqft, 1000	2000 sqft, >2000 sqft)
  - `is_outlier` (IQR-based outlier flag on rent price)
  - Fills missing `Area` values using `Sub_area` where applicable

  The transformed dataset is saved as `bproperty_rentals_transformed.xlsx`.

*Note:* Both notebooks contain example file paths (Windows-style). Before running them, update `file_path` and output paths to match your environment or move the CSV/XLSX files to the expected locations.

---

## Analysis & Visualization

The cleaned dataset was analyzed in Python and visualized in Tableau.  
🔗 **Interactive Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/ashir.intheshar/viz/ComparitiveanalysisofDhakasRentalMarket/DhakasrentalmarketOverview?publish=yes)

The dashboard includes:
- **Overview**  
- **Trends and Distribution**  
- **Segmentation**

---

## Key Findings

- **Most common unit:** 3-bedroom apartments (majority of listings).  
- **Popular areas:** Bashundhara R-A, Uttara, Mohammadpur, and Banasree.  
- **Rent variation by area:**  
  - Upscale areas like Gulshan and Baridhara have **much higher rents per sqft** compared to residential zones like Mohammadpur or Bashundhara.  
- **Median rents:**  
  - 3-bed ≈ 30,000 BDT/month  
  - 4-bed ≈ 60,000 BDT/month  
  - 5-bed ≈ 100,000 BDT/month  
- **Average rent per sqft:** ~25 BDT overall, but >40 BDT in high-end neighborhoods.

---

## Tools & How to run

- **Requirements:** Python 3, pip packages: `selenium`, `pandas`, and a working Chrome/ChromeDriver installation.
- **Run scraper:**
  1. Ensure ChromeDriver is installed and available in PATH.
  2. Install dependencies: `pip install selenium pandas`.
  3. Run: `python scraper.py` (the script opens Chrome; it currently sleeps 30s per page and saves `dhaka_rental_properties.csv`).
- **Run notebooks:** open `data_process.ipynb` and `data_process_new.ipynb` in Jupyter. Update file paths in the notebooks to match where `dhaka_rental_properties.csv` is located if necessary.

---

If you plan to re-run the full pipeline, ensure you update the file paths in the notebooks (they contain Windows absolute paths) and that ChromeDriver matches your installed Chrome version.
