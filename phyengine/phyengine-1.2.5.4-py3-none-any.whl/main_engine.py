from tkinter import Tk, Canvas
import tkinter as tk

from math_engine import Vector
import math_engine as math_e

def simple_update():
    return 0

class BasicWindow(Tk):
    def __init__(self, sizex, sizey, ping = 30, scale = 10):
        super().__init__()
        self.geometry("{}x{}".format(sizex, sizey))
        self.x, self.y = sizex, sizey
        self.resizable(False, False)
        self.title("Experiment")
        self.Objects: list[DynamicObject] = list()
        self.ping = ping
        self.scale = scale

        self.update = simple_update

        self.canvas = Canvas(self)
        self.after(self.ping, lambda: self.raw_update_w())

    def start(self):
        self.canvas.pack(fill = tk.BOTH, expand = 1)
        self.mainloop()

    def InitObjects(self, *objects):
        self.Objects.extend(objects)

    @property
    def update(self):
        return self.raw_update_w

    @update.setter
    def update(self, fun):
        def wrap():
            fun()
            for obj in self.Objects:
                obj.raw_update_()
            self.after(self.ping, lambda: self.update())
        self.raw_update_w = wrap

class DynamicObjectBehaivour:
    def __init__(self, bounce_from_borders_friction = -1, gravity = -1,
    air_friction = -1):
        self.bounce_from_borders_friction = bounce_from_borders_friction
        self.gravity = gravity
        self.air_friction = air_friction

    @classmethod
    def STANDART(cls):
        return cls()

class DynamicObject:
    def __init__(self, window: BasicWindow, x, y, size, color = "red",
     collidable = True, behaivour: DynamicObjectBehaivour = DynamicObjectBehaivour.STANDART()):
        self.window = window
        self.canvas = window.canvas
        self.x, self.y, self.d = x, y, size
        self.color = color
        self.collidable = collidable
        self.behaivour = behaivour
        self.r_velocity: Vector = None
        self.r_acceleration: Vector = None

        self.speed = Vector.ZERO()
        self.acceleration = Vector.ZERO()

        self.index = len(self.window.Objects) + 1
        self.update = simple_update

        self.object = self.canvas.create_oval(x - size/2, y - size/2, x + size/2, y + size/2, fill=color)
        window.InitObjects(self)

    def __eq__(self, other):
        return self.index == other.index

    def move(self, dx, dy):
        self.canvas.move(self.object, dx, dy)
        self.x += dx
        self.y += dy

    def stamp(self, color):
        self.canvas.create_oval(self.x - self.d/8, self.y - self.d/8,
         self.x + self.d/8, self.y + self.d/8, fill=color, width=0)

    def standart_move(self):
        self.move(*((self.r_velocity * self.dt + (self.r_acceleration * (self.dt)**2)/2)
             * self.window.scale))

    @property
    def update(self):
        return self.raw_update_

    @property
    def dt(self):
        return self.window.ping / 1000

    @property
    def position(self):
        return Vector(self.x, self.y)
    
    @property
    def speed(self):
        return self.r_velocity

    @property
    def acceleration(self):
        return self.r_acceleration

    @position.setter
    def position(self, new_position: Vector):
        x, y = new_position
        self.canvas.move(self.object, x - self.x, y - self.y)
        self.x, self.y = x, y

    @speed.setter
    def speed(self, new_speed):
        self.r_velocity = new_speed

    @acceleration.setter
    def acceleration(self, new_acceleration: Vector):
        extra = Vector.ZERO()
        if self.behaivour.gravity > 0:
            extra += Vector(0, self.behaivour.gravity)
        if self.behaivour.air_friction > 0:
            extra += -self.r_velocity.unit * self.behaivour.air_friction * abs(self.r_velocity)**2
        self.r_acceleration = new_acceleration + extra
    
    @update.setter
    def update(self, fun):
        def wrap():
            fun()
            self.r_velocity += self.r_acceleration * self.dt
            self.standart_move()

            if self.behaivour.bounce_from_borders_friction >= 0:
                new_x, new_y = self.x, self.y
                if not (0 <= self.x <= self.window.x):
                    self.r_velocity.x *= -self.behaivour.bounce_from_borders_friction
                    new_x = self.window.x * (1 + math_e.sgn(self.x)) / 2
                if not (0 <= self.y <= self.window.y):
                    self.r_velocity.y *= -self.behaivour.bounce_from_borders_friction
                    new_y = self.window.y * (1 + math_e.sgn(self.y)) / 2
                self.position = new_x, new_y

        self.raw_update_ = wrap

    @staticmethod
    def is_collision(first, second):
        if (not first.collidable) or (not second.collidable):
            return False
        return (first.x - second.x) ** 2 + (first.y - second.y) ** 2 <= ((first.d + second.d)**2)/4