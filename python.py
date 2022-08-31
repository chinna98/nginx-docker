from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def performane_cacl(url2):
    #driver.get(url2)
    #driver.refresh()
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    ''' Calculate the performance'''
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print(driver.current_url)
    print("Back End FOR Current PAGE: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)


def performane_caclu(url2):
    driver.get(url2)
    #driver.refresh()
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    ''' Calculate the performance'''
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart
    print(driver.current_url)
    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)



#driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome()

#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()
#navigate to the url  
driver.get("http://dashboard.sellerapp.com")

username_field = driver.find_element_by_name("user-email")
username_field.send_keys("demo@sellerapp.com")
#email_field = driver.find_element(id: 'user_email')
#email_field.send_keys("user@test.com")

password_field = driver.find_element_by_name("user-password")
password_field.send_keys("SellerApp@123")

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End FOR LOGGINING IN: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

#sign_in_button = driver.find_element_by_id("auth-login")

#sign_in_button.click()
driver.find_element_by_id("auth-login").click()
#login=find_elements("auth-login")
#login.click()

time.sleep(5)
#driver.get("http://35.202.129.90:4002/seller/dashboard")


print("Function values performance")
performane_cacl(driver.current_url)
print(driver.current_url)
#navigate=driver.navigate().to("http://35.202.129.90:4002/seller/dashboard");

#identify the Google search text box and enter the value
#driver.find_element_by_name("q").semat-button-wrappernd_keys("javatpoint")
#time.sleep(10)
#click on the Google search button
#driver.find_element_by_name("Profile").click()
#time.sleep(3)
#close the browser
#username_field = driver.find_element_by_id("menu-home")
#username_field.send_keys("demo@sellerapp.com")
#home_button = driver.find_element_by_id("menu-home")
#home_button.click()
#print(driver.current_url)
driver.implicitly_wait(10)
print("Function values performance for HOME PAGE")
#performane_cacl(driver.current_url)
print(driver.current_url)

driver.execute_script("scrollBy(0,-500);")
time.sleep(5)

driver.execute_script("scrollBy(0,400);")
time.sleep(5)

driver.execute_script("scrollBy(0,-600);")
time.sleep(5)



print("wait for some time")
time.sleep(30)

from selenium.webdriver.common.keys import Keys
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

driver.find_element_by_class_name("text-link-hover").click()
#profile = driver.find_element_by_id("menu-profile")
#profile.click()
driver.find_element_by_id("menu-profile").click()
print("Function values performance for PROFILE PAGE")
performane_cacl(driver.current_url)

time.sleep(30)

menupi = driver.find_element_by_id("menu-pi")
menupi.click()
print("Function values performance for PI HOME PAGE")
performane_cacl(driver.current_url)

print("Going inside all product intelligece menu for one asin")
driver.refresh()

print("waiting for some time")
#time.sleep(30)
#asin_field = driver.find_element_by_id("ag-90-input")
#username_field.send_keys("B09KWJTZ4V")
driver.get("https://dashboard.sellerapp.com/seller/tracked-products/asin/overview/B09KWJTZ4V")
print("Function values performance for PI ASIN PAGE")
performane_cacl(driver.current_url)
time.sleep(30)
#pk_field = driver.find_element_by_name("Product Keyword").first().click()
#pk_field.send_keys("demo@sellerapp.com")

print("Product Keyword for ASIN")
performane_caclu("https://dashboard.sellerapp.com/seller/tracked-products/asin/product-keyword/B09KWJTZ4V")
time.sleep(17)
print("Keyword tracking for ASIN")
performane_caclu("https://dashboard.sellerapp.com/seller/tracked-products/asin/keyword-tracking/B09KWJTZ4V")
time.sleep(18)
print("INDEX CHECKER for ASIN")
performane_caclu("https://dashboard.sellerapp.com/seller/tracked-products/asin/index-checker/B09KWJTZ4V")
time.sleep(16)
print("Listing Quality for ASIN")
performane_caclu("https://dashboard.sellerapp.com/seller/tracked-products/asin/listing-quality/B09KWJTZ4V")

print("PI test case successfully completed")

print("PPC Overview")
driver.find_element_by_id("menu-ppc").click()
performane_cacl(driver.current_url)
time.sleep(10)
print("PPC Insigts")
driver.find_element_by_id("menu-ppc-is").click()
performane_cacl(driver.current_url)
time.sleep(10)
print("PPC Posstive search terms")
driver.find_element_by_id("menu-ppc-pst").click()
performane_cacl(driver.current_url)
time.sleep(10)
print("PPC Auto to Manual")
driver.find_element_by_id("menu-ppc-atm").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("PPC Target Improvement")
driver.find_element_by_id("menu-ppc-ti").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("PPC Bid Optimization")
driver.find_element_by_id("menu-ppc-bo").click()
performane_cacl(driver.current_url)
time.sleep(10)
print("PPC Possitive Asin")
driver.find_element_by_id("menu-ppc-pasin").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("PPC Negative Asin")
#find_elements("menu-ppc-nasin").click()
driver.find_element_by_id("menu-ppc-nasin").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("Automation")
driver.find_element_by_id("menu-ppc-automation").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("Search term explorer")
driver.find_element_by_id("menu-ppc-ste").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("Product Analysis")
driver.find_element_by_id("menu-ppc-pa").click()
performane_cacl(driver.current_url)
time.sleep(10)


print("Campain Manager")
driver.find_element_by_id("menu-ppc-cm").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("Report Central")
driver.find_element_by_id("menu-ppc-rc").click()
performane_cacl(driver.current_url)
time.sleep(10)

print("History")
driver.find_element_by_id("menu-ppc-history").click()
performane_cacl(driver.current_url)
time.sleep(10)

time.sleep(10)
print("SALES")
driver.find_element_by_id("menu-sales").click()
performane_cacl(driver.current_url)
time.sleep(30)


print("KR")
driver.find_element_by_id("menu-kt").click()
performane_cacl(driver.current_url)

time.sleep(20)

'''
kr_field = driver.find_element_by_class_name("mat-input-element mat-form-field-autofill-control mat-autocomplete-trigger ng-tns-c93-17 ng-pristine ng-valid cdk-text-field-autofill-monitored ng-touched")
kr_field.send_keys("chinna")
time.sleep(20)
driver.find_element_by_class_name("mat-focus-indicator mat-button-input-inline search-button button-l mat-flat-button mat-button-base mat-primary").click()
performane_cacl(driver.current_url) '''


print("Keyworsd Research")
driver.find_element_by_id("menu-kt-ra").click()
performane_cacl(driver.current_url)

time.sleep(40)





print("Product Research")
driver.find_element_by_id("menu-pr").click()
performane_cacl(driver.current_url)

time.sleep(10)




driver.close()






