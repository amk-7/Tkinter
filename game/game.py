import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager
pygame.init()


class Game:

	def  __init__(self): 
		# Définire si  notre jeu a commencé  ou non
		self.is_playing = False
		#generer notre joueur
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		# gérer l'evenement de cette plui de comet
		self.comet_event = CometFallEvent(self)
		# groupe de monstre
		self.all_monsters = pygame.sprite.Group()
		# gérer le son
		self.sound_manager = SoundManager()
		self.font = pygame.font.Font("assets/my.ttf", 25)
		#self.font =pygame.font.SysFont("monospace", 16)
		# mettre le score à 0
		self.score = 0
		self.pressed = {}
		

	def start(self):
		self.is_playing = True
		self.spawn_monster(Mummy)
		self.spawn_monster(Mummy)
		self.spawn_monster(Alien)

	def add_score(self, points = 10):
		self.score += points


	def game_over(self):
		# remettre le jeu à neuf(game over)
		self.all_monsters = pygame.sprite.Group()
		self.comet_event.all_comets = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.reset_percent()
		self.is_playing = False
		self.score = 0
		# jouer le son
		self.sound_manager.play('game_over')



	def update(self, screen):
		# afficher le score sur l'ecran
		
		score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
		screen.blit(score_text, (20, 20))

		# appliquer l'image de mon joueur
		screen.blit(self.player.image, self.player.rect)


		# actualiser la barre de vie du joueur
		self.player.update_health_bar(screen)

		#  print(game.pressed)


		# actualiser la barre d'evenement du jeu
		self.comet_event.update_bar(screen)

		# actualiser l'animation du joueur
		self.player.update_animation()

		# recuperer les projectiles du joueur
		for projectile in self.player.all_projectiles:
			projectile.move()

		# recuperer les monstres de notre jeu

		for monster in self.all_monsters:
			monster.forward()
			monster.update_health_bar(screen)
			monster.update_animation()

		# recupérer les cometes de notre jeu
		for comet in self.comet_event.all_comets:
			comet.fall()

		# appliquer l'ensemble des images de mon group de projectiles
		self.player.all_projectiles.draw(screen)

		# appliquer l'ensemble des images de mon group de monstres
		self.all_monsters.draw(screen)

		# appliquer l'ensemble des image de mon group de cometes
		self.comet_event.all_comets.draw(screen)
	 
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width  < screen.get_width():
			#print("déplacement vers la droite")
			self.player.move_right()

		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			#print("déplacement vers la gauche")
			self.player.move_left()


		#print(game.player.rect.x)


	def check_collision(self, sprite, group): # pour detecter les colission player monster
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	def spawn_monster(self, monster_class_name):	# regouper les montres
		self.all_monsters.add(monster_class_name.__call__(self))
