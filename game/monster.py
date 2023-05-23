import pygame
import random
import animation

#créer une classe qui va gérer la notion de monstre sur notre jeu

class Monster(animation.AnimateSprite):

	def __init__(self, game, name, size, offset = 0):
		super().__init__(name, size)
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 0.3 
		self.rect = self.image.get_rect()
		self.rect.x = 1000 + random.randint(0, 300)
		self.rect.y = 540 - offset
		self.loot_amount = 10
		self.start_animation()

	def set_speed(self, speed):
		self.default_speed = speed
		self.velocity = random.randint(1, 3)

	def set_loot_amount(self, amount):
		self.loot_amount = amount


	def damage(self, amount):
		# Infliger les degats

		self.health -= amount

		# verifier si son nouveau nombre de points de vie est <= 0 

		if self.health <= 0:
			# Reapparaitre comme un nouveau monstre

			self.rect.x = 1000 + random.randint(0, 300)
			self.velocity = random.randint(1, self.default_speed)
			self.health = self.max_health

			# ajouter le nombre de point à ce score
			self.game.add_score(self.loot_amount)
			

			# si la barre d'evenement est chargé à son maximun
			if self.game.comet_event.is_full_loaded():
				# retirer du jeu
				self.game.all_monsters.remove(self)

				# appel de la méthode pour essayeer de déclencher la pluie de cometes
				self.game.comet_event.attempt_fall()


	def update_animation(self):
		self.animate(loop=True)

	def update_health_bar(self, surface):
		# définir une couleur pour notre jauge de vie (vert claire)
		bar_color = (111, 210, 46)

		# définir une couleur pour l'arriere plan de la jauge ( gris foncé)
		back_bar_color = (60, 63, 60)

		# definir la position de notre jauge de vie ainsi que sa largeur et son épaiseur

		x = self.rect.x + 10
		y = self.rect.y - 20
		w = self.health
		h = 5
		bar_position = [x, y, w, h]

		# définir la position de l'arriere plan de notre jauge de vie

		w = self.max_health
		h = 5
		back_bar_position = [x, y, w, h]


		# dessiner notre barre de vie
		pygame.draw.rect(surface, back_bar_color, back_bar_position)

		pygame.draw.rect(surface, bar_color, bar_position)



	def forward(self): 	# methode de deplacement du monstre
		# le déplacement ne se fait que si il n'y a pas de colision avec un group de joueur

		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity

		# si le monstre est en colision avec le joueur
		else:

			# Infliger des déga

			self.game.player.damage(self.attack)

# definire  classe pour la momie
class Mummy(Monster):

	def __init__(self, game):
		super().__init__(game, "mummy", (130, 130))
		self.set_speed(3)
		self.set_loot_amount(20)


# definire  classe pour l'alien
class Alien(Monster):

	def __init__(self, game):
		super().__init__(game, "alien", (300, 300), 130)
		self.health = 250
		self.max_health = 250
		self.attack = 0.8
		self.set_speed(1)
		self.set_loot_amount(80)
