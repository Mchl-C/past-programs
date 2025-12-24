import pygame

# Load the images
image1 = pygame.image.load("image1.png")
image2 = pygame.image.load("image2.png")

# Get the rectangles for the images
rect1 = image1.get_rect()
rect2 = image2.get_rect()

# Calculate the position for image2 so that it is centered on image1
rect2.centerx = rect1.centerx
rect2.centery = rect1.centery

# Blit image2 onto image1
image1.blit(image2, rect2)

# Now image1 contains both images, with image2 centered in the middle
