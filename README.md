#  Catcher Game

A fun and simple **Python Arcade** game created as a class project.  
The goal is to move your basket to catch falling gems while avoiding misses.  
As you score more points, the game levels up and becomes faster and more challenging!

[Software Demo Video]

# Development Environment

This project was developed using **Visual Studio Code** as the main code editor and **GitHub** for version control and repository hosting.

The programming language used is **Python**, which provides a clear and structured way to demonstrate basic syntax, output, and project setup.

# Useful Websites
1. https://github.com/pythonarcade/arcade
2. https://learn.arcade.academy/en/latest/examples/index.html
 
---

##  Game Overview

**Title:** Catcher  
**Genre:** Arcade / Skill Game  
**Framework:** [Python Arcade](https://api.arcade.academy/)  
**Language:** Python 3  

The player controls a basket at the bottom of the screen and catches gems that fall from the top.  
Each caught gem adds to the score, while missed gems reduce your lives.  
Once all lives are lost, the game ends

---


### **Basic Requirements**
-  **Graphics:** Uses Arcade’s rendering and sprite system  
-  **User Input:** Keyboard controls for movement, pause, and save/load  
-  **Moveable Objects:** Player basket and falling gems  

### **Additional Requirement**
-  **Levels:** The game includes difficulty that automatically increase speed of falling objects as time goes on  
  

---

##  Controls

| Key | Action |
|-----|---------|
| ← / A | Move Left |
| → / D | Move Right |

---

##  How to Play

1. Run the game (see setup instructions below).  
2. Use the arrow keys to move the basket left and right.  
3. Catch as many falling gems as you can!  
4. Every 15 seconds increases the **speed** of falling objects, making gems fall faster.  
5. When you run out of lives, The game ends

---

##  How to Run

1. Install Python 3.8 or later  
2. Install the Arcade library:
   ```bash
   pip install arcade


## More to Add
1. Pause system
2. Leaderboard to see how you progressively do
3. Bonus falling objects/shapes?
4. Power ups?