import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

'''使浏览器静音'''
options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
# 填写webdriver的保存目录

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 记得写完整的url 包括http和https
driver.get('https://cn.bing.com/search?q=0&form=CHRDEF&sp=-1&lq=0&pq=0&sc=10-1&qs=n&sk=&cvid=BB393FAA7013407287D52DF7395A19B4&ghsh=0&ghacc=0&ghpl=')

# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies.txt', 'r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)

    # 方法1 将expiry类型变为int
    for cookie in cookies_list:
        # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
driver.refresh()
for i in range(0,38):
    driver.get(f"https://cn.bing.com/search?q={str(i)+'a'}&qs=n&form=QBRE&sp=-1&lq=0&pq=1&sc=10-1&sk=&cvid=FEDE7C3215D2434DB108136E25D71940&ghsh=0&ghacc=0&ghpl=")
    time.sleep(0.6)
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', {'deviceName': 'Galaxy S5'})  # 模拟iPhone X浏览
driver = webdriver.Chrome(options=options)
driver.get('https://cn.bing.com/search?q=0&form=CHRDEF&sp=-1&lq=0&pq=0&sc=10-1&qs=n&sk=&cvid=BB393FAA7013407287D52DF7395A19B4&ghsh=0&ghacc=0&ghpl=')
driver.delete_all_cookies()
with open('cookies.txt', 'r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)

    # 方法1 将expiry类型变为int
    for cookie in cookies_list:
        # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
driver.refresh()
time.sleep(2)
driver.refresh()
for i in range(0,34):
    driver.get(f"https://cn.bing.com/search?q={str(i)+'b'}&qs=ds&form=QBRE&pc=BG00")
    time.sleep(0.6)



