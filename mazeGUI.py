import tkinter as tk
import random

# Maze parameters
MAZE_WIDTH = 15
MAZE_HEIGHT = 10
CELL_SIZE = 30

class MazeGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=MAZE_WIDTH * CELL_SIZE, height=MAZE_HEIGHT * CELL_SIZE)
        self.canvas.pack()

        self.maze = self.generate_maze()
        self.draw_maze()

        # Player position
        self.player_pos = (0, 0)
        self.draw_player()

        # Bind arrow key events
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)


    def generate_maze(self):
        maze = [[1 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]

        stack = [(0, 0)]
        while stack:
            current = stack[-1]
            maze[current[1]][current[0]] = 0
            neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if
                         0 <= current[0] + dx < MAZE_WIDTH and 0 <= current[1] + dy < MAZE_HEIGHT and
                         maze[current[1] + dy][current[0] + dx]]
            if neighbors:
                next_cell = random.choice(neighbors)
                stack.append(next_cell)
            else:
                stack.pop()

        return maze

    def draw_maze(self):
        for i in range(MAZE_HEIGHT):
            for j in range(MAZE_WIDTH):
                if self.maze[i][j]:
                    self.canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE,
                                                 fill="black")



    def draw_player(self):
        x, y = self.player_pos
        self.canvas.create_oval(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill="blue")

    def move_up(self, event):
        new_pos = (self.player_pos[0], max(0, self.player_pos[1] - 1))
        if self.maze[new_pos[1]][new_pos[0]] == 0:
            self.canvas.delete("player")
            self.player_pos = new_pos
            self.draw_player()

    def move_down(self, event):
        new_pos = (self.player_pos[0], min(MAZE_HEIGHT - 1, self.player_pos[1] + 1))
        if self.maze[new_pos[1]][new_pos[0]] == 0:
            self.canvas.delete("player")
            self.player_pos = new_pos
            self.draw_player()

    def move_left(self, event):
        new_pos = (max(0, self.player_pos[0] - 1), self.player_pos[1])
        if self.maze[new_pos[1]][new_pos[0]] == 0:
            self.canvas.delete("player")
            self.player_pos = new_pos
            self.draw_player()

    def move_right(self, event):
        new_pos = (min(MAZE_WIDTH - 1, self.player_pos[0] + 1), self.player_pos[1])
        if self.maze[new_pos[1]][new_pos[0]] == 0:
            self.canvas.delete("player")
            self.player_pos = new_pos
            self.draw_player()


if 1 == 1:
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()
