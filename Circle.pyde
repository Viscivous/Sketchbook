def setup():
  size (1000, 1000)
  x = width/2
  y = height/2
  
x = 0
y = 0
c = 0
xdir = 25
ydir = 10
  

def draw():
  background(255, 255, 255)
  noStroke()
  global x
  global y
  global c
  global xdir
  global ydir          
  
  colorMode(RGB)
  blendMode(SUBTRACT)
  fill(100, 200, 75)
  rect(0, 0, width * 4, height * 4)
  blendMode(BLEND)
  colorMode(RGB)
  circle(x, y, 50)
  x = x+xdir
  y = y+ydir
  c = c+1
  if x > width or x < 0:
      xdir = -xdir
  if y > height or y < 0:
      ydir = -ydir  
  
