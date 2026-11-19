# E-Commerce Sales, Customer & Profitability Analysis using Python

## Project Overview

This project focuses on analyzing e-commerce sales data to identify business performance trends, customer purchasing behaviour, product performance, geographical sales patterns, and profitability.

The project uses Python for data cleaning, exploratory data analysis (EDA), statistical analysis, and business insights generation.

The objective is to transform raw sales data into meaningful information that can support data-driven business decisions.

**Note:** This project uses a synthetic dataset created for analytical and educational purposes. It does not represent actual company transactions.

## Business Objectives

- Evaluate overall sales and profit performance.
- Identify monthly and quarterly sales trends.
- Analyze category and subcategory performance.
- Identify top-performing products.
- Understand customer purchasing behaviour.
- Compare customer segments and demographics.
- Analyze state-wise and city-wise sales.
- Evaluate payment methods and sales channels.
- Analyze order status and delivery performance.
- Understand the relationship between discounts and profitability.
- Identify loss-making orders, categories, and products.

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Exploratory analysis |
| VS Code | Development environment |
| Git & GitHub | Version control and project hosting |
| Power BI | Business dashboard development |

## Dataset Information

The dataset contains 5,000 cleaned records and 28 columns.

It includes information about:

- Orders and order dates
- Customers and customer segments
- Products and product categories
- Quantity and pricing
- Discounts and shipping fees
- Sales, cost, and profit
- Payment methods and sales channels
- Order status and delivery performance
- Customer ratings and demographics
- Data quality indicators

## Project Structure

```text
Retail-Sales-Analysis/
│
├── data/
│   ├── raw/
│   │   └── retail_sales_raw.csv
│   │
│   └── processed/
│       └── retail_sales_cleaned.csv
│
├── notebooks/
│   ├── 01_Data_Inspection.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   └── 03_Exploratory_Data_Analysis.ipynb
│
├── src/
│   ├── data_loader.py
│   └── eda.py
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Data Cleaning

The raw dataset was inspected and cleaned before analysis.

Major cleaning activities included:

- Identifying and removing duplicate records.
- Handling missing values.
- Detecting invalid dates.
- Identifying invalid age, discount, and rating values.
- Correcting invalid quantity values.
- Validating sales and profit calculations.
- Standardizing column names.
- Creating data quality indicator columns.

The final processed dataset contains 5,000 rows and 28 columns.

## Exploratory Data Analysis

The project includes the following analytical areas:

1. Business Performance KPIs
2. Monthly Sales Analysis
3. Quarterly Sales Analysis
4. Category Performance Analysis
5. Subcategory Performance Analysis
6. Top 5 Product Analysis
7. Customer Behaviour Analysis
8. Customer Segment Analysis
9. Gender-wise Analysis
10. Age Group Analysis
11. State-wise Sales Analysis
12. City-wise Sales Analysis
13. Payment Method Analysis
14. Sales Channel Analysis
15. Order Status Analysis
16. Discount Analysis
17. Delivery Performance Analysis
18. Correlation Analysis
19. Loss Analysis

## Key Business Metrics

| Metric | Result |
|---|---:|
| Total Orders | 5,000 |
| Total Customers | 1,675 |
| Total Units Sold | 11,897 |
| Recorded Sales | ₹2,42,40,547.70 |
| Total Cost | ₹1,74,98,399.67 |
| Total Profit | ₹67,42,148.03 |
| Average Order Value | ₹4,848.11 |
| Profit Margin | 27.81% |

*Recorded financial totals include all order statuses and should not be interpreted as realized revenue.*

## Key Business Insights

- Electronics generated the highest category-level sales and profit.
- Home & Kitchen was the highest-performing subcategory by sales.
- Repeat customers contributed approximately 93.99% of recorded sales.
- The 26–35 age group generated the highest sales among age groups.
- Madhya Pradesh recorded the highest state-level sales.
- Bhopal recorded the highest city-level sales.
- Mobile App was the leading sales channel by recorded sales.
- Higher discount bands were associated with lower profit margins.
- The dataset contained 116 loss-making orders with a combined loss of ₹26,364.

## Visualizations

The project generates 13 charts covering:

- Monthly sales and profit trends
- Category performance
- Top-performing products
- Customer demographics
- State and city performance
- Sales channels
- Order status
- Delivery performance
- Correlation analysis
- Category-wise and product-wise losses

Charts are stored in the `outputs/charts/` directory.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Retail-Sales-Analysis
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Analysis

```bash
python src/eda.py
```

## Future Improvements

- Develop an interactive Power BI dashboard.
- Add advanced customer segmentation.
- Perform sales forecasting.
- Build an automated reporting system.
- Explore customer retention and cohort analysis.

## Author

**Data Analytics Portfolio Project**

Skills demonstrated: Python, Pandas, NumPy, Data Cleaning, Exploratory Data Analysis, Business Analysis, Data Visualization, and SQL/Power BI project integration.

---

**Disclaimer:** This project is intended for educational and portfolio demonstration purposes. The dataset is synthetic and business insights are based only on the generated data.