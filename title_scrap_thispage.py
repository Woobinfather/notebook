from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

# 새로운 Chrome 브라우저 실행
service = Service('C:\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # 특정 웹사이트 열기
    driver.get("https://www.skku.edu/skku/index.do")
    print("웹사이트 열림")
    
    # 명시적 대기 (페이지 로딩 대기용)
    wait = WebDriverWait(driver, 20)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item_body"]/div/div[1]/div[1]/div/ul/li[4]/a')))
    print("로그인 버튼 대기 완료")
    
    # 로그인 버튼 클릭
    login_button.click()
    print("로그인 버튼 클릭됨")
    
    # 페이지가 완전히 로드될 때까지 대기
    time.sleep(5)  # 충분한 대기 시간 추가

    # # 로그인 페이지 로딩 대기 (아이디 입력 필드가 나타날 때까지 대기)
    # id_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div/div/div[1]/input')))
    # print("아이디 입력 필드 대기 완료")
    
    # # 아이디 입력 필드에 값 입력
    # id_field.send_keys('jw1113.kwon')
    # print("아이디 입력 완료")

    # 로그인 버튼 클릭 대기 및 클릭 (ActionChains 사용)
    login_button_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LoginForm"]/div/div/div[3]/label')))
    action.move_to_element(login_button_confirm).click().perform()
    print("로그인 확인 버튼 클릭됨")

finally:
    # 브라우저 닫기
    driver.quit()
    print("브라우저 닫힘")
