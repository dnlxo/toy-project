import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import subprocess
import shutil
from time import sleep


# 응모할 아디, 비번
id_list = ['id1', 'id2']
pw_list = ['pw1', 'pw2']


# 크롬 실행
try :
    shutil.rmtree("/Users/wetaeyoung/Desktop/abc/ccfiles")  # 쿠키 / 캐쉬파일 삭제
except :
    pass

subprocess.Popen('/Applications/Google\ Chrome.app/Contents/MacOS/Google\ chrome --remote-debugging-port=9222 --user-data-dir="/Users/wetaeyoung/Desktop/abc/ccfiles"', shell=True)
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    service = Service(f'./{chrome_ver}/chromedriver')
    driver = webdriver.Chrome(service=service, options=option)
except:
    chromedriver_autoinstaller.install(True)
    service = Service(f'./{chrome_ver}/chromedriver')
    driver = webdriver.Chrome(service=service, options=option)


# 사이트 열고 로그인
def open_and_login(user_id, user_pw) :
    sleep(3)
    driver.get('https://www.nike.com/kr/launch/')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="jq_m_right_click"]/div/ul/li[2]/a').click()
    driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="j_username"]'))).send_keys(user_id)
    WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="j_password"]'))).send_keys(user_pw)
    driver.find_element_by_xpath('//*[@id="common-modal"]/div/div/div/div/div[2]/div/div[2]/div/button').click()
    driver.implicitly_wait(5)


# 상품 클릭 후 응모
def click_and_draw() :
    sleep(3)
    now_drawing = driver.find_elements_by_xpath("//*[contains(text(),'THE DRAW 응모하기')]")
    for product in now_drawing :
        product.click()
        driver.implicitly_wait(10)
        sleep(3)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkTerms"]/label/i'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="optionPrivacy"]/label/i'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/section/div[2]/aside/div[2]/div[2]/div/div/div/form/div/div[2]/a/span'))).click()
        sleep(0.1)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[1]/section/div[2]/aside/div[2]/div[2]/div/div/div/form/div/div[2]/ul/li[9]/a/span'))).click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="btn-buy"]').click()
        driver.get('https://www.nike.com/kr/launch/')
        driver.implicitly_wait(10)
    
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="jq_m_right_click"]/div/ul/li[1]/div/div/label'))).click()
    sleep(1)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="jq_m_right_click"]/div/ul/li[1]/div/div/ul/li[4]/a'))).click()
    sleep(1)


# 아이디 별로 응모
for i in range(len(id_list)) :
    open_and_login(id_list[i], pw_list[i])
    click_and_draw()