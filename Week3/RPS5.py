import pygame
import random

# initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
window = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Rock Paper Scissors, Enter R, S or P to play")

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the font for text display
font = pygame.font.Font(None, 50)

# Function to display text
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill(white)

    # Display the prompt
    display_text("Rock, Paper, Scissors!", black, window_size[0] // 2, window_size[1] // 4)

    # Get player choice
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        player_choice = "rock"
    elif keys[pygame.K_p]:
        player_choice = "paper"
    elif keys[pygame.K_s]:
        player_choice = "scissors"
    else:
        player_choice = None

    # Display player choice
    if player_choice:
        display_text("You chose " + player_choice, black, window_size[0] // 2, window_size[1] // 2)

        # Generate computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        display_text("Computer chose " + computer_choice, black, window_size[0] // 2, window_size[1] // 2 + 50)

        # Determine the winner
        if player_choice == computer_choice:
            result = "Tie!"
        elif player_choice == "rock" and computer_choice == "scissors":
            result = "You win!"
        elif player_choice == "paper" and computer_choice == "rock":
            result = "You win!"
        elif player_choice == "scissors" and computer_choice == "paper":
            result = "You win!"
        else:
            result = "You lose."

        # Display the result
        display_text(result, black, window_size[0] // 2, window_size[1] * 3 // 4)

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
