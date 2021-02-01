from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import random

def main():
    driver = webdriver.Chrome()

    driver.get('https://discord.com/login')

    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys('email@domain.com')

    elem = driver.find_element_by_name("password")
    elem.clear()
    elem.send_keys('Password')

    elem.send_keys(Keys.ENTER)
    time.sleep(15)

    driver.get('https://discord.com/channels/id/id')
    time.sleep(15)
    leeted_today = False
    
    sep = ':'
    time_list = ['13', '37', str(random.randint(10,48))]
    leettime = sep.join(time_list)
    now = datetime.now()
    current_day = str(now.strftime("%Y-%m-%d"))
    print("TODAY is: ", current_day,"and LEETtime is; " ,leettime)

    while True:
        now = datetime.now()
        current_time = str(now.strftime("%H:%M:%S"))

        if current_time == leettime and not leeted_today:
            driver.switch_to.active_element.send_keys(':leet:')
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            leeted_today = True
            print("LEETED", current_day, current_time)

            
        if current_day != str(now.strftime("%Y-%m-%d")):
            current_day = str(now.strftime("%Y-%m-%d"))
            leeted_today = False
            time_list = ['13', '37', str(random.randint(10,48))]
            leettime = sep.join(time_list)
            print("----------------------")
            print("TODAY IS: ", current_day, leettime) 
            
        time.sleep(1)

if __name__ == "__main__":
    print("*****************")
    print("* LEETBOT BOT *")
    print("*****************")
    now = datetime.now()
    current_day = str(now.strftime("%Y-%m-%d"))
    current_time = str(now.strftime("%H:%M:%S"))
    print("STARTED: ", current_day, current_time)
    
    main()

