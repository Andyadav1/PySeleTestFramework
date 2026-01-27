Web Automation QA Assignment
🎯 Objective
Automate two real-world scenarios on a live e-commerce site to assess:

UI interaction skills


Dynamic filtering


Cart validation


Conditional screenshot capture


🔗 Test Website
🌐 https://www.saucedemo.com/

Credentials to use:

Username: standard_user


Password: secret_sauce


🧪 Test Case 1: Successful Purchase Flow
✅ Automate and validate a complete login and purchase flow with cart price validation.

Steps:
Navigate to https://www.saucedemo.com/


Log in using the credentials provided above.


From the product list:


Apply the “Price (low to high)” filter


Programmatically identify the 2 most expensive items (i.e., reverse the sorted list)


Add these 2 products to the cart


Go to the Cart page


Validate that exactly 2 items are added


Calculate and verify that the total sum of the individual item prices equals the expected total


Proceed to Checkout


Enter:


First Name: John


Last Name: Doe


Postal Code: 226001


Continue through to the final confirmation page.


Assert that the final page contains the message: "THANK YOU FOR YOUR ORDER"


If this message is present, take a screenshot and save it as: purchase_success.png


🧪 Test Case 2: Login Failure
❌ Test behavior on invalid login and capture appropriate output

Steps:
Open https://www.saucedemo.com/


Enter incorrect credentials:


Username: invalid_user


Password: wrong_pass


Click the Login button


Verify:


An error message appears (e.g., “Epic sadface: Username and password do not match…”)


Log "Login failed as expected with invalid credentials" to console


Take a screenshot named: login_failed.png


📤 What to Submit
✅ Selenium test script (.py, .java, or .js)


✅ Screenshot purchase_success.png


✅ Screenshot login_failed.png


✅ A README.txt with:


Language used


Selenium version


Steps to run your script
Swag Labs
Sauce Labs Swag Labs app