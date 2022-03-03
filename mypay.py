from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from dotenv import load_dotenv
import os

load_dotenv()

phone=os.getenv("USER_NAME")
password = os.getenv("PASS_WORD")
bank_id = os.getenv('BANK_ID')
bank_pw = os.getenv('BANK_PW')
top_upno = os.getenv("TOP_UP_NO")
amt = os.getenv('TOP_AMT')
refund_id = os.getenv("REFUND_ID")
refund_amt= os.getenv('REFUND_AMT')
new_pw = os.getenv('NEW_PW')

# print(phone,password,bank_id,bank_pw,top_upno,amt,refund_id,refund_amt,new_pw)
edge_options = EdgeOptions()
edge_options.use_chromium = True 

edge_options.add_argument('user-data-dir=C:\\Users\\Sandeep\\AppData\\Local\\Microsoft\\Edge\\User Data\Default')
edge_options.add_argument("profile-directory=Default");
edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

browser = Edge(options = edge_options, executable_path= "H:\ps\id card\edgedriver_win64\msedgedriver.exe")
url = "https://client.mypay.com.np/Home/login"
browser.get(url)
def create_name():
    f_name = ["sandip","sudip","sadikshya","prajwal","denjing","mana","ayu","paru"]
    l_name = ["bista","thapa","kunwar","rai","limbu","tamang","giri","bhandari"]
    real_name = random.choice(f_name)+" "+random.choice(l_name)
    return real_name
def load_money():
    element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'profile-card')))
    if(element):
        browser.find_element_by_xpath('/html/body/section/div/aside/div[6]/a/span').click()
        # time.sleep(5)
        browser.find_element_by_xpath('/html/body/section/div/aside/div[6]/div/a[2]').click()
        # time.sleep(5)
        browser.find_element_by_xpath('//*[@id="main"]/div/div[4]/div[25]/a/img').click()
        # time.sleep(5)
        
        amount = browser.find_element_by_xpath('//*[@id="amount"]')
        amount.send_keys(400)
        
        select = Select(browser.find_element_by_id('remarks'))
        select.select_by_value('1')
        
        browser.find_element_by_xpath('//*[@id="ConfirmButton"]').click()
        element2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section[2]/h1')))
        if(element2):
            bank_mobile = browser.find_element_by_xpath('/html/body/div/main/section[2]/form[1]/div[1]/input')
            bank_mobile.send_keys(bank_id)
            
            bank_password =  browser.find_element_by_xpath('/html/body/div/main/section[2]/form[1]/div[2]/input')
            bank_password.send_keys(bank_pw)
            
            browser.find_element_by_xpath('/html/body/div/main/section[2]/form[1]/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/div/main/section[2]/form[1]/div[2]/button').click()
            
            otp = int(input("Enter Otp: "))
            put_otp =  browser.find_element_by_xpath('//*[@id="first_otp"]')
            put_otp.send_keys(otp)
            browser.find_element_by_xpath('/html/body/div/main/section[2]/form[1]/div[3]/button').click()
            browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[6]/a/button').click()

def top_up():
    time.sleep(3)
    
    browser.find_element_by_xpath('//*[@id="main"]/div/div/ul/li[6]/a/div').click()  #ncell
    # browser.find_element_by_xpath('//*[@id="main"]/div/div/ul/li[1]/a/div').click() #ntc
    number = browser.find_element_by_xpath('//*[@id="MobileNo"]')
    number.send_keys(top_upno)

    amount = browser.find_element_by_xpath('//*[@id="Amount"]')
    amount.send_keys(amt)
    browser.find_element_by_xpath('//*[@id="yoBtn"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    time.sleep(2)

def refund():
    browser.find_element_by_xpath('/html/body/section/div/aside/div[2]/a/span').click()
    browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/a/p').click()

    number = browser.find_element_by_xpath('//*[@id="MobileNumber"]')
    number.send_keys(refund_id)

    amount = browser.find_element_by_xpath('//*[@id="Amount"]')
    amount.send_keys(refund_amt)

    select = Select(browser.find_element_by_id('Purpose'))
    select.select_by_value('1')

    remarks = browser.find_element_by_xpath('//*[@id="Remarks"]')
    remarks.send_keys("Thank you.")

    browser.find_element_by_xpath('//*[@id="sendForm"]/div[4]/button').click()


def logout():
    browser.find_element_by_xpath('//*[@id="profile-card"]').click()
    browser.find_element_by_xpath('//*[@id="profile-card-container"]/ul/li[5]/a').click()

def signup():
    global phone
    element = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.ID, "RememberMe")))
    if(element):
        browser.find_element_by_xpath('/html/body/section/div/div/div/div[2]/a').click()
        time.sleep(2)
        name = create_name()
        f_name = name.split(" ")[0]
        email = f_name+str(random.randint(0,50))+"@gmail.com"
        full_name = browser.find_element_by_xpath('//*[@id="FullName"]')
        full_name.send_keys(name)

        full_email = browser.find_element_by_xpath('//*[@id="EmailAddress"]')
        full_email.send_keys(email)

        phone = int(input("Please enter phone number"))
        full_phone = browser.find_element_by_xpath('//*[@id="MobileNo"]')
        full_phone.send_keys(phone)

    gender = browser.find_element_by_xpath('//*[@id="formGroupExampleInput2"]').click()
    submit = browser.find_element_by_xpath('//*[@id="signupForm"]/button').click()
    activation_key = int(input("activation code: "))
    enter_activation = browser.find_element_by_xpath('//*[@id="ActivationNumber"]')
    enter_activation.send_keys(activation_key)
    activate = browser.find_element_by_xpath('//*[@id="Submit-OTP"]').click()
    element5 = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="reg_btn"]')))
    if(element5):
        new_password = browser.find_element_by_xpath('//*[@id="Password"]')
        new_password.send_keys(new_pw)
        confirm_password = browser.find_element_by_xpath('//*[@id="ConfirmPassword"]')
        confirm_password.send_keys(new_pw)
        browser.find_element_by_xpath('//*[@id="reg_btn"]').click()
        browser.find_element_by_xpath('//*[@id="activate_btn"]').click()

def login():  
    element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "RememberMe")))
    if(element):
        id = browser.find_element_by_xpath('//*[@id="user_name"]')
        id.send_keys(phone)
        # time.sleep(2)
        pw =browser.find_element_by_xpath('//*[@id="Password"]')
        pw.send_keys(password)
        browser.find_element_by_xpath('//*[@id="loginform"]/button').click()
def check():
    element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "RememberMe"))
        )
    if(element):
        print("got it")
    else:
        print("no")
def main():
    print(os.getenv('USER_NAME'),"hi")
    choice = "y"
    while(choice == "y"):
            
            signup()
            login()
            load_money()
            top_up()
            refund()
            logout()
            choice = str(input("Do you want to register new client? y/n: "))
        # except:
        #     print("error")
       
        # finally:
        #     browser.quit()

        
main()


# In[ ]:




