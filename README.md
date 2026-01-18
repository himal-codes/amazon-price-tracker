# 🛒 Amazon Price Tracker

### 🚀 Overview
This is a Python automation tool that tracks the live price of products on Amazon (like the iPhone 13). It automatically bypasses bot detection and alerts the user when the price drops below a specific budget.

### 🛠️ Technologies Used
* **Python 3.14**
* **Requests** (for fetching web data)
* **BeautifulSoup4** (for parsing HTML)
* **Web Scraping Logic** (User-Agent rotation)

### ⚙️ How It Works
1.  The script connects to the Amazon product page using a custom "User-Agent" to mimic a real human browser.
2.  It extracts the HTML content and finds the specific price tag class.
3.  It cleans the data (removes commas/symbols) and converts it to an integer.
4.  If the price is lower than the user's budget, it triggers a "DEAL ALERT".

### 👨‍💻 Author
**Himal Singh** - Aspiring Python Developer
