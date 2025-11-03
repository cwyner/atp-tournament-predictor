import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ======================================================= #
# CONFIG SETTINGS - change when grabbing different tables #
# ======================================================= #
court_type = "Clay"             # OPTIONS: Hard, Grass, Clay
stat_category = "pressure"      # OPTIONS: serve, return, pressure


url = "https://www.atptour.com/en/stats/leaderboard?boardType=" + stat_category + "&timeFrame=52week&surface=" + court_type + "&versusRank=all&formerNo1=false"


# Simulate browser and let js run to render HTML
driver = webdriver.Chrome()
driver.get(url)

# Automatically click load more button in browser to access the full table
wait = WebDriverWait(driver, 10)

while True:
    try:
        show_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.atp_button.atp_button--secondary')))
        driver.execute_script("arguments[0].click();", show_more)
        time.sleep(2)
    except Exception:
        break

# Parse the rendered html content
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

# Find the leaderboard's table
tables = soup.find_all('table')
table = tables[0]

# Quit the browser sim
driver.quit()

# Extract header info
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Extract table body info
data = []
tbody = table.find('tbody')
for row in tbody.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())
    if row_data:
        data.append(row_data)

# Convert data into pandas DataFrame
df = pd.DataFrame(data, columns=headers)
print(df)

# Save dataframe to csv file (manually moved to raw-data)
df.to_csv(stat_category + "_" + court_type.lower() + ".csv", index=False, header=True)
