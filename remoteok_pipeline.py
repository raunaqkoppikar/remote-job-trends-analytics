import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# ==== CONFIGURATION ====
NEON_USER = "your_username"
NEON_PASSWORD = "your_password"
NEON_HOST = "your_host"
NEON_DB = "your_db"
NEON_PORT = "5432"

# ==== EXTRACT ====
url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
data = response.json()

# Skip first element (metadata)
jobs = pd.DataFrame(data[1:])

# ==== TRANSFORM ====
# Rename columns
jobs = jobs.rename(columns={
    'position': 'job_title',
    'company': 'company_name',
    'location': 'location',
    'date': 'posted_date',
    'tags': 'skills'
})

# Keep relevant columns
cols_to_keep = ['job_title', 'company_name', 'location', 'posted_date', 'skills', 'url']
jobs = jobs[cols_to_keep]

# Convert date and calculate days since posting
jobs['posted_date'] = pd.to_datetime(jobs['posted_date'], errors='coerce').dt.tz_localize(None)
jobs['days_since_posting'] = (datetime.now() - jobs['posted_date']).dt.days

# Convert skills list to comma-separated string
jobs['skills'] = jobs['skills'].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)

# ==== LOAD ====
# Create SQLAlchemy engine for Neon
engine = create_engine(f"postgresql+psycopg2://{NEON_USER}:{NEON_PASSWORD}@{NEON_HOST}:{NEON_PORT}/{NEON_DB}")

# Create table (replace if exists)
jobs.to_sql('remote_jobs', engine, if_exists='replace', index=False)

print(f"✅ Successfully loaded {len(jobs)} rows into Neon Postgres.")
