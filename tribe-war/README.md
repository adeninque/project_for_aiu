# DISCRIPRION FOR TRIBE WAR

This game is based on Conway's game "Game of life".

To create this game I made class Cell. And this class has 'color' and 'tribe' arguments to identify cell 
![CELL_CLASS](screenshots/class_Cell.png)

So after preperation I started writing Game
![GAME_CLASS](/screenshots/game_Class.png)
Game class takes three arguments 'n' - rows, 'm' - columns and '*tribes' - all tribe.

Game class has private method '__generate_field'. It generates 'n by m' game_field and fills it randomly for each tribes
![GENARATING](/screenshots/generating_fiction.png)

The next thing that i want to show is 'step' function. It is one of the main function. All game logic is written here. This function checks every cell for conditions, remembers changes and executes them after checking.
![STEP_METHOD](/screenshots/main__fuction.png)

Second main function is 'start'. This method responsible for imaging all steps. 
![START_METHOD](/screenshots/starting%20function.png)

Rules:
- Cell dies if there more than 3 allies or if enemies > allies. In case if there count of enemies and allies are equal, then it will choose randomly between 'death' and 'live'
- if the cell is empty, it will come to life by taking the side of the tribe with the largest number of living cells in the range [2:3] in its field of view