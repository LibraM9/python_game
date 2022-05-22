# -*- coding: utf-8 -*-
# @Time    : 2022/5/21 10:08
# @Author  : Li Meng
# @File    : 原始代码.py
# @Desc    :
import pygame as py
import sys
import random
from pygame.locals import *

# ===========================================================
# ========================前期准备===========================
py.init()


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
# =========================图书馆内==========================

def knowledge(selection):
    path = 'Files\\inside_liberary\\knowledge' + str(selection) + '.jpg'
    know = py.image.load(path)
    know = py.transform.smoothscale(know, (1000, 650))
    screen.blit(know, (0, 0))
    exits = py.image.load('Files\\inside_liberary\\back.png')
    exits = py.transform.smoothscale(exits, (72, 72))
    exit_button = screen.blit(exits, (918, 570))
    exit_button = Button(exit_button)
    py.display.flip()
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
    ilib = py.image.load('Files\\inside_liberary\\Inside.jpg')
    ilib = py.transform.smoothscale(ilib, (1000, 650))
    screen.blit(ilib, (0, 0))
    # 退出图书馆的按钮
    exits = py.image.load('Files\\inside_liberary\\exit.png')
    exits = py.transform.smoothscale(exits, (72, 81))
    exit_button = screen.blit(exits, (5, 560))
    exit_button = Button(exit_button)
    # 厨余垃圾按钮
    rubbish1 = py.image.load('Files\\inside_liberary\\rubbish1.png')
    rubbish1 = py.transform.smoothscale(rubbish1, (150, 298))
    rubbish1_button = screen.blit(rubbish1, (80, 150))
    rubbish1_button = Button(rubbish1_button)
    # 可回收垃圾按钮
    rubbish2 = py.image.load('Files\\inside_liberary\\rubbish2.png')
    rubbish2 = py.transform.smoothscale(rubbish2, (150, 298))
    rubbish2_button = screen.blit(rubbish2, (310, 150))
    rubbish2_button = Button(rubbish2_button)
    # 有害垃圾按钮
    rubbish3 = py.image.load('Files\\inside_liberary\\rubbish3.png')
    rubbish3 = py.transform.smoothscale(rubbish3, (150, 298))
    rubbish3_button = screen.blit(rubbish3, (540, 150))
    rubbish3_button = Button(rubbish3_button)
    # 不可回收垃圾按钮
    rubbish4 = py.image.load('Files\\inside_liberary\\rubbish4.png')
    rubbish4 = py.transform.smoothscale(rubbish4, (150, 298))
    rubbish4_button = screen.blit(rubbish4, (770, 150))
    rubbish4_button = Button(rubbish4_button)
    # 图鉴按钮
    rubbish5 = py.image.load('Files\\inside_liberary\\rubbish5.png')
    rubbish5 = py.transform.smoothscale(rubbish5, (82, 72))
    rubbish5_button = screen.blit(rubbish5, (903, 560))
    rubbish5_button = Button(rubbish5_button)

    py.display.flip()
    selection = -1
    # 进入事件循环
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                # 点击离开图书馆
                if exit_button.has(pos):
                    selection = 0
                    break
                # 点击厨余垃圾
                if rubbish1_button.has(pos):
                    selection = 1
                    break
                # 点击可回收垃圾
                if rubbish2_button.has(pos):
                    selection = 2
                    break
                # 点击有害垃圾
                if rubbish3_button.has(pos):
                    selection = 3
                    break
                # 点击不可回收垃圾
                if rubbish4_button.has(pos):
                    selection = 4
                    break
                # 点击图鉴
                if rubbish5_button.has(pos):
                    selection = 5
                    break
        if selection != -1:
            break
    if selection:
        knowledge(selection)
        inside_Liberary()


# ===========================================================
# =========================图书馆外==========================

def outside_Liberary():
    olib = py.image.load('Files\\outside_liberary\\Outside.jpg')
    olib = py.transform.smoothscale(olib, (1000, 650))
    screen.blit(olib, (0, 0))
    # 进入图书馆的按钮
    enter = py.image.load('Files\\outside_liberary\\enter_lib.png')
    enter = py.transform.smoothscale(enter, (72, 72))
    enter_button = screen.blit(enter, (470, 550))
    enter_button = Button(enter_button)
    # 退出图书馆的按钮
    exits = py.image.load('Files\\outside_liberary\\playground.png')
    exits = py.transform.smoothscale(exits, (72, 51))
    exit_button = screen.blit(exits, (5, 590))
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
                # 点击进入图书馆
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
    background = py.image.load('Files\\help\\background.jpg')
    background = py.transform.smoothscale(background, (1000, 650))
    screen.blit(background, (0, 0))
    # 返回按钮
    exits = py.image.load('Files\\help\\back.png')
    exits = py.transform.smoothscale(exits, (72, 57))
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
    path = 'Files\\game_over\\result' + str(result) + '.png'
    background = py.image.load(path)
    background = py.transform.smoothscale(background, (1000, 650))
    screen.blit(background, (0, 0))
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

choices = ['01', '02', '11', '12', '21', '22', '31']


class Rubbish():
    def __init__(self, sort):
        self.sort = sort
        self.img = py.image.load('Files\\playground\\' + sort + '.png')
        x = random.randint(100, 1400)
        y = random.randint(110, 900)
        self.position = self.img.get_rect()
        self.position = self.position.move((x, y))
        screen.blit(self.img, self.position)


class Role():
    def __init__(self, role):
        self.r_side = py.image.load('Files\\playground\\' + role + '1.png')
        self.r_walk = py.image.load('Files\\playground\\' + role + '2.png')
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
        self.img = py.image.load('Files\\playground\\' + str(num) + '.png')
        self.img = py.transform.smoothscale(self.img, (100, 92))
        self.position = self.img.get_rect()
        self.position = self.position.move((100 + num * 200, 0))
        screen.blit(self.img, self.position)


def playground(selection):
    background = py.image.load('Files\\playground\\Playground.jpg')
    screen.blit(background, [0, 0])
    lib = py.image.load('Files\\playground\\liberary.png')
    lib = py.transform.smoothscale(lib, (78, 72))
    lib_button = screen.blit(lib, (900, 10))
    lib_button = Button(lib_button)
    trash_can = []
    for num in range(0, 4):
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
        lib = py.image.load('Files\\playground\\liberary.png')
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
    background = py.image.load('Files\\choose_player\\background.jpg')
    background = py.transform.smoothscale(background, (1000, 650))
    screen.blit(background, (0, 0))
    man = py.image.load('Files\\choose_player\\man.png')
    man = py.transform.smoothscale(man, (123, 325))
    man_button = screen.blit(man, (200, 200))
    man_button = Button(man_button)
    woman = py.image.load('Files\\choose_player\\woman.png')
    woman = py.transform.smoothscale(woman, (113, 325))
    woman_button = screen.blit(woman, (687, 200))
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
    background = py.image.load('Files\\start\\background.jpg')
    background = py.transform.smoothscale(background, (1000, 650))
    screen.blit(background, (0, 0))
    start_game = py.image.load('Files\\start\\start_game.png')
    start_game = py.transform.smoothscale(start_game, (140, 149))
    start_button = screen.blit(start_game, (150, 330))
    start_button = Button(start_button)
    game_help = py.image.load('Files\\start\\game_help.png')
    game_help = py.transform.smoothscale(game_help, (280, 182))
    help_button = screen.blit(game_help, (380, 320))
    help_button = Button(help_button)
    quit_game = py.image.load('Files\\start\\quit_game.png')
    quit_game = py.transform.smoothscale(quit_game, (200, 160))
    quit_button = screen.blit(quit_game, (680, 330))
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
    start()


start()
