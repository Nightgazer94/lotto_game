from flask import Flask, render_template, request, redirect, url_for
import random

# Create an instance of the Flask application
app = Flask(__name__)

# Generate and shuffle a list of numbers for lotto
random_numbers = [i for i in range(1, 50)]


def new_lotto_numbers():
    """
    Function to generate new lotto numbers.
    Shuffles the list of numbers and selects the first six numbers, which are then sorted.

    Returns:
        list: A list of six numbers to be used as lotto results.
    """
    random.shuffle(random_numbers)
    new_lotto_list = [random_numbers[0], random_numbers[1], random_numbers[2],
                      random_numbers[3], random_numbers[4], random_numbers[5]]
    new_lotto_list.sort()
    return new_lotto_list


# Initialize global variables
lotto_numbers = new_lotto_numbers()
nums_list = []  # List of user-selected numbers
rounds = 1  # Count of rounds the user has played
founded_equals = 0  # Count of matched numbers between lotto and user numbers
message = ""  # Result message to be displayed


@app.route('/', methods=['GET', 'POST'])
def nums_request():
    """
    Handles GET and POST requests on the main page.
    Allows the user to submit numbers and check if they match the lotto numbers.

    Returns:
        str: HTML template with the current round and list of user-submitted numbers.
    """
    global nums_list, rounds, founded_equals, message

    if request.method == 'POST':
        one_number_str = request.form['number']

        if one_number_str.isdigit():
            one_number = int(one_number_str)

            # Check if the number is within the allowed range and has not been submitted before
            if one_number not in nums_list and 1 <= one_number <= 49:
                if len(nums_list) < 6:
                    nums_list.append(one_number)
                    rounds += 1

            # Once six numbers are submitted, compare them with the lotto numbers
            if len(nums_list) >= 6:
                nums_list.sort()
                for i in range(len(lotto_numbers)):
                    if lotto_numbers[i] == nums_list[i]:
                        founded_equals += 1

                # Set the message based on the number of matches
                if founded_equals == 6:
                    message = "Congratulations! You won the grand prize of $100,000!"
                elif founded_equals == 5:
                    message = "Amazing! You won the second prize of $50,000!"
                elif founded_equals == 4:
                    message = "Great job! You won the third prize of $20,000!"
                elif founded_equals == 3:
                    message = "Well done! You won the fourth prize of $10,000!"
                elif founded_equals in [1, 2]:
                    message = "So close! Better luck next time!"
                else:
                    message = "No matches, better luck next time!"

                return redirect(url_for('result'))

    return render_template('get_user_numbers.html', round=rounds, nums_list=nums_list)


@app.route('/result')
def result():
    """
    Displays the result of the game, showing both the lotto numbers and the user's selected numbers.

    Returns:
        str: HTML template with the game results.
    """
    global nums_list, lotto_numbers, message

    return render_template(
        'result.html',
        lotto_number1=lotto_numbers[0],
        lotto_number2=lotto_numbers[1],
        lotto_number3=lotto_numbers[2],
        lotto_number4=lotto_numbers[3],
        lotto_number5=lotto_numbers[4],
        lotto_number6=lotto_numbers[5],
        user_number1=nums_list[0],
        user_number2=nums_list[1],
        user_number3=nums_list[2],
        user_number4=nums_list[3],
        user_number5=nums_list[4],
        user_number6=nums_list[5],
        founded_equals=message
    )


@app.route('/reset_game', methods=['GET'])
def reset_game():
    """
    Resets the game by clearing the list of user-submitted numbers, shuffling the lotto numbers,
    and resetting global variables.

    Returns:
        werkzeug.wrappers.Response: Redirect to the main game page.
    """
    global nums_list, rounds, founded_equals, message, lotto_numbers

    lotto_numbers = new_lotto_numbers()
    nums_list = []
    rounds = 1
    founded_equals = 0
    message = ""

    return redirect(url_for('nums_request'))


if __name__ == '__main__':
    app.run(debug=True)
