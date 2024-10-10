# Amazon Price Tracker Bot

This project is an Amazon price tracking bot that scrapes product prices from Amazon and sends an email alert if the price drops below a specified target price. The bot is built using `BeautifulSoup` for web scraping, `requests` for making HTTP requests, and `smtplib` for sending emails.

## Features

- Scrapes the price of a product from Amazon.
- Sends an email alert when the product price is below the defined target price.
- Uses environment variables to store sensitive email credentials.

## Requirements

- Python 3.x
- BeautifulSoup
- lxml
- requests
- python-dotenv

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/angelikizoi/BeautifulSoup_AmazonPriceTracker.git
cd BeautifulSoup_AmazonPriceTracker
```
### Step 2: Create a virtual environment (optional but recommended)
On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Set up environment variables
Create a .env file in the project root directory and add your email credentials and password:

```bash
EMAIL=your_email@example.com
EMAIL_PASSWORD=your_email_password
```
These values will be used by the script to send email alerts.

### Step 5: Run the script
```bash
python main.py
```
The bot will scrape the product price from Amazon and send an email alert if the price drops below the target price.

## Customization
You can modify the following variables in the script:

- TARGET_PRICE: Change this to the price below which you want to receive an alert.
- URL: Replace this with the URL of the Amazon product you want to track.
Example:
```python
TARGET_PRICE = 100  # Set your target price here
URL = "https://www.amazon.com/dp/product_id_here"
```