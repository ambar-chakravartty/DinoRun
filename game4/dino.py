import pygame

class Dino(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.imgs = []
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run1.png'),(52,52)))
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run2.png'),(52,52)))
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run3.png'),(52,52)))
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run4.png'),(52,52)))
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run5.png'),(52,52)))
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run6.png'),(52,52)))
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run7.png'),(52,52)))
		self.imgs.append(pygame.transform.smoothscale(pygame.image.load('run8.png'),(52,52)))
		self.index = 0
		self.image = self.imgs[self.index]
		self.x = x
		self.y = y
		self.rect = self.image.get_rect()
		self.rect.center = [self.x,self.y]

	def update(self,c):
		self.index += c
		if int(self.index) >= len(self.imgs):
			self.index = 0

		self.image = self.imgs[self.index]

	def jump(self,v,g):
		self.y += v
		self.y += g

		if self.y > 320:
			self.y = 320
			gravity = 0

		if self.y < 20:
			self.y = 320
			thrust = 0

		self.rect.center = [self.x,self.y]

def new_plant():
	rect = cactus.get_rect(center=(500,330))
	return rect 

def move_plant(plants,v):
	for plant in plants:
		plant.centerx -= v

def show_plant(plants):
	for plant in plants:
		screen.blit(cactus,plant)

def crash(a,b):  #Function to detect collision between bird and pipes
	ctol = -0
	if(a.colliderect(b)):
		if a.centerx-b.centerx < ctol:
			return True	
	else:
		return False

pygame.init()
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption('DinoRun')
clock = pygame.time.Clock()

bg = pygame.image.load('bg2.jpg')

icon = pygame.image.load('run6.png')
pygame.display.set_icon(icon)

dino = Dino(200,320)
group = pygame.sprite.Group()
group.add(dino)

floor = pygame.Surface((800,400))
floor_rect = floor.get_rect()
floor_rect.topleft = (0,520)

cactus = pygame.image.load('cactus.png')
cactus = pygame.transform.smoothscale(cactus, (32, 32))
cactii = []

go_img = pygame.transform.smoothscale(pygame.image.load('gameover.png'),(256,256))

PLANT = pygame.USEREVENT
time = 2000
timer = pygame.time.set_timer(PLANT,time)

thrust = 0
gravity = 0

count = 1
v = 5

quit = False
ctnue = False

score = 0
font = pygame.font.Font("freesansbold.ttf",32)
s = 1

running = True 
while running:
	score += s
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				gravity = 0
				thrust = -15

			if event.key == pygame.K_0:
				ctnue = True 

			if event.key == pygame.K_1:
				quit = True

		if event.type == pygame.KEYUP:
			thrust = 0
			gravity = 10
			#ctnue = False
			quit =False

		if event.type == PLANT:
			cactii.append(new_plant())
	
	screen.fill((66,179,245))
	screen.blit(bg,(0,0))	

	show_plant(cactii)
	move_plant(cactii,v)
	#pygame.draw.rect(screen,(0,0,0),)
	group.draw(screen)
	dino.update(count)
	dino.jump(thrust,gravity)


	for p in cactii:
		if crash(p,dino.rect):
			s = 0 
			print('pygame.sprite.get_bottom_layer')
			screen.blit(go_img,(110,20))
			count = 0
			v = 0


	text =  font.render(str(score),False,(255,255,255))
	screen.blit(text,(5,5))
		
	pygame.display.update()
	clock.tick(30)