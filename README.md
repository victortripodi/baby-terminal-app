# Baby Terminal App

Referenced sources: [Python](https://docs.python.org/3/), [Testing](https://docs.pytest.org/en/7.1.x/contents.html)

Source control repository [Github](https://github.com/victortripodi/baby-terminal-app.git)

## Presentation
vimeo: (https://vimeo.com/849725013/f25b6b87ea?share=copy)

## Styling conventions

I adhered to the PEP 8 style guide for Python. PEP 8 is the official style guide for Python code and provides guidelines on how to format Python code to enhance readability and maintainability. Key conventions that I followed:
- Indentation: Four spaces are used for indentation in the code.
- Line Length: Lines are kept within the recommended maximum length of 79 characters to enhance readability.
- Naming Conventions: Descriptive names are used for variables and functions, following the lowercase with underscores style (snake_case) for variable and function names.
- Import Statements: Import statements are placed at the top of the file, and each import is on a separate line.
- Whitespace: Consistent use of whitespace around operators, after commas, and between functions and control structures.
- Function and Class Definitions: Functions and classes are separated by two blank lines to improve readability.
- Comments: Descriptive comments are included in the code to explain the purpose of functions and blocks of code.

## Features of the application

The terminal Baby Tracker application allows users to record various activities related to a baby, remove specific entries, and view weekly totals of nappies and bottles for each baby. The application provides a menu-based interface for interacting with these features.

1. Record Baby Activities:
This feature allows the user to record various activities related to a baby, such as the number of nappies changed, the number of 100ml bottles fed, the baby's weight, the baby's length, and the date of the activities. The user will be prompted to input the baby's name and the activity details, and the data will be saved for future reference.
2. View Total Activities per Week:
With this feature, the user can view the total number of nappies changed and the total number of 100ml bottles fed for a specific baby per week. The user will be prompted to enter the baby's name, and the application will calculate and display the total activities for each week based on the recorded data.
3. Remove Baby Entry:
This feature allows the user to remove specific baby activity entries from the recorded data. The user will be prompted to enter the baby's name, and the application will display all the recorded entries for that baby. The user can then select a specific entry to remove from the records.


## Implementation Plan

I used Trello to track the implementation plan. 

1. Record Baby Activities (Priority: High)

Duration: 1 day
Checklist:
 - Create the record_baby_activities() function.
 - Implement input validation for baby name, nappies, bottles, weight, length, and date.
 - Write data to the 'baby_data.txt' file in CSV format.
 - Add a success message after data recording.
 - Test the function with various inputs to ensure correctness.

2. Remove Entry (Priority: High)

Duration: 2 days
Checklist:
 - Create the remove_baby_entry() function.
 - Implement input for baby name and validate its existence in the data file.
 - Display entries for the specified baby and allow the user to select one for removal.
 - Remove the selected entry from the 'baby_data.txt' file.
 - Add a success message after entry removal.
 - Test the function with various inputs to ensure correctness.

3. Total Data per Week (Priority: High)

Duration: 2 days
Checklist:
 - Create the totalize_data_per_week() function.
 - Read data from the 'baby_data.txt' file.
 - Calculate weekly totals of nappies and bottles for each baby.
 - Display the results for each baby and each week.
 - Test the function with various data to ensure correctness.


## Baby Tracker Application - Help Documentation

1. Introduction
The Baby Tracker Application is a terminal-based tool designed to help parents to keep track of their baby's activities, such as diaper changes, bottle feedings, weight, and length measurements. This documentation provides instructions on how to install, run, and use the application effectively.
2. Installation
Follow these steps to install the Baby Tracker Application:
Step 1: Download the Baby Tracker Application files to your local machine. You can either clone the repository from GitHub or download the ZIP archive and extract it.
Step 2: Navigate to the application directory using the terminal.
Step 3: Run the app
- If you have Python installed, type the following comand in the terminal/command prompt
python baby_tracker.py
- If you have multiple versions of Python installed, you may need to use python3 instead of python, like this:
python3 baby_tracker.py
- If you don't have any Python version installed, don't worry, type the following comand
./script.sh
but first, you will to change the permission typing the following comand
chmod +x script.sh  


3. System/Hardware Requirements
The Baby Tracker Application is a lightweight terminal-based tool and should run without any specific hardware requirements. It is compatible with Windows, macOS, and Linux operating systems.
4. How to Use the Application
To run the Baby Tracker Application, follow these steps:
Step 1: Open a terminal or command prompt on your system.
Step 2: Navigate to the application directory.
Step 3: Launch the application by running the following command:
     ./script.sh
5. Using the Application
Upon launching the application, you will see a menu with different options. Follow the prompts and enter the required information to record baby activities (this function also allows users to quit entering baby activities at any stage during the data input process entering "q"), view total activities per week, or remove baby entries. The application will guide you through each step, and you can use the menu options to navigate between features.
6. Exiting the Application
To exit the Baby Tracker Application, select option 4 from the menu. The application will gracefully terminate, and you will return to the command prompt.

