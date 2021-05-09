import pygame
import os
import math
from math import sqrt
import numpy as np 
# import sys

# def resource_path(relative_path):
#     try:
#     # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)
faces2 = [[12,4,5,13],[12,4,0,8],[13,5,1,9],[0,1,9,8]]

faces3 = [[7,6,14,15],[7,15,11,3],[3,11,10,2],[2,10,14,6]]
os.environ["SDL_VIDEO_CENTERED"]='1'
black, white, blue  = (20, 20, 20), (230, 230, 230), (130, 182, 217)
width, height = 1920, 1080

pygame.init()
pygame.display.set_caption("3D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
black = (0,0,0)
grey = (20,20,20)
green = (0,200 ,0)
red, sgreen, blue = (239, 134, 119), (160, 231, 125), (130, 182, 217)
colors=[blue,red,sgreen]


# faces = np.array([[1, 2, 4, 3], [1, 2, 6, 5], [1, 2, 10, 9], [1, 3, 7, 5, 0], [1, 3, 11, 9, 0], [1, 5, 13, 9, 0],
# [2, 4, 8, 6], [2, 4, 12, 10], [2, 6, 14, 10], [3, 4, 8, 7], [3, 4, 12, 11], [3, 7, 15, 11, 0],
# [4, 8, 16, 12], [5, 6, 8, 7], [5, 6, 14, 13], [5, 7, 15, 13, 0], [6, 8, 16, 14], [7, 8, 16, 15],
# [9, 10, 12, 11], [9, 10, 14, 13], [9, 11, 15, 13, 0], [10, 12, 16, 14], [11, 12, 16, 15],
# [13, 14, 16, 15]])

# faces = np.array([[1, 2, 4, 3, 1], [1, 2, 6, 5, 1], [1, 2, 10, 9, 1], [1, 3, 7, 5, 2], [1, 3, 11, 9, 2], [1, 5, 13, 9, 2],
# [2, 4, 8, 6, 3], [2, 4, 12, 10, 3], [2, 6, 14, 10, 3], [3, 4, 8, 7, 1], [3, 4, 12, 11, 1], [3, 7, 15, 11, 2],
# [4, 8, 16, 12, 3], [5, 6, 8, 7, 1], [5, 6, 14, 13, 1], [5, 7, 15, 13, 2], [6, 8, 16, 14, 3], [7, 8, 16, 15, 1],
# [9, 10, 12, 11, 1], [9, 10, 14, 13, 1], [9, 11, 15, 13, 2], [10, 12, 16, 14, 3], [11, 12, 16, 15, 1],
# [13, 14, 16, 15, 1]])

# faces -= 1
twenty_four_cells_vertices = [[1/2, 1/2, 1/2, -1/2],
 [1/2, 1/2, 1/2, 1/2],
 [1/2, 1/2, -1/2, 1/2],
 [1, 0, 0, 0],
 [1/2, -1/2, 1/2, 1/2],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1],
 [-1/2, 1/2, 1/2, 1/2],
 [1/2, 1/2, -1/2, -1/2],
 [1/2, -1/2, 1/2, -1/2],
 [0, 0, 0, -1],
 [-1/2, 1/2, 1/2, -1/2],
 [1/2, -1/2, -1/2, 1/2],
 [0, 0, -1, 0],
 [-1/2, 1/2, -1/2, 1/2],
 [1/2, -1/2, -1/2, -1/2],
 [-1/2, 1/2, -1/2, -1/2],
 [0, -1, 0, 0],
 [-1/2, -1/2, 1/2, 1/2],
 [-1/2, -1/2, 1/2, -1/2],
 [-1/2, -1/2, -1/2, 1/2],
 [-1/2, -1/2, -1/2, -1/2],
 [-1, 0, 0, 0]]

twenty_four_cell_edges = [((-1, 0, 0, 0), (-1/2, -1/2, -1/2, -1/2)),
 ((-1, 0, 0, 0), (-1/2, -1/2, -1/2, 1/2)),
 ((-1, 0, 0, 0), (-1/2, -1/2, 1/2, -1/2)),
 ((-1, 0, 0, 0), (-1/2, -1/2, 1/2, 1/2)),
 ((-1, 0, 0, 0), (-1/2, 1/2, -1/2, -1/2)),
 ((-1, 0, 0, 0), (-1/2, 1/2, -1/2, 1/2)),
 ((-1, 0, 0, 0), (-1/2, 1/2, 1/2, -1/2)),
 ((-1, 0, 0, 0), (-1/2, 1/2, 1/2, 1/2)),
 ((-1/2, -1/2, -1/2, -1/2), (-1/2, -1/2, -1/2, 1/2)),
 ((-1/2, -1/2, -1/2, -1/2), (-1/2, -1/2, 1/2, -1/2)),
 ((-1/2, -1/2, -1/2, -1/2), (-1/2, 1/2, -1/2, -1/2)),
 ((-1/2, -1/2, -1/2, -1/2), (0, -1, 0, 0)),
 ((-1/2, -1/2, -1/2, -1/2), (0, 0, -1, 0)),
 ((-1/2, -1/2, -1/2, -1/2), (0, 0, 0, -1)),
 ((-1/2, -1/2, -1/2, -1/2), (1/2, -1/2, -1/2, -1/2)),
 ((-1/2, -1/2, -1/2, 1/2), (-1/2, -1/2, 1/2, 1/2)),
 ((-1/2, -1/2, -1/2, 1/2), (-1/2, 1/2, -1/2, 1/2)),
 ((-1/2, -1/2, -1/2, 1/2), (0, -1, 0, 0)),
 ((-1/2, -1/2, -1/2, 1/2), (0, 0, -1, 0)),
 ((-1/2, -1/2, -1/2, 1/2), (0, 0, 0, 1)),
 ((-1/2, -1/2, -1/2, 1/2), (1/2, -1/2, -1/2, 1/2)),
 ((-1/2, -1/2, 1/2, -1/2), (-1/2, -1/2, 1/2, 1/2)),
 ((-1/2, -1/2, 1/2, -1/2), (-1/2, 1/2, 1/2, -1/2)),
 ((-1/2, -1/2, 1/2, -1/2), (0, -1, 0, 0)),
 ((-1/2, -1/2, 1/2, -1/2), (0, 0, 0, -1)),
 ((-1/2, -1/2, 1/2, -1/2), (0, 0, 1, 0)),
 ((-1/2, -1/2, 1/2, -1/2), (1/2, -1/2, 1/2, -1/2)),
 ((-1/2, -1/2, 1/2, 1/2), (-1/2, 1/2, 1/2, 1/2)),
 ((-1/2, -1/2, 1/2, 1/2), (0, -1, 0, 0)),
 ((-1/2, -1/2, 1/2, 1/2), (0, 0, 0, 1)),
 ((-1/2, -1/2, 1/2, 1/2), (0, 0, 1, 0)),
 ((-1/2, -1/2, 1/2, 1/2), (1/2, -1/2, 1/2, 1/2)),
 ((-1/2, 1/2, -1/2, -1/2), (-1/2, 1/2, -1/2, 1/2)),
 ((-1/2, 1/2, -1/2, -1/2), (-1/2, 1/2, 1/2, -1/2)),
 ((-1/2, 1/2, -1/2, -1/2), (0, 0, -1, 0)),
 ((-1/2, 1/2, -1/2, -1/2), (0, 0, 0, -1)),
 ((-1/2, 1/2, -1/2, -1/2), (0, 1, 0, 0)),
 ((-1/2, 1/2, -1/2, -1/2), (1/2, 1/2, -1/2, -1/2)),
 ((-1/2, 1/2, -1/2, 1/2), (-1/2, 1/2, 1/2, 1/2)),
 ((-1/2, 1/2, -1/2, 1/2), (0, 0, -1, 0)),
 ((-1/2, 1/2, -1/2, 1/2), (0, 0, 0, 1)),
 ((-1/2, 1/2, -1/2, 1/2), (0, 1, 0, 0)),
 ((-1/2, 1/2, -1/2, 1/2), (1/2, 1/2, -1/2, 1/2)),
 ((-1/2, 1/2, 1/2, -1/2), (-1/2, 1/2, 1/2, 1/2)),
 ((-1/2, 1/2, 1/2, -1/2), (0, 0, 0, -1)),
 ((-1/2, 1/2, 1/2, -1/2), (0, 0, 1, 0)),
 ((-1/2, 1/2, 1/2, -1/2), (0, 1, 0, 0)),
 ((-1/2, 1/2, 1/2, -1/2), (1/2, 1/2, 1/2, -1/2)),
 ((-1/2, 1/2, 1/2, 1/2), (0, 0, 0, 1)),
 ((-1/2, 1/2, 1/2, 1/2), (0, 0, 1, 0)),
 ((-1/2, 1/2, 1/2, 1/2), (0, 1, 0, 0)),
 ((-1/2, 1/2, 1/2, 1/2), (1/2, 1/2, 1/2, 1/2)),
 ((0, -1, 0, 0), (1/2, -1/2, -1/2, -1/2)),
 ((0, -1, 0, 0), (1/2, -1/2, -1/2, 1/2)),
 ((0, -1, 0, 0), (1/2, -1/2, 1/2, -1/2)),
 ((0, -1, 0, 0), (1/2, -1/2, 1/2, 1/2)),
 ((0, 0, -1, 0), (1/2, -1/2, -1/2, -1/2)),
 ((0, 0, -1, 0), (1/2, -1/2, -1/2, 1/2)),
 ((0, 0, -1, 0), (1/2, 1/2, -1/2, -1/2)),
 ((0, 0, -1, 0), (1/2, 1/2, -1/2, 1/2)),
 ((0, 0, 0, -1), (1/2, -1/2, -1/2, -1/2)),
 ((0, 0, 0, -1), (1/2, -1/2, 1/2, -1/2)),
 ((0, 0, 0, -1), (1/2, 1/2, -1/2, -1/2)),
 ((0, 0, 0, -1), (1/2, 1/2, 1/2, -1/2)),
 ((0, 0, 0, 1), (1/2, -1/2, -1/2, 1/2)),
 ((0, 0, 0, 1), (1/2, -1/2, 1/2, 1/2)),
 ((0, 0, 0, 1), (1/2, 1/2, -1/2, 1/2)),
 ((0, 0, 0, 1), (1/2, 1/2, 1/2, 1/2)),
 ((0, 0, 1, 0), (1/2, -1/2, 1/2, -1/2)),
 ((0, 0, 1, 0), (1/2, -1/2, 1/2, 1/2)),
 ((0, 0, 1, 0), (1/2, 1/2, 1/2, -1/2)),
 ((0, 0, 1, 0), (1/2, 1/2, 1/2, 1/2)),
 ((0, 1, 0, 0), (1/2, 1/2, -1/2, -1/2)),
 ((0, 1, 0, 0), (1/2, 1/2, -1/2, 1/2)),
 ((0, 1, 0, 0), (1/2, 1/2, 1/2, -1/2)),
 ((0, 1, 0, 0), (1/2, 1/2, 1/2, 1/2)),
 ((1/2, -1/2, -1/2, -1/2), (1/2, -1/2, -1/2, 1/2)),
 ((1/2, -1/2, -1/2, -1/2), (1/2, -1/2, 1/2, -1/2)),
 ((1/2, -1/2, -1/2, -1/2), (1/2, 1/2, -1/2, -1/2)),
 ((1/2, -1/2, -1/2, -1/2), (1, 0, 0, 0)),
 ((1/2, -1/2, -1/2, 1/2), (1/2, -1/2, 1/2, 1/2)),
 ((1/2, -1/2, -1/2, 1/2), (1/2, 1/2, -1/2, 1/2)),
 ((1/2, -1/2, -1/2, 1/2), (1, 0, 0, 0)),
 ((1/2, -1/2, 1/2, -1/2), (1/2, -1/2, 1/2, 1/2)),
 ((1/2, -1/2, 1/2, -1/2), (1/2, 1/2, 1/2, -1/2)),
 ((1/2, -1/2, 1/2, -1/2), (1, 0, 0, 0)),
 ((1/2, -1/2, 1/2, 1/2), (1/2, 1/2, 1/2, 1/2)),
 ((1/2, -1/2, 1/2, 1/2), (1, 0, 0, 0)),
 ((1/2, 1/2, -1/2, -1/2), (1/2, 1/2, -1/2, 1/2)),
 ((1/2, 1/2, -1/2, -1/2), (1/2, 1/2, 1/2, -1/2)),
 ((1/2, 1/2, -1/2, -1/2), (1, 0, 0, 0)),
 ((1/2, 1/2, -1/2, 1/2), (1/2, 1/2, 1/2, 1/2)),
 ((1/2, 1/2, -1/2, 1/2), (1, 0, 0, 0)),
 ((1/2, 1/2, 1/2, -1/2), (1/2, 1/2, 1/2, 1/2)),
 ((1/2, 1/2, 1/2, -1/2), (1, 0, 0, 0)),
 ((1/2, 1/2, 1/2, 1/2), (1, 0, 0, 0))]

twenty_four_cells_tuples = [tuple(item) for item in twenty_four_cells_vertices]
vertices_id = dict(zip(twenty_four_cells_tuples, range( len(twenty_four_cells_vertices))))
edges_id = [] 
for vertex1, vertex2 in twenty_four_cell_edges: 
    edges_id.append((vertices_id[vertex1], vertices_id[vertex2]))
points = [[[int(2*x)], [int(2*y)], [int(2*z)], [int(2*w)]] for [x, y, z, w] in twenty_four_cells_vertices]


global xy,xz,xw,yw,yz,zw
xy,xz,xw,yw,yz,zw = False,False,False,False,False,False

angle = 0.01
cube_position = [width//2, (height//2)-150]
scale = 2500
speed = 0.01


def kee (x):
    sum = 0
    for k in x:
        w = 1/(5 - points[k][2][0])
        sum+=(points[k][1][0])*w
    return sum

def connect_point(i, j, k, offset, color):
    a = k[i + offset]
    b = k[j + offset]
    pygame.draw.line(screen, color, (a[0], a[1]), (b[0], b[1]), 2)
def surface(x,y,z,w,color,projected_points):
    pygame.draw.polygon(screen,color,[projected_points[x],projected_points[y],projected_points[z],projected_points[w]])

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global xy,xz,xw,yw,yz,zw
    on = False
    if msg == "xy":
        if xy: on = True
    elif msg == "xz":
        if xz : on = True
    elif msg == "xw":
        if xw: on = True
    elif msg == "yz":
        if yz: on = True
    elif msg == "yw":
        if yw: on = True
    elif msg =="zw":
        if zw: on = True
    if on:
        pygame.draw.circle(screen,green,(x+w+10,y+h/2), 5)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0]:
            if msg == "xy":
                xy = not xy
            elif msg == "xz":
                xz = not xz
            elif msg == "xw":
                xw = not xw
            elif msg == "yz":
                yz = not yz
            elif msg == "yw":
                yw = not yw
            elif msg =="zw":
                zw = not zw
            pygame.draw.circle(screen,green,(x+w+10,y+h/2), 5)
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    font = pygame.font.SysFont("comicsansms", 20)
    img = font.render(msg, True, green)
    rect = img.get_rect()
    rect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(img,rect)


    # mouse = pygame.mouse.get_pos()

    # if x+w > mouse[0] > x and y+h > mouse[1] > y:
    #     pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    # else:
    #     pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    # smallText = pygame.font.Font("freesansbold.ttf",20)
    # textSurf, textRect = text_objects(msg, smallText)
    # textRect.center = ( (x+(w/2)), (y+(h/2)) )
    # gameDisplay.blit(textSurf, textRect)

run = True
while run:
    clock.tick(fps)
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    index = 0
    projected_points = [j for j in range(len(points))]
    
    #3d matrix rotations
    rotation_x = np.array([[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]])

    rotation_y = np.array([[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]])

    rotation_z = np.array([[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle), 0],
                  [0, 0 ,1]])
    tesseract_rotation = np.array([[1, 0, 0],
                          [0, math.cos(-math.pi/2), -math.sin(-math.pi/2)],
                          [0, math.sin(-math.pi/2), math.cos(-math.pi/2)]])
    #4d matrix rotations

    rotation4d_xy= np.array([[math.cos(angle), -math.sin(angle), 0, 0],
                  [math.sin(angle), math.cos(angle), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    rotation4d_xz = np.array([[math.cos(angle), 0, -math.sin(angle), 0],
                     [0, 1, 0, 0],
                     [math.sin(angle), 0, math.cos(angle), 0],
                     [0, 0, 0, 1]])
    rotation4d_xw = np.array([[math.cos(angle), 0, 0, -math.sin(angle)],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [math.sin(angle), 0, 0, math.cos(angle)]])
    rotation4d_yz = np.array([[1, 0, 0, 0],
                     [0, math.cos(angle), -math.sin(angle), 0],
                     [0, math.sin(angle), math.cos(angle), 0],
                     [0, 0, 0, 1]])
    rotation4d_yw = np.array([[1, 0, 0, 0],
                     [0, math.cos(angle), 0, -math.sin(angle)],
                     [0, 0, 1, 0],
                     [0, math.sin(angle), 0, math.cos(angle)]])
    rotation4d_zw = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, math.cos(angle), -math.sin(angle)],
                     [0, 0, math.sin(angle), math.cos(angle)]])
   
    for i, point in enumerate(points):
        rotated_3d = point
        if(xy):
            rotated_3d = np.matmul(rotation4d_xy, rotated_3d)
        if(xz):
            rotated_3d = np.matmul(rotation4d_xz, rotated_3d)
        if(xw):
            rotated_3d = np.matmul(rotation4d_xw, rotated_3d)
        if(yz):
            rotated_3d = np.matmul(rotation4d_yz, rotated_3d)
        if(yw):
            rotated_3d = np.matmul(rotation4d_yw, rotated_3d)
        if(zw):
            rotated_3d = np.matmul(rotation4d_zw, rotated_3d)
        points[i] = rotated_3d
        

        distance = 5
        w = 1/(distance - rotated_3d[3][0])
        projection_matrix4 = np.array([[w, 0, 0, 0],
                            [0, w, 0, 0],
                            [0, 0, w, 0]])

        projected_3d = np.matmul(projection_matrix4, rotated_3d)
        rotated_2d =  np.matmul(tesseract_rotation, projected_3d)
        z = 1/(distance - (rotated_2d[2][0] + rotated_3d[3][0]))
        projection_matrix = np.array([[z, 0, 0],
                            [0, z, 0 ]])

        #rotated_2d = matrix_multiplication(rotation_x, projected_3d)
        projected_2d = np.matmul(projection_matrix, rotated_2d)
        x = int(projected_2d[0][0] * scale) + cube_position[0]
        y = int(projected_2d[1][0] * scale) + cube_position[1]
        # projected_points[index] = [int(projected_2d[0][0] * scale), int(projected_2d[1][0] * scale)]
        projected_points[index] = [x, y]
        index += 1
    
    
    
    
    # below comments in terms of initial orientation
    # front back mini
    
    
    # draw edges
    # for m in range(4):
    #     connect_point(m, (m+1)%4, projected_points, 8, grey)
    #     connect_point(m+4, (m+1)%4 + 4, projected_points, 8, grey)
    #     connect_point(m, m+4, projected_points, 8, grey)

    # for m in range(4):
    #     connect_point(m, (m+1)%4, projected_points, 0, grey)
    #     connect_point(m+4, (m+1)%4 + 4, projected_points, 0, grey)
    #     connect_point(m, m+4, projected_points, 0, grey)

    # for m in range(8):
    #     connect_point(m,  m+8, projected_points, 0, grey)
    for i,(vertex1, vertex2) in enumerate(edges_id): 
        connect_point(vertex1, vertex2, projected_points,0,colors[i%len(colors)])
    for i,m in enumerate(projected_points):
        x,y = m
        pygame.draw.circle(screen, black, (x, y), 15)
        font = pygame.font.SysFont("comicsansms", 20)
        img = font.render(str(i+1), True, green)
        rect = img.get_rect()
        rect.center = (x,y)
        screen.blit(img,rect)
    
    
    # surface(8,9,13,12,red,projected_points)
    # surface(10,11,15,14,red,projected_points)

    # # left right mini
    # surface(8,11,15,12,red,projected_points)
    # surface(9,10,14,13,red,projected_points)

    # # top bottom mini
    # surface(8,11,10,9,red,projected_points)
    # surface(12,15,14,13,red,projected_points)

    # # front back big
    # surface(0,1,5,4,blue,projected_points)
    # surface(2,3,7,6,blue,projected_points)

    # top bottom big
    # surface(0,3,2,1,blue,projected_points)
    # surface(4,7,6,5,blue,projected_points)

    # # left right big
    # surface(0,3,7,4,blue,projected_points)
    # surface(1,2,6,5,blue,projected_points)
    
    
   
    button ("xy" , 300,100,60,40,grey,black)
    button ("xz" , 300,200,60,40,grey,black)
    button ("xw" , 300,300,60,40,grey,black)
    button ("yz" , 300,400,60,40,grey,black)
    button ("yw" , 300,500,60,40,grey,black)
    button ("zw" , 300,600,60,40,grey,black)
    
    
#      x,y,width, height
#     x,y x,z xw yz yw zw 
    
    
    
    
    
#     print(mouse)
    
    
    pygame.display.update()

pygame.quit()