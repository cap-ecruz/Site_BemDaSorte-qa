from selenium.webdriver.common.by import By

class PaginaCheckoutElementos(object):
    VALOR_TOTAL = (By.XPATH, '/html/body/app-root/div/ng-component/main/section/div[2]/div/div[2]')
    SUBTOTAL = (By.XPATH, '/html/body/app-root/div/ng-component/main/section/div[1]/div/div/div/ul/li/app-cart-item/div/div[3]/div[2]/span')