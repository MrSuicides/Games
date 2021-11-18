import pygame
import requests

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
board = response.json()['board']
buffer = 1
WIDTH = 550
gray_background = (0, 0, 0)

element_color = (255, 255, 255)

result_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]

def music():
    pygame.init()
    pygame.mixer.music.load('Music1.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    return

def input(win, position):
    i, j = position[1], position[0]
    font = pygame.font.SysFont('comicsans', 30, True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (result_board[i - 1][j - 1] != 0):
                    return
                if (event.key == 48):
                    board[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(win, gray_background, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10):
                    pygame.draw.rect(win, gray_background, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    value = font.render(str(event.key - 48), True, (255, 0, 0))
                    win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    board[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return


def static():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, WIDTH))  # создаем окно WIDTH на WIDTH
    pygame.display.set_caption("Lab_1")
    window.fill(gray_background)
    font = pygame.font.SysFont('comicsans', 30, True)

    for i in range(0, 10):  # рисуем сетку
        if (i % 3) == 0:
            pygame.draw.line(window, (255, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 6)
            pygame.draw.line(window, (255, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 6)

        pygame.draw.line(window, (255, 255, 255), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(window, (255, 255, 255), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(0, len(result_board[0])):
        for j in range(0, len(result_board[0])):
            if (0 < result_board[i][j] < 10):
                value = font.render(str(result_board[i][j]), True, element_color)
                window.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                input(window, (pos[0] // 50, pos[1] // 50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == '__main__':
    music()
    static()
