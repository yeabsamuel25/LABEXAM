import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    glColor3f(1.0, 1.0, 1.0)  # Set line color to white
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def main():
    # Initialize PyGame
    pygame.init()
    display = (800, 600)
    
    # Set up the PyGame display with an OpenGL context
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Set up the projection (for 2D drawing, we can use an orthographic projection)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, display[0], 0, display[1])
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw a line from (100, 100) to (700, 500)
        draw_line(100, 100, 700, 500)
        
        # Swap the display buffers to show the rendered image
        pygame.display.flip()
        pygame.time.wait(10)
    
    pygame.quit()

if __name__ == "__main__":
    main()
