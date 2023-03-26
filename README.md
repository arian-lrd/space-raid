# Alien Invasion
This repository will contain the code I wrote for my simple python game which I like to call "Space Raid". <br />
A game inspired by "River Raid & "Space Raid" from "Atari 2600" which I used to play as a kid. <br />
Since I used to play this game as a kid. So I was very interested in making a similar game using my programming knowledge. <br />
Youtube link to the demo: https://youtu.be/vjRvryA7hCU

##Important
To run the game on your system on lines 427 and 434 of ~game_functions.py~ file change the path to the path on your own sytem.

## Background & Notes
space_raid was my first proper programing project, with Python, the first programming language I started experimenting with. <br />

After 1 month of consuming pyhton knwoledge I decided to do something more ambitiouss than some easy practices. <br />
So I took one of the practices that interested me the most, "alien-invasion" skeleton practice from the "Python crash course" book, worked on it for 100 hours and turned it into the final version that I'm posting here. <br />


In the duration of coding this project I spent many hours reading documentations, asking questions online namely on Stack Overflow, re-reading
what I had learnt earlier, and trying to fix the problems that arose after each modification to the game. <br />
This was the most valuable aspect of the project, as it taught me how to find my answers when I'm creating something from scratch and out of the academic setting where there's a guide for every step of the projects.


***Final remarks:***
Towards the end of making this game I realized that every time I'd come close to finishing up, a new idea would pop up in my head which took a few hours to fully implement into the game. Thus after a while I decided not to follow up on my ideas anymore because it might've forced me to spend a hundred hours more on the project. <br />
*Yet I'm quite happy with the end result.*



## Intro
This game is inspired by "River Raid" which I used to play as a kid with an old "Atari 2600". <br />
The player has should try to eliminate as many enemy ship fleets as possible. <br />
As the player proceeds through the levels the game will speed up and give more points per kill. The player's ship, as well as enemy fleet and their bullets will all speed up by a factor of "1.5" after each wave. <br />
Player has 3 lives to clear as many enemy waves as possible, and at the end their score will be comppared to the highest score, replacing it if the player has scored more points. <br />

## Structure
The skeleton code for the game is based on one of practices in the book *"python crash course: a hands-on, project-based introduction to programming"*.
But the practice was very simple and lacked all of the functionalities that make the game interesting. <br />
A quarteer of my time was spent on refining the games's existing functionalities. The rest of it was spent on adding features and debugging. 


I added all of the following features to the game:
1. Main menu - A dedicated screen for the main menu with instructions and a background theme song 
2. Theme song - A unique theme song for the game's menu
3. Background music - A playlist of 5 songs randomly playing in the duration of the game.
4. Space background - A background of space and stars to give the game a more immersive feel
5. Enemies shooting back - With this add-on the enemy ships shoot back at the player when the player shoots at them which increases the challenge.
6. Explosion sounds - Explosion sounds that play when an enemy ship or the player's ship is destroyed
7. Game Over sound - A sound that plays when the player is out of lives.
8. New ship designs - I replaced the player's ship and uniquely redesigned enemy ships to look  more *"cool"*
9. If player makes contact with aliens or they reach the bottom of the screen player loses a life.


## Files
```alien_invasion.py``` - *Contains the game's main function & loop.* <br />
```alien_bullet.py``` - *Manages bullets fired from aliens.* <br />
```all_time_high.json``` - *Stores highest recorded score.* <br />
```button.py``` - *Displays play button on the game's main screen.* <br />
```explosion.py``` - *Display ship explosion images to the screen.* <br />
```game_functions.py``` - *Contains the bulk of the code which are the games's functions.* <br />
```game_stats.py``` - *Initialize & track game's statics (e.g., level, score, ships left).* <br />
"Music" - *Has to be deleted*  <br /> 
```scoreboard.py``` - *Keep track of & display score statics (e.g., score, high score, level, player's remaininng ships).* <br /> 
```settings.py``` - *Store the game's settings. Initialize at the beginning & make changes during the game.* <br /> 
```ship``` - *Store and visualize the ship.* <br />
```sound_and_music.py``` - *Play the game's sounds and music.* <br />



***In making this game I also used the ```"Pygame"``` library.*** <br />
***I havn't added the music, font, and image files to this repository.*** <br />



