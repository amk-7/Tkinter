import pygame



# définire une classe qui va s'occuper des animations

class AnimateSprite(pygame.sprite.Sprite):
	# définir les choses à faire à la création de l'entité
	def __init__(self, sprite_name, size=(200, 200)):

		super().__init__()
		self.size = size
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.image = pygame.transform.scale(self.image, size)
		self.current_image = 0 # commencer l'anim à l'image 0
		self.images = animations.get(sprite_name)
		self.animations = False

	# définire une méthode pour démarré l'animation
	def start_animation(self):
		self.animations = True

	# definire une methode pour animer le sprite
	def animate(self, loop = False):

		# verifier si l'anim est active 
		if self.animations:

			# passer à l'image suivante
			self.current_image += 1

			# verifier si on à attient la fin de l'anim
			if self.current_image >= len(self.images):
				# remettre l'anim au départ
				self.current_image = 0

				# vérifier si l'animation n'est pas en mode boucle
				if loop is False:

					# désactiver l'anim
					self.animations = False

			# modifier l'image précedente par la suivante
			self.image = self.images[self.current_image]
			self.image = pygame.transform.scale(self.image, self.size)

# definire une fonction pour charger les image d'un sprite

def load_animation_images(sprite_name):

	# charger les 24 images de ce sprite dans le dossier correspondant
	images = []
	# récupérer le chemin du dossier pour ce sprite 
	path = f"assets/{sprite_name}/{sprite_name}"

	# boucler sur chaque image ce dossier pour les ajouter à la liste
	for num in range(1, 24):
		image_path = path+str(num)+'.png'
		images.append(pygame.image.load(image_path))

	# renvoyer le contenu de la liste d'image

	return images

# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png, ...]
# player -> [...player1.png, ...player2.png, ...]

animations = {
	'mummy': load_animation_images('mummy'),
	'player': load_animation_images('player'),
	'alien': load_animation_images('alien')

}