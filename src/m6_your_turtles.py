"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Arthur Ostrowski.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

banshee = rg.SimpleTurtle('turtle')
banshee.pen = rg.Pen('Blue',4)
banshee.speed = 9001

size = 150

for k in range(20):

    banshee.draw_circle(size)

    banshee.pen_up()
    banshee.right(45)
    banshee.forward(10)
    banshee.left(45)
    banshee.pen_down()

    size = size - 15

ashe = rg.SimpleTurtle('turtle')
ashe.pen = rg.Pen('Yellow',1.6)
ashe.speed = 9001
ashe.backward(100)

for k in range(15):
    ashe.draw_regular_polygon(5,50)
    ashe.left(76)
    ashe.backward(150)

window.tracer(100)



window.close_on_mouse_click()