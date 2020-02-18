# bnk
from selenium.webdriver.common.by import By

class Locators():
    LOGIN_BUTTON1=(By.XPATH, "//*[@id="menu-item-781"]/a")

    INPUT_USERNAME_BOX=(By.ID, "txtUsername")
    INPUT_PASSWORD_BOX=(By.XPATH, "//*[@id="dv-clientlogin"]/div[2]/input")
    LOGIN_BUTTON2=(By.ID, "btnSubmitLogin")

    AGREED_BOX=(By.ID, "Agreed")
    CONTINUE_BUTTON=(By.ID, "continue")

    GRAPH_TOGGLE=(By.XPATH, "//*[@id="primary-navbar-collapse"]/ul[1]/li[2]/a")
    GRAPHING_TOOL=(By.XPATH, "//*[@id="primary-navbar-collapse"]/ul[1]/li[2]/ul/li[1]/a")

    DC_CA=(By.XPATH, "//*[@id="598_anchor"]")
    DC_CAT=(By.XPATH, "//*[@id="598|185_anchor"]")
    DC_CAWS=(By.XPATH, "//*[@id="598|184_anchor"]")
    PLOT_BTN=(By.ID, "btnPlot")
