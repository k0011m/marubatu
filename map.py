import sys
import pygame
import pyautogui
import keyboard

#pygame初期化
pygame.init()
display = pygame.display.set_mode((400,400))
pygame.display.set_caption("ゲーム")

#画像読み込み
maru_skin = pygame.image.load("ゲーム/maru.png")
batu_skin = pygame.image.load("ゲーム/batu.png")
local_skin = pygame.image.load("ゲーム/local.png")
cp_skin = pygame.image.load("ゲーム/cp.png")
retry_skin = pygame.image.load("ゲーム/retry.png")
space_skin = pygame.image.load("ゲーム/space.png")
maru_win_skin = pygame.image.load("ゲーム/maru_win.png")
batu_win_skin = pygame.image.load("ゲーム/batu_win.png")


#リサイズ
long_size = (300, 141)
local_skin = pygame.transform.scale(local_skin, (long_size))
cp_skin = pygame.transform.scale(cp_skin, (long_size))
retry_skin = pygame.transform.scale(retry_skin, (long_size))
maru_win_skin = pygame.transform.scale(maru_win_skin, (long_size))
batu_win_skin = pygame.transform.scale(batu_win_skin, (long_size))

short_size = (133, 133)
maru_skin = pygame.transform.scale(maru_skin, (short_size))
batu_skin = pygame.transform.scale(batu_skin, (short_size))
space_skin = pygame.transform.scale(space_skin, (short_size))


def win_check():
    pass


def local_game():
        global display
        display.fill((255,255,255))
        pygame.display.update()
        local_playgame = localgame()
        while True:
            if len(local_playgame.list) >= 7:
                pos = local_playgame.attack_pos(0)
                display.blit(space_skin, pos)
                pygame.display.update()
            pos = local_playgame.attack_pos(1)
            local_playgame.turn += 1
            if local_playgame.turn % 2 == 0:
                display.blit(maru_skin, pos)
            else:
                display.blit(batu_skin, pos)
            pygame.display.update()
            win_check()

class localgame:
    def __init__(self):
        self.list = []
        self.turn = 1


    def attack_pos(self,space):
        if space == 1:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pyautogui.position()
                        pos = self.check_pos(x, y,0,0)
                        if pos != (-1,-1):
                            return pos
                        
        if space == 0:
            pos_num = self.list.pop(0)
            pos_num = pos_num[0]
            pos = self.check_pos(-1,-1,1,pos_num)
            return pos

    
    def check_pos(self,x,y,space,pos_num):
        if (x <= 893 and y <= 533 and space == 0) or pos_num == 11:
            if not any(11 in i for i in self.list):
                if space != 1:
                    self.list.append((11,self.turn%2))
                return 0, 0
        elif (x <= 1026 and y <= 533 and x >= 893 and space == 0) or pos_num == 12:
            if not any(12 in i for i in self.list):
                if space != 1:
                    self.list.append((12,self.turn%2))
                return 133, 0
        elif (x >= 1026 and y <= 533 and space == 0) or pos_num == 13:
            if not any(13 in i for i in self.list):
                if space != 1:
                    self.list.append((13,self.turn%2))
                return 266, 0
        elif (x <= 893 and y <= 666 and y >= 533 and space == 0) or pos_num == 21:
            if not any(21 in i for i in self.list):
                if space != 1:
                    self.list.append((21,self.turn%2))
                return 0, 133
        elif (x >= 893 and x <= 1026 and y >= 533 and y <= 666 and space == 0) or pos_num == 22:
            if not any(22 in i for i in self.list):
                if space != 1:
                    self.list.append((22,self.turn%2))
                return 133, 133
        elif (x >= 1026 and y >= 533 and y <= 666 and space == 0) or pos_num == 23:
            if not any(23 in i for i in self.list):
                if space != 1:
                    self.list.append((23,self.turn%2))
                return 266, 133
        elif (x <= 893 and y >= 666 and space == 0) or pos_num == 31:
            if not any(31 in i for i in self.list):
                if space != 1:
                    self.list.append((31,self.turn%2))
                return 0, 266
        elif (x >= 893 and x <= 1026 and y >= 666 and space == 0) or pos_num == 32:
            if not any(32 in i for i in self.list):
                if space != 1:
                    self.list.append((32,self.turn%2))
                return 133, 266
        elif (x >= 1026 and y >= 666 and space == 0) or pos_num == 33:
            if not any(33 in i for i in self.list):
                if space != 1:
                    self.list.append((33,self.turn%2))
                return 266, 266
        return -1, -1

def main():
    global display
    display.fill((255,255,255))
    pygame.display.update()
    display.blit(local_skin, (50, 29.5))
    display.blit(cp_skin, (50, 229.5))
    pygame.display.update()

    #local_button = pygame.Rect(50, 29.5, 300, 141)
    #cp_button = pygame.Rect(50, 229.5, 300, 141)
    
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pyautogui.position()
                if y >= 600:
                    start = False
                    print('CP')
                else:
                    start = False
                    local_game()
                    print('Local')
                
                

if __name__ == '__main__':
    main()