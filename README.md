# Total Luck UI Automation Test

A Python Selenium script for end-to-end automation testing of [Total Luck](https://www.total-luck.com/), including site load verification, video interaction, and user registration flow.

##How to Run

    1. Install the required libraries:
       ```bash
       pip install -r requirements.txt '''
    2. Make sure chromedriver.exe is placed in your project directory.
    3. Run the script:
         ```bash
        python main.py


  The browser will open automatically, perform the automation steps, and print progress messages to the console.


Total Luck Automation Test

A Python Selenium script designed to automatically test the Total Luck website, including loading the site, playing a promotional video, and registering a new user.

The code is modular and divided into functions to allow easy testing of specific flows such as login/registration and video playback.

#### ✨ Features
```markdown
## Features

✅ **Website Load Test** – Verifies that the site loads within 30 seconds.

✅ **Video Playback Test** – Clicks on the homepage banner and plays a promotional video.

✅ **Registration Flow Test** – Automates full user registration:
   - Opens the registration form
   - Enters a randomly generated email and password
   - Accepts Terms of Service
   - Completes registration
   - Logs out

## Code Structure

- `check_site_loads(driver)`: Verifies the website loads.
- `check_logo_play(driver)`: Tests clicking the logo and playing video.
- `check_registration(driver)`: Completes registration flow.
- Helper functions like `await_presence_click` and `await_find_click` abstract common actions.

## Requirements

- Python 3.7+
- Selenium
- Google Chrome
- Chromedriver (version must match Chrome browser)

## Notes

- Generates a **random email** each time to avoid duplication.
- Uses `time.sleep()` to simulate realistic user behavior.
- Errors are logged via try-except blocks.
- You can easily add more tests using the modular function structure.


## Credits

    Website: Total Luck

    Automation: Selenium WebDriver

##Tags

#selenium #automation #python #testing #qa #e2e-testing
