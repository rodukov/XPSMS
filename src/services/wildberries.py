def wildberries(driver, aim, code):
    from time import sleep
    driver.get("https://www.wildberries.by/security/login?returnUrl=https%3A%2F%2Fwww.wildberries.by%2F")
    sleep(2.5)
    driver.find_element("xpath", "/html/body/div[1]/main/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[2]/input").send_keys(aim.replace(code, ""))
    driver.find_element("xpath", '//*[@id="requestCode"]').click()
    sleep(2.5)