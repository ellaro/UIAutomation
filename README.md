# UIAutomation
total-luck.com UI Automation

pip install -r requirements.txt

Total Luck Automation Test

A Python Selenium script designed to automatically test the Total Luck website, including loading the site, playing a promotional video, and registering a new user.

The code is modular and divided into functions to allow easy testing of specific flows such as login/registration and video playback.
Features

    Website Loading Test: Checks if the website loads successfully within a timeout.

    Logo Play Test: Clicks on the homepage banner and plays a video for 5 seconds.

    Registration Flow Test:

        Opens the registration form.

        Fills in a randomly generated email and a fixed password.

        Accepts the terms of service.

        Completes the registration process.

        Logs out after registration.

Each part of the site is tested separately via its own function.
Requirements

    Python 3.7+

    selenium package

    Google Chrome browser installed

    chromedriver.exe (placed in the project directory)

Installation

Install the required Python packages:

pip install selenium

Download the correct version of chromedriver.exe matching your Chrome version and place it in the same folder as your script.
How the Code Works

    check_site_loads(driver)
    Verifies that the main website (https://www.total-luck.com/) loads within 30 seconds.

    await_presence_click(driver, xpath, keys=None)
    Waits for an element to appear, clicks it, and optionally sends keyboard input (like filling text fields).

    await_find_click(driver, xpath, keys=None)
    Immediately finds an element, clicks it, and optionally sends keyboard input.

    check_logo_play(driver)

        Loads the homepage.

        Clicks the main logo/banner.

        Starts playing the promotional video.

        Waits 5 seconds to simulate video viewing.

    check_registration(driver)

        Loads the homepage.

        Opens the registration form.

        Fills in a random email and password.

        Accepts terms of service.

        Completes the registration.

        Logs out after the registration is successful.

    Main Execution
    The script creates a Chrome WebDriver session and calls the check_registration(driver) function.
    (Other tests like check_logo_play(driver) can easily be enabled by uncommenting them.)

How to Run

    Make sure you have chromedriver.exe placed in your project directory.

    Save the script (for example, total_luck_automation.py).

    Run the script:

python total_luck_automation.py

    Watch as the browser automatically opens, interacts with the site, and prints progress messages to the console.

Notes

    Random Email Generation:
    Each time the script runs, it generates a slightly different email to avoid duplication during registration.

    Delays:
    time.sleep() is used to simulate real user behavior and allow page elements to fully load.

    Error Handling:
    The script includes try-except blocks to catch and print errors if a step fails.

    Extendability:
    You can easily add more tests by following the function-based structure of the code.

Credits

    Website: Total Luck

    Automation: Selenium WebDriver
