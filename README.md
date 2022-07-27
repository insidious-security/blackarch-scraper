# Blackarch Tool Scraper

<p align="left">
  <img src="https://img.shields.io/github/last-commit/insidious-security/blackarch-scraper.svg?style=for-the-badge">
  <img src="https://img.shields.io/github/license/insidious-security/blackarch-scraper?style=for-the-badge">
</p>

This project scrapes all available tools, versions and descriptions from the blackarch.org/tools.html overview and inserts this data in a docker postgresql database.

The FastAPI can be used as an application backend to serve data in json format.

## Usage
```bash
# Clone this repository
git clone http://raptor/sidious/blackarch-scraper.git

# Install the python requirements:
sudo pip3 install -r requirements.txt

# Run the docker_container.sh
chmod +x docker_container.sh
./docker_container.sh

# Connect to the database
psql -h localhost -U postgres

# Create the pentest database
create database pentest;

# Change the ip-address in the .env file 

# Run the bls-scraper.py
python3 bls_scraper.py

# Run the bls-api.py
uvicorn bls-api:app --reload --host 0.0.0.0

# Test the api with curl
curl http://10.0.0.196:8000/black/2107
```
