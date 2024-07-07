import math
import random
import time
import pygame

pygame.init()

WIDTH, HEIGHT = 800,600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainer")

background_color = (0,25,45)
MAX_LIVES = 3
TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 40
top_bar_height = 50

LABEL_FONT = pygame.font.SysFont("comicsans",28, bold = False)

class Target:
    MAX_SIZE = 40
    GROWTH_RATE = 0.2
    COLOR_FIRST = "red"
    COLOR_SECOND = "white"

    def __init__(self,x,y): #x and y are the positions of the target
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow == True:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self,win):
        pygame.draw.circle(win, self.COLOR_FIRST, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.COLOR_SECOND, (self.x, self.y), self.size*0.8)
        pygame.draw.circle(win, self.COLOR_FIRST, (self.x, self.y), self.size*0.6)
        pygame.draw.circle(win, self.COLOR_SECOND, (self.x, self.y), self.size*0.4)
        pygame.draw.circle(win, self.COLOR_FIRST, (self.x, self.y), self.size * 0.25)
        pygame.draw.circle(win, self.COLOR_SECOND, (self.x, self.y), self.size * 0.1)

    def collide(self,x,y):
        dist  = math.sqrt((self.x-x)**2 + (self.y-y)**2)
        return dist <= self.size
def drawTarget(self,targets):
    WIN.fill(background_color)

    for target in targets:
        target.draw(WIN)

def find_nearest_target(targets, x, y):
    if not targets:
        return None
    return min(targets, key=lambda t: math.sqrt((t.x - x)**2 + (t.y - y)**2))

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000)/100)
    seconds = int(round(secs%60,1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"
def draw_top_bar(elapsed_time, targets_pressed,misses):
    pygame.draw.rect(WIN, "white",(0,0, WIDTH, top_bar_height))
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}",1,"black")

    speed = round(targets_pressed/elapsed_time,1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s",1,"orange")
    hits = targets_pressed
    hits_label = LABEL_FONT.render(f"Hits: {hits}",1,"violet")
    lives_label = LABEL_FONT.render(f"Lives: {MAX_LIVES-misses}",1,"green")
    WIN.blit(time_label,(5,5))
    WIN.blit(speed_label,(255,5))
    WIN.blit(hits_label,(500,5))
    WIN.blit(lives_label,(675,5))

def end_screen(win,elapsed_time, targets_pressed, clicks):
    win.fill(background_color)
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "white")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "orange")
    hits = targets_pressed
    hits_label = LABEL_FONT.render(f"Hits: {hits}", 1, "violet")
    accuracy = 0
    if targets_pressed!=0:
        accuracy = round(clicks*100/targets_pressed,1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}", 1, "green")

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 250))
    win.blit(hits_label, (get_middle(hits_label), 350))
    win.blit(accuracy_label, (get_middle(accuracy_label), 455))

    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                quit()

def get_middle(surface):
    return WIDTH/2 - surface.get_width()/2


def mode_selection_screen(win):
    win.fill(background_color)
    regular_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 4, 50)
    god_button = pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 50)

    regular_text = LABEL_FONT.render("Regular Mode", 1, "white")
    god_text = LABEL_FONT.render("God Mode", 1, "white")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if regular_button.collidepoint(event.pos):
                    return "regular"
                elif god_button.collidepoint(event.pos):
                    return "god"

        pygame.draw.rect(win, "red", regular_button)
        pygame.draw.rect(win, "green", god_button)
        win.blit(regular_text, (regular_button.x + 10, regular_button.y + 10))
        win.blit(god_text, (god_button.x + 10, god_button.y + 10))
        pygame.display.update()
def main():
    mode = mode_selection_screen(WIN)
    if mode is None:
        return
    run = True
    targets = []
    clock = pygame.time.Clock()
    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    # above line triggers TARGET_EVENT evert TARGET_INCREMENT ms

    while run:
        clock.tick(60)
        # click = False
        mouse_pos = pygame.mouse.get_pos()
        mouseX = mouse_pos[0]
        mouseY = mouse_pos[1]
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT: # listening for the event
                xcoord = random.randint(TARGET_PADDING,WIDTH - TARGET_PADDING)
                ycoord = random.randint(TARGET_PADDING + top_bar_height,HEIGHT - TARGET_PADDING)
                target = Target(xcoord,ycoord)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # click = True
                clicks += 1
                if mode == "regular":
                    for target in targets[:]:
                        if target.collide(mouseX, mouseY):
                            targets.remove(target)
                            target_pressed += 1
                            break
                elif mode == "god":
                    nearest_target = find_nearest_target(targets, mouseX, mouseY)
                    if nearest_target:
                        targets.remove(nearest_target)
                        target_pressed += 1

        for target in targets:
            target.update()  # change their size

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            # if click and mode == "regular" and target.collide(mouseX,mouseY):
            #     targets.remove(target)
            #     target_pressed+=1
            # if click and mode == "god":
            #     nearest_target =  find_nearest_target(targets,mouseX,mouseY)
            #     if nearest_target:
            #         targets.remove(nearest_target)
            #         target_pressed += 1
        if misses >= MAX_LIVES:
            end_screen(WIN,elapsed_time,target_pressed,clicks)

        drawTarget(WIN,targets)
        draw_top_bar(elapsed_time,target_pressed,misses)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
