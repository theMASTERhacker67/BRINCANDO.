import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Windows XP - O Jogo")

# Cores
BLUE_XP = (49, 106, 197) # Azul da barra de tarefas do XP
GREEN_START = (58, 110, 165) # Cor do botão iniciar do XP
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)

# Fontes
font = pygame.font.Font(None, 24)

# Carregar imagens (placeholders por enquanto)
# No futuro, precisaremos de imagens para o Windows XP, ícone do Google, hacker, etc.
# Para simplificar, vou criar retângulos coloridos como placeholders.

# Ícone do Google (placeholder)
google_icon_rect = pygame.Rect(50, 50, 64, 64)

# Função para desenhar o desktop do Windows XP
def draw_windows_xp_desktop():
    # Fundo azul padrão do XP
    SCREEN.fill(BLUE_XP)

    # Barra de tarefas
    pygame.draw.rect(SCREEN, (192, 192, 192), (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40))
    pygame.draw.rect(SCREEN, (128, 128, 128), (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 2)) # Linha superior da barra

    # Botão Iniciar
    pygame.draw.rect(SCREEN, GREEN_START, (5, SCREEN_HEIGHT - 35, 70, 30))
    start_text = font.render("Iniciar", True, WHITE)
    SCREEN.blit(start_text, (15, SCREEN_HEIGHT - 30))

    # Ícone do Google
    pygame.draw.rect(SCREEN, (255, 0, 0), google_icon_rect) # Vermelho para representar o Google
    google_text = font.render("Google", True, WHITE)
    SCREEN.blit(google_text, (google_icon_rect.x + 5, google_icon_rect.y + 20))

# Loop principal do jogo
running = True
game_state = "DESKTOP_XP"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "DESKTOP_XP":
                if google_icon_rect.collidepoint(event.pos):
                    print("Google Clicado!")
                    # Mudar para o estado do hacker ou batalha
                    game_state = "HACKER_APPEARS"

    if game_state == "DESKTOP_XP":
        draw_windows_xp_desktop()
    elif game_state == "HACKER_APPEARS":
        SCREEN.fill(BLACK) # Tela preta para o hacker aparecer
        hacker_text = font.render("Hacker Aparece! Hahahahaha!", True, (0, 255, 0)) # Texto verde para o hacker
        SCREEN.blit(hacker_text, (SCREEN_WIDTH // 2 - hacker_text.get_width() // 2, SCREEN_HEIGHT // 2 - hacker_text.get_height() // 2))
        # Adicionar som de risada aqui no futuro
        # Mudar para o estado de batalha após um tempo ou clique
        # Para demonstração, vamos mudar para batalha imediatamente após um pequeno atraso
        pygame.display.flip()
        pygame.time.wait(2000) # Espera 2 segundos
        game_state = "BATTLE_START"

    elif game_state == "BATTLE_START":
        SCREEN.fill(BLACK) # Fundo da batalha
        battle_text = font.render("Batalha Undertale Começa!", True, WHITE)
        SCREEN.blit(battle_text, (SCREEN_WIDTH // 2 - battle_text.get_width() // 2, SCREEN_HEIGHT // 2 - battle_text.get_height() // 2))
        # Aqui entraria a lógica da batalha Undertale
        # Por enquanto, apenas um texto indicando o início da batalha

    pygame.display.flip()

pygame.quit()

