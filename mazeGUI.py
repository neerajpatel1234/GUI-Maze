import tkinter as tk
import random

# Maze parameters
MAZE_WIDTH = 15
MAZE_HEIGHT = 10
CELL_SIZE = 30

class MazeGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=MAZE_WIDTH*CELL_SIZE, height=MAZE_HEIGHT*CELL_SIZE)
        self.canvas.pack()

        self.maze = self.generate_maze()
        self.draw_maze()

    def generate_maze(self):
        maze = [[1 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]

        stack = [(0, 0)]
        while stack:
            current = stack[-1]
            maze[current[1]][current[0]] = 0
            neighbors = [(current[0]+dx, current[1]+dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if 0 <= current[0]+dx < MAZE_WIDTH and 0 <= current[1]+dy < MAZE_HEIGHT and maze[current[1]+dy][current[0]+dx]]
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
                    self.canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()
