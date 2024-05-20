import multiprocessing
import random
import requests
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_embed_webhook(username, password):
    embed = {
        "title": "Roblox",
        "description": "Roblox Account",
        "color": 65280,
        "fields": [
            {"name": "Username", "value": username, "inline": True},
            {"name": "Password", "value": password, "inline": True}
        ],
        "thumbnail": {"url": "https://img2.pic.in.th/pic/logofa984ef83df8c4a3.png"}
    }

    payload = {
        "username": "Roblox Bot",
        "embeds": [embed]
    }

    webhook_url = "https://discord.com/api/webhooks/1242131249779183688/KUkd_a28Rbs1mrqXahY4gUZWlhsSi5E8zdEc6hYjqdv8KHKTq-WBDm8zN6Bn17O7J5-t"
    requests.post(webhook_url, json=payload)

while True:
    options = Options()
    options.add_argument("--window-size=300,300")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.roblox.com/CreateAccount')
    Name = ''.join(random.choices(string.ascii_lowercase, k=7))
    Password = ''.join(random.choices(string.ascii_lowercase, k=7))
    Number = random.randint(999, 2435)
    N = Name + str(Number)
    P = Password + str(Number)
    D = random.randint(1, 28)
    M = random.randint(1, 12)
    Y = random.randint(25, 32)
    
    Day = Select(driver.find_element(By.XPATH, '//*[@id="DayDropdown"]')).select_by_index(D)
    Month = Select(driver.find_element(By.XPATH, '//*[@id="MonthDropdown"]')).select_by_index(M)
    Year = Select(driver.find_element(By.XPATH, '//*[@id="YearDropdown"]')).select_by_index(Y)
    Name = driver.find_element(By.XPATH, '//*[@id="signup-username"]').send_keys(N)
    Passwords = driver.find_element(By.XPATH, '//*[@id="signup-password"]').send_keys(P)
    Next = driver.find_element(By.XPATH, '//*[@id="signup-button"]').click()
    WebDriverWait(driver, 99999999).until(EC.url_changes(driver.current_url))
    send_embed_webhook(N, P)
    driver.quit()