# filterstocks
FilterStocks is a simple Python tool that helps you quickly find dividend stocks worth a look. It grabs data from Yahoo Finance, checks things like dividend yield, P/E ratio, and earnings growth, and gives you back a clean list of stocks that pass the test.
📊 FilterStocks

Ever wished you could quickly check which dividend stocks are worth a closer look?
FilterStocks is a simple Python tool I built to do just that. It pulls real stock data from Yahoo Finance and runs a few basic checks, like:

Does the company pay a solid dividend?

Is the P/E ratio reasonable (not sky-high)?

Is the business still growing its earnings?

If a stock passes the test, it shows up in a neat little table so you can see the numbers at a glance.

🔎 What it does

Fetches up-to-date stock info automatically (no manual research needed).

Screens companies based on dividend yield, P/E ratio, and earnings growth.

Lets you tweak the rules — so you can adjust for your own investing style.

Gives you results in a clean, pandas DataFrame that you can print, save, or export.

🚀 Getting Started

Install the requirements:

pip install yfinance pandas


Clone the repo and run the script:

python filterstocks.py


The output will show which stocks meet the criteria.

🛠️ Why I built this

I wanted a lightweight, no-nonsense stock screener that focuses on long-term dividend stocks. Instead of wading through endless financial websites, this script gives me a quick shortlist to research further.

🌱 Future ideas

Add a proper 5-year EPS growth calculation

Export results to Excel/CSV

Make it work as a small web app for easier use