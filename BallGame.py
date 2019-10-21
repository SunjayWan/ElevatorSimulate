import tkinter as tk
import random,time

class Ball():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-3]
        self.x = 0
        self.y = -1
        self.canvas_height = canvas.winfo_height()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        
        
        
        
class BallGame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("BallGame")
        self.grid()
        canvas = tk.Canvas(self,width=500, height=400, bd=0)
        canvas.grid()
        self._build_ball()
    def _build_ball():
        
    
        
        
def start(bg):
    pass

        