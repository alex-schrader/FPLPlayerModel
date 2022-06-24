# FPL Player Model

Fantasy Premier League is a game played by ~10 million players where you select players who you anticipate will score the most goals and assists before a gameweek. When selecting a player, 3 variables are generally considered:
 - Player Form
 - Player Quality
 - Upcoming Fixture Difficulty

There are many well made models predicting a players production and the impact of these stats. However, none of these publically available algoritms take into account an individual players proclivity to produce more when they play against worse clubs, and an individual players proclivity to produce more when they are in form. Some players perform much better against worse sides, some perform much better when on a run of form. This should be highlighted to managers. Thus, I decided to make an algorithm to calculate that

### Demo
![flixSchradersuper3](https://user-images.githubusercontent.com/85814674/175180886-b21692b4-d0c9-4969-a678-c5bf60786a0c.gif)


## How to Use
1. Find your prospective player ID number on understat.com
2. Enter in the difficulty for the players upcoming 4 games(1 is hardest, 20 is easiest)
3. Compare expected points with other players you enter

## Model Details
Data used: all data was pulled from understat.com, where player xG(expected goals) and xA(expected assists) are provided for each match. These values were converted to expected points using the official FPL scoring system. Fixture difficulty was ranked based on their current standing in the premier league. Additionally, each match was also given data on the player's most recent 4 fixtures, to indicate the current form of the player. From this, the model was trained using a linear regression model from sklearn.linear_model. 

## Results
The results indicate that certain players are much more susceptive to good form and good fixtures then others. For example, we can calculate the difference in points when a player is in top form versus in poor form(delta_form), and when a player is in good fixtures versus and bad fixtures(delta_fixtures). Here are a few players delta values:

| Name     | delta_form         | delta_fixture  | Accuracy(r^2)  |
| ------------- |:-------------:| -----:| ------:|
| Harry Kane   | 6.32 | 1.30 | 0.31 |
| Mo Salah      | 6.14     |   0.71 | 0.26 |
| Cristiano Ronaldo | 5.05      |    2.83 | 0.34 |
| Son Heung Min   | 7.20 | 0.32 | 0.31 |
| Jamie Vardy    | 6.06    |   0.91 | 0.34 |
| Kevin De Bruyne | 6.00      |    -0.40 | 0.26 |
| Immanuel Dennis   | 4.98 | 0.49 | 0.26


Certain players are very sensitive to fixture quality such as Ronaldo, who performs significantly better against worse clubs. However some are less sensitive to this, with Kevin De Bruyne even performing better against better clubs. Similarly, a player like Son Heung Min performs better when in good form, whereas a player like Immanuel Dennis is much less effected. 

The r^2 value for all players is relatively low, ~0.3 for most. This shows that ultimately, the model isn't perfect at predicting as soccer is so unpredictable, but the data can still be used when trying to maximize oppurtunity. 

Of the top 100 players in xG last season: <br />
Top 5 Players against strong teams: <br />Ilkay Gündogan, Conor Gallagher, Gabriel Martinelli, Wout Weghorst, Alexandre Lacazette <br /><br />
Top 5 Players against weak teams: <br />Timo Werner, Ivan Toney, Patson Daka, Pierre-Emerick Aubameyang, Callum Wilson <br /><br />
Top 5 Players when in form: Gabriel Martinelli, João Pedro, Timo Werner, Ademola Lookman, Mohamed Elyounoussi <br /><br />
Top 5 Players when not in form: <br />Christian Nørgaard, Wout Weghorst, Tomas Soucek, Daniel James, Emmanuel Dennis <br /><br />

Data for all 100 players is in results.txt

