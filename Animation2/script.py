#Yet to be completed

from manimlib.imports import *
import numpy as np
import math

class intro(Scene):
    def construct(self):
        text=TextMobject("Consider the ","plot ","obtained from the ","experimental ","data").scale(0.7).set_color_by_tex_to_color_map({"experimental":YELLOW,"plot":BLUE})
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))

class graphScene(GraphScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 6,
        "y_min": -2,
        "y_max": 3,
        
        "graph_origin": ORIGIN+2*LEFT+0.5*DOWN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$t$(ksec)",
        "y_axis_label": "$R_t$(cm)",
        "exclude_zero_label": True,
        "x_labeled_nums": range(0, 7),
        "y_labeled_nums": range(0,4)
    }
    def construct(self):
        self.setup_axes(animate=True)
        self.wait(2)
        
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)
        
        addp=lambda p,i,j:p.shift(ORIGIN+2*LEFT+0.5*DOWN+i*x_each_unit*RIGHT+j*y_each_unit*UP)
        points = [ Dot(color = RED, radius = 0.05) for dot in range(1,11) ]
        pointslocx=[0.8,1.3,2,2.6,3.2,3.8,4.2,4.8,5.4,6]
        pointslocy=[1,1.4,1.7,1.9,2.05,2.1,2.15,2.17,2.19,2.2]
        
        for i in range(len(points)):
            addp(points[i],pointslocx[i],pointslocy[i])
        
        self.play(FadeIn(points[0]),FadeIn(points[1]),FadeIn(points[2]),FadeIn(points[3]),FadeIn(points[4]),FadeIn(points[5]),FadeIn(points[6]),FadeIn(points[7]),FadeIn(points[8]),FadeIn(points[9]))
        
        self.wait(1)
        ks=[0,8,0.1,7,0.2,6,0.3,5,0.5,3,0.6,1.5,0.7,1,0.74,0.8,0.74]
        graphs=[]
        for k in ks:
            graphs.append(self.get_graph(lambda t:(2.2-((2.2-0.29)*math.exp(-1*k*t))),color=BLUE,x_min=0,x_max=6))
        
        self.play(ShowCreation(graphs[0]))
        self.wait(0.25)
        for i in range(1,len(ks)):
            self.play(ReplacementTransform(graphs[i-1],graphs[i]))
            self.wait(0.25)
        self.wait(4)


