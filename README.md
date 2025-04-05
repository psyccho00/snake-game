# 🐍 Snake Game

Welcome to the **Snake Game**, a Python-based recreation of the classic arcade game. Built using the `turtle` graphics module, this game is an excellent demonstration of object-oriented programming and basic game logic.

---

## 📂 Repository Structure

```
snake-game/
│
├── main.py            # Game loop and user interaction
├── snake.py           # Snake class (movement and growth logic)
├── food.py            # Food class (placement and behavior)
└── scoreboard.py      # Score tracking and game-over message
```

---

## 🎮 How to Play

- Use **arrow keys** to control the snake.
- Eat the blue food circles to grow the snake and increase your score.
- Avoid colliding with the walls or yourself.
- The game ends if the snake crashes!

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3 installed on your machine.

### Installation

```bash
git clone https://github.com/psyccho00/snake-game.git
cd snake-game
python main.py
```

---

## 🧠 Code Overview

### `main.py` – Game Setup and Loop

- Initializes game screen and all objects (`Snake`, `Food`, `Scoreboard`)
- Listens for key presses
- Runs the game loop:
  - Updates the screen
  - Moves the snake
  - Detects collisions with food, walls, and itself

```python
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
```

```python
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
```

### `snake.py` – Snake Class

Handles:

- Creation of the initial snake
- Movement logic
- Growing the snake when food is eaten
- Turning direction with key inputs

```python
class Snake:
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
```

### `food.py` – Food Class

- Inherits from `Turtle`
- Creates a small blue dot at random positions
- Refreshes position when eaten

```python
class Food(Turtle):
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
```

### `scoreboard.py` – Score Tracking

- Displays the score at the top of the screen
- Increments score on eating food
- Shows "GAME OVER" on collision

```python
class Scoreboard(Turtle):
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
```

---

## 🌟 Features

✅ Real-time Snake movement  
✅ Collision detection (food, wall, self)  
✅ Random food placement  
✅ Score tracking and display  
✅ Game over logic  

---

## 🧠 Concepts Practiced

- Object-Oriented Programming (OOP)
- Inheritance in Python
- List and coordinate manipulation
- Event listeners with `onkey()`
- Game loop logic

---

## 📸 Screenshot

```
+----------------------------+
|                            |
|        🐍 --->             |
|                            |
|     🍽️ Blue Food           |
|                            |
|  Score: 3                 |
+----------------------------+
```

---

## 👨‍💻 Author

Developed by [psyccho00](https://github.com/psyccho00)

If you enjoyed this or found it helpful, give the repo a ⭐!

---

Enjoy playing and happy coding!
