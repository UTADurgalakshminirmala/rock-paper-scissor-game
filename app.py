from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    result = None
    computer_choice_name = None
    if request.method == "POST":
        num = int(request.form["choice"])
        choices = ["rock", "paper", "scissors"]
        user_choice = choices[num]

        random_choice = random.randint(0, 2)
        computer_choice = choices[random_choice]
        computer_choice_name = computer_choice

        if num == random_choice:
            result = f"Both chose {user_choice}. It's a tie!"
        elif (num == 0 and random_choice == 1) or (num == 1 and random_choice == 2) or (num == 2 and random_choice == 0):
            result = f"You chose {user_choice}, computer chose {computer_choice}. Computer wins!"
        else:
            result = f"You chose {user_choice}, computer chose {computer_choice}. You win!"

    return render_template("index.html", result=result, computer_choice=computer_choice_name)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
