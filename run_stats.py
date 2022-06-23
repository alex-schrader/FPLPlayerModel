
import make_model
import numpy as np

def main():
    playerIDs = [3585,
 647,
 4105,
 522,
 6026,
 7052,
 9738,
 1801,
 7696,
 8720,
 7698,
 531,
 7700,
 844,
 6552,
 6681,
 7322,
 2335,
 672,
 8865,
 6818,
 675,
 3621,
 5543,
 6055,
 7083,
 3635,
 5555,
 5556,
 314,
 8379,
 318,
 447,
 8384,
 65,
 7230,
 2371,
 2379,
 453,
 838,
 6854,
 7752,
 7490,
 2498,
 843,
 1228,
 3277,
 3278,
 2381,
 9040,
 465,
 594,
 6482,
 468,
 9301,
 8272,
 7768,
 8026,
 5595,
 986,
 3420,
 606,
 8288,
 1250,
 482,
 5220,
 101,
 998,
 2662,
 4456,
 5735,
 618,
 1389,
 750,
 6894,
 1776,
 3697,
 755,
 501,
 762]
    deltas = []
    for player in playerIDs:
        temp = get_deltas(player)
        deltas.append(temp)
    print(deltas)

    fixtures = sorted(deltas, key=lambda x: x[1], reverse=True)
    form = sorted(deltas, key=lambda x: x[2], reverse=True)
    print('Best against bad teams')
    for i in range(5):
        print(i+1, fixtures[i][0])
    print('Best against good teams')
    for i in range(5):
        print(i+1, fixtures[-i-1][0])
    print("Best in good form")
    for i in range(5):
        print(i+1, form[i][0])
    print("Best in bad form")
    for i in range(5):
        print(i+1, form[-i-1][0])

def get_deltas(id):
    model, form_vals, name = make_model.make_model(id)
    peak_form = np.array([[10, 8]])
    peak_pred = model.predict(peak_form)
    bot_form = np.array([[10, 2]])
    bot_pred = model.predict(bot_form)
    delta_form = peak_pred - bot_pred
    peak_fix = np.array([[20, 4]])
    peak_pred = model.predict(peak_fix)
    bot_fix = np.array([[1, 4]])
    bot_pred = model.predict(bot_fix)
    delta_fix = peak_pred - bot_pred
    player = [name, round(delta_fix[0], 2), round(delta_form[0], 2)]
    print(name)
    return player

main()