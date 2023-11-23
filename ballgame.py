import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Game")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# 공 정보
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 0
ball_speed_y = 0
gravity = 1
bounce_factor = 1

# 노란색 공 정보
yellow_ball_radius = 30
yellow_ball_x = screen_width // 4
yellow_ball_y = screen_height // 2

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 화면을 검은색으로 채우기
    screen.fill(black)

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_speed_x = -5
    elif keys[pygame.K_RIGHT]:
        ball_speed_x = 5
    else:
        ball_speed_x = 0

    # 중력 적용
    ball_speed_y += gravity

    # 공 좌표 갱신
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 화면 밖으로 나가지 않도록 제한
    if ball_x - ball_radius < 0:
        ball_x = ball_radius
    elif ball_x + ball_radius > screen_width:
        ball_x = screen_width - ball_radius

    if ball_y - ball_radius < 0:
        ball_y = ball_radius
        ball_speed_y = -ball_speed_y * bounce_factor
    elif ball_y + ball_radius > screen_height:
        ball_y = screen_height - ball_radius
        ball_speed_y = -ball_speed_y * bounce_factor

    # 노란색 공 그리기
    pygame.draw.circle(screen, yellow, (int(yellow_ball_x), int(yellow_ball_y)), yellow_ball_radius)

    # 하얀색 공 그리기
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_radius)

    # 하얀색 공과 노란색 공 충돌 체크
    distance = pygame.math.Vector2(ball_x - yellow_ball_x, ball_y - yellow_ball_y).length()
    if distance < ball_radius + yellow_ball_radius:
        pygame.quit()
        sys.exit()

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 설정
    pygame.time.Clock().tick(60)
