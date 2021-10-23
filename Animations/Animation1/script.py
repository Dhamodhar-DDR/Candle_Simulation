from manimlib.imports import *
import numpy as np
import math

class intro(Scene):
    def construct(self):
        text=TextMobject("Consider the ","plot ","obtained from the ","experimental ","data").scale(0.7).set_color_by_tex_to_color_map({"experimental":YELLOW,"plot":BLUE})
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        
        self.wait(2)

class graphScene(GraphScene,MovingCameraScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 30,
        "y_min": -2,
        "y_max": 3,
        
        "graph_origin": ORIGIN+2.5*LEFT+0.5*DOWN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$t$(ksec)",
        "y_axis_label": "$R_t$(cm)",
        "exclude_zero_label": True,
        "x_labeled_nums": range(0, 31,5),
        "y_labeled_nums": range(0,3),
    }
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        self.setup_axes(animate=True)
        self.wait(1)
        
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)
        
        addp=lambda p,i,j:p.shift(ORIGIN+2.5*LEFT+0.5*DOWN+i*x_each_unit*RIGHT+j*y_each_unit*UP)
        points = [ Dot(color = RED, radius = 0.05) for dot in range(1,11) ]
        pointslocx=[0.8,1,3,4,4.7,6,8,10,12.5,13.8,15,17,25,28]
        pointslocy=[0.5,0.7,0.8,0.9,1,1.2,1.4,1.6,1.75,1.85,2,2.3,2.4]
        
        for i in range(len(points)):
            addp(points[i],pointslocx[i],pointslocy[i])
        
        self.play(FadeIn(points[0]),FadeIn(points[1]),FadeIn(points[2]),FadeIn(points[3]),FadeIn(points[4]),FadeIn(points[5]),FadeIn(points[6]),FadeIn(points[7]),FadeIn(points[8]),FadeIn(points[9]))

        self.wait(2)

        text2=TextMobject("Now plot the ","approximate ","curve").scale(0.7).shift(UP+1.9*RIGHT).set_color_by_tex_to_color_map({"approximate":YELLOW,"curve":BLUE})
        eqtext=TextMobject("joining all the ","points!").scale(0.43).shift(UP+1.9*RIGHT).set_color_by_tex_to_color_map({"points!":GREEN})
        self.play(Write(text2))
        self.wait(0.5)
        self.play(ReplacementTransform(text2,eqtext))
        self.wait(1)
        self.play(ApplyMethod(eqtext.shift,3.7*RIGHT+2.5*UP))
        
        g=self.get_graph(lambda t:2.2-((2.2-0.29)*math.exp(-0.75*t)),color=BLUE,x_min=0,x_max=6)

        self.play(ShowCreation(g))
        self.wait(0.8)

        t1=TextMobject("The ","points ","and the ","curve ","almost coincide!").scale(0.6).shift(3.5*RIGHT+2.5*DOWN).set_color_by_tex_to_color_map({"points":YELLOW,"curve":BLUE})
        t2a=TextMobject("Hence the ","Theoritical ","and ","Experimental ","results").scale(0.6).shift(3.5*RIGHT+2.5*DOWN).set_color_by_tex_to_color_map({"Theoritical":BLUE,"Experimental":YELLOW})
        t2b=TextMobject("obey with each other!").scale(0.6).shift(3.5*RIGHT+3*DOWN)
        self.play(Write(t1))
        self.wait(0.5)

        self.camera_frame.save_state() 

        play=lambda x,y:self.play(self.camera_frame.set_width, 4,self.camera_frame.move_to, ORIGIN+2*LEFT+0.5*DOWN+x*x_each_unit*RIGHT+y*y_each_unit*UP)
        for i in range(0,10,3):
            play(pointslocx[i],pointslocy[i])
            self.wait(0.7)
        self.wait(0.8)

        self.play(self.camera_frame.set_width,15,self.camera_frame.move_to, ORIGIN)
        self.wait(0.8)
        self.play(ReplacementTransform(t1,t2a))
        self.play(Write(t2b))
        self.wait(2)
