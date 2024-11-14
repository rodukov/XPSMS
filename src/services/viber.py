def viber(driver, aim, code):
    driver.get("https://account.viber.com/en/forget-password")

    driver.find_element("xpath", "/html/body/div[1]/div/div[2]/section/div/div/div/div/form/div/div[1]/div[2]/div/input[2]").send_keys(aim.replace(code, ""))
    driver.find_element("xpath", "/html/body/div[1]/div/div[2]/section/div/div/div/div/form/div/div[3]/button").click()

    return driver.title