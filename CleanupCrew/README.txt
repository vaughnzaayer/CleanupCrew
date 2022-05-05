Project 4 - Vaughn Zaayer

-- CLEANUP CREW --

In this 2d arcade game, you must explore an infested space station in order to
find three data drives, and return them to safety. You will need to face
challenging packs of enemies, equipped with a sidearm and your own two fists.

- HOW TO PLAY -

To launch the game, use the terminal to access the Cleanup Crew folder,
and launch to the main title using 'python3 main.py'.

There is a brief control layout in the "How to Play" section of the
main menu, but I will also give a brief description here:

- left and right arrow keys to move left and right, respectively
- up arrow key will control your jump, or will allow you to
climb ladders
- down arrow key allows you to climb down ladders
- Z key will allow you to interact with and enter doors
- X key will activate a melee attack, pushing back nearby enemies in front of
you
- C key will fire your sidearm in the direction you are facing -- you only have
10 shots, so make them count!
- ESC key will pause/resume the game


Your objective is to collect 3 data drives, found in the center of random rooms



- POINT BREAKDOWN -
(The entire game is made from my own code and pygame)

FROM THE MENU: (37pts)
- basic platform (12pts)
- game pause/resume (4pts)
- status (4pts) -> The player's health is displayed in the battery in the top
right of the screen, and the player's ammunition is displayed on the left
- win/lose (4pts)
- transporter (3pts) -> The player can enter doors, transporting them to another
room
- bigger world (4pts) -> The player can traverse different rooms in a space
station that is procedurally generated
- limited power (4pts) -> The player has a limited amount of ammunition,
forcing them to conserve ammo and take more risks
- breakout rules (6pts) -> The player can traverse different rooms, which are
organized by the game as "scenes"

MAKE YOUR OWN:
- procedural generation -> The space station will have a different layout each
time you play, with different locations for the data drives and enemies
- handmade animations -> The player and enemies have unique animations made
by yours truly! In order for the animations to take effect, I had to create
2 new classes: one to read spritesheets and their corresponding JSON files, as
well as an animation handler that controls what animations to play and when,
also making it easy to create new animations for any sprite on the fly
- mixed combat -> The easiest way to take out an enemy is to use the ranged
sidearm -- however, with limited ammunition, the player must also use their
melee attack to push back enemies, and to run away if outnumbered
- in-app new games -> You don't need to close the app when you win, lose, or exit
the game -- the main menu can launch a new map and game at any time!

- KNOWN ISSUES -

- When initializing a new game, the map generation may cause the game to crash
on rare occasions. To work around this, simply relaunch the app and reinitialize.

- Very rarely, the map will generate with very few rooms. You will need to reinitialize
the game in order to fix this. No need to restart the app itself, however.

- In extremely rare cases, entering a room with aliens will create a "blanket" of alien sprites.
 This bug is not game-breaking, and fixes itself in a few seconds. It is scary, though!


 Thank you for playing my game! I hope you have a wonderful holiday break! :)
