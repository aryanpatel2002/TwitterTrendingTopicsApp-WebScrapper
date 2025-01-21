# Twitter Trending Topic App

## Overview
A Python-based application that scrapes the top 5 trending topics from Twitter's "What’s Happening" section. It uses Selenium for web automation, ProxyMesh for proxy rotation, and MongoDB for storing the data.

## Features
- Fetches the top 5 trending topics from Twitter's homepage.
- Ensures anonymity and avoids rate-limiting by using ProxyMesh for IP rotation.
- Stores the scraped data in MongoDB with the following fields:
  - Unique ID
  - Names of the top 5 trends
  - Date and time of the script execution
  - IP address used

## Technologies Used
- **Python**: Core programming language.
- **Selenium**: For browser automation and data scraping.
- **ProxyMesh**: To send requests through different IPs.
- **MongoDB**: For storing the scraped data.
- **HTML**: For a simple interface to trigger the script and display results.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/TwitterTrendingTopicsApp-WebScrapper.git
   cd twitter-trending-topic-app
