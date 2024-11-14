Lotto Game Web Application

This is a simple web-based Lotto game built using Flask. Users can select numbers and check if they match randomly generated Lotto numbers to win various prizes.

Features

Users can select 6 numbers between 1 and 49.

The application generates random Lotto numbers and checks how many user-selected numbers match the Lotto numbers.

Prize levels based on the number of matches.

Users can reset the game and play multiple times.

How to Run

Install Dependencies: Make sure you have Python installed. Install Flask using pip:

pip install Flask

Run the Application:

python app.py

The application will run on http://127.0.0.1:5000/ by default.

Access the Game: Open a web browser and navigate to http://127.0.0.1:5000/ to start playing.

Game Flow

Number Selection: On the main page, the user can input a number between 1 and 49. The user needs to select a total of 6 numbers.

Results Display: After selecting 6 numbers, the game will compare the user's numbers with randomly generated Lotto numbers. The result page will display both sets of numbers and indicate the prize, if any.

Reset Game: The user can reset the game at any time to start over.

Prizes

6 Matches: Grand prize of $100,000

5 Matches: Second prize of $50,000

4 Matches: Third prize of $20,000

3 Matches: Fourth prize of $10,000

1 or 2 Matches: "Better luck next time!"

No Matches: "No matches, better luck next time!"

Code Overview

app.py: Main application file containing all logic for the game.

Global Variables:

lotto_numbers: Holds the randomly generated Lotto numbers.

nums_list: Holds the numbers selected by the user.

rounds: Tracks the number of rounds played.

founded_equals: Tracks the number of matches between the user's numbers and Lotto numbers.

message: Stores the result message.

Routes:

/: Main page where users can select numbers.

/result: Displays the result of the game.

/reset_game: Resets the game to start over.

Templates

get_user_numbers.html: Template for the main page where users can input their numbers.

result.html: Template for displaying the result after the user has selected all six numbers.

Dependencies

Flask: A lightweight WSGI web application framework for Python.

random: Used to shuffle and generate random Lotto numbers.

Notes

Make sure to keep the Flask server running while interacting with the web application.

The game is purely for entertainment purposes and does not involve real money.

License

This project is licensed under the MIT License.