def ozon(driver, aim, code):
    from time import sleep
    driver.get("https://www.ozon.ru/ozonid")
    sleep(2.5)
    driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div/div[1]/section/div/div/div/div/div[3]/div/div/div[1]/label/div/div/input").send_keys(aim.replace(code, ""))
    driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div/div[1]/section/div/div/div/div/div[4]/button').click()
    sleep(2.5)