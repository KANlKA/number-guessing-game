from flask import Flask, render_template, request
import random
num = random.randint(2, 100)
print(num)
results = []
app = Flask(__name__, template_folder='static')
def check_number_show_message(guessed_number, computer_number):
  if guessed_number < computer_number:
    return f'{guessed_number} is too low'
  elif guessed_number > computer_number:
    return f'{guessed_number} is too high'
  else:
    return f'{guessed_number} is correct'
@app.route('/',methods=['GET', 'POST']) 
def main():
#route handler get is retreiving data and post is submitting data and form is doing that
    if request.method == 'POST':
        guess = request.form['number_guess']
        guessed_number = int(guess)
    try:
        results.append(check_number_show_message(guessed_number,num))
    except:
      pass
    return render_template("home.html", results_get = reversed(results))
@app.route('/reset',methods=['GET'])
#This line defines a route for the "/reset" URL that responds to GET requests.
def reset():
    global num
    global results
    num = random.randint(2, 100)
    results = []
    return render_template("home.html", results = results)
app.run("0.0.0.0")
#This line starts the Flask application, making it listen for incoming requests.