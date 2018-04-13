
"""
正常打开网页
# -*- coding: utf-8 -*-

from selenium import webdriver
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
#options.add_experimental_option("prefs", prefs)
# 设置UA
options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"')
# 设置无头
# options.add_argument('--headless')
#options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
mobile_emulation = {"deviceName": "Google Nexus 5" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options=options)

# self.driver.implicitly_wait(20)
driver.get("http://www.baidu.com")
#driver.get('https://www.zhihu.com/signup')
driver.close()
print (driver.url)
'''

#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#模拟移动设备登录网页
mobile_emulation = {"deviceMetrics": {"width": 750, "height": 1334, "pixelRatio": 6.0}, # 定义设备高宽，像素比
                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) " # 通过user agent代理来模拟
                "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
chrome_options = Options() 
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options) 
driver.get("http://www.baidu.com") 
#time.sleep(5)
#driver.close()