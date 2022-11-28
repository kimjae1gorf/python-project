from selenium import webdriver # 셀레니움의 기능중 웹 드라이버를 사용하기 위해 셀레니움으로부터 임포트
from selenium.webdriver.common.by import By # 웹 드라이버 기능 중 웹 요소를 출력하기 위한 by 입포트
import time # 시간 설정을 위해 타임 임포트



driver = webdriver.Chrome("chromedriver") # 실행 시 웹 브라우저 중 크롬을 사용하기 위해 크롬드라이버를 불러옴
driver.get("https://kosis.kr/covid/covid_index.do") # 실행 시 크롬으로 불러올 사이트를 설정(코로나 현황을 나타내주는 통계청 사이트)

entire_situation = driver.find_elements(By.CLASS_NAME, 'DashboardBox') # 통계청 사이트의 요소 중 코로나 바이러스 현황이 나타나있는 현황판의 수치를 출력하기 위해 해당 요소를 정의함
for i in entire_situation: # 정의한 요소들을 텍스트로 출력하기 위해 텍스트로 새로 정의한 뒤 출력
    entire_situation = i.text
    print(entire_situation)
time.sleep(3) # 출력한 뒤 3초간 정지


cl = driver.find_element(By.CSS_SELECTOR, '#byDateTab') # 통계청 사이트 내에 버튼 요소중 일별 현황에 대한 수치 현황판을 정의
cl.click() # 정의한 현황판을 클릭
time.sleep(3) # 클릭한 후 3초간 정지


today = driver.find_elements(By.CLASS_NAME, 'DashboardBox.Type3')[1].text # 위에서 클릭한 일별 현황판에 대한 요소를 정의. 같은 이름의 클래스를 가진 요소가 여러개 있기 때문에 그 중 해당 현황판에 해당하는 순서를 리스트로 설정 후 
#텍스트로 출력하기 위해 텍스트로 정의
print(today) 
time.sleep(3) # 출력한 후 3초간 정지. 그후 불러온 통계청 사이트 종료.
