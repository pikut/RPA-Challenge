from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd

# otwarcie arkusza
df_challenge = pd.read_excel(r'Inputs/challenge.xlsx', 'Sheet1')

field_names_to_fill = [
    'First Name',
    'Last Name',
    'Company Name',
    'Role in Company',
    'Address',
    'Email',
    'Phone Number',
]

# otwarcie przeglądarki na stronie wyzwania
browser = webdriver.Chrome()
browser.get('https://www.rpachallenge.com/')

# znalezienie przycisku rozpoczęcia wyzwania oraz jego kliknięcie
bttn_start = browser.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
bttn_start.click()

# godzina rozpoczęcia zadania
start = datetime.now()
start_time = start.strftime('%H:%M:%S')

# pętla po wszystkich wierszach z arkusza
for _, row in df_challenge[0:10].iterrows():
    for i, _ in enumerate(field_names_to_fill, 1):
        lbl = f'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[{i}]/rpa1-field/div/label'
        inp = f'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[{i}]/rpa1-field/div/input'

        lblName = browser.find_element(By.XPATH, lbl)
        inpName = browser.find_element(By.XPATH, inp)

        if lblName.text in field_names_to_fill:
            inpName.send_keys(row[lblName.text])

    bttnSubmit = browser.find_element(
        By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input'
    )
    bttnSubmit.click()

stop = datetime.now()
stop_time = stop.strftime("%H:%M:%S")
print('Robot pracował:', 'od', start_time, 'do', stop_time)
time_delta = stop - start
print('Robot wykonał pracę w:', time_delta, 'sekund')

