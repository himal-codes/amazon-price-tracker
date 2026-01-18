import requests
from bs4 import BeautifulSoup
import time

# 1. SETUP
# The product we are tracking (iPhone 13)
url = "https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/"
my_budget = 60000  # Set this to a price you are willing to pay

# The "Disguise" so Amazon thinks we are a human
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_price():
    print("🕵️  Spying on Amazon...")
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the price text (it looks like "59,900")
        price_tag = soup.find("span", {"class": "a-price-whole"})
        
        if price_tag:
            # Clean the data: Remove the comma so Python understands it as a number
            price_text = price_tag.text.strip().replace(",", "").replace(".", "")
            current_price = int(price_text)
            
            print(f"💰 Found Price: ₹{current_price}")
            
            # THE LOGIC: Compare price to your budget
            if current_price < my_budget:
                print("🚨 DEAL ALERT! The price is DOWN!")
                print("👉 GO BUY IT NOW!")
            else:
                print("😴 Price is still too high. I'll check again later.")
        else:
            print("⚠️ Could not find price tag.")
            
    except Exception as e:
        print(f"Error: {e}")

# Run the function
check_price()
