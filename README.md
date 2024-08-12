# BMC Ticketing Software Automation

This project automates the process of handling tickets within the BMC Remedy platform. The automation script performs tasks from logging in, answering security questions, navigating through the incident management console, assigning tickets, changing ticket statuses, and closing tickets. The script is built using Python with the Selenium WebDriver for browser automation.

# Features
Automated Login: The script handles the login process, including answering security questions based on pre-defined answers.
Incident Management: Automates the navigation to the Incident Management Console, where it identifies unassigned tickets and assigns them to the specified engineer.
Ticket Assignment: Automatically assigns tickets to the specified user or group.
Status Update: Changes the status of tickets to "In Progress" and ensures that tickets are properly updated in the system.
Session Management: Handles alerts and pop-ups to ensure smooth navigation and execution within the BMC Remedy platform.
Logout and Cleanup: The script gracefully logs out and closes the browser session once the tasks are completed.

# Requirements
Python 3.x
Selenium WebDriver
Firefox WebDriver (GeckoDriver) or ChromeDriver, depending on the browser you wish to use.
