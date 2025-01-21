import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Added import for By
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient

# Set up Chrome options (if any)
options = webdriver.ChromeOptions()

# Proxy configuration (update with your ProxyMesh details if required)
PROXY = "http://your-proxymesh-credentials@proxy-ip:port"
options.add_argument('--proxy-server=%s' % PROXY)

# Set up the Chrome driver using Service
service = Service(ChromeDriverManager().install())

# Initialize the driver with service and options
driver = webdriver.Chrome(service=service, options=options)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_data"]
collection = db["trending_topics"]

try:
    # Navigate to Twitter login
    driver.get("https://twitter.com/login")
    time.sleep(2)

    # Log in to Twitter (update with your credentials)
    driver.find_element(By.NAME, "session[username_or_email]").send_keys("your-username")
    driver.find_element(By.NAME, "session[password]").send_keys("your-password")
    driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()
    time.sleep(5)

    # Scrape the top 5 trending topics
    trends = driver.find_elements(By.XPATH, '//div[@aria-label="Timeline: Trending now"]//span')[:5]
    trending_topics = [trend.text for trend in trends]

    # Insert data into MongoDB
    record = {
        "_id": random.randint(1000, 9999),
        "trend1": trending_topics[0],
        "trend2": trending_topics[1],
        "trend3": trending_topics[2],
        "trend4": trending_topics[3],
        "trend5": trending_topics[4],
        "timestamp": time.ctime(),
        "ip_address": PROXY.split('@')[-1] if '@' in PROXY else "No Proxy"
    }
    collection.insert_one(record)
    print("Data inserted successfully into MongoDB!")

finally:
    driver.quit()



