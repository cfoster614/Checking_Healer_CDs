# Healer Assignment Checker

## Overview

This application was designed to help healing officers determine if their co-healers are using their cooldowns at the assigned times in World of Warcraft. This app will let you keep track of when you assigned cooldowns and the will pull up the encounter of your choice. You can quickly see when your healers *actually* used their cooldowns in warcraftlogs vs when they were assigned.  

## How to Use this App  

1. Select a boss that you want to check your assigned cooldowns on.
2. Insert the log that you want to check.  
3. On the new page, select which pull you want to use.  
4. Under **Add a Spell**, select which cooldowns you want to check, the player name, and the times you assigned the cooldown. *Make sure the player name is accurate to their in-game name.*
5. Click the **See Result** button to go to the final page. The **Your Assignments** section shows the cooldowns you wanted to check, and the times. The spell timeline after it shows when the players used their cooldowns for that pull.

## How to Install and Run this App

1. Create a virtual environment: `python3 -m venv venv`.  
2. Install the dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file in the root folder: `touch .env`.
4. Inside of the `.env` file, set a `SECRET_KEY` variable for the config. You need a secret key to use flask sessions.  

    Example: `SECRET_KEY = 'itsasecret'`
5. Inside the `.env` file, also include:  
    `DEBUG=True`  
    `FLASK_ENV=development `
6. In your terminal (make sure you're in your venv), type `flask run`.
7. You will need to get access to the warcraftlogs API. Head to the official documentation for the [warcraftlogs](https://www.warcraftlogs.com/api/docs) API and follow the instructions on getting a token.
8. Add the token to your `.env` file.
9. The `.env` file has things you don't want seen by others so make sure to add it to a `.gitignore` file.

## License  
[MIT](https://choosealicense.com/licenses/mit/)

