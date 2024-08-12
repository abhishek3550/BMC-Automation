print("BMC automation is starting..............")
from SPFOL import username,password,question1,question2,question3,securityans1,securityans2,securityans3,assignto
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains  # for mouse action
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
driver=webdriver.Firefox()
print(assignto)
driver.get("https://flipkart.onbmc.com/arsys/forms/onbmc-s/SHR%3ALandingConsole/Default+Administrator+View/?cacheid=ed31a938")
driver.maximize_window()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, by this have make site to waite for some time.
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]'))).send_keys(username)
Clickcontinue = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/form/div/div[3]/div/button')
Clickcontinue.click()
time.sleep(2)
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys(password)

driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/form/div/div[3]/div/button').click()
driver.implicitly_wait(10)
time.sleep(2)

#1 Security Question
Q1=driver.find_element_by_xpath('//label[contains(@class,"sc-iwsKbI hOobUj")]')
print(Q1.text)
if Q1.text == question1:
    securityq = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secure-answer"]')))
    securityq.send_keys(securityans1)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div/form/div/div[2]/button').click()
elif Q1.text == question2:
    securityq = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secure-answer"]')))
    securityq.send_keys(securityans2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div/form/div/div[2]/button').click()
elif Q1.text == question3:
    securityq = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secure-answer"]')))
    securityq.send_keys(securityans3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div/form/div/div[2]/button').click()

else:
    print("Ans don't match")
time.sleep(2)
print("Correct Answer")
#2 Security Question
Q2=driver.find_element_by_xpath('//label[contains(@class,"sc-iwsKbI hOobUj")]')
print(Q2.text)

if Q2.text == question1:
    securityq = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secure-answer"]')))
    securityq.send_keys(securityans1)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div/form/div/div[2]/button').click()

elif Q2.text == question2:
    securityq = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secure-answer"]')))
    securityq.send_keys(securityans2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div/form/div/div[2]/button').click()
elif Q2.text == question3:
    securityq = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secure-answer"]')))
    securityq.send_keys(securityans3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[3]/div/form/div/div[2]/button').click()
else:
    print("Ans don't match")

print("Correct Answer")
rememberbutton = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/button')))
rememberbutton.click()
time.sleep(13)

def alert_accept():
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Alert detected, accept it")
        return True
    except UnexpectedAlertPresentException:
        print("Hum..., continue?")
        return False
    except NoAlertPresentException:
        print("1.No alert here")
        return False

while alert_accept() == True:
    alert_accept()
print('login clear')
driver.implicitly_wait(10)
time.sleep(10)
app = WebDriverWait(driver,130).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="reg_img_304316340"]')))
app.click()
time.sleep(2)
driver.implicitly_wait(20)
incident=driver.find_elements_by_xpath('//*[@id="FormContainer"]/div//a/span')

for incid in incident:
    if incid.text == "Incident Management":
        incid.click()
        break
driver.implicitly_wait(20)
inci=driver.find_elements_by_xpath('//span[contains(@class,"navLabel root ")]')
for inc in inci:
    if inc.text == 'Incident Management':
        inc.click()
        break

time.sleep(2)
driver.implicitly_wait(20)
incns =driver.find_elements_by_xpath('//span[contains(@class,"navLabel lvl1 ")]')
for incnso in incns:
    if incnso.text == 'Incident Management Console':
        action = ActionChains(driver)
        action.move_to_element(incnso).click().perform()
        driver.implicitly_wait(30)
        time.sleep(8)
        break

print('Incident Management Console')
def alert_accept2():
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Alert detected 2 accept it")
        return True
    except UnexpectedAlertPresentException:
        print("Hum..., continue?")
        return False
    except NoAlertPresentException:
        print("2.No alert here")
        return False
while alert_accept2() == True:
    alert_accept2()
##show =
time.sleep(3)
show = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_303174300"]/div/a/img')))
show.click()
time.sleep(15)
# selet group assign
driver.implicitly_wait(30)
menu = driver.find_element_by_id('arid_WIN_3_303174300')
menu.click()
time.sleep(10)

driver.implicitly_wait(30)
listass = driver.find_elements_by_xpath("//tbody[contains(@class,'MenuTableBody')]//tr")
for value in listass:
    if value.text == 'Assigned To All My Groups':
        value.click()  # if is True then Assigned To All My Groups  will be selected
        break  # and loop will break

unassigned = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_304017000"]/div/div')))
unassigned.click()


while True:
    time.sleep(10)
    driver.implicitly_wait(30)
    ticketstatus = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_302087200"]/div[1]/table/tbody/tr/td[1]')))

    if ticketstatus.text != 'Showing 0 - 0 of 0':
        view = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_301428900"]/div[2]/div')))
        print(view.text)
        view.click()
        asstoenggdown = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_4_1000000218"]/a')))
        asstoenggdown.click()
        time.sleep(20)
        driver.implicitly_wait(30)
        asstoengg = driver.find_elements_by_xpath("//tr[contains(@class,'MenuTableRow')]//td")
        for asval in asstoengg:
            u = asval.text
            print(u)  # value #now we can print value of list one by one in text
        for asval in asstoengg:
            if asval.text == assignto:
                asval.click()  # if is True then Assigned To All My Groups  will be selected
                break  # and loop will break
        time.sleep(5)
        driver.implicitly_wait(10)
        print("assign to",assignto)
        time.sleep(15)
        driver.implicitly_wait(10)
        statusdown = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_4_7"]/div/a')))
        statusdown.click()

        time.sleep(5)
        driver.implicitly_wait(30)

        statuslist = driver.find_elements_by_xpath("//tr[contains(@class,'MenuTableRow')]//td")
        for val in statuslist:
            if val.text == 'In Progress':
                val.click()  # if is True then Assigned To All My Groups  will be selected
                break  # and loop will break
        time.sleep(5)
        print("Ticket is in In-progress mode")
        time.sleep(10)
        driver.implicitly_wait(50)
        save = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_4_301614800"]/div/div')))
        save.click()
        time.sleep(10)
        driver.implicitly_wait(10)
        print('Saving')
        indidenconsolback = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_0_304248710"]/fieldset/div/dl/dd[3]/span[2]/a')))
        indidenconsolback.click()
        unassigned = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_304017000"]/div/div')))
        unassigned.click()
        driver.get_screenshot_as_file("A.png")

        # break
    elif ticketstatus.text == 'Showing 0 - 0 of 0':
        print("No ticket in  unassigned mode")
        print(ticketstatus.text)
        Unacknowledged=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="WIN_3_304017100"]/div/div')))
        Unacknowledged.click()

        break

while True:
    time.sleep(5)
    driver.implicitly_wait(10)
    ticketstatus = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_302087200"]/div[1]/table/tbody/tr/td[1]')))

    if ticketstatus.text != 'Showing 0 - 0 of 0':
        print("checking Unacknowledged mode")
        view = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_301428900"]/div[2]/div')))
        print(view.text)
        view.click()
        asstoenggdown = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_4_1000000218"]/a')))
        asstoenggdown.click()
        time.sleep(20)
        driver.implicitly_wait(30)
        asstoengg = driver.find_elements_by_xpath("//tr[contains(@class,'MenuTableRow')]//td")
        for asval in asstoengg:
            if asval.text == assignto:
                asval.click()  # if is True then Assigned To All My Groups  will be selected
                break  # and loop will break
        time.sleep(5)
        driver.implicitly_wait(10)
        print("Ticket Assign to",assignto)
        time.sleep(15)
        driver.implicitly_wait(10)
        statusdown = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_4_7"]/div/a')))
        statusdown.click()

        time.sleep(5)
        driver.implicitly_wait(30)

        statuslist = driver.find_elements_by_xpath("//tr[contains(@class,'MenuTableRow')]//td")
        for val in statuslist:
            if val.text == 'In Progress':
                val.click()  # if is True then Assigned To All My Groups  will be selected
                break  # and loop will break
        time.sleep(5)
        print("Ticket is in In-progress mode")
        time.sleep(10)
        driver.implicitly_wait(50)
        save = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_4_301614800"]/div/div')))
        save.click()
        time.sleep(10)
        driver.implicitly_wait(10)
        print('Saving')
        indidenconsolback = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_0_304248710"]/fieldset/div/dl/dd[3]/span[2]/a')))
        indidenconsolback.click()
        Unacknowledged = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="WIN_3_304017100"]/div/div')))
        Unacknowledged.click()

    elif ticketstatus.text == 'Showing 0 - 0 of 0':
        print("No ticket  to Assign")
        print(ticketstatus.text)
        logout = driver.find_element_by_xpath('//*[@id="WIN_0_300000044"]/div/div')
        logout.click()
        time.sleep(3)
        driver.quit()
        print("Thankyou Abhishek Singh")
    else:
        logout = driver.find_element_by_xpath('//*[@id="WIN_0_300000044"]/div/div')
        logout.click()
        time.sleep(3)
        driver.quit()
        print("Abhishek Singh")