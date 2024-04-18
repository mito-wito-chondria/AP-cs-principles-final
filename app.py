import random
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "rock paper scissors!"

@app.route('/rps', methods = ['GET', 'POST'])
def rps():
    choices = ['rock', 'paper', 'scissors']

    if request.method == 'GET':
        return render_template('rps.html', choices = choices)

    if request.method == 'POST':
        # human selection
        human = request.form['selected']
        return rock_paper_scissors(human)
    
@app.route('/simulation', methods = ['GET', 'POST'])
def simulation():
    choices = ['rock', 'paper', 'scissors']

    if request.method == 'GET':
        return render_template('simulation.html', choices = choices)

    if request.method == 'POST':
        human = request.form['selected']
        return rps_simulation(human)

def rock_paper_scissors(human: str) -> str:
    choices = ['rock', 'paper', 'scissors']
    i = random.randint(0, len(choices) - 1)
    computer = choices[i]
    
    if computer == human:
        return 'tie! human: ' + human + ' computer: ' + computer
    if computer == 'rock' and human == 'scissors':
        return 'computer selected: ' + computer + ', human selected: ' + human + ', computer wins!'
    if computer == 'rock' and human == 'paper':
        return 'computer selected: ' + computer + ', human selected: ' + human + ', you win!'
    if computer == 'paper' and human == 'rock':
        return 'computer selected: ' + computer + ', human selected: ' + human + ', computer wins!'
    if computer == 'paper' and human == 'scissors':
        return 'computer selected: ' + computer + ', human selected: ' + human + ', you win!'
    if computer == 'scissors' and human == 'paper':
        return 'computer selected: ' + computer + ', human selected: ' + human + ', computer wins!'
    if computer == 'scissors' and human == 'rock':
        return 'computer selected: ' + computer + ', human selected: ' + human + ', you win!'

def rps_simulation(human: str) -> str:
    choices = ['rock', 'paper', 'scissors']
    computers = []

    wins = 0
    losses = 0
    ties = 0

    for x in range(10):
        i = random.randint(0, len(choices) - 1)
        computers.append(choices[i])

    for y in range(10):
        if computers[y] == human:
            ties += 1
        if computers[y] == 'rock' and human == 'scissors':
            losses += 1
        if computers[y] == 'rock' and human == 'paper':
            wins += 1
        if computers[y] == 'paper' and human == 'rock':
            losses += 1
        if computers[y] == 'paper' and human == 'scissors':
            wins += 1
        if computers[y] == 'scissors' and human == 'paper':
            losses += 1
        if computers[y] == 'scissors' and human == 'rock':
            wins += 1

    return 'you selected ' + human + ' and won ' + str(wins) + ' times, lost ' + str(losses) + ' times and tied ' + str(ties) + ' times! computer choices: ' + str(computers)


if __name__ == "__main__":
    app.run(debug=True)