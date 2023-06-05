from bs4 import BeautifulSoup
import requests,random,string,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = "https://steamcommunity.com/login"

global k
k = 3

def setup():
    url ="https://steamcommunity.com/login"
    user = str(input("Enter you username: "))
    pwd = str(input("Enter your password: "))
    driver.get(url)
    
    driver.find_element_by_id("input_username").send_keys(user)
    driver.find_element_by_id("input_password").send_keys(pwd)
    sumbit = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div/div[1]/div/div/div/div/div[3]/div[1]/button")
    sumbit.click()
    auth = str(input("Enter auth code: "))
    try:
        driver.find_element_by_class_name("authcode").send_keys(auth)
        authsubmit = driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/div/div/form/div[4]/div[1]/div[1]")
        continueButton = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]")
        authsubmit.click()
        continueButton.click()
    except:
        pass
    try:
        driver.find_element_by_id("twofactorcode_entry").send_keys(auth)
        authsubmit = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]")
        continueButton = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]")
        authsubmit.click()
        continueButton.click()
    except:
        pass
    driver.implicitly_wait(5)
    edit_profile = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[1]/div/div/div/div[3]/div[2]/a/span")
    edit_profile.click()
    print("[+] Setup Complete!")

def sniper(id):
    try:    
        driver.find_element_by_name("customURL").clear()
        driver.find_element_by_name("customURL").send_keys(id, Keys.ENTER)
    except Exception:
        driver.find_element_by_name("customURL").send_keys(id, Keys.ENTER)
    time.sleep(3)
    if len(driver.current_url.split("/")[4]) == k:
        print("""
        ▄████ ▓█████▄▄▄█████▓     ██████  ███▄    █  ██▓ ██▓███  ▓█████ ▓█████▄ 
        ██▒ ▀█▒▓█   ▀▓  ██▒ ▓▒   ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▒██▀ ██▌
        ▒██░▄▄▄░▒███  ▒ ▓██░ ▒░   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ░██   █▌
        ░▓█  ██▓▒▓█  ▄░ ▓██▓ ░      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ░▓█▄   ▌
        ░▒▓███▀▒░▒████▒ ▒██▒ ░    ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░▒████▓ 
        ░▒   ▒ ░░ ▒░ ░ ▒ ░░      ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░ ▒▒▓  ▒ 
        ░   ░  ░ ░  ░   ░       ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░ ░ ▒  ▒ 
        ░ ░   ░    ░    ░         ░  ░  ░     ░   ░ ░  ▒ ░░░          ░    ░ ░  ░ 
            ░    ░  ░                 ░           ░  ░              ░  ░   ░    
                                                                        ░      \n[+] The ID is %s.""" %(id))
        return True
        #print('[+] False Positive')

def main():
    setup()
    while True:
        id = ''.join(random.choices(string.ascii_uppercase +  string.digits + "-" + "_", k=k)) 
        print(id)
        botak = sniper(id)
        if botak == True:
            break

main()
