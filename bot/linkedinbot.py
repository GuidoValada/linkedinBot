from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(5)
#linkedIN log in
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

#sending credentials
your_username = "usuario123"
your_password = "contraseña123"
user = driver.find_element_by_id("username")
user.send_keys(your_username)
password = driver.find_element_by_id("password")
password.send_keys(your_password)
password.send_keys(Keys.RETURN)


#number of pages of paginator for this search
for index in range(1,101):
    #url of GET request from 'IT Recruiter' search
    base_url = f"https://www.linkedin.com/search/results/all/?keywords=IT%20recruiter&origin=HISTORY&page={index}"
    driver.get(base_url)

    #Scroll to bottom to load the whole page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #recruiters connect button list
    recruiters = driver.find_elements_by_xpath("//button[text()='Conectar']")
    for recruiter in recruiters:
        #connect click
        driver.execute_script("arguments[0].click();", recruiter)
        try:
            #normal confirm
            send =  driver.find_element_by_xpath("//span[text()='Enviar invitación']").click()
        except:
            #close if email is requested
            ActionChains(driver).move_to_element(recruiter).click().perform()
driver.close()
