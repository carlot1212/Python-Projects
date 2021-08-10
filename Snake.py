
import pygame
import random
import time

pygame.init()

screenWidth = 720
screenHeight = 720
menu = True
run = True
game = False
multiplayer = False
pause = False
freeze = False
freeze2 = False

menuBG = pygame.image.load("MenuScreen.png")
menuImage = pygame.image.load("Menu.png")
multiplayerImage = pygame.image.load("Multiplayer.png")
singleplayerImage = pygame.image.load("Singleplayer.png")
playImage = pygame.image.load("Play.png")
quitImage = pygame.image.load("Quit.png")
restartImage = pygame.image.load("Restart.png")
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

class button():
   def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

   def draw(self, window):
      window.blit(self.image, (self.x, self.y))

   def isOver(self, pos):
      if mouse[0] > self.x and mouse[0] < self.x + self.width:
         if mouse[1] > self.y and mouse[1] < self.y + self.height:
            return True
      return False

class snake():
   headImage1 = [pygame.image.load("Head1.png"), pygame.image.load("Head2.png"), pygame.image.load("Head3.png"), pygame.image.load("Head4.png")]
   headImage2 = [pygame.image.load("Head5.png"), pygame.image.load("Head6.png"), pygame.image.load("Head7.png"), pygame.image.load("Head8.png")]
   bodyImage1 = pygame.image.load("Body1.png")
   bodyImage2 = pygame.image.load("Body2.png")
   eatSound = pygame.mixer.Sound("Eat.wav")

   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.length = 3
      self.width = 8
      self.height = 8
      self.speed = 8
      self.right = True
      self.left = False
      self.up = False
      self.down = False
      self.body = [((self.x - self.width), self.y), ((self.x - (2 * self.width)), self.y)]

   def draw(self, window, snake):
      global freeze
      global freeze2
      if snake == 1:
         if self.right == True:
            window.blit(self.headImage1[1], (self.x, self.y))
            if freeze == False:
               self.body.pop(self.length - 2)
               self.body.insert(0, (self.x - self.width, self.y))
               if pause == True:
                  freeze = True
         elif self.left == True:
            window.blit(self.headImage1[3], (self.x, self.y))
            if freeze == False:
               self.body.pop(self.length - 2)
               self.body.insert(0, (self.x + self.width, self.y))
               if pause == True:
                   freeze = True
         elif self.up == True:
            window.blit(self.headImage1[0], (self.x, self.y))
            if freeze == False:
               self.body.pop(self.length - 2)
               self.body.insert(0, (self.x, self.y + self.height))
               if pause == True:
                   freeze = True
         elif self.down == True:
            window.blit(self.headImage1[2], (self.x, self.y))
            if freeze == False:
               self.body.pop(self.length - 2)
               self.body.insert(0, (self.x, self.y - self.height))
               if pause == True:
                   freeze = True
         for i in range(self.length):
            window.blit(self.bodyImage1, self.body[i - 1])

      if snake == 2:
         if self.right == True:
             window.blit(self.headImage2[1], (self.x, self.y))
             if freeze2 == False:
                self.body.pop(self.length - 2)
                self.body.insert(0, (self.x - self.width, self.y))
                if pause == True:
                   freeze2 = True
         elif self.left == True:
             window.blit(self.headImage2[3], (self.x, self.y))
             if freeze2 == False:
                self.body.pop(self.length - 2)
                self.body.insert(0, (self.x + self.width, self.y))
                if pause == True:
                   freeze2 = True
         elif self.up == True:
             window.blit(self.headImage2[0], (self.x, self.y))
             if freeze2 == False:
                self.body.pop(self.length - 2)
                self.body.insert(0, (self.x, self.y + self.height))
                if pause == True:
                   freeze2 = True
         elif self.down == True:
             window.blit(self.headImage2[2], (self.x, self.y))
             if freeze2 == False:
                self.body.pop(self.length - 2)
                self.body.insert(0, (self.x, self.y - self.height))
                if pause == True:
                   freeze2 = True
         for i in range(self.length):
            window.blit(self.bodyImage2, self.body[i - 1])
      

   def eat(self):
      self.eatSound.play()
      if self.body[self.length - 2][0] < self.body[self.length - 3][0]:
         self.body.append((self.body[self.length - 2][0] - self.width, self.body[self.length - 2][1]))
      elif self.body[self.length - 2][0] > self.body[self.length - 3][0]:
         self.body.append((self.body[self.length - 2][0] + self.width, self.body[self.length - 2][1]))
      elif self.body[self.length - 2][1] < self.body[self.length - 3][1]:
         self.body.append((self.body[self.length - 2][0], self.body[self.length - 2][1] - self.height))
      elif self.body[self.length - 2][1] > self.body[self.length - 3][1]:
         self.body.append((self.body[self.length - 2][0] - self.width, self.body[self.length - 2][1], + self.height))

      self.length += 1


   def hit(self):
       font1 = pygame.font.SysFont("comicsans", 50)
       text = font1.render("Game Over. Score: " + str(snake1.length), 1, (255, 0, 0))
       window.blit(text, ((screenWidth // 2) - (text.get_width() // 2), (screenHeight // 2) - (text.get_height() // 2)))
       pygame.display.update()
       time.sleep(5)



class food():   
   foodIcon = pygame.image.load("Food.png")

   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.width = 8
      self.height = 8
      self.eaten = False

   def draw(self, window):
      window.blit(self.foodIcon, (self.x, self.y))

def drawGameWindow():
   bg = pygame.draw.rect(window, (0, 0, 0), (0, 0, screenHeight, screenWidth))
   score = font.render("Length: " + str(snake1.length), 1, (200,0,55))
   window.blit(score, (580, 10))
   snake1.draw(window, 1)
   food1.draw(window)
   if multiplayer == True:
      snake2.draw(window, 2)
   menuButton.draw(window)
   pygame.display.update()

font = pygame.font.SysFont("comicsans", 30)
menuButton = button(0, 0, 72, 77, menuImage)
singleplayerButton = button(170, 500, 72, 77, singleplayerImage)
multiplayerButton = button(320, 500, 72, 77, multiplayerImage)
quitButton = button(470, 500, 72, 77, quitImage)
playButton = button(170, 500, 72, 77, playImage)
restartButton = button(320, 500, 72, 77, restartImage)

def drawMainMenu():
    bg = pygame.draw.rect(window, (0, 0, 0), (0, 0, screenHeight, screenWidth))
    window.blit(menuBG, (160, 140))
    singleplayerButton.draw(window)
    multiplayerButton.draw(window)
    quitButton.draw(window)
    pygame.display.update()

def drawPauseMenu():
   bg = pygame.draw.rect(window, (0, 0, 0), (0, 0, screenHeight, screenWidth))
   score = font.render("Length: " + str(snake1.length), 1, (200,0,55))
   window.blit(score, (580, 10))
   snake1.draw(window, 1)
   food1.draw(window)
   if multiplayer == True:
      snake2.draw(window, 2)
   playButton.draw(window)
   restartButton.draw(window)
   quitButton.draw(window)
   pygame.display.update()




while run == True:

   keys = pygame.key.get_pressed()
   mouse = pygame.mouse.get_pos()

   if menu == True:
      drawMainMenu()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
            if singleplayerButton.isOver(mouse) == True:
               menu = False
               game = True
               snake1 = snake(screenWidth // 2, screenHeight // 2)
               foodX = random.randint(0, 90) * 8
               foodY = random.randint(5, 90) * 8 
               food1 = food(foodX, foodY)
            elif multiplayerButton.isOver(mouse) == True:
               menu = False
               game = True
               multiplayer = True
               snake1 = snake(screenWidth // 4 * 3, screenHeight // 2)
               snake2 = snake(screenWidth // 4, screenHeight // 2)
               foodX = random.randint(0, 90) * 8
               foodY = random.randint(5, 90) * 8 
               food1 = food(foodX, foodY)
            elif quitButton.isOver(mouse) == True:
               menu = False
               run = False
   if pause == True:
      drawPauseMenu()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
            if playButton.isOver(mouse) == True:
               pause = False
               game = True
               freeze = False
               freeze2 = False
            elif restartButton.isOver(mouse) == True:
               del snake1
               snake1 = snake(screenWidth // 2, screenHeight // 2)
               foodX = random.randint(0, 90) * 8
               foodY = random.randint(5, 90) * 8 
               food1 = food(foodX, foodY)
               if multiplayer == True:
                  del snake2
                  snake2 = snake(screenWidth // 4, screenHeight // 2)
               pause = False
               game = True
               freeze = False
               freeze2 = False
            elif quitButton.isOver(mouse) == True:
               pause = False
               menu = True

   while game == True:

      clock.tick(20)

      keys = pygame.key.get_pressed()
      mouse = pygame.mouse.get_pos()

      if food1.eaten == True:
         food1.x = random.randint(0, 90) * 8
         food1.y = random.randint(5, 90) * 8
         food1.eaten = False

      if snake1.x == food1.x and snake1.y == food1.y:
         snake1.eat()
         food1.eaten = True

      if snake1.x < 0 or snake1.x >= 720 or snake1.y < 0 or snake1.y >= 720:
         snake1.hit()

      for i in snake1.body:
         if snake1.x == i[0] and snake1.y == i[1]:
            snake1.hit()

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
            if menuButton.isOver(mouse) == True:
               menu = False
               game = False
               pause = True
       
      if keys[pygame.K_RIGHT] and snake1.left == False:
         snake1.right = True
         snake1.left = False
         snake1.up = False
         snake1.down = False
      
      elif keys[pygame.K_LEFT] and snake1.right == False:
         snake1.right = False
         snake1.left = True
         snake1.up = False
         snake1.down = False

      elif keys[pygame.K_UP] and snake1.down == False:
         snake1.right = False
         snake1.left = False
         snake1.up = True
         snake1.down = False

      elif keys[pygame.K_DOWN] and snake1.up == False:
         snake1.right = False
         snake1.left = False
         snake1.up = False
         snake1.down = True

      if snake1.right == True:
         snake1.x += snake1.speed

      elif snake1.left == True:
          snake1.x -= snake1.speed

      elif snake1.up == True:
          snake1.y -= snake1.speed

      elif snake1.down == True:
          snake1.y += snake1.speed

      if multiplayer == True:
         if keys[pygame.K_d] and snake2.left == False:
            snake2.right = True
            snake2.left = False
            snake2.up = False
            snake2.down = False
         
         if keys[pygame.K_a] and snake2.right == False:
            snake2.right = False
            snake2.left = True
            snake2.up = False
            snake2.down = False

         elif keys[pygame.K_w] and snake2.down == False:
            snake2.right = False
            snake2.left = False
            snake2.up = True
            snake2.down = False
         
         elif keys[pygame.K_s] and snake2.up == False:
            snake2.right = False
            snake2.left = False
            snake2.up = False
            snake2.down = True

         if snake2.right == True:
            snake2.x += snake2.speed

         elif snake2.left == True:
            snake2.x -= snake2.speed

         elif snake2.up == True:
            snake2.y -= snake2.speed

         elif snake2.down == True:
            snake2.y += snake2.speed

         if snake2.x == food1.x and snake2.y == food1.y:
            snake2.eat()
            food1.eaten = True

         if snake2.x < 0 or snake2.x >= 720 or snake2.y < 0 or snake2.y >= 720:
            snake2.hit()

         for i in snake1.body:
            if snake1.x == i[0] and snake1.y == i[1]:
               snake1.hit()
            if snake2.x == i[0] and snake2.y == i[1]:
               snake2.hit()

         for i in snake2.body:
            if snake1.x == i[0] and snake1.y == i[1]:
               snake1.hit()
            if snake2.x == i[0] and snake2.y == i[1]:
               snake2.hit()

         if snake1.x == snake2.x and snake1.y == snake2.y:
            if snake1.length > snake2.length:
               snake2.hit()
            elif snake2.length > snake1.length:
               snake1.hit()
            else:
                print("tie")

      drawGameWindow()
  

pygame.quit()