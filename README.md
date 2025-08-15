# Remote Work Job Trends – Cloud ETL Pipeline & Dashboard

A cloud-native ETL pipeline that ingests live remote job postings from the [Remote OK API](https://remoteok.com/api), processes them using Python, stores results in a serverless PostgreSQL database hosted on [Neon.tech](https://neon.tech), and visualizes key insights in **Google Data Studio**.  
The pipeline is automated with **GitHub Actions** to refresh data daily.

---

## 📌 Project Overview

The goal of this project is to analyze **global remote work trends** in near real-time by:
- Ingesting fresh job posting data daily
- Cleaning and enriching the dataset for analytics
- Storing results in a cloud-based PostgreSQL warehouse
- Building an interactive dashboard to explore remote job market insights

---

## 🛠 Tech Stack

- **Python** – Data extraction, cleaning, transformation
- **Pandas** – Data wrangling
- **Neon.tech** – Serverless PostgreSQL database
- **Google Data Studio** – Visualization and reporting
- **GitHub Actions** – Workflow automation
- **Requests** – API integration
- **SQLAlchemy / psycopg2** – Database connectivity

---

## 🔄 ETL Workflow

**1. Extract**  
- Pulls live remote job postings from the Remote OK public API

**2. Transform**  
- Standardizes column names  
- Parses and cleans posting dates  
- Calculates "Days Since Posting"  
- Converts skills/tags lists into comma-separated strings

**3. Load**  
- Uploads cleaned dataset to Neon Postgres in a `remote_jobs` table  
- Replaces table daily to keep data fresh

**4. Visualize**  
- Google Data Studio dashboard shows:  
  - Top job titles  
  - Most in-demand skills  
  - Jobs by location (map view)  
  - Trends over time

---

## 📊 Dashboard Preview

![Dashboard Screenshot](docs/dashboard_screenshot.png)  
*(Replace with your actual dashboard screenshot)*

---

## 🚀 How to Run Locally

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/remoteok-pipeline.git
cd remoteok-pipeline
