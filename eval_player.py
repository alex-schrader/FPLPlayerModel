import make_model
import numpy as np

def main():
    print("Welcome to transfer picker!")
    id = input("Player ID: ")
    print("making model...")
    model, form_vals, name = make_model.make_model(id)

    form = 0
    for match in form_vals:
        form += float(match['xG']) * 5 / 4 + float(match['xA']) * 3 / 4
    txt = "Please enter {player}'s opponent's table position for the upcoming 4 matches"

    #txt = "For only {price:.2f} dollars!"
    print(txt.format(player=name))
    diffi = [0,0,0,0]
    diffi[0] = int(input("Game 1: "))
    diffi[1] = int(input("Game 2: "))
    diffi[2] = int(input("Game 3: "))
    diffi[3] = int(input("Game 4: "))

    avg = sum(diffi) / 4
    test_data = np.array([[diffi[0], form]])
    top_pred = model.predict(test_data)
    print("Fixture 1 Expected Points: %.2f" % top_pred[0])
    test_data = np.array([[diffi[1], form]])
    top_pred = model.predict(test_data)
    print("Fixture 2 Expected Points: %.2f" % top_pred[0])
    test_data = np.array([[diffi[2], form]])
    top_pred = model.predict(test_data)
    print("Fixture 3 Expected Points: %.2f" % top_pred[0])
    test_data = np.array([[diffi[3], form]])
    top_pred = model.predict(test_data)
    print("Fixture 4 Expected Points: %.2f" % top_pred[0])
    test_data = np.array([[avg, form]])
    top_pred = model.predict(test_data)
    print("Average Expected Points: %.2f" % top_pred[0])




main()