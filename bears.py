import pygame, time
from random import randint

def delete_bear():
    global bears, player, score
    if bears[0].y < 510:
        if player.x <= bears[0].x + 25 <= player.x + 60:
            score += 1
            bears = bears[1:]
    elif bears[0].y > 590:
        bears = bears[1:]



class Bear:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.y = 0
        self.size = 50
        self.text = 'bear'

        self.bear_surf = pygame.Surface((self.size, self.size))
        self.bear_txt = pygame.font.SysFont('TimesNewRoman', 30).render(self.text, True, 'black')


        self.bear_rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def running(self):
        self.bear_surf.fill('black')
        pygame.draw.rect(self.bear_surf, 'white', (1, 1, 48, 48))
        self.bear_surf.blit(self.bear_txt, [
            self.bear_rect.width / 2 - self.bear_txt.get_rect().width / 2,
            self.bear_rect.height / 2 - self.bear_txt.get_rect().height / 2
        ])


        self.screen.blit(self.bear_surf, (self.x, self.y, self.size, self.size))
        self.y += 1

        if self.y >= 500:
            delete_bear()


class Player:
    def __init__(self, screen):
        self.x = 370
        self.y = 550
        self.width = 60
        self.height = 40
        self.text = 'you'
        self.screen = screen

        self.player_surf = pygame.Surface((self.width, self.height))
        self.player_text = pygame.font.SysFont('TimesNewRoman', 35).render(self.text, True, 'black')


        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, x):
        if 0 <= self.x + x <= 740:
            self.x += x

        self.player_surf.fill('black')
        pygame.draw.rect(self.player_surf, 'white', (1, 1, self.width - 2, self.height - 2))
        self.player_surf.blit(self.player_text, [
            self.player_rect.width / 2 - self.player_text.get_rect().width / 2,
            self.player_rect.height / 2 - self.player_text.get_rect().height / 2
        ])


        self.screen.blit(self.player_surf, (self.x, self.y, self.width, self.height))

def main():
    global bears, player, score
    pygame.init()

    display = pygame.display.set_mode((800, 600))
    timer = time.time()

    bears = [Bear(display, randint(0, 751))]
    player = Player(display)
    clock = pygame.time.Clock()

    score = 0
    x = 0
    count = 0
    while True:
        display.fill('white')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -1
                elif event.key == pygame.K_RIGHT:
                    x = 1
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    x = 0


        if int(time.time()) - int(timer) >= 100:
            print(score)
            print(int(time.time()) - int(timer))
            pygame.quit()

        player.move(x)
        for bear in bears:
            bear.running()

        clock.tick(120)
        pygame.display.flip()
        count += 1

        if count == 240:
            bears.append(Bear(display, randint(0, 751)))
            count = 0


if __name__ == '__main__':
    main()
