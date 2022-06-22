import make_model
import numpy as np

def main():
    id = input("what player id? ")
    model, form_vals, name = make_model.make_model(id)

    form = 0
    for match in form_vals:
        form += float(match['xG']) * 5 / 4 + float(match['xA']) * 3 / 4
    txt = "Please enter {player}'s opponent's position for the upcoming 4 matches"

    #txt = "For only {price:.2f} dollars!"
    print(txt.format(player=name))
    diffi = [0,0,0,0]
    diffi[0] = int(input("game 1: "))
    diffi[1] = int(input("game 2: "))
    diffi[2] = int(input("game 3: "))
    diffi[3] = int(input("game 4: "))

    avg = sum(diffi) / 4



    test_data = np.array([[avg, form]])
    top_pred = model.predict(test_data)
    print("Expected Points:", top_pred)




main()