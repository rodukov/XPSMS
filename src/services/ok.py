def ok(driver, aim, code):
    from time import sleep
    driver.get("https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink")
    
    sleep(2.5)

    driver.find_element("xpath", '//*[@id="field_phone"]').send_keys(aim.replace(code, ''))
    driver.find_element("xpath", "/html/body/div[12]/div[4]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[4]/div/div/main/div/div/div/div[1]/div[2]/div[2]/form/div[2]/input").click()

    sleep(2.5)
