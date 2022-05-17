import pygame as py
import sys
import random
from pygame.locals import *

# ===========================================================
# ========================前期准备===========================
py.init()
py.mixer.init()
src_path = "./src/"
py.mixer.music.load(src_path + "music.mp3")  # 播放音乐
py.mixer.music.play(-1)


# 注：游戏需要的所有文件（图片等）都放在同游戏目录的"Files"目录下。
# 定义一个按钮类
class Button(py.rect.Rect):
    def __init__(self, obj):
        super().__init__(obj)

    def has(self, pos):
        if self.right >= pos[0] >= self.left and self.bottom >= pos[1] >= self.top:
            return True
        else:
            return False


screen = py.display.set_mode((1000, 650))


# ===========================================================
# =========================知识库内==========================

def knowledge(selection):
    path = src_path + '/inside_library/knowledge' + str(selection) + '.png'
    know = py.image.load(path)
    know = py.transform.smoothscale(know, (1000, 650))
    screen.blit(know, (0, 0))
    exits = py.image.load(src_path + '/inside_library/back.png')
    exits = py.transform.smoothscale(exits, (72, 72))
    exit_button = screen.blit(exits, (918, 570))
    exit_button = Button(exit_button)
    py.display.flip() # 更新图像到窗口
    # 进入事件循环
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                # 点击离开该页面
                if exit_button.has(pos):
                    selection = 0
                    break
        if not selection:
            break


def inside_Liberary():
    ilib = py.image.load(src_path + '/inside_library/Inside.png')
    ilib = py.transform.smoothscale(ilib, (1000, 650))
    screen.blit(ilib, (0, 0))  # 设置未知
    # 退出知识库的按钮
    exits = py.image.load(src_path + '/inside_library/exit.png')
    exits = py.transform.smoothscale(exits, (60, 60))
    exit_button = screen.blit(exits, (5, 560))
    exit_button = Button(exit_button)
    # 化石能源按钮
    rubbish1 = py.image.load(src_path + '/inside_library/rubbish1.png')
    rubbish1 = py.transform.smoothscale(rubbish1, (400, 300))
    rubbish1_button = screen.blit(rubbish1, (50, 150))
    rubbish1_button = Button(rubbish1_button)
    # 新能源按钮
    rubbish2 = py.image.load(src_path + '/inside_library/rubbish2.png')
    rubbish2 = py.transform.smoothscale(rubbish2, (400, 300))
    rubbish2_button = screen.blit(rubbish2, (550, 150))
    rubbish2_button = Button(rubbish2_button)

    py.display.flip()
    selection = -1
    # 进入事件循环
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                # 点击离开知识库
                if exit_button.has(pos):
                    selection = 0
                    break
                # 点击化石能源
                if rubbish1_button.has(pos):
                    selection = 1
                    break
                # 点击新能源
                if rubbish2_button.has(pos):
                    selection = 2
                    break
        if selection != -1:
            break
    if selection:
        knowledge(selection)
        inside_Liberary()


# ===========================================================
# =========================知识库外==========================

def outside_Liberary():
    olib = py.image.load(src_path + '/outside_library/Outside.png')
    olib = py.transform.smoothscale(olib, (1000, 650))
    screen.blit(olib, (0, 0))
    # 进入知识库的按钮
    enter = py.image.load(src_path + '/outside_library/enter_lib.png')
    enter = py.transform.smoothscale(enter, (100, 100))
    enter_button = screen.blit(enter, (450, 500))
    enter_button = Button(enter_button)
    # 退出知识库的按钮
    exits = py.image.load(src_path + '/outside_library/playground.png')
    exits = py.transform.smoothscale(exits, (60, 60))
    exit_button = screen.blit(exits, (15, 580))
    exit_button = Button(exit_button)
    py.display.flip()
    selection = -1
    # 进入事件循环
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                # 点击返回操场
                if exit_button.has(pos):
                    selection = 0
                    break
                # 点击进入知识库
                if enter_button.has(pos):
                    selection = 1
                    break
        if selection != -1:
            break
    if selection:
        inside_Liberary()
        outside_Liberary()


# ===========================================================
# ==========================游戏帮助=========================

def help_page():
    background = py.image.load(src_path + '/help/background.png')
    background = py.transform.smoothscale(background, (1000, 650))
    screen.blit(background, (0, 0))
    # 返回按钮
    exits = py.image.load(src_path + '/help/back.png')
    exits = py.transform.smoothscale(exits, (60, 60))
    exit_button = screen.blit(exits, (5, 585))
    exit_button = Button(exit_button)
    py.display.flip()
    back = 0
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if exit_button.has(pos):
                    back = 1
                    break
        if back:
            break


# ===========================================================
# ==========================游戏结束=========================

def game_over(result):
    path = src_path + '/game_over/result' + str(result) + '.png'
    result = py.image.load(path)
    result = py.transform.smoothscale(result, (1300, 650))
    screen.blit(result, (-120, 0))
    py.display.flip()
    temp = 0
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                temp = 1
                break
        if temp:
            break


# ===========================================================
# ==========================操场环节=========================

choices = ['01', '02', '03', '11', '12', '13', '14']


class Rubbish():
    def __init__(self, sort):
        self.sort = sort
        self.img = py.image.load(src_path + '/playground/' + sort + '.png')
        self.img = py.transform.smoothscale(self.img, (100, 100))  # 分类图标大小
        x = random.randint(100, 1400)
        y = random.randint(110, 900)
        self.position = self.img.get_rect()
        self.position = self.position.move((x, y))
        screen.blit(self.img, self.position)


class Role():
    def __init__(self, role):
        self.r_side = py.image.load(src_path + '/playground/' + role + '1.png')
        self.r_walk = py.image.load(src_path + '/playground/' + role + '2.png')
        self.l_side = py.transform.flip(self.r_side, True, False)
        self.l_walk = py.transform.flip(self.r_walk, True, False)
        self.img = self.r_side
        self.position = self.img.get_rect()
        screen.blit(self.img, self.position)
        self.rubbish = None

    def move(self, key):
        if key == K_UP:
            if self.position.top <= 200:
                return (0, 2)
            else:
                self.position = self.position.move(0, -2)
                return 0
        if key == K_DOWN:
            if self.position.bottom >= 450:
                return (0, -2)
            else:
                self.position = self.position.move(0, 2)
                return 0
        if key == K_RIGHT:
            if self.position.right >= 800:
                return (-2, 0)
            else:
                self.position = self.position.move(2, 0)
                return 0
        if key == K_LEFT:
            if self.position.left <= 200:
                return (2, 0)
            else:
                self.position = self.position.move(-2, 0)
                return 0


class Trash_can():
    def __init__(self, num):
        self.num = num
        self.img = py.image.load(src_path + '/playground/' + str(num) + '.png')
        self.img = py.transform.smoothscale(self.img, (200, 150))  # 分类图标大小
        self.position = self.img.get_rect()
        self.position = self.position.move((100 + num * 200, 0))
        screen.blit(self.img, self.position)


def playground(selection):
    background = py.image.load(src_path + '/playground/Playground.jpeg')
    background = py.transform.smoothscale(background, (1920, 1080))
    screen.blit(background, [0, 0])
    lib = py.image.load(src_path + '/playground/library.png')
    # lib = py.transform.smoothscale(lib, (78, 72))
    lib_button = screen.blit(lib, (900, 10))
    lib_button = Button(lib_button)
    trash_can = []
    for num in range(0, 2):  # 分类数量
        trash_can.append(Trash_can(num))
    role = Role(selection)
    rubbish = []
    for sort in choices:
        rubbish.append(Rubbish(sort))
    py.display.flip()
    down = 0
    go = None
    move_bg = [0, 0]
    temp = 0
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if lib_button.has(pos):
                    outside_Liberary()
            if event.type == KEYDOWN and \
                    event.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT):
                if event.key == K_RIGHT:
                    role.img = role.r_side
                elif event.key == K_LEFT:
                    role.img = role.l_side
                down = 1
                go = event.key
            if event.type == KEYUP and event.key == go:
                if event.key == K_RIGHT:
                    role.img = role.r_side
                elif event.key == K_LEFT:
                    role.img = role.l_side
                down = 0
        take = role.position.collidelist([each.position for each in rubbish])
        if take >= 0 and not role.rubbish:
            role.rubbish = rubbish[take].sort[0]
            del rubbish[take]
        put = role.position.collidelist([each.position for each in trash_can])
        if put >= 0 and role.rubbish:
            if role.rubbish == str(trash_can[put].num):
                role.rubbish = None
                if not len(rubbish):
                    game_over(1)
                    break
            else:
                game_over(2)
                break
        if down:
            moved = role.move(go)
            temp += 1
            if not temp % 20:
                if role.img == role.r_side:
                    role.img = role.r_walk
                elif role.img == role.r_walk:
                    role.img = role.r_side
                elif role.img == role.l_side:
                    role.img = role.l_walk
                else:
                    role.img = role.l_side
            if moved:
                if 0 >= moved[0] + move_bg[0] >= -497 and \
                        0 >= moved[1] + move_bg[1] >= -326:
                    for i in range(2):
                        move_bg[i] += moved[i]
                    for each in rubbish:
                        each.position = each.position.move(moved)
                    for each in trash_can:
                        each.position = each.position.move(moved)
                elif role.position.left - moved[0] >= 0 and \
                        role.position.right - moved[0] <= 1000 and \
                        role.position.top - moved[1] >= 0 and \
                        role.position.bottom - moved[1] <= 650:
                    role.position = role.position.move([-i for i in moved])
        screen.blit(background, move_bg)
        lib = py.image.load(src_path + '/playground/library.png')
        lib = py.transform.smoothscale(lib, (78, 72))
        lib_button = screen.blit(lib, (900, 10))
        lib_button = Button(lib_button)
        for each in trash_can:
            screen.blit(each.img, each.position)
        for each in rubbish:
            screen.blit(each.img, each.position)
        screen.blit(role.img, role.position)
        py.display.flip()


# ===========================================================
# ==========================选择人物=========================

def choose_role():
    background = py.image.load(src_path + '/choose_player/background.png')
    background = py.transform.smoothscale(background, (1000, 650))
    screen.blit(background, (0, 0))
    man = py.image.load(src_path + '/choose_player/man.png')
    man = py.transform.smoothscale(man, (150, 243))
    man_button = screen.blit(man, (280, 220))
    man_button = Button(man_button)
    woman = py.image.load(src_path + '/choose_player/woman.png')
    woman = py.transform.smoothscale(woman, (150, 243))
    woman_button = screen.blit(woman, (560, 220))
    woman_button = Button(woman_button)
    py.display.flip()
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if man_button.has(pos):
                    return 'man'
                if woman_button.has(pos):
                    return 'woman'


# ===========================================================
# ========================开始游戏界面========================

def start():
    background = py.image.load(src_path + '/start/background.png')
    background = py.transform.smoothscale(background, (1000, 650))  # 缩放到任意大小
    screen.blit(background, (0, 0))  # 设置位置
    start_game = py.image.load(src_path + '/start/start_game.png')
    start_game = py.transform.smoothscale(start_game, (300, 128))
    start_button = screen.blit(start_game, (80, 330))
    start_button = Button(start_button)
    game_help = py.image.load(src_path + '/start/game_help.png')
    game_help = py.transform.smoothscale(game_help, (300, 128))
    help_button = screen.blit(game_help, (370, 330))
    help_button = Button(help_button)
    quit_game = py.image.load(src_path + '/start/quit_game.png')
    quit_game = py.transform.smoothscale(quit_game, (300, 128))
    quit_button = screen.blit(quit_game, (660, 330))
    quit_button = Button(quit_button)
    py.display.flip()
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if start_button.has(pos):
                    role = choose_role()
                    playground(role)
                    break
                elif help_button.has(pos):
                    help_page()
                    break
                elif quit_button.has(pos):
                    sys.exit()
        break
    # start()


if __name__ == '__main__':
    while True:
        start()
