from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Generate and shuffle a list of numbers for lotto
random_numbers = [i for i in range(1, 50)]
random.shuffle(random_numbers)

# Select the first 6 numbers as the lotto numbers
lotto_numbers = [random_numbers[0], random_numbers[1], random_numbers[2],
                 random_numbers[3], random_numbers[4], random_numbers[5]]
lotto_numbers.sort()

# Initialize global variables
nums_list = []  # List of user-selected numbers
rounds = 1      # Count of rounds the user has played
founded_equals = 0  # Count of matched numbers between user and lotto numbers
message = ""    # Result message to be displayed


@app.route('/', methods=['GET', 'POST'])
def nums_request():
    """
    Handles GET and POST requests for the main page.
    Allows the user to submit numbers and check if they match the lotto numbers.
    """
    global nums_list, rounds, founded_equals, message

    if request.method == 'POST':
        one_number_str = request.form['number']

        if one_number_str.isdigit():
            one_number = int(one_number_str)

            if one_number not in nums_list and 1 <= one_number <= 49:
                if len(nums_list) < 6:
                    nums_list.append(one_number)
                    rounds += 1

            if len(nums_list) >= 6:
                nums_list.sort()
                for i in range(len(lotto_numbers)):
                    if lotto_numbers[i] == nums_list[i]:
                        founded_equals += 1

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
    Resets the game by clearing user-selected numbers, shuffling lotto numbers,
    and resetting global variables.
    """
    global nums_list, rounds, founded_equals, message, lotto_numbers

    random.shuffle(random_numbers)
    lotto_numbers = [random_numbers[0], random_numbers[1], random_numbers[2],
                     random_numbers[3], random_numbers[4], random_numbers[5]]
    lotto_numbers.sort()

    nums_list = []
    rounds = 1
    founded_equals = 0
    message = ""

    return redirect(url_for('nums_request'))


if __name__ == '__main__':
    app.run(debug=True)

