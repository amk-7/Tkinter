import pygame

# definire la classe qui va gérer "le projectile" (notion) du joueur

class Projectile(pygame.sprite.Sprite):

	# definire le constructeur de cette classe
	def __init__(self, player):
		super().__init__()
		self.velocity = 5
		self.player = player
		self.image = pygame.image.load('assets/projectile.png')
		self.image = pygame.transform.scale(self.image, (50, 50)) # le couple(50,50) est une nouvelle taille de l'image
		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x + 120	# mettre le projectile au niveau du joueur
		self.rect.y = player.rect.y + 80
		self.origine_image = self.image
		self.angle = 0


	def rotate(self):

		# tourner le projectile
		self.angle += 7
		self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
		self.rect = self.image.get_rect(center = self.rect.center)


	def remove(self): # pour supprimer un projectiles

		self.player.all_projectiles.remove(self)

	def move(self):
		self.rect.x += self.velocity
		self.rotate()

		# verifier si le projectile entre en collision avec un monstre
		for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
			# supprimer le projectile
			self.remove()

			# infliger des dégats

			monster.damage(self.player.attack)

		# verifier si notre projectile n'est plus présent sur l'ecran
		if self.rect.x > 1080:

			# supprimer le projectile (en dehors de l'ecran)
			self.remove()
			#print("delete")
			
  