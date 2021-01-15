from selenium import webdriver
import time
import schedule
import random

students_infos = []

time_array = ['07:55', '08:00', '08:10', '08:15', '08:20', '08:25', '08:30', '08:35', '08:40', '08:45']

random.shuffle(students_infos)
random.shuffle(time_array)

def macro () :
    global students_infos

    driver = webdriver.Edge('D:\school\대회 및 프로젝트\자가진단 매크로 v2\msedgedriver.exe')
    driver.implicitly_wait(3)

    driver.quit()

    for student_info in students_infos :
        driver = webdriver.Edge('D:\school\대회 및 프로젝트\자가진단 매크로 v2\msedgedriver.exe')
        driver.implicitly_wait(3)

        driver.get('https://hcs.eduro.go.kr/')
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button').click()
        time.sleep(1)

        region = webdriver.support.ui.Select(driver.find_element_by_xpath('//*[@id="sidolabel"]'))

        if student_info[0] == '' :
            region.select_by_value('16')
            time.sleep(1)

        elif student_info[0] == '' :
            region.select_by_value('06')
            time.sleep(1)

        else :
            region.select_by_value('03')
            time.sleep(1)

        grade = webdriver.support.ui.Select(driver.find_element_by_xpath('//*[@id="crseScCode"]'))
        grade.select_by_value('4')
        time.sleep(1)

        if student_info[0] == '' :
            for i in '' :
                driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(i)
                time.sleep(0.2)

        elif student_info[0] == '' :
            for i in '' :
                driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(i)
                time.sleep(0.2)

        else :
            for i in '' :
                driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(i)
                time.sleep(0.2)

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
        time.sleep(1)

        for i in student_info[0] :
            driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(i)
            time.sleep(0.2)

        time.sleep(1)

        for i in student_info[1] :
            driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(i)
            time.sleep(0.2)

        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(1)

        for i in student_info[2] :
            driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(i)
            time.sleep(0.2)

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="topMenuBtn"]').click()
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="topMenuWrap"]/ul/li[4]/button').click()
        time.sleep(1)

        logout = driver.switch_to_alert()
        logout.accept()
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/button').click()
        time.sleep(1)

        account = driver.switch_to_alert()
        account.accept()
        time.sleep(1)

        driver.quit()

        print(F'{student_info[0]}님, 자가진단을 완료했습니다.')

    print('자가진단 완료 !')

print(F'내일은 {time_array[0]}에 자가진단을 합니다')

while True :
