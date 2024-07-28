from manim import *
import numpy as np


class NapraviOprugu(VMobject):
    def __init__(
            self,
            XY_start=np.array([0, 0, 0]),  # Start spring point
            XY_end=np.array([1, 0, 0]),  # End spring point
            num_loops=2,  # number of loops of spring
            width = 0.5,
            boja_linija = GRAY_B,
            opacitivnost = 1.0,
            debljina_linije = 4,
            frclek = 0.2,
            radius_tocke=0.1,
            boja_tocke=GRAY_B,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)
        L = np.sqrt(
            np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1])) - 2*frclek  # Length of spring

        theta = np.arctan2(
            XY_end[1]-XY_start[1],XY_end[0]-XY_start[0]
        )

        delx = L/(num_loops+1)


        op = VGroup()



        for xy in range(num_loops + 4):

            if xy == 0:
                linija = Line(start=XY_start,
                              end=np.array([((XY_start[0]+frclek)-XY_start[0])*np.cos(theta)-0*np.sin(theta)+XY_start[0],
                                            ((XY_start[0]+frclek)-XY_start[0])*np.sin(theta)+0*np.cos(theta)+XY_start[1],
                                            0]),
                              color=boja_linija, stroke_opacity=opacitivnost,stroke_width=debljina_linije)
                op.add(linija)

            elif xy == num_loops + 3:
                linija = Line(start=op[xy - 1].get_end(), end=XY_end, color=boja_linija, stroke_opacity=opacitivnost,stroke_width=debljina_linije)
                op.add(linija)

            elif xy == num_loops + 2:

                linija = Line(start=op[xy - 1].get_end(),
                              end=np.array([(((xy - 1) * delx + XY_start[0] + frclek) - XY_start[0]) * np.cos(theta) - 0 * np.sin(theta) + XY_start[0],
                                            (((xy - 1) * delx + XY_start[0] + frclek) - XY_start[0]) * np.sin(theta) + 0 * np.cos(theta) + XY_start[1],
                                            0]),
                              color=boja_linija, stroke_opacity=opacitivnost, stroke_width=debljina_linije)
                op.add(linija)


            else:
                linija = Line(start=op[xy-1].get_end(),
                              end=np.array([(((xy-0.5)*delx+XY_start[0]+frclek)-XY_start[0])*np.cos(theta)-((XY_start[1]+(-1)**(xy + 1)*width/2)-XY_start[1])*np.sin(theta)+XY_start[0],
                                            (((xy-0.5)*delx+XY_start[0]+frclek)-XY_start[0])*np.sin(theta)+((XY_start[1]+(-1)**(xy + 1)*width/2)-XY_start[1])*np.cos(theta)+XY_start[1],
                                            0]),
                              color=boja_linija, stroke_opacity=opacitivnost, stroke_width=debljina_linije)
                op.add(linija)

        tocka1 = always_redraw(lambda: Dot(point=op[0].get_start(), color=boja_tocke, radius=radius_tocke, fill_opacity=opacitivnost))
        tocka2 = always_redraw(lambda: Dot(point=op[-1].get_end(), color=boja_tocke, radius=radius_tocke, fill_opacity=opacitivnost))

        opruga = VGroup(op, tocka1, tocka2)

        self.add(opruga)

class NapraviOpruguBezTocke(VMobject):
    def __init__(
            self,
            XY_start=np.array([0, 0, 0]),  # Start spring point
            XY_end=np.array([1, 0, 0]),  # End spring point
            num_loops=2,  # number of loops of spring
            width = 0.5,
            boja_linija = GRAY_B,
            opacitivnost = 1.0,
            debljina_linije = 4,
            frclek = 0.2,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)
        L = np.sqrt(
            np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1])) - 2*frclek  # Length of spring

        theta = np.arctan2(
            XY_end[1]-XY_start[1],XY_end[0]-XY_start[0]
        )

        delx = L/(num_loops+1)


        op = VGroup()



        for xy in range(num_loops + 4):

            if xy == 0:
                linija = Line(start=XY_start,
                              end=np.array([((XY_start[0]+frclek)-XY_start[0])*np.cos(theta)-0*np.sin(theta)+XY_start[0],
                                            ((XY_start[0]+frclek)-XY_start[0])*np.sin(theta)+0*np.cos(theta)+XY_start[1],
                                            0]),
                              color=boja_linija, stroke_opacity=opacitivnost,stroke_width=debljina_linije)
                op.add(linija)

            elif xy == num_loops + 3:
                linija = Line(start=op[xy - 1].get_end(), end=XY_end, color=boja_linija, stroke_opacity=opacitivnost,stroke_width=debljina_linije)
                op.add(linija)

            elif xy == num_loops + 2:

                linija = Line(start=op[xy - 1].get_end(),
                              end=np.array([(((xy - 1) * delx + XY_start[0] + frclek) - XY_start[0]) * np.cos(theta) - 0 * np.sin(theta) + XY_start[0],
                                            (((xy - 1) * delx + XY_start[0] + frclek) - XY_start[0]) * np.sin(theta) + 0 * np.cos(theta) + XY_start[1],
                                            0]),
                              color=boja_linija, stroke_opacity=opacitivnost, stroke_width=debljina_linije)
                op.add(linija)


            else:
                linija = Line(start=op[xy-1].get_end(),
                              end=np.array([(((xy-0.5)*delx+XY_start[0]+frclek)-XY_start[0])*np.cos(theta)-((XY_start[1]+(-1)**(xy + 1)*width/2)-XY_start[1])*np.sin(theta)+XY_start[0],
                                            (((xy-0.5)*delx+XY_start[0]+frclek)-XY_start[0])*np.sin(theta)+((XY_start[1]+(-1)**(xy + 1)*width/2)-XY_start[1])*np.cos(theta)+XY_start[1],
                                            0]),
                              color=boja_linija, stroke_opacity=opacitivnost, stroke_width=debljina_linije)
                op.add(linija)



        opruga = VGroup(op)

        self.add(opruga)




class ObicanStap(VMobject):

    def __init__(
            self,
            XY_start=np.array([-3, 0, 0]),  # Start spring point
            XY_end=np.array([3, 0, 0]),  # End spring point
            debljina=0.2,
            opacitivnost=1.0,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        duzina = np.sqrt(np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1]))
        theta = np.arctan2(XY_end[1]-XY_start[1],XY_end[0]-XY_start[0])
        sredina = (XY_end+XY_start)/2

        tijelo = Rectangle(height=debljina,width=duzina,fill_opacity=opacitivnost).move_to(sredina)
        tijelo.set_color(color=[GRAY_BROWN,GRAY_D])
        color_direction=[-1,-1,0]
        tijelo.set_sheen_direction(color_direction)

        krug1 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(LEFT))
        krug1.set_color(GRAY_D)

        krug2 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(RIGHT))
        krug2.set_color(GRAY_BROWN)


        stap = VGroup(krug1,krug2,tijelo).rotate(theta)

        self.add(stap)



class ObicanStapTockica(VMobject):

    def __init__(
            self,
            XY_start=np.array([-3, 0, 0]),  # Start spring point
            XY_end=np.array([3, 0, 0]),  # End spring point
            debljina=0.2,
            opacitivnost=1.0,
            boja_tockica = GRAY_B,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        duzina = np.sqrt(np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1]))
        theta = np.arctan2(XY_end[1]-XY_start[1],XY_end[0]-XY_start[0])
        sredina = (XY_end+XY_start)/2

        tijelo = Rectangle(height=debljina,width=duzina,fill_opacity=opacitivnost).move_to(sredina)
        tijelo.set_color(color=[GRAY_BROWN,GRAY_D])
        color_direction=[-1,-1,0]
        tijelo.set_sheen_direction(color_direction)

        krug1 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(LEFT))
        krug1.set_color(GRAY_D)

        krug2 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(RIGHT))
        krug2.set_color(GRAY_BROWN)



        tockica1 = Dot().scale(0.75).move_to(krug1.get_center())
        tockica2 = Dot().scale(0.75).move_to(krug2.get_center())
        tockica1.set_color(boja_tockica)
        tockica2.set_color(boja_tockica)

        stap = VGroup(krug1,krug2,tijelo,tockica1,tockica2).rotate(theta)

        self.add(stap)




class ObicanStapKrugovi(VMobject):

    def __init__(
            self,
            XY_start=np.array([-3, 0, 0]),  # Start spring point
            XY_end=np.array([3, 0, 0]),  # End spring point
            debljina=0.2,
            opacitivnost=1.0,
            boja_kruga=GRAY_B,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        duzina = np.sqrt(np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1]))
        theta = np.arctan2(XY_end[1]-XY_start[1],XY_end[0]-XY_start[0])
        sredina = (XY_end+XY_start)/2

        tijelo = Rectangle(height=debljina,width=duzina,fill_opacity=opacitivnost).move_to(sredina)
        tijelo.set_color(color=[GRAY_BROWN,GRAY_D])
        color_direction=[-1,-1,0]
        tijelo.set_sheen_direction(color_direction)

        krug1 = Circle(radius=debljina,fill_opacity=opacitivnost).move_to(tijelo.get_corner(LEFT))
        krug1.set_color(boja_kruga)

        krug2 = Circle(radius=debljina,fill_opacity=opacitivnost).move_to(tijelo.get_corner(RIGHT))
        krug2.set_color(boja_kruga)




        stap = VGroup(tijelo,krug1,krug2).rotate(theta)

        self.add(stap)



class TankiStap(VMobject):

    def __init__(
            self,
            XY_start=np.array([-3, 0, 0]),  # Start spring point
            XY_end=np.array([3, 0, 0]),  # End spring point
            debljina=0.025,
            opacitivnost=1.0,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        duzina = np.sqrt(np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1]))
        theta = np.arctan2(XY_end[1]-XY_start[1],XY_end[0]-XY_start[0])
        sredina = (XY_end+XY_start)/2

        tijelo = Rectangle(height=debljina,width=duzina,fill_opacity=opacitivnost).move_to(sredina)
        tijelo.set_color(color=[GRAY_BROWN,GRAY_D])
        color_direction=[-1,-1,0]
        tijelo.set_sheen_direction(color_direction)

        krug1 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(LEFT))
        krug1.set_color(GRAY_D)

        krug2 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(RIGHT))
        krug2.set_color(GRAY_BROWN)


        stap = VGroup(krug1,krug2,tijelo).rotate(theta)

        self.add(stap)



class TankiStapTockica(VMobject):

    def __init__(
            self,
            XY_start=np.array([-3, 0, 0]),  # Start spring point
            XY_end=np.array([3, 0, 0]),  # End spring point
            debljina=0.025,
            opacitivnost=1.0,
            boja_tockica = GRAY_B,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        duzina = np.sqrt(np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1]))
        theta = np.arctan2(XY_end[1]-XY_start[1],XY_end[0]-XY_start[0])
        sredina = (XY_end+XY_start)/2

        tijelo = Rectangle(height=debljina,width=duzina,fill_opacity=opacitivnost).move_to(sredina)
        tijelo.set_color(color=[GRAY_BROWN,GRAY_D])
        color_direction=[-1,-1,0]
        tijelo.set_sheen_direction(color_direction)

        krug1 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(LEFT))
        krug1.set_color(GRAY_D)

        krug2 = Circle(radius=debljina/2,fill_opacity=opacitivnost).move_to(tijelo.get_corner(RIGHT))
        krug2.set_color(GRAY_BROWN)



        tockica1 = Dot().scale(0.75).move_to(krug1.get_center())
        tockica2 = Dot().scale(0.75).move_to(krug2.get_center())
        tockica1.set_color(boja_tockica)
        tockica2.set_color(boja_tockica)

        stap = VGroup(krug1,krug2,tijelo,tockica1,tockica2).rotate(theta)

        self.add(stap)




class TankiStapKrugovi(VMobject):

    def __init__(
            self,
            XY_start=np.array([-3, 0, 0]),  # Start spring point
            XY_end=np.array([3, 0, 0]),  # End spring point
            debljina=0.025,
            opacitivnost=1.0,
            boja_krug = GRAY_B,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        duzina = np.sqrt(np.square(XY_end[0] - XY_start[0]) + np.square(XY_end[1] - XY_start[1]))
        theta = np.arctan2(XY_end[1]-XY_start[1],XY_end[0]-XY_start[0])
        sredina = (XY_end+XY_start)/2

        tijelo = Rectangle(height=debljina,width=duzina,fill_opacity=opacitivnost).move_to(sredina)
        tijelo.set_color(color=[GOLD_E,GOLD_E])
        color_direction=[-1,-1,0]
        tijelo.set_sheen_direction(color_direction)

        krug1 = Circle(radius=debljina,fill_opacity=opacitivnost).move_to(tijelo.get_corner(LEFT))
        krug1.set_color(boja_krug)

        krug2 = Circle(radius=debljina,fill_opacity=opacitivnost).move_to(tijelo.get_corner(RIGHT))
        krug2.set_color(boja_krug)




        stap = VGroup(tijelo,krug1,krug2).rotate(theta)

        self.add(stap)





class PomicniLezaj(VMobject):
    def __init__(
            self,
            broj_crtica=5,
            boja_linija=GRAY_B,
            duljina_srafure=0.5,
            debljina_srafura=1.5,
            radius_kuglica = 0.3,
            debljina_linije = 3,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)

        trokut = Triangle(color=boja_linija,stroke_width=debljina_linije)
        kuglice = VGroup()
        linija = Line(color=boja_linija,stroke_width=debljina_linije).next_to(trokut,DOWN,buff=0.3)


        b = float(linija.get_length())



        sredisnja_kuglica = Circle(radius=radius_kuglica,color=boja_linija,stroke_width=debljina_linije).next_to(trokut,DOWN,buff=0)
        lijeva_kuglica = Circle(radius=radius_kuglica,color=boja_linija,stroke_width=debljina_linije).next_to(trokut,DOWN,buff=0).shift(b/3*LEFT)
        desna_kuglica = Circle(radius=radius_kuglica, color=boja_linija,stroke_width=debljina_linije).next_to(trokut, DOWN, buff=0).shift(b/3*RIGHT)

        kuglice.add(sredisnja_kuglica,lijeva_kuglica,desna_kuglica)

        linija.next_to(sredisnja_kuglica,DOWN,buff=0)


        razmak = np.linspace(0,b,broj_crtica+2)
        srafura = VGroup()

        for i in range (len(razmak)):

            if i==len(razmak)-1:
                pass

            else:
                crta_srafura = Line(
                    start=linija.get_start()+np.array([razmak[i],0,0]),
                    end=linija.get_start()+np.array([razmak[i] + duljina_srafure * np.cos(PI / 4), -duljina_srafure * np.sin(PI / 4), 0]),
                    color=boja_linija,stroke_width=debljina_srafura)

                srafura.add(crta_srafura)

        lezaj = VGroup(srafura,trokut,linija,kuglice).scale(0.25)

        self.add(lezaj)


class NepomicniLezaj(VMobject):
    def __init__(
            self,
            broj_crtica=5,
            boja_linija=GRAY_B,
            duljina_srafure=0.5,
            debljina_srafura=1.5,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        trokut = Triangle(color=boja_linija)
        linija = Line(start=trokut.get_corner(DL)-np.array([0.5,0,0]),end=trokut.get_corner(DR)+np.array([0.5,0,0]),color=boja_linija)


        b = float(linija.get_length())

        razmak = np.linspace(0,b,broj_crtica+2)
        srafura = VGroup()

        for i in range (len(razmak)):

            if i==len(razmak)-1:
                pass

            else:
                crta_srafura = Line(
                    start=linija.get_start()+np.array([razmak[i],0,0]),
                    end=linija.get_start()+np.array([razmak[i] + duljina_srafure * np.cos(PI / 4), -duljina_srafure * np.sin(PI / 4), 0]),
                    color=boja_linija,stroke_width=debljina_srafura)

                srafura.add(crta_srafura)


        sve=VGroup(trokut,linija,srafura).scale(0.25)

        self.add(sve)



class Podloga(VMobject):
    def __init__(
            self,
            XY_start=np.array([0, 0, 0]),
            XY_end=np.array([3, 0, 0]),
            broj_crtica=5,
            boja_linija=GRAY_B,
            duljina_srafure=1.5,
            debljina_srafura=1,
            debljina_podloge= 3,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)

        L = np.sqrt(
            np.square(XY_end[1]-XY_start[1])
            +np.square(XY_end[0]-XY_start[0]))

        theta = np.arctan2(
            XY_end[1]-XY_start[1],XY_end[0]-XY_start[0]
        )

        linija = Line(start=XY_start, end=XY_end,stroke_width=debljina_podloge)

        srafura = VGroup()

        razmak = np.linspace(0,L,broj_crtica+2)


        for i in range (len(razmak)):

            if i==len(razmak)-1:
                pass

            else:
                crta_srafura = Line(
                    start=linija.get_start()+np.array([razmak[i]*np.cos(theta),razmak[i]*np.sin(theta),0]),
                    end=linija.get_start()+np.array([(razmak[i] + duljina_srafure * np.cos(PI/4))*np.cos(theta)+duljina_srafure * np.sin(PI / 4)*np.sin(theta),
                                                     -duljina_srafure * np.sin(PI / 4)*np.cos(theta) + (razmak[i] + duljina_srafure * np.cos(PI / 4))*np.sin(theta),
                                                     0]),
                    color=boja_linija,stroke_width=debljina_srafura)

                srafura.add(crta_srafura)


        sve = VGroup(srafura,linija)

        self.add(sve)




def SrafuraZaPodlogu(linija,broj_crtica,duljina_srafure,debljina_srafura,kut_srafure):

    L = np.sqrt(
        np.square(linija.get_end()[1] - linija.get_start()[1])
        + np.square(linija.get_end()[0] - linija.get_start()[0]))


    theta = np.arctan2(
        linija.get_end()[1] - linija.get_start()[1], linija.get_end()[0] - linija.get_start()[0]
    )

    srafura = VGroup()


    razmak = np.linspace(0, L, broj_crtica + 2)

    for i in range(len(razmak)):

        if i == len(razmak) - 1:
            pass

        else:
            crta_srafura = Line(
                start=linija.get_start() + np.array([razmak[i] * np.cos(theta), razmak[i] * np.sin(theta), 0]),
                end=linija.get_start() + np.array([(razmak[i] + duljina_srafure * np.cos(kut_srafure)) * np.cos(theta) + duljina_srafure * np.sin(kut_srafure) * np.sin(theta),
                                                   -duljina_srafure * np.sin(kut_srafure) * np.cos(theta) + (razmak[i] + duljina_srafure * np.cos(kut_srafure)) * np.sin(theta),
                                                   0]),
                color=linija.get_color(), stroke_width=debljina_srafura)

            srafura.add(crta_srafura)


    return srafura


def SrafuraZaLuk(linija,duljina_srafure,debljina_srafure,kut_srafure):


    tocke = []


    for i in range (len(linija.get_all_points())):

        if i % 4==0:
            pass

        elif i == len(linija.get_all_points()):
            pass

        else:
            tocke.append(linija.get_all_points()[i])

    srafura = VGroup()

    for x in range (len(tocke)):

        if x == 0 or x%4==0:
            crta_srafura = Line(start=tocke[x], end=tocke[x]+np.array([duljina_srafure*np.cos(kut_srafure),duljina_srafure*np.sin(kut_srafure),0]),
                                color=linija.get_color(), stroke_width=debljina_srafure)
            srafura.add(crta_srafura)

        else:
            pass

    return srafura



def Kotac(skala, boja):



    radius1 = 0.25
    radius2 = 0.2
    radius3 = 0.05
    debljina_crte = 3 * skala

    g1 = Circle(radius=radius1, color=boja, stroke_width=debljina_crte)
    g2 = Circle(radius=radius2, color=boja, stroke_width=debljina_crte)
    g3 = Circle(radius=radius3, color=boja, stroke_width=debljina_crte)

    f1 = Line(start=g3.get_corner(UP), end=g2.get_corner(UP), stroke_width=debljina_crte,color=boja)
    f2 = Line(start=np.array([radius3 * np.cos(3 * PI / 4), radius3 * np.sin(3 * PI / 4), 0]),
              end=np.array([radius2 * np.cos(3 * PI / 4), radius2 * np.sin(3 * PI / 4), 0])
              , stroke_width=debljina_crte,color=boja)
    f3 = Line(start=g3.get_corner(LEFT), end=g2.get_corner(LEFT), stroke_width=debljina_crte,color=boja)
    f4 = Line(start=np.array([radius3 * np.cos(5 * PI / 4), radius3 * np.sin(5 * PI / 4), 0]),
              end=np.array([radius2 * np.cos(5 * PI / 4), radius2 * np.sin(5 * PI / 4), 0])
              , stroke_width=debljina_crte,color=boja)
    f5 = Line(start=g3.get_corner(DOWN), end=g2.get_corner(DOWN), stroke_width=debljina_crte)
    f6 = Line(start=np.array([radius3 * np.cos(7 * PI / 4), radius3 * np.sin(7 * PI / 4), 0]),
              end=np.array([radius2 * np.cos(7 * PI / 4), radius2 * np.sin(7 * PI / 4), 0])
              , stroke_width=debljina_crte,color=boja)
    f7 = Line(start=g3.get_corner(RIGHT), end=g2.get_corner(RIGHT), stroke_width=debljina_crte,color=boja)
    f8 = Line(start=np.array([radius3 * np.cos(1 * PI / 4), radius3 * np.sin(1 * PI / 4), 0]),
              end=np.array([radius2 * np.cos(1 * PI / 4), radius2 * np.sin(1 * PI / 4), 0])
              , stroke_width=debljina_crte,color=boja)

    kotac = VGroup(g1, g2, g3, f1, f2, f3, f4, f5, f6, f7, f8)

    return kotac


def Karoserija1(kotac1,kotac2,skala,boja):


    debljina_crte = skala*3



    theta = np.arctan2(
        kotac2.get_center()[1] - kotac1.get_center()[1], kotac2.get_center()[0] - kotac1.get_center()[0]
    )

    luk1 = Arc(radius=0.35,start_angle=theta+PI,angle=-PI, arc_center=kotac1.get_center(), stroke_width=debljina_crte,color=boja)
    luk2 = Arc(radius=0.35, start_angle=theta+PI,angle=-PI, arc_center=kotac2.get_center(), stroke_width=debljina_crte,color=boja)
    kar1 = Line(start=luk1.get_start(), end=luk1.get_start() + np.array([0.3*np.cos(theta-PI), 0.3*np.sin(theta-PI), 0]), stroke_width=debljina_crte,color=boja)
    kar2 = Line(start=kar1.get_end(), end=kar1.get_end() + np.array([0+np.sin(theta-PI)*0.5,-np.cos(theta-PI)*0.5, 0]), stroke_width=debljina_crte,color=boja)
    luk3 = ArcBetweenPoints(radius=0.2, start=kar2.get_end() - np.array([0.2*np.cos(theta-PI)-0.2*np.sin(theta-PI), 0.2*np.cos(theta-PI)+0.2*np.sin(theta-PI), 0]), end=kar2.get_end(),
                            stroke_width=debljina_crte,color=boja)
    kar3 = Line(start=luk3.get_start(), end=luk3.get_start() - np.array([0.5*np.cos(theta-PI), 0.5*np.sin(theta-PI), 0]), stroke_width=debljina_crte,color=boja)
    kar4 = Line(start=kar3.get_end(), end=kar3.get_end() - np.array([0.3*np.cos(theta-PI)-0.5*np.sin(theta-PI), 0.3*np.sin(theta-PI)+0.5*np.cos(theta-PI), 0]), stroke_width=debljina_crte,color=boja)
    kar5 = Line(start=kar4.get_end(), end=kar4.get_end() - np.array([1.25*np.cos(theta-PI),1.25*np.sin(theta-PI), 0]), stroke_width=debljina_crte,color=boja)
    kar6 = Line(start=luk2.get_end(), end=luk2.get_end() - np.array([0.15*np.cos(theta-PI),np.sin(theta-PI)*0.15, 0]), stroke_width=debljina_crte,color=boja)
    kar7 = Line(start=kar6.get_end(), end=kar6.get_end() - np.array([-0.5*np.sin(theta-PI), 0.5*np.cos(theta-PI), 0]), stroke_width=debljina_crte,color=boja)
    kar8 = Line(start=kar7.get_end(), end=kar5.get_end(), stroke_width=debljina_crte,color=boja)
    kar9 = Line(start=luk1.get_end(), end=luk2.get_start(), stroke_width=debljina_crte,color=boja)

    prozor1 = Line(start=kar3.get_end() - np.array([0.1*np.cos(theta-PI), 0.1*np.sin(theta-PI), 0]),
                   end=kar3.get_end() - np.array([0.1*np.cos(theta-PI), 0.1*np.sin(theta-PI), 0]) - 0.8 * np.array([0.3*np.cos(theta-PI)-0.5*np.sin(theta-PI),0.3*np.sin(theta-PI)+0.5*np.cos(theta-PI), 0]),
                   stroke_width=debljina_crte,color=boja)
    prozor2 = Line(start=prozor1.get_end(), end=prozor1.get_end() - np.array([0.5*np.cos(theta-PI),0.5*np.sin(theta-PI), 0]), stroke_width=debljina_crte,color=boja)
    prozor3 = Line(start=prozor2.get_end(), end=prozor2.get_end() - np.array([0.8 * 0.5*np.sin(theta-PI), -0.8 * 0.5*np.cos(theta-PI), 0]),
                   stroke_width=debljina_crte,color=boja)
    prozor4 = Line(start=prozor3.get_end(), end=prozor1.get_start(), stroke_width=debljina_crte,color=boja)

    drugi_prozor1 = Line(start=prozor3.get_end() - np.array([0.1*np.cos(theta-PI), 0.1*np.sin(theta-PI), 0]),
                         end=prozor3.get_end() - np.array([0.1*np.cos(theta-PI)-0.8*0.5*np.sin(theta-PI), 0.1*np.sin(theta-PI)+0.8*0.5*np.cos(theta-PI), 0]), stroke_width=debljina_crte,color=boja)
    drugi_prozor2 = Line(start=drugi_prozor1.get_end(), end=drugi_prozor1.get_end() - np.array([0.5*np.cos(theta-PI), 0.5*np.sin(theta-PI), 0]),
                         stroke_width=debljina_crte,color=boja)
    drugi_prozor3 = Line(start=drugi_prozor2.get_end(), end=drugi_prozor2.get_end() - np.array([0.225*np.cos(theta-PI)+0.8*0.5*np.sin(theta-PI),0.225*np.sin(theta-PI)-0.8*0.5*np.cos(theta-PI), 0]),
                         stroke_width=debljina_crte,color=boja)
    drugi_prozor4 = Line(start=drugi_prozor3.get_end(), end=drugi_prozor1.get_start(), stroke_width=debljina_crte,color=boja)


    auto = VGroup(kotac1, kotac2, luk1, luk2, kar1, kar2, luk3, kar3, kar4, kar5, kar6, kar7, kar8, kar9, prozor1,
                  prozor2, prozor3, prozor4, drugi_prozor1, drugi_prozor2, drugi_prozor3, drugi_prozor4)

    return auto

def Automobil(skala,boja):

    kotac1 = Kotac(skala,WHITE).shift(LEFT)
    kotac2 = Kotac(skala,WHITE).shift(RIGHT)


    debljina_crte = skala*3

    luk1 = Arc(radius=0.35, angle=PI, arc_center=kotac1.get_center(), stroke_width=debljina_crte,color=boja)
    luk2 = Arc(radius=0.35, angle=PI, arc_center=kotac2.get_center(), stroke_width=debljina_crte,color=boja)
    kar1 = Line(start=luk2.get_start(), end=luk2.get_start() + np.array([0.3, 0, 0]), stroke_width=debljina_crte,color=boja)
    kar2 = Line(start=kar1.get_end(), end=kar1.get_end() + np.array([0, 0.5, 0]), stroke_width=debljina_crte,color=boja)
    luk3 = ArcBetweenPoints(radius=0.2, start=kar2.get_end(), end=kar2.get_end() + np.array([-0.2, 0.2, 0]),
                            stroke_width=debljina_crte,color=boja)
    kar3 = Line(start=luk3.get_end(), end=luk3.get_end() - np.array([0.5, 0, 0]), stroke_width=debljina_crte,color=boja)
    kar4 = Line(start=kar3.get_end(), end=kar3.get_end() + np.array([-0.3, 0.5, 0]), stroke_width=debljina_crte,color=boja)
    kar5 = Line(start=kar4.get_end(), end=kar4.get_end() - np.array([1.75, 0, 0]), stroke_width=debljina_crte,color=boja)
    kar6 = Line(start=luk1.get_end(), end=luk1.get_end() - np.array([0.15, 0, 0]), stroke_width=debljina_crte,color=boja)
    kar7 = Line(start=kar6.get_end(), end=kar6.get_end() + np.array([0, 0.5, 0]), stroke_width=debljina_crte,color=boja)
    kar8 = Line(start=kar7.get_end(), end=kar5.get_end(), stroke_width=debljina_crte,color=boja)
    kar9 = Line(start=luk1.get_start(), end=luk2.get_end(), stroke_width=debljina_crte,color=boja)

    prozor1 = Line(start=kar3.get_end() - np.array([0.2, 0, 0]),
                   end=kar3.get_end() - np.array([0.2, 0, 0]) + 0.8 * np.array([-0.3, 0.5, 0]),
                   stroke_width=debljina_crte,color=boja)
    prozor2 = Line(start=prozor1.get_end(), end=prozor1.get_end() + np.array([-0.65, 0, 0]), stroke_width=debljina_crte,color=boja)
    prozor3 = Line(start=prozor2.get_end(), end=prozor2.get_end() + np.array([0, -0.8 * 0.5, 0]),
                   stroke_width=debljina_crte,color=boja)
    prozor4 = Line(start=prozor3.get_end(), end=prozor1.get_start(), stroke_width=debljina_crte,color=boja)

    drugi_prozor1 = Line(start=prozor3.get_end() - np.array([0.1, 0, 0]),
                         end=prozor3.get_end() + np.array([-0.1, 0.8 * 0.5, 0]), stroke_width=debljina_crte,color=boja)
    drugi_prozor2 = Line(start=drugi_prozor1.get_end(), end=drugi_prozor1.get_end() - np.array([0.74, 0, 0]),
                         stroke_width=debljina_crte,color=boja)
    drugi_prozor3 = Line(start=drugi_prozor2.get_end(), end=drugi_prozor2.get_end() + np.array([-0.275, -0.8 * 0.5, 0]),
                         stroke_width=debljina_crte,color=boja)
    drugi_prozor4 = Line(start=drugi_prozor3.get_end(), end=drugi_prozor1.get_start(), stroke_width=debljina_crte,color=boja)


    karoserija = VGroup(kotac1, kotac2, luk1, luk2, kar1, kar2, luk3, kar3, kar4, kar5, kar6, kar7, kar8, kar9, prozor1,
                  prozor2, prozor3, prozor4, drugi_prozor1, drugi_prozor2, drugi_prozor3, drugi_prozor4)

    auto = VGroup(kotac1,kotac2,karoserija).scale(skala)

    return auto


def JednolikoOpterecenje(duljina,razmak,smjer,velicina,boja,debljina):


    vektori = VGroup()

    for i in range(int(duljina/razmak+1)):

        if smjer == "DOLJE":

            if i == 0:
                veki = Arrow(start=np.array([-duljina/2,0,0]),end=np.array([-duljina/2,-velicina,0]),color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([razmak,0,0]),end=vektori[i-1].get_end()+np.array([razmak,0,0]),
                                     color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(drugi_vekiji)
        elif smjer == "GORE":
            if i == 0:
                veki = Arrow(start=np.array([-duljina/2,0,0]),end=np.array([-duljina/2,velicina,0]),color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([razmak,0,0]),end=vektori[i-1].get_end()+np.array([razmak,0,0]),
                                     color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(drugi_vekiji)
        elif smjer == "LIJEVO":
            if i == 0:
                veki = Arrow(start=np.array([0,duljina/2,0]),end=np.array([-velicina,duljina/2,0]),color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([0,-razmak,0]),end=vektori[i-1].get_end()+np.array([0,-razmak,0]),
                                     color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(drugi_vekiji)
        else:
            if i == 0:
                veki = Arrow(start=np.array([0,duljina/2,0]),end=np.array([velicina,duljina/2,0]),color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([0,-razmak,0]),end=vektori[i-1].get_end()+np.array([0,-razmak,0]),
                                     color=boja,buff=0,stroke_width=2*debljina)
                vektori.add(drugi_vekiji)



    linija1= Line(start=vektori[0].get_start(),end=vektori[-1].get_start(),color=boja,stroke_width=debljina/2)
    linija2= Line(start=vektori[0].get_end(),end=vektori[-1].get_end(),color=boja,stroke_width=debljina/2)
    vektori.add(linija1)
    vektori.add(linija2)


    return vektori


def Profil(duljina,razmak,smjer,velicina1,velicina2,boja,debljina):

    vektori = VGroup()

    for i in range(int(duljina/razmak+1)):

        if smjer == "DOLJE":

            if i == 0:
                veki = Arrow(start=np.array([-duljina/2,0,0]),end=np.array([-duljina/2,-velicina1,0]),
                             color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([razmak,0,0]),
                                     end=vektori[i-1].get_end()+np.array([razmak,(velicina1-velicina2)/(duljina/razmak),0]),
                                     color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(drugi_vekiji)

        elif smjer == "GORE":

            if i == 0:
                veki = Arrow(start=np.array([-duljina/2,0,0]),end=np.array([-duljina/2,velicina1,0]),
                             color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([razmak,0,0]),
                                     end=vektori[i-1].get_end()+np.array([razmak,-(velicina1-velicina2)/(duljina/razmak),0]),
                                     color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(drugi_vekiji)

        elif smjer == "LIJEVO":
            if i == 0:
                veki = Arrow(start=np.array([0,duljina/2,0]),end=np.array([-velicina1,duljina/2,0]),
                             color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([0,-razmak,0]),
                                     end=vektori[i-1].get_end()+np.array([(velicina1-velicina2)/(duljina/razmak),-razmak,0]),
                                     color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(drugi_vekiji)
        else:
            if i == 0:
                veki = Arrow(start=np.array([0,duljina/2,0]),end=np.array([velicina1,duljina/2,0]),
                             color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(veki)
            else:
                drugi_vekiji = Arrow(start=vektori[i-1].get_start()+np.array([0,-razmak,0]),
                                     end=vektori[i-1].get_end()+np.array([-(velicina1-velicina2)/(duljina/razmak),-razmak,0]),
                                     color=boja,buff=0,stroke_width=2*debljina,max_stroke_width_to_length_ratio=20,tip_length=0.1,max_tip_length_to_length_ratio=0.5)
                vektori.add(drugi_vekiji)



    linija1= Line(start=vektori[0].get_start(),end=vektori[-1].get_start(),color=boja,stroke_width=debljina/2)
    linija2= Line(start=vektori[0].get_end(),end=vektori[-1].get_end(),color=boja,stroke_width=debljina/2)
    vektori.add(linija1)
    vektori.add(linija2)



    return vektori




class TriDimNepomicniLezaj(VMobject):     ###### ako imaš slučaj s rotiranim ležajem ->
                                    ###### lezaj.rotate(iznoskuta,about_point=lezaj.get_corner(UP))
    def __init__(
            self,
            broj_crtica=5,
            boja_linija=WHITE,
            duljina_srafure=0.5,
            debljina_srafura=2,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)


        trokut = Triangle(color=boja_linija)
        linija = Line(start=trokut.get_corner(DL)-np.array([0.5,0,0]),end=trokut.get_corner(DR)+np.array([0.5,0,0]))


        b = float(linija.get_length())

        razmak = np.linspace(0,b,broj_crtica+2)
        srafura = VGroup()

        for i in range (len(razmak)):

            if i==len(razmak)-1:
                pass

            else:
                crta_srafura = Line(
                    start=linija.get_start()+np.array([razmak[i],0,0]),
                    end=linija.get_start()+np.array([razmak[i] + duljina_srafure * np.cos(PI / 4), -duljina_srafure * np.sin(PI / 4), 0]),
                    color=boja_linija,stroke_width=debljina_srafura)

                srafura.add(crta_srafura)


        sve=VGroup(trokut,linija,srafura)

        self.add(sve)


class CrtkanaKocka(VMobject):

    def __init__(
            self,
            XY_start=np.array([0, 0, 0]),
            XY_end=np.array([1, 1, 1]),
            boja_linija=WHITE,
            duljina=0.05,
            debljina_linije=1.0,
            *args,
            **kwargs
    ):
        VMobject.__init__(self)

        x = XY_end[0]-XY_start[0]
        y = XY_end[1] - XY_start[1]
        z = XY_end[2] - XY_start[2]

        linija1 = DashedLine(start=XY_start,end=XY_start+np.array([x,0,0]),color=boja_linija,dash_length=duljina)
        linija2 = DashedLine(start=linija1.get_end(), end=linija1.get_end()+np.array([0,y,0]),color=boja_linija,dash_length=duljina)
        linija3 = DashedLine(start=linija2.get_end(), end=linija2.get_end()+np.array([-x,0,0]),color=boja_linija,dash_length=duljina)
        linija4 = DashedLine(start=linija3.get_end(), end=linija3.get_end()+np.array([0,-y,0]),color=boja_linija,dash_length=duljina)

        linija5 = DashedLine(start=XY_start+np.array([0,0,z]),end=XY_start+np.array([x,0,z]),color=boja_linija,dash_length=duljina)
        linija6 = DashedLine(start=linija5.get_end(), end=linija5.get_end()+np.array([0,y,0]),color=boja_linija,dash_length=duljina)
        linija7 = DashedLine(start=linija6.get_end(), end=linija6.get_end()+np.array([-x,0,0]),color=boja_linija,dash_length=duljina)
        linija8 = DashedLine(start=linija7.get_end(), end=linija7.get_end()+np.array([0,-y,0]),color=boja_linija,dash_length=duljina)

        linija9 = DashedLine(start=linija1.get_start(),end=linija5.get_start(),color=boja_linija,dash_length=duljina)
        linija10 = DashedLine(start=linija2.get_start(),end=linija6.get_start(),color=boja_linija,dash_length=duljina)
        linija11 = DashedLine(start=linija3.get_start(),end=linija7.get_start(),color=boja_linija,dash_length=duljina)
        linija12 = DashedLine(start=linija4.get_start(),end=linija8.get_start(),color=boja_linija,dash_length=duljina)

        gr = VGroup(linija1,linija2,linija3,linija4,linija5,linija6,linija7,linija8,linija9,linija10,linija11,linija12)

        #linija5,linija6,linija7,linija8,linija9,linija10,linija11,linija12

        self.add(gr)

