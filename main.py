import pygame as g
import sys
from pygame.locals import QUIT
import math

SW = 858
SH = 525

g.init()
screen = g.display.set_mode((SW, SH))
g.display.set_caption('Pong')

rw = 10
rh = 80

bs = 10

px = SW / 2
py = SH / 2
vel = 3
vx = vel
vy = vel

y1 = (SW / 2) - (rh / 2)
x1 = 10

y2 = y1
x2 = (SW - rw) - 10

clock = g.time.Clock()
score1 = 0
score2 = 0

white = (255,255,255)

font = g.font.Font('font.ttf', 32)

def ddl(): # Draw dotted line
  l = []
  for i in range(0, SH, 20):
    l.append(i)
  
  for i in range(0,len(l),3):
    g.draw.line(screen, white, ((SW/2), l[i]), ((SW/2), l[i+1]))

def db():
  g.draw.lines(screen, white, True, ((0,0),(SW,0),(SW,SH),(0,SH)))

def ds():
  text = font.render(str(score1), True, white)
  screen.blit(text, ((SW / 2) - 60, 60))
  text = font.render(str(score2), True, white)
  screen.blit(text, ((SW / 2) + 60, 60))

print("started")

while True:
  for event in g.event.get():
    if event.type == QUIT:
      g.quit()
      sys.exit()

  screen.fill((0,0,0))

  pressed = g.key.get_pressed()

  y1 -= (pressed[g.K_w] - pressed[g.K_s]) * 10
  y1 = max(min(y1,(SH - rh)), 0)
  y2 -= (pressed[g.K_UP] - pressed[g.K_DOWN]) * 10
  y2 = max(min(y2,(SH - rh)), 0)

  p1 = g.Rect(10, y1, rw, rh)
  p2 = g.Rect(x2, y2, rw, rh)

  g.draw.rect(screen, white, p1)
  g.draw.rect(screen, white, p2)

  px += vx
  py += vy

  if py < 0:
    vy = vel
  elif py > SH - bs:
    vy = -vel
  if px < 0:
    px = SW / 2
    score2 += 1
  elif px > SW:
    px = SW / 2
    score1 += 1

  p3 = g.Rect(px - (bs / 2), py - (bs / 2), bs, bs)
  g.draw.rect(screen, white, p3)

  if p3.colliderect(p1):
    vx = vel
  elif p3.colliderect(p2):
    vx = -vel
  
  g.draw.rect(screen, white, p1)

  ds()
  ddl()
  db()

  vel = (math.floor((score1 + score2)/10) * 3) + 3
    
  g.display.flip()
  clock.tick(24)