from seleniumbase import SB

with SB(uc=True) as sb:
    sb.driver.get("https://www.ozon.ru/ozonid")