def viber(driver, aim, code):
    from time import sleep
    driver.get("https://account.viber.com/en/forget-password")
    sleep(2.5)
    driver.find_element("xpath", "/html/body/div[1]/div/div[2]/section/div/div/div/div/form/div/div[1]/div[2]/div/input[2]").send_keys(aim.replace(code, ""))
    driver.find_element("xpath", "/html/body/div[1]/div/div[2]/section/div/div/div/div/form/div/div[3]/button").click()
    sleep(2.5)