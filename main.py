from selenium import webdriver
from threading import Timer

END_TIMER = 300 # 5mins
PURCHASE_TIME = 2
chrome_web_driver = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_web_driver)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')

game_on = True

def purchase_phase():
    global game_on
    # purchase_phase to be called every 2 second(s)
    t = Timer(PURCHASE_TIME, purchase_phase)
    t.start()
    if not game_on:
        t.cancel()
        return
    try:
    # purchases
        cookie_maker = driver.find_elements_by_css_selector("#store #products .unlocked")
        cookie_maker[-1].click()
        cookie_maker[-2].click()
        cookie_maker[-3].click()
        crate_upgrade = driver.find_element_by_css_selector("#store .crate")
        crate_upgrade.click()
        reindeer = driver.find_element_by_css_selector(".shimmer")
        reindeer.click()
    except:
        pass

# ending of game
def close_game():
    global game_on
    game_on = False
    score = driver.find_elements_by_css_selector("#game #cookies")
    print(score[0].text)
    driver.close()

t2 = Timer(END_TIMER, close_game)
t2.start()


purchase_phase()
while game_on:
    cookie.click()
