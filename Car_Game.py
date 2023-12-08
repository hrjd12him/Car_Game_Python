import random
import pygame, time

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# load image
carimage = pygame.image.load("python_project/Car_Game/car3.png")

# message
endfont = pygame.font.SysFont("None", 100)
render_text = endfont.render("End Game", 1, (250, 250, 250))

# grass img
grass = pygame.image.load("python_project/Car_Game/grass.jpg")
yellow_strip = pygame.image.load("python_project/Car_Game/white_strip.png")
strip = pygame.image.load("python_project/Car_Game/strip.jpg")

# time module
clock = pygame.time.Clock()


# window name
pygame.display.set_caption("Car Race")


# obstacle
def obstacle(obs_x, obs_y, obs):
    if obs == 0:
        obs_pic = pygame.image.load("python_project/Car_Game/car2.png")
    elif obs == 1:
        obs_pic = pygame.image.load("python_project/Car_Game/car1.png")
    elif obs == 2:
        obs_pic = pygame.image.load("python_project/Car_Game/car3.png")
    screen.blit(obs_pic, (obs_x, obs_y))


# Background img
def background():
    screen.blit(grass, (0, 0))
    screen.blit(grass, (700, 0))
    screen.blit(yellow_strip, (370, 20))
    screen.blit(yellow_strip, (370, 120))
    screen.blit(yellow_strip, (370, 220))
    screen.blit(yellow_strip, (370, 320))
    screen.blit(yellow_strip, (370, 420))
    screen.blit(yellow_strip, (370, 520))
    screen.blit(strip, (120, 0))
    screen.blit(strip, (680, 0))


# Image placing
def car(x, y):
    screen.blit(carimage, (x, y))


# game loop
def game_loop():
    bumped = False
    x_change = 0
    x = 380
    y = 500
    car_width = 43
    car_height = 100
    obstacle_speed = 10
    obs = 0
    y_change = 0
    obs_x = random.randrange(200, 650)
    obs_y = -750
    enemy_width = 43
    enemy_height = 100

    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                bumped = True

        # move x and y cordinates
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2

            if event.key == pygame.K_RIGHT:
                x_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change

        # background color
        screen.fill((0, 0, 0))
        background()
        obs_y -= obstacle_speed / 4
        obstacle(obs_x, obs_y, obs)
        obs_y += obstacle_speed

        # call the car function
        car(x, y)
        # creating limitation of width
        if x > 680 - car_width or x < 120:  # car width == 43
            screen.blit(render_text, (220, 240))
            pygame.display.update()
            time.sleep(5)
            game_loop()

        if obs_y > height:
            obs_y = 0 - enemy_height
            obs_x = random.randrange(130, width - 190)
            obs = random.randrange(0, 3)
        # enemy car crossing you
        if y < obs_y + enemy_height:
            if (
                x > obs_x
                and x < obs_x + car_width
                or x + car_width > obs_x
                and x + car_width < obs_x + enemy_width
            ):
                screen.blit(render_text, (220, 240))
                pygame.display.update()
                time.sleep(5)
                game_loop()

        # update the game
        pygame.display.update()
        clock.tick(100)  # mili sec


game_loop()
pygame.quit()
quit()
