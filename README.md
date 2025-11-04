#  Catcher Game

A fun and simple **Python Arcade** game created as a class project.  
The goal is to move your basket to catch falling gems while avoiding misses.  
As you score more points, the game levels up and becomes faster and more challenging!

---

##  Game Overview

**Title:** Catcher  
**Genre:** Arcade / Skill Game  
**Framework:** [Python Arcade](https://api.arcade.academy/)  
**Language:** Python 3  

The player controls a basket at the bottom of the screen and catches gems that fall from the top.  
Each caught gem adds to the score, while missed gems reduce your lives.  
Once all lives are lost, the game ends — but you can restart or save your high score.

---

## Features and Requirements Met

### **Basic Requirements**
-  **Graphics:** Uses Arcade’s rendering and sprite system  
-  **User Input:** Keyboard controls for movement, pause, and save/load  
-  **Moveable Objects:** Player basket and falling gems  

### **Additional Requirement**
-  **Levels:** The game includes levels that automatically increase difficulty as you earn points  
  *(Bonus: also includes high-score save/load functionality)*  

---

##  Controls

| Key | Action |
|-----|---------|
| ← / A | Move Left |
| → / D | Move Right |
| P | Pause / Unpause |
| S | Save High Score |
| L | Load High Score |
| R | Restart (after Game Over) |
| Esc | Quit Game |

---

##  How to Play

1. Run the game (see setup instructions below).  
2. Use the arrow keys (or A/D) to move the basket left and right.  
3. Catch as many falling gems as you can!  
4. Every few points increase the **level**, making gems fall faster.  
5. When you run out of lives, press **R** to restart or **S** to save your high score.  

---

##  How to Run

1. Install Python 3.8 or later  
2. Install the Arcade library:
   ```bash
   pip install arcade
