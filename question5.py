import pygame 
from pygame.locals import * 
import OpenGL 
import OpenGL.GL 
import OpenGL.GLU 
import OpenGL.GLUT 


vertices = ( 
(0, 1, 0),  #top vertex 
(-1, -1, 0), #bottom left vertex 
(1, -1, 0), #bottom right vertex 
)

colors = ( 
(1, 0, 0),  #red color 
(1, 0, 0),  #red color 
(1, 0, 0),  #red color 
# (0, 1, 0), #green color 
#(0, 0, 1), #red color 
) #case 1

colors = ( 
(1, 0, 0),  #red color 
(0, 1, 0), #green color 
(0, 0, 1), #red color 
) #case 2 

def Triangle(): 
glBegin(GL_TRIANGLES) 
for i in range(len(vertices)): 
glColor3f(colors[i][0], colors[i][1], colors[i][2]) 
glVertex3f(vertices[i][0], vertices[i][1], vertices[i][2]) 
glEnd() 

def main(): 
pygame.init() 
display = (800, 600) 
pygame.display.set_mode(display, DOUBLEBUF|OPENGL) 
gluPerspective(45, display[0] / display[1]), 0.1, 50.0) 
glTranslatef(0.0, 0.0, -5.0) 
while True: 
for event in pygame.event.get(): 
if event.type == pygame.QUIT: 
pygame.quit() 
quit() 
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
Triangle() 
pygame.display.flip() 
pygame.time.wait(10) 
main()