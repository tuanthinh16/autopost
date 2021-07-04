from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='chromedriver.exe')
username = 'admin'
password = '1'
email = 'thinh@thinh.com'
title = """TTessting"""
type = 'Free Lance'
details = """Hello
"""
keySearch = type
comment = 'first comment'
driver.get('http://127.0.0.1:3000')
time.sleep(2)

# # dang ky
# driver.get('http://localhost:3000/resigter')
# time.sleep(3)
# driver.find_element_by_id('inputUsername').send_keys(username)
# time.sleep(1)
# driver.find_element_by_id('inputPassword').send_keys(password)
# time.sleep(1)
# driver.find_element_by_id('inputrepassword').send_keys(password)
# time.sleep(1)
# driver.find_element_by_id('inputemail').send_keys(email)
# time.sleep(1)
# driver.find_element_by_id('btn-create').click()
# time.sleep(1)

# dang nhap
driver.get('http://127.0.0.1:3000/login')
time.sleep(3)
driver.find_element_by_id('inputUsername').send_keys(username)
time.sleep(1)
driver.find_element_by_id('inputPassword').send_keys(password)
time.sleep(1)
driver.find_element_by_id('btn-login').click()
time.sleep(1)
driver.get('http://127.0.0.1:3000/addpost')
time.sleep(2)

# dang bai
driver.find_element_by_id('inputtitle').send_keys(title)
time.sleep(1)
select = Select(driver.find_element_by_id('type'))
select.select_by_visible_text(type)
time.sleep(2)
driver.find_element_by_id('textareadetail').send_keys(details)
time.sleep(4)
driver.find_element_by_id('add').click()
time.sleep(3)
# luot homepage
driver.execute_script('window.scroll(0,300)')
time.sleep(1)
driver.execute_script('window.scroll(0,500)')
time.sleep(2)
driver.execute_script('window.scroll(0,700)')
time.sleep(1)
driver.execute_script('window.scroll(0,900)')
time.sleep(1)
driver.execute_script('window.scroll(0,1100)')
time.sleep(1)
driver.execute_script('window.scroll(0,1300)')
time.sleep(1)
# tim bai vua dang
driver.find_element_by_name('searchValue').send_keys(keySearch)
time.sleep(1)
driver.find_element_by_id('search').click()
time.sleep(2)
# cmt vao bai vua dang
driver.find_element_by_id('cmt').click()
time.sleep(2)
driver.execute_script('window.scroll(0,300)')
time.sleep(2)
driver.find_element_by_name('comment').send_keys(comment)
time.sleep(2)
driver.find_element_by_id('push-comment').click()
time.sleep(2)
driver.execute_script('window.scroll(0,500)')
time.sleep(2)


# show theo the loai
# driver.get('http://localhost:3000/showbyid/1')
# time.sleep(2)
# driver.execute_script('window.scroll(0,300)')
# time.sleep(2)
# driver.get('http://localhost:3000/showbyid/2')
# time.sleep(2)
# driver.execute_script('window.scroll(0,300)')
# time.sleep(2)
# driver.get('http://localhost:3000/showbyid/3')
# time.sleep(2)
# driver.execute_script('window.scroll(0,300)')
# time.sleep(2)
# driver.get('http://localhost:3000/showbyid/4')
# time.sleep(2)
# driver.execute_script('window.scroll(0,300)')
# time.sleep(2)
# driver.get('http://localhost:3000/showbyid/5')
# time.sleep(2)
# driver.execute_script('window.scroll(0,300)')
# time.sleep(2)
# driver.get('http://localhost:3000/showbyid/6')
# time.sleep(2)
# driver.execute_script('window.scroll(0,300)')
# time.sleep(2)

driver.quit()
