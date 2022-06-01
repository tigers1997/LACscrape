from zyte_smartproxy_selenium import webdriver

browser = webdriver.Chrome(spm_options={'spm_apikey': '1605d5d6013b4a96983c1aaa1b611524'})
browser.get('https://toscrape.com')
browser.save_screenshot('screenshot.png')
browser.close()