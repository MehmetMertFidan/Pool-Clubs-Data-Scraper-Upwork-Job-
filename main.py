import numpy as np
import pandas
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.get("https://www.usms.org/clubs")
browser.maximize_window()

select_range = browser.find_element(By.ID, "search-filter__range")
selected_range = Select(select_range)
selected_range.select_by_value("max")

scrollable_div = browser.find_element(By.XPATH, "//*[contains(@class, 'club-list-new') and contains(@class, 'list--nostyle')]")

last_height = browser.execute_script("return arguments[0].scrollHeight", scrollable_div)

while True:
    time.sleep(2)
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    time.sleep(5)

    new_height = browser.execute_script("return arguments[0].scrollHeight", scrollable_div)
    if new_height == last_height:
        break
    last_height = new_height

elems=browser.find_elements(By.CLASS_NAME,"club-list-item-new__details-link")
data=[]

for elem in elems:
    href = elem.get_attribute("href")
    if href:
        browser.execute_script("window.open('"+href+"');")
        time.sleep(0.4)
        browser.switch_to.window(browser.window_handles[-1])

        club_name = np.nan
        club_website = np.nan
        club_mail = np.nan
        club_contact_name = np.nan

        try:
            club_name=browser.find_element(By.CLASS_NAME,"club__header").text
            print(club_name.text)
        except NoSuchElementException:
            pass
        try:
            club_link=browser.find_element(By.CLASS_NAME,"btn-link")
            club_website=club_link.get_attribute("href")
            print(club_link.get_attribute("href"))
        except NoSuchElementException:
            pass
        try:
            contact=browser.find_element(By.CLASS_NAME,"club-contact__content")
            texts=contact.find_elements(By.TAG_NAME,"p")
        except NoSuchElementException:
            texts=[]

        if len(texts) > 0:
            if not texts[0].text.endswith(".com"):
                club_contact_name = texts[0].text
                print(club_contact_name)
                if len(texts) > 1 and texts[1].text.endswith(".com"):
                    club_mail = texts[1].text
                    print(club_mail)
            elif texts[0].text.endswith(".com"):
                club_mail = texts[0].text
                print(club_mail)
                club_contact_name =np.nan
        else:
            club_contact_name=np.nan
            club_mail=np.nan
            print(club_contact_name)
            print(club_mail)
        print("\n")
        data.append([club_name,club_contact_name,club_mail,club_website])
        browser.close()
        browser.switch_to.window(browser.window_handles[0])


df=pandas.DataFrame(data=data,columns=["Club Name","Club Contact Name","Club Mail Address","Club Website"])
df.to_excel("clubs.xlsx", index=False, engine="openpyxl")

input("Entara basarak tarayıcıyı kapatabilirsiniz.")
browser.quit()