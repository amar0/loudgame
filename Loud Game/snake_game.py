import pygame, sys, time
import random,math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([1300,650])
global player_score
player_score = 0

font = pygame.font.SysFont("monospace",15)
label = font.render("Welcome! to the Loud Game",1,(255,255,255))
result = font.render("The Score : ",1,(255,255,255))

WHITE = (255,255,255)
BLACK = (0,0,0)
width = 1366
height = 768

frame_count = 0
frame_rate = 60
start_time = 90
clock = pygame.time.Clock()

#------------------------------------------------------------------------#

def doRectsOverlap(obj1, obj2):
    for a, b in [(obj1, obj2), (obj2, obj1)]:
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True
    return False

def isPointInsideRect(x, y, obj):
    if (x > obj.left) and (x < obj.right) and (y > obj.top) and (y < obj.bottom):
        return True
    else:
        return False

#------------------------------------------------------------------------#

FPS = 30
fpsClock = pygame.time.Clock()

linkedinImg = pygame.image.load('linkedin.png')
linkedinImg_x1 = random.randint(10,width)
linkedinImg_y1 = random.randint(200,height)
target_radius_linkedinImg = 15

twitterImg = pygame.image.load('twitter.png')
twitterImg_x2 = random.randint(10,width)
twitterImg_y2 = random.randint(200,height)
target_radius_twitterImg = 15

photoshopImg = pygame.image.load('photoshop.png')
photoshopImg_x3 = random.randint(10,width)
photoshopImg_y3 = random.randint(200,height)
target_radius_photoshopImg = 15

windowsImg = pygame.image.load('facebook.png')
windowsImg_x4 = random.randint(10,width)
windowsImg_y4 = random.randint(200,height)
target_radius_windowsImg = 15

googleImg = pygame.image.load('google+.png')
googleImg_x5 = random.randint(10,width)
googleImg_y5 = random.randint(200,height)
target_radius_googleImg = 15

adobeImg = pygame.image.load('adobe.png')
adobeImg_x6 = random.randint(10,width)
adobeImg_y6 = random.randint(200,height)
target_radius_adobeImg = 15

telegramImg = pygame.image.load('telegram.png')
telegramImg_x7 = random.randint(5,width)
telegramImg_y7 = random.randint(200,height)
target_radius_telegramImg = 15

#--------------------------------------------------------------#

DISPLAYSURF = pygame.display.set_mode((width,height),RESIZABLE)
pygame.display.set_caption('Loud Game')
bgImg = pygame.image.load('mywall.png')

lcImg = pygame.image.load('loudchilli.png')
lcx = 10
lcy = 10

#--------------------------------------------------------------#

#snake_x = 15
#snake_y = 13
snake_x = 10
snake_y = 10
snake_color = (0,0,0)
snake_radius = 13
direction = "right"
speed = 10
target_x = random.randint(5,width)
target_y = random.randint(5,height)
target_radius = 13

#--------------------------------------------------------------#

def new_target_location():
    global target_x,target_y,linkedinImg_x1,linkedinImg_y1,twitterImg_x2,twitterImg_y2,photoshopImg_x3,photoshopImg_y3,windowsImg_x4,windowsImg_y4,googleImg_x5,googleImg_y5,adobeImg_x6,adobeImg_y6,telegramImg_x7,telegramImg_y7
    target_x = random.randint(1,width)
    target_y = random.randint(1,height)
    
    linkedinImg_x1 = random.randint(20,width)
    linkedinImg_y1 = random.randint(200,height)

    twitterImg_x2 = random.randint(20,width)
    twitterImg_y2 = random.randint(200,height)

    photoshopImg_x3 = random.randint(20,width)
    photoshopImg_y3 = random.randint(200,height)

    windowsImg_x4 = random.randint(20,width)
    windowsImg_y4 = random.randint(200,height)

    googleImg_x5 = random.randint(20,width)
    googleImg_y5 = random.randint(200,height)

    adobeImg_x6 = random.randint(20,width)
    adobeImg_y6 = random.randint(200,height)

    telegramImg_x7 = random.randint(20,width)
    telegramImg_y7 = random.randint(200,height)

#--------------------------------------------------------------#

running = True
#player_score = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #---------------Timer------------------#            
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, (255,255,255))
    frame_count += 2
    clock.tick(frame_rate)
    #---------------------------------------#
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            lcx -= 10
            snake_x -= speed
        if event.key == pygame.K_RIGHT:
            lcx += 10
            snake_x += speed
        if event.key == pygame.K_UP:
            lcy -= 10
            snake_y -= speed
        if event.key == pygame.K_DOWN:
            lcy += 10
            snake_y += speed

    #DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(bgImg, (0,0))
    DISPLAYSURF.blit(lcImg, (lcx, lcy))
    
    pygame.draw.circle(DISPLAYSURF, snake_color, [snake_x,snake_y], snake_radius)
    pygame.draw.line(DISPLAYSURF,WHITE,(200,100),(1120,100))

    DISPLAYSURF.blit(linkedinImg,(linkedinImg_x1,linkedinImg_y1))
    DISPLAYSURF.blit(twitterImg,(twitterImg_x2,twitterImg_y2))
    DISPLAYSURF.blit(photoshopImg,(photoshopImg_x3,photoshopImg_y3))
    DISPLAYSURF.blit(windowsImg,(windowsImg_x4,windowsImg_y4))
    DISPLAYSURF.blit(googleImg,(googleImg_x5,googleImg_y5))
    DISPLAYSURF.blit(adobeImg,(adobeImg_x6,adobeImg_y6))
    DISPLAYSURF.blit(telegramImg,(telegramImg_x7,telegramImg_y7))
    DISPLAYSURF.blit(label,(520,80))
    DISPLAYSURF.blit(result,(1000,80))
    DISPLAYSURF.blit(text, [200, 80])

    snake_rect = pygame.Rect(snake_x-snake_radius, snake_y-snake_radius, snake_radius*2,snake_radius*2)    
    target_rect1 = pygame.Rect(linkedinImg_x1-target_radius_linkedinImg,linkedinImg_y1-target_radius_linkedinImg,target_radius_linkedinImg*2,target_radius_linkedinImg*2)
    target_rect2 = pygame.Rect(twitterImg_x2-target_radius_twitterImg,twitterImg_y2-target_radius_twitterImg,target_radius_twitterImg*2,target_radius_twitterImg*2)
    target_rect3 = pygame.Rect(photoshopImg_x3-target_radius_photoshopImg,photoshopImg_y3-target_radius_photoshopImg,target_radius_photoshopImg*2,target_radius_photoshopImg*2)
    target_rect4 = pygame.Rect(windowsImg_x4-target_radius_windowsImg,windowsImg_y4-target_radius_windowsImg,target_radius_windowsImg*2,target_radius_windowsImg*2)
    target_rect5 = pygame.Rect(googleImg_x5-target_radius_googleImg,googleImg_y5-target_radius_googleImg,target_radius_googleImg*2,target_radius_googleImg*2)
    target_rect6 = pygame.Rect(adobeImg_x6-target_radius_adobeImg,adobeImg_y6-target_radius_adobeImg,target_radius_adobeImg*2,target_radius_adobeImg*2)
    target_rect7 = pygame.Rect(telegramImg_x7-target_radius_telegramImg,telegramImg_y7-target_radius_telegramImg,target_radius_telegramImg*2,target_radius_telegramImg*2)
    
    if doRectsOverlap(snake_rect,target_rect1):
        player_score += 1
        result = font.render("The Score : "+str(player_score),1,(255,255,255))
        new_target_location()
        
    elif doRectsOverlap(snake_rect,target_rect2):
        player_score += 1
        result = font.render("The Score : "+str(player_score),1,(255,255,255))
        new_target_location()
        
    elif doRectsOverlap(snake_rect,target_rect3):
        player_score += 1
        result = font.render("The Score : "+str(player_score),1,(255,255,255))
        new_target_location()
        
    elif doRectsOverlap(snake_rect,target_rect4):
        player_score += 1
        result = font.render("The Score : "+str(player_score),1,(255,255,255))
        new_target_location()
        
    elif doRectsOverlap(snake_rect,target_rect5):
        player_score += 1
        result = font.render("The Score : "+str(player_score),1,(255,255,255))
        new_target_location()
        
    elif doRectsOverlap(snake_rect,target_rect6):
        player_score += 1
        result = font.render("The Score : "+str(player_score),1,(255,255,255))
        new_target_location()
        
    elif doRectsOverlap(snake_rect,target_rect7):
        player_score += 1
        result = font.render("The Score : "+str(player_score),1,(255,255,255))
        new_target_location()

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
