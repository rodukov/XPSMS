def yandex(driver, aim, code):
    from time import sleep
    driver.get("https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fhelpers.tap.yandex.ru%2Freturn-to-app%3Ffb%3Dhttps%3A%2F%2Ftaxi.yandex.ru%2F&origin=taxi_front_form")
    sleep(2.5)
    driver.find_element("xpath", "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[2]/button").click()
    driver.find_element("xpath", '//*[@id="passp-field-phone"]').send_keys(aim.replace(code, ''))
    driver.find_element("xpath", '//*[@id="passp:sign-in"]').click()
    sleep(2.5)