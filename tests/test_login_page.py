import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):
        driver = webdriver.Chrome()
        time.sleep(3)

        # 웹페이지 열기
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # 사용자 이름 필드에 이동
        username_locator = driver.find_element(By.ID, "username")
        # 사용자 이름 필드에 사용자 이름 student 입력
        username_locator.send_keys("student")
        #비밀번호 필드에 이동
        password_locator = driver.find_element(By.NAME, "password")
        # 비밀번호 필드에 password 123 입력
        password_locator.send_keys("Password123")
        # 제출 버튼 이동
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        #제출버튼 누르기
        submit_locator.click()
        time.sleep(2)
        # 새 페이지 URL에 practicetestautomation.com/logged-in-successfully 이 포함되어 있는지 확인합니다
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        # 새 페이지에 예상 텍스트('Congratulations' 또는 'successfully logged in'가 포함되어 있는지 확인합니다
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"
        # 새 페이지에 로그아웃 확인 버튼이 표시됩니다
        log_out_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_locator.is_displayed()