from ulaz import *
from mozak import *

from manim import *
from elementi import *



Force_1 = Calculate_Q(loads_1)
Q_coo_1 = Force_1.return_Q_coord()

Moment_1 =  Calculate_M(loads_1, delta=delta_1)
M_coo_1 = Moment_1.return_M_coord_list()
X_coo_1 = Moment_1.return_x_coord_list()



class Z_1(Scene):
   
    def construct(self):

        delta = delta_1
        beam = beam_1
        Q_coo = Q_coo_1

        x_range = [0,12,2]     
        x_length = 6           

        y_range_Q = [0,80,2]      
        y_length_Q = 2.5       



        sustav_Q = Axes(x_range=x_range,y_range=y_range_Q,x_length=x_length,y_length=y_length_Q,
                      axis_config={'include_ticks': False,'tip_shape': StealthTip,"tip_width": 0,
                                   "tip_height": 0,'stroke_width': 0}) # Stavis 0 ako ne zelis da se vidi
        beam_line = Line(start=sustav_Q.c2p(beam["start"],0),end=sustav_Q.c2p(beam["end"],0),stroke_color=YELLOW,stroke_width=4)
        

        hatches_Q, curves_Q = [], []
        curves_Q = VGroup()
        hatch_list_Q = []
        for n in range(1,len(Q_coo)):
            A, B = Q_coo[n-1],  Q_coo[n]
            
            line = Line(start=sustav_Q.c2p(*A),end=sustav_Q.c2p(*B))
            curves_Q.add(line)

            if A[0] == B[0]: continue
            
            hatch = VGroup()
            for step in np.arange(A[0], B[0]+delta, delta):
                hatch_line = Line(start=sustav_Q.c2p(step,0),end=sustav_Q.c2p(step,LinearEquation(A, B, step).get_value()),stroke_color=BLUE,stroke_width=2)
                hatch.add(hatch_line)
            hatch_list_Q.append(hatch)   



        # self.add(sustav_Q)
        # self.play(Create(beam_line))
        # self.play(Create(curves_Q))

        # for i in hatch_list_Q:
        #     self.play(Create(i))




###################################################################################################################################

        X_coo = X_coo_1
        M_coo = M_coo_1

        y_range_M = [0,80,2]      
        y_length_M = 2.5  



        sustav_M = Axes(x_range=x_range,y_range=y_range_M,x_length=x_length,y_length=y_length_M,
                      axis_config={'include_ticks': False,'tip_shape': StealthTip,"tip_width": 0,
                                   "tip_height": 0,'stroke_width': 0}) # Stavis 0 ako ne zelis da se vidi
        

        hatches_M, curves_M = [], []
        for n_list in range(len(X_coo)):
            
            line_list, hatch_list= VGroup(), VGroup()
            for n_elem in range(1, len(X_coo[n_list])):
                
                x_A = X_coo[n_list][n_elem-1]
                m_A = M_coo[n_list][n_elem-1]             
                x_B = X_coo[n_list][n_elem]
                m_B = M_coo[n_list][n_elem]

                line = Line(start=sustav_M.c2p(x_A, m_A),end=sustav_M.c2p(x_B, m_B))
                hatch_line = Line(start=sustav_M.c2p(x_B,0),end=sustav_M.c2p(x_B, m_B),stroke_color=BLUE,stroke_width=2)


                line_list.add(line)
                hatch_list.add(hatch_line)
            curves_M.append(line_list)
            hatches_M.append(hatch_list)



        self.play(Create(beam_line))

        for i in curves_M:
            for j in i:
                self.play(Create(j))

        for i in hatches_M:
            self.play(Create(i))