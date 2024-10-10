from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch email credentials and other sensitive data from environment variables
email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PASSWORD")
TARGET_PRICE = 105  # Set the target price for the product
URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Define headers to mimic a real browser visit (avoiding bot detection)
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "el-GR,el;q=0.9,en;q=0.8",
}

# Send a GET request to the Amazon product page
response = requests.get(URL, headers=amazon_headers)
lxml_txt = response.text

# Parse the HTML content using BeautifulSoup and lxml
soup = BeautifulSoup(lxml_txt, "lxml")

# Extract the price of the product (removes the "$" sign and converts to float)
price = float(soup.select_one(".a-offscreen").get_text().strip("$"))

# Extract the product name from the page
name_object = soup.select_one("#productTitle").get_text().strip()

# Check if the price is below the target price
if price < TARGET_PRICE:
    # If the price is lower, send an email alert
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=email, password=password)  # Log in to the email account
        # Send the email alert
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject: Amazon Price Alert!\n\n{name_object} is now ${price}."
        )

