
 ASTEROID SHOOTING GAME

Asteroid Shooting Game is a small Python-based game developed using Python. The primary goal of this project is to reinforce Object-Oriented Programming (OOP) 
concepts while practicing the use of Pygame for game development.

 FEATURES

- Spaceship Control: Navigate the spaceship across the screen with smooth movements and shooting capabilities.

- Asteroid Field: Randomly spawning and moving asteroids that can split into smaller ones when hit

- Screen Wrapping: The spaceship wrap around the edges of the screen for continuous gameplay.

- Collision Mechanics: Bullets destroy asteroids, and the spaceship crashes when it collides with an asteroid.

- Extensible Design: Organized code with reusable classes for future game enhancements.

 GAMEPLAY

- Use W, A, S and D keys to move and rotate the spaceship.

- Press SPACE to fire bullets at asteroids.

- Avoid crashing into asteroids to keep the game running.

  INSTALLATION

 1. Clone the repository:
  
 Bash
 
 git clone https://github.com/m-peckus/game_project
 cd game_project

 2. Install dependencies:
 
 Bash 

 pip install pygame

 3. Run the game:

The main.py file contains the core game logic and mechanics. To run the game directly from the command line, ensure the following prerequisites are met:

Bash

chmod +x main.py

Execute the file using:

Bash

./main.py
 
Ensure you have Python3 installed and the required dependencies (pygame) set up before running the game.


  PROJECT STRUCTURE

-  main.py: Game loop and core mechanics.

-  player.py: Spaceship class with movement, shooting, and screen wrapping logic.

-  asteroid.py: Asteroid class with splitting and movement mechanics.
 
-  asteroidfield.py: Spawner and manager for asteroids.

-  shot.py: Bullet (shot) class for firing at asteroids.
 
-  constants.py: Game-wide constants for screen size, speeds, and settings


 LEARNING HIGHLIGHTS

 This project demonstrates:
 
-  Inheritance: The Asteroid class inherits from a base CircleShape class for reusability.

-  Encapsulation: Each game element (spaceship, asteroids, bullets) is encapsulated in its own class.

-  Polymorphism: Shared methods like update and draw behave differently for each class.

 Game Development Concepts:

 - Using sprite groups for efficient updates and rendering.

 - Handling real-time user input (keyboard).

 - Managing object interactions and collisions.


 CONTRIBUTING

 This is a learning-focused project, but suggestions are welcome!

 Feel free to fork the repository and create pull requests for improvements or additional features.


 FUTURE ENHANCEMENTS

 - Add sound effects for firing bullets and asteroid collisions.

 - Implement a scoring system for destroyed asteroids.

 - Adapt the game for mobile devices by:

  Introducing touch controls for movement and shooting.

  Adjusting the game resolution and UI to fit smaller screens.

  Packaging the game using tools like Kivy or Pygame Subset for Android (pgs4a).
   
 - Include power-ups and new asteroid types.

 LICENSE

 This project is licensed under the MIT License

 ACKNOWLEDGMENTS

 - Pygame Documentation for detailed guidance on the library

 - Various online tutorials on OOP and game development concepts
