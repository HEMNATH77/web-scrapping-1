# web-scrapping-1

<h1>Web Scraping E-Commerce Product Data</h1>
<p>This repository contains a Python script that scrapes product information from the WebScraper Test Site using requests, BeautifulSoup, and Pandas. The data is then saved into a CSV file for further analysis.</p>

<h1> Overview</h1>
<h3>This script extracts product details such as:</h3>
   <ul> Product Name</ul>
   <ul>Price</ul>
   <ul>Description</ul>
   <ul>Review Counts</ul>
<p>The data is gathered from an e-commerce website designed for web scraping practice. After scraping, the data is stored in a CSV file for easy access and analysis.</p>  



https://github.com/user-attachments/assets/c257afcb-5447-436a-a069-1db058e6ef21


<h1>Libraries Used</h1>
<ol>1. requests: To send HTTP requests to the website.</ol>
<ol>2. BeautifulSoup (from bs4): To parse and navigate through the HTML content.</ol>
<ol>3. Pandas: To store and manipulate the extracted data in a structured format (DataFrame) and save it as a CSV file.</ol>
<p>Make sure you have Python installed. And install pandas, requests and BeautifulSoup by using <a href="https://packaging.python.org/en/latest/tutorials/installing-packages/">pip</a> Command </p>

<h1>Sample Outputs Be:</h1>
<h3>The output CSV will have the following columns:</h3>
<ol>Product Name: The name of the product.</ol>
<ol>Prices: The price of the product.</ol>
<ol>Description: A short description of the product.</ol>
<ol>Reviews: The number of reviews for the product.</ol>
<img src="https://github.com/user-attachments/assets/9d89486d-ce25-4280-a0f5-c6d84aee62e5">

<h1>OverAll</h1>
<p>This web scraping project successfully demonstrates how to extract product information such as names, prices, descriptions, and review counts from a practice e-commerce website. Using Python libraries like requests, BeautifulSoup, and Pandas, the script efficiently gathers the data and organizes it into a CSV file for analysis or further use.

The project provides a solid foundation for building more advanced web scrapers. Future enhancements could include scraping additional product categories, gathering more detailed product information (such as ratings or images), and implementing automation to collect data periodically. This approach can be scaled and adapted to real-world e-commerce platforms for data collection and analytics purposes.</p>
