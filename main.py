from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd
import os

DOCKER_RUN = os.getenv("DOCKER_CONTAINER")

df_challenge = pd.read_excel(r"Inputs/challenge.xlsx", "Sheet1")

field_names_to_fill = [
    "First Name",
    "Last Name",
    "Company Name",
    "Role in Company",
    "Address",
    "Email",
    "Phone Number",
]

chrome_options = webdriver.ChromeOptions()

if DOCKER_RUN:
    browser = webdriver.Remote(
        command_executor="http://chrome:4444/wd/hub", options=chrome_options
    )
else:
    browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.rpachallenge.com/")

button_start = browser.find_element(
    By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button"
)
button_start.click()

start = datetime.now()
start_time = start.strftime("%H:%M:%S")

for _, row in df_challenge[0:10].iterrows():
    for i, _ in enumerate(field_names_to_fill, 1):
        label = f"/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[{i}]/rpa1-field/div/label"
        input_ = f"/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[{i}]/rpa1-field/div/input"

        label_name = browser.find_element(By.XPATH, label)
        input_name = browser.find_element(By.XPATH, input_)

        if label_name.text in field_names_to_fill:
            input_name.send_keys(row[label_name.text])

    button_submit = browser.find_element(
        By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input"
    )
    button_submit.click()

stop = datetime.now()
stop_time = stop.strftime("%H:%M:%S")

print("Robot pracował:", "od", start_time, "do", stop_time)
time_delta = stop - start
print("Robot wykonał pracę w:", time_delta, "sekund")
