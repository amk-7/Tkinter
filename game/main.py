import pygame
from game import Game
import math
pygame.init()


# définire une clock
clock = pygame.time.Clock()
FPS = 60


pygame.display.set_caption("Comet fall Game") # for change window title
screen = pygame.display.set_mode((1080, 720)) # for window size 
background = pygame.image.load('assets/bg.jpg') # for add backgroung

# Inporter , charger notre bannière

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

# importer ou charger notre bouton pour lancer la partie

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)

# charger notre joueur
game = Game()

# maintenir la fenetre eveiller
running = True

# tantque running est vrai on maintient la fenetre
while running:
	# appiquer la fenetre du jeu
	screen.blit(background,(0,-200))

	# verifier si notre jeu a commencé ou non
	if game.is_playing:
		# déclancher les instructions de la partie
		game.update(screen)

	# verifier si notre jeu n'a pas commencé
	else:
		screen.blit(play_button, play_button_rect)

		screen.blit(banner, banner_rect)

	# Mettre à jour l'ecran
	pygame.display.flip()
 
	# si le joueur ferme la fenêtre event <==> evenement ici fermeture la fenetre
	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			#print("fermeture du jeu")
			
  		# detecter si un joueur lache une touche du clavier

		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True

			# detecter si la touche espace est enclanché pour lancer notre projectile
			if event.key == pygame.K_SPACE :
				if game.is_playing:
					game.player.launch_projectile()
				else:
					# mettre le jeu en mode "lancé"
					game.start()
					# jouer le son
					game.sound_manager.play('click')

		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False


		elif event.type == pygame.MOUSEBUTTONDOWN:
			# verification pour savoir si la souris est en collision avec la bouton jouer
			if play_button_rect.collidepoint(event.pos):
				# mettre le jeu en mode "lancé"
				game.start()
				# jouer le son
				game.sound_manager.play('click')


	# fixer le monbre de fps sur ma clock
	#clock.tick(FPS)