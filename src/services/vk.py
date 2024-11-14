def vk(driver, aim, code):
    from time import sleep
    driver.get("https://id.vk.com/restore/#/resetPassword")
    
    sleep(2.5)

    driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div/div/div/div/section/div/div/div/div/div/div[2]/section/div/form/div[1]/span[1]/input").send_keys(aim)
    driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div/div/div/div/section/div/div/div/div/div/div[2]/section/div/form/div[2]/div/button").click()

    return driver.title