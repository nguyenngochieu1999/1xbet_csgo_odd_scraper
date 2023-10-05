from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import datetime
import time

driver = webdriver.Firefox()
driver.get("https://1xbet.com/en/sports/esports/live/480622274-gate-warriors-team-ercrim")
time.sleep(1)
sub_game = driver.find_element(By.CLASS_NAME, "sub-game")
map_order = sub_game.find_element(By.CLASS_NAME, "betTypeName").text
print(map_order)
map_markets = sub_game.find_element(By.CLASS_NAME, "c-sport-markets")
bet_groups = map_markets.find_elements(By.CLASS_NAME, "bet_group")
moneyline_group = bet_groups[0]
handicap_group = bet_groups[2]
# moneyline_title = moneyline_group.find_element(By.CLASS_NAME, "bet-title-label")
# handicap_title = handicap_group.find_element(By.CLASS_NAME, "bet-title-label")
# print(moneyline_title.text)
# print(handicap_title.text)



home_moneyline_odd = 0.0
away_moneyline_odd = 0.0
try:
    while map_markets.find_elements(By.CLASS_NAME, "bet_group"):
        moneyline_title = moneyline_group.find_element(By.CLASS_NAME, "bet-title-label")
        try:
            bet_detail_moneyline = moneyline_group.find_element(By.CLASS_NAME, "betCols2")
            moneyline_inner = bet_detail_moneyline.find_elements(By.CLASS_NAME, "bet-inner")
            home_team = moneyline_inner[0].find_element(By.CLASS_NAME, "bet_type").text
            away_team = moneyline_inner[1].find_element(By.CLASS_NAME, "bet_type").text
            live_home_moneyline_odd = moneyline_inner[0].find_element(By.CLASS_NAME, "koeff__label").text
            live_away_moneyline_odd = moneyline_inner[1].find_element(By.CLASS_NAME, "koeff__label").text
            if home_moneyline_odd != live_home_moneyline_odd:
                home_moneyline_odd = live_home_moneyline_odd
                away_moneyline_odd = live_away_moneyline_odd
                moneyline_data = {
                    home_team: home_moneyline_odd,
                    away_team: away_moneyline_odd
                }
                print(datetime.datetime.now(), moneyline_data)
            

        except NoSuchElementException:
            moneyline_title.click()

except StaleElementReferenceException:
    print("Match Ended")