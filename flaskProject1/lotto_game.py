from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Function to generate new lottery numbers
def new_lotto_numbers():
    return sorted(random.sample(range(1, 50), 6))

# Global variables
lotto_numbers = new_lotto_numbers()
nums_list, rounds, message = [], 1, ""

@app.route('/', methods=['GET', 'POST'])
def nums_request():
    global nums_list, rounds, message

    if request.method == 'POST':
        one_number_str = request.form['number']

        if one_number_str.isdigit():
            one_number = int(one_number_str)
            if one_number not in nums_list and 1 <= one_number <= 49:
                nums_list.append(one_number)
                rounds += 1

            if len(nums_list) == 6:
                matches = len(set(lotto_numbers) & set(nums_list))
                message = {
                    6: "Congratulations! You won the grand prize of $100,000!",
                    5: "Amazing! You won the second prize of $50,000!",
                    4: "Great job! You won the third prize of $20,000!",
                    3: "Well done! You won the fourth prize of $10,000!"
                }.get(matches, "No matches, better luck next time!")
                return redirect(url_for('result'))

    return render_template('get_user_numbers.html', round=rounds, nums_list=nums_list)

@app.route('/result')
def result():
    return render_template(
        'result.html',
        lotto_number1=lotto_numbers[0],
        lotto_number2=lotto_numbers[1],
        lotto_number3=lotto_numbers[2],
        lotto_number4=lotto_numbers[3],
        lotto_number5=lotto_numbers[4],
        lotto_number6=lotto_numbers[5],
        user_number1=nums_list[0] if len(nums_list) > 0 else None,
        user_number2=nums_list[1] if len(nums_list) > 1 else None,
        user_number3=nums_list[2] if len(nums_list) > 2 else None,
        user_number4=nums_list[3] if len(nums_list) > 3 else None,
        user_number5=nums_list[4] if len(nums_list) > 4 else None,
        user_number6=nums_list[5] if len(nums_list) > 5 else None,
        message=message
    )

@app.route('/reset_game', methods=['GET'])
def reset_game():
    global nums_list, rounds, message, lotto_numbers
    lotto_numbers, nums_list, rounds, message = new_lotto_numbers(), [], 1, ""
    return redirect(url_for('nums_request'))

if __name__ == '__main__':
    app.run(debug=True)
