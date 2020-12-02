import numpy, pygame, sys, os, random, threading


q = 0.01
size = 30


class Graph:
    def __init__(self, var, area1, area2):
        self.var = var
        self.graph = numpy.array([(var[0]*pow(i*q, 2)+var[1]*i*q+var[2], i*q) for i in range(int(area1/q), int(area2/q))])


    def __add__(self, graph):
        if type(graph) == Graph:
            for i in range(0, len(self.graph)):
                for _, x in graph.graph:
                    if self.graph[i][1] == x: self.graph[i][0] = (self.graph[i][1]+x)/2


def ball_physics():
    x = random.randint(-6/q, 6/q)*q
    while run:
        clock.tick(60)
        y = ball["func"].var[0]*pow(x, 2)+ball["func"].var[1]*x+ball["func"].var[2]
        ball["pos"] = (x, y)
        # print(x, y/x)
        if x != 0:
            ball["gradient"] = (ball["func"].var[0]*2*x+ball["func"].var[1])
            x -= (ball["func"].var[0]*2*x+ball["func"].var[1])
        else:
            ball["gradient"] = 0


def render():
    screen.fill((0, 0, 0))
    for i in funcs:
        # pygame.draw.circle(screen, (255, 255, 255), i.graph, 3)
        v = i.graph[0]
        for j in i.graph:
            pygame.draw.line(screen, (255, 255, 255), ((v[1]*size)+cx, -(v[0]*size)+cy), ((j[1]*size)+cx, -(j[0]*size)+cy), 2)
            v = j
        pygame.draw.circle(screen, (255, 255, 0), (int(ball["pos"][0]*size)+cx, -int(ball["pos"][1]*size)+cy), 8)
    pygame.display.update()


w, h = 300*2, 240*2; cx, cy = w//2, h//2; run = True
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.display.set_caption("A.I. Calculus")


func = Graph([0.1, 1, -3], -7, 7)
# func2 = Graph([0.5, 0, 0], -3, 3)
print(func.graph)
# func + func2
funcs = [func]


ball = {
    "func" : func,
    "pos" : (0, 0),
    "gradient" : 0
}

threading.Thread(target=ball_physics).start()
print(ball["gradient"])

while run:
    clock.tick(60)
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); run = False; sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    if key[pygame.K_ESCAPE]:
        pygame.quit(); run = False; sys.exit()

    render()