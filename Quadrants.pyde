def setup():
  size (500, 500)
  
def draw():
  background(200, 200, 200)
  noStroke()
  fill(255, 0, 255)
  if mouseX < width/2 and mouseY < height/2:
    rect(0, 0, width/2, height/2)
  elif mouseX > height/2 and mouseY < height/2:
      fill(31, 81, 255)
      rect(width/2, 0, width/2, height/2)
  elif mouseX > width/2 and mouseY > height/2:
      fill(207, 159, 255)
      rect(width/2, height/2, width/2, height/2)  
  else:
    fill(80, 200, 120)
    rect(0, height/2, width/2, height/2)
