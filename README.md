# FanCode API Automation Assignment Project - Pundalik Mhamal
## Project Overview

This project is designed to automate the verification that all users from the city `FanCode` have more than half of their todo tasks completed. The city `FanCode` can be identified by latitudes between -40 and 5, and longitudes between 5 and 100, based on user data from the provided APIs.

## Project Structure

api_automation/
│
├── features/
│ ├── steps/
│ │ ├── init.py
│ │ ├── user_steps.py
│ ├── init.py
│ ├── fancode_users.feature
│
├── src/
│ ├── init.py
│ ├── api_client.py
│ ├── user_service.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── behave.ini

## Setup

1. Clone the repository:
    ```
    git clone <repository_url>
    cd api_automation
    ```

2. Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Running the Tests

**Run the Tests using Behave**:
    ```
    behave
    ```

## Explanation of Steps

- **Given the list of users and their todos**:
    - Fetches the list of users and their todo tasks from the API.

- **When filtering users from the city "FanCode"**:
    - Filters the users based on the specified latitude and longitude ranges.

- **Then each FanCode user should have more than 50% of their todos completed**:
    - Verifies that each user from the city `FanCode` has completed more than 50% of their todo tasks.
