import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura, altura = 600, 400
tamanho_celula = 20
cor_fundo = (255, 255, 255)
cor_snake = (0, 128, 0)
cor_comida = (255, 0, 0)

# Classe Snake
class Snake:
    def __init__(self):
        self.corpo = [(100, 100), (90, 100), (80, 100)]
        self.direcao = (1, 0)  # (x, y)

    def mover(self):
        x, y = self.corpo[0]
        dx, dy = self.direcao
        novo_cabeca = ((x + dx) % largura, (y + dy) % altura)
        self.corpo.insert(0, novo_cabeca)

    def colidir(self):
        return len(self.corpo) != len(set(self.corpo))

    def crescer(self):
        self.corpo.append(self.corpo[-1])

# Função principal
def main():
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    comida = (random.randrange(0, largura, tamanho_celula),
              random.randrange(0, altura, tamanho_celula))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direcao != (0, 1):
                    snake.direcao = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direcao != (0, -1):
                    snake.direcao = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direcao != (1, 0):
                    snake.direcao = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direcao != (-1, 0):
                    snake.direcao = (1, 0)

        snake.mover()

        if snake.corpo[0] == comida:
            comida = (random.randrange(0, largura, tamanho_celula),
                      random.randrange(0, altura, tamanho_celula))
            snake.crescer()

        if snake.colidir():
            pygame.quit()
            sys.exit()

        tela.fill(cor_fundo)
        pygame.draw.rect(tela, cor_comida, (comida[0], comida[1], tamanho_celula, tamanho_celula))

        for segmento in snake.corpo:
            pygame.draw.rect(tela, cor_snake, (segmento[0], segmento[1], tamanho_celula, tamanho_celula))

        pygame.display.flip()
        clock.tick(10)  # Ajuste a velocidade da cobra

if __name__ == "__main__":
    main()
