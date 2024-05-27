# Selenium UI & API Tests with Robot Framework

This repository contains practice projects I've completed as part of my studies.

## Instructor
- [Rahul Shetty](https://www.udemy.com/user/rahul445/)
- [Jose Portilla](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/?couponCode=ST12MT030524#instructor-1)

## Course Links
- [Udemy: Robot Framework with Python Selenium](https://www.udemy.com/course/robot-framework-with-python-selenium/?couponCode=ST15MT31224)
- [Udemy: Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/?couponCode=ST12MT030524#instructor-1)

## Credits

I would like to extend my gratitude to both Rahul Shetty and Jose Portilla, as well as Udemy, for their excellent teaching and guidance. The ongoing practice projects included in this repository are based on lessons and instructions from their courses.

## Contributors
- [Girish Devappa](https://www.linkedin.com/in/girish-devappa-5539b4190/) (Student Contributor)
- [The Internet Heroku App](https://the-internet.herokuapp.com/) (System Under Test)
- [YouTube Tutorial: How to handle Checkbox in Selenium | Selenium Webdriver with Java tutorials](https://youtu.be/7BtHDhaN65o?si=HxI3ChnrJBNnXc1X) (Knowledge Reference)

I am pushing into GitHub in gradual progression of practice projects as part of my ongoing learning journey on Udemy.

### API Testing
- [The GitHub API](https://docs.github.com/en/rest?apiVersion=2022-11-28) (offers a wide range of endpoints)

**Install Dependencies**
https://github.com/giri81/Udemy-Selenium-UI-API-Tests-Robot-Framework/blob/main/requirements.txt

## Usage Information for Web_UI in Windows Environment 
To run the tests in a Windows environment, follow these steps:
1. Navigate to the repository directory: Open a command prompt, navigate to the directory where you cloned the repository.
2. Run the Robot Framework tests by executing the following command: `robot --variable BROWSER:chrome your_test_file.robot`. This command will run the tests using Chrome as the browser.

## Usage Information for Local REST EndPoint Testing
1. Run the API test script `test_api.py`. The HTTP server will automatically start before running the tests and stop after they have completed, ensuring that the tests can be executed against a running server.
2. The script will then test the local API endpoint and log the results to a new log file in the `logs` directory.
