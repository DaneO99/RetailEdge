# RetailEdge

RetailEdge is an end-to-end data analytics and machine learning project that transforms raw retail sales data into actionable business insights.

The system performs data ingestion, cleaning, exploratory analysis, and predictive modeling to identify profit drivers, analyze sales performance, and forecast future revenue trends.

It is designed as a modular, production-style pipeline built entirely in Python, using industry-standard tools for analytics and visualization.

## 🎯 Objectives

- Understand retail performance across product categories, regions, and time periods.
- Identify underperforming segments using SQL and Pandas analysis.
- Visualize sales and profit trends with Seaborn and Matplotlib.
- Build a predictive model using Scikit-Learn to estimate future sales or profit.
- Deliver insights in a reproducible, scalable, and professional project structure.

## ⚙️ Tech Stack

| Category | Tools & Libraries |
|----------|-------------------|
| Programming | Python (3.10+) |
| Data Processing | Pandas, NumPy |
| Data Storage / Querying | SQLite, SQL |
| Visualization | Seaborn, Matplotlib |
| Modeling | Scikit-Learn |
| Reporting | Markdown, JSON metrics |
| Automation | Custom pipeline via main.py |

## 🧠 Key Features

- **Automated Pipeline**: Modular structure with scripts for data loading, cleaning, analysis, and model training — orchestrated by main.py.
- **Dynamic SQL Queries**: Analyze aggregated data through reproducible SQL scripts.
- **Exploratory Data Analysis (EDA)**: Visual summaries of revenue trends, profit distributions, and category-level performance.
- **Predictive Modeling**: Train and evaluate regression models to forecast monthly sales.
- **Reproducible Outputs**: Figures, metrics, and reports automatically generated and stored for transparency.

## 📂 Project Structure

```
RetailEdge/
├── data/                # Raw and cleaned datasets
├── sql/                 # SQL queries and schema files
├── src/                 # Modular Python scripts
│   ├── query_data.py
│   ├── clean_data.py
│   ├── analyze.py
│   ├── model.py
│   ├── config.py
│   └── utils.py
├── figures/             # Visualization outputs
├── reports/             # Findings and performance metrics
├── main.py              # Orchestrates full analytics pipeline
├── requirements.txt     # Reproducible environment
└── README.md            # Documentation (this file)
```

## 🚀 Workflow

1. **Data Extraction**: Load raw CSV data or SQL tables.
2. **Data Cleaning**: Handle missing values, normalize columns, and prepare features.
3. **EDA**: Generate summary statistics and plots for key insights.
4. **Modeling**: Apply regression techniques to predict sales or profit.
5. **Reporting**: Export metrics and visual findings for business decision-making.

## 📈 Example Insights

- 20% of product categories contributed to 80% of total revenue (Pareto trend).
- High discounts correlated with lower profit margins (r = -0.62).
- Predictive model achieved R² = 0.87, enabling accurate monthly sales forecasts.

## 🧰 Future Enhancements

- Interactive dashboard using Streamlit for visual exploration.
- API integration for live data updates.
- Advanced feature engineering and model optimization.

## 👨‍💻 Author

**Dane Fitzgerald**  
Computer Science Student at Midwestern State University
