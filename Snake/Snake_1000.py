import pygame , sys
from random import randint

window = pygame.display.set_mode((400,430))
pygame.display.set_caption('The Ultimate Snake')
screen = pygame.Surface((400,400))
inf_string = pygame.Surface((400, 30))

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255,255,255))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))
        
def get_tale(last_x, last_y, x, y, next_x, next_y):
    if last_x == x and next_x == x:
        return 'tale1.png'
    elif last_y == y and next_y == y:
        return 'tale2.png'
    elif (last_x == x and last_y == y+40 and next_x == x+40 and next_y == y) or (last_x == x+40 and last_y == y and next_x == x and next_y == y+40):
        return 'tale3.png'
    elif (last_x == x and last_y == y+40 and next_x == x-40 and next_y == y) or (last_x == x-40 and last_y == y and next_x == x and next_y == y+40):
        return 'tale4.png'
    elif (last_x == x and last_y == y-40 and next_x == x-40 and next_y == y) or (last_x == x-40 and last_y == y and next_x == x and next_y == y-40):
        return 'tale5.png'
    else:
        return 'tale6.png'

#Menu
class Menu:
    def __init__(self, main = [120, 140 ,u'point' , (250,250,250),(250,30,250)]):
        self.main = main

    def render(self, place, font, num_point):
        for i in self.main:
            if num_point == i[5]:
                place.blit(font.render(i[2], 1, i[4]), (i[0] , i[1]-50))
            else:
                place.blit(font.render(i[2], 1, i[3]), (i[0] , i[1]-50))
    
    def menu(self):
        done = True
        font_menu = pygame.font.SysFont('Impact', 50 )
        pygame.key.set_repeat(0,0)
        pygame.mouse.set_visible(True)
        point = 0
        while done:
                inf_string.fill((0, 100, 200))
                screen.fill((0, 100, 200))
                
                mousekeys = pygame.mouse.get_pos()
                for i in self.main:
                        if mousekeys[0] > i[0] and mousekeys[0]< i[0] + 155 and mousekeys[1] > i[1] and mousekeys[1] < i[1] + 50:
                                       point = i[5]          
                self.render(screen, font_menu, point)        
                for e in pygame.event.get():
                            if e.type ==  pygame.QUIT:
                                sys.exit()
                            if e.type == pygame.KEYDOWN:
                                if e.key == pygame.K_ESCAPE:
                                    sys.exit()
                                if e.key == pygame.K_UP:
                                    if point > 0:
                                            point -= 1
                                if e.key == pygame.K_DOWN:
                                    if point < len(self.main)-1:
                                                 point += 1
                            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                                    if point == 0:
                                            done = False
                                    elif point == 1:
                                        pygame.quit()
                                    


                window.blit(inf_string, (0,0))
                window.blit(screen, (0,30))
                pygame.display.flip()


#Fonts
pygame.font.init()
speed_font = pygame.font.SysFont("Arial", 24, True)
inf_font = pygame.font.SysFont("Arial", 24, True)
end = pygame.font.SysFont('Times new roman', 50)
again = pygame.font.SysFont('Times new roman', 30)

head = Sprite(40,0,'head_up.png')
tale = Sprite(0,0,'tale1.png')
apple = Sprite(120,200,'apple.png')
last_x = 80
last_y = 80
done = True
K_direct = 'UP'
tale_list = [[0,0],[0,0]]
rand_ready = True
dir_list = [0,0,0,0]
dir_control = [[head.x-40,head.y],[head.x,head.y-40],[head.x+40,head.y],[head.x,head.y+40]]
#menucreating
main = [(120, 140, u'Start', (250,250,30), (250,30,250), 0), (130,210, u'Quit',(250,250,30),(250,30,250),1)]

game = Menu(main)
game.menu()

def game_go():
    #Variables
    head = Sprite(200,200,'head_up.png')
    tale = Sprite(200,240,'tale.png')
    apple = Sprite(120,200,'apple.png')
    last_x = 80
    last_y = 80
    done = True
    K_direct = 'UP'
    tale_list = [[200,240],[200,280]]
    rand_ready = True
    dir_list = [0,0,0,0]

    pygame.key.set_repeat(1,1)
    life = 1
    numeral = -1
    while done:
        
        
        #Tale x,y
        first_i = True
        for i in tale_list:
            if first_i:
                save_x = i[0]
                save_y = i[1]
                i[0] = head.x
                i[1] = head.y
                first_i = False
            else:
                save1_x = i[0]
                save1_y = i[1]
                i[0] = save_x
                i[1] = save_y
                save_x = save1_x
                save_y = save1_y
                
        #Keys control
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT and dir_list[0]:
                    K_direct = 'LEFT'
                if e.key == pygame.K_UP and dir_list[1]:
                    K_direct = 'UP'
                if e.key == pygame.K_RIGHT and dir_list[2]:
                    K_direct = 'RIGHT'
                if e.key == pygame.K_DOWN and dir_list[3]:
                    K_direct = 'DOWN'
                if e.key == pygame.K_ESCAPE:
                    game.menu()
        
                            

        x = -100
        y = -200
        z = -300
        #Head movement
        if K_direct == 'LEFT':
            if head.x > 0:
                head.x -= 40
            else:
                done = False
        if K_direct == 'UP':
            if head.y > 0:
                head.y -= 40
            else:
                done = False
        if K_direct == 'RIGHT':
            if head.x < 360:
                head.x += 40
            else:
                done = False
        if K_direct == 'DOWN':
            if head.y < 360:
                head.y += 40
            else:
                done = False
        
        #Death
        if [head.x,head.y] in tale_list:
            done = False
            life = 0
            if life <= 0 :
                y = 200
                x = 150
                z = 240
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        life = 1
                        numeral = 0
                    if e.key == pygame.K_ESCAPE:
                        pygame.key.set_repeat(1,1)
                        pygame.mouse.set_visible(False)
                        game.menu()
                        
        #Direct control 
        if tale_list[0] == [head.x-40,head.y] or tale_list[0] == [360,head.y] and head.x == 0:
            dir_list[0] = 0
        else:
            dir_list[0] = 1
        if tale_list[0] == [head.x,head.y-40] or tale_list[0] == [head.x,360] and head.y == 0:
            dir_list[1] = 0
        else:
            dir_list[1] = 1
        if tale_list[0] == [head.x+40,head.y] or tale_list[0] == [0,head.y] and head.x == 360:
            dir_list[2] = 0
        else:
            dir_list[2] = 1
        if tale_list[0] == [head.x,head.y+40] or tale_list[0] == [head.x,0] and head.y == 360:
            dir_list[3] = 0
        else:
            dir_list[3] = 1
        
        #Food
        if [apple.x,apple.y] == [head.x,head.y]:
            tale_list.append([save_x,save_y])
            rand_ready = True
            
        #Apple spawn
        while rand_ready:
            apple.x = randint(0,9) * 40
            apple.y = randint(0,9) * 40
            if [apple.x,apple.y] not in tale_list and [apple.x,apple.y] != [head.x,head.y]:
                rand_ready = False
                numeral += 1
        #Background        
        screen.fill((50,50,50))
        inf_string.fill((100, 100, 100))
        
        #Tale render
        num = 0
        for i in tale_list:
            if num == 0:
                tale.bitmap = pygame.image.load(get_tale(head.x, head.y, tale_list[num][0], tale_list[num][1], tale_list[num+1][0], tale_list[num+1][1]))
            elif num == len(tale_list)-1:
                if tale_list[-2][0] == i[0] and tale_list[-2][1] == i[1]-40:
                    tale.bitmap = pygame.image.load('tale_end1.png')
                elif tale_list[-2][0] == i[0]+40 and tale_list[-2][1] == i[1]:
                    tale.bitmap = pygame.image.load('tale_end2.png')
                elif tale_list[-2][0] == i[0] and tale_list[-2][1] == i[1]+40:
                    tale.bitmap = pygame.image.load('tale_end3.png')
                elif tale_list[-2][0] == i[0]-40 and tale_list[-2][1] == i[1]:
                    tale.bitmap = pygame.image.load('tale_end4.png')                    
            else:
                tale.bitmap = pygame.image.load(get_tale(tale_list[num-1][0], tale_list[num-1][1], tale_list[num][0], tale_list[num][1], tale_list[num+1][0], tale_list[num+1][1]))
            tale.x = i[0]
            tale.y = i[1]            
            tale.render()
            num += 1
        #Head render
        if K_direct == 'LEFT':
            head.bitmap = pygame.image.load('head_left.png')
        if K_direct == 'UP':
            head.bitmap = pygame.image.load('head_up.png')
        if K_direct == 'RIGHT':
            head.bitmap = pygame.image.load('head_right.png')
        if K_direct == 'DOWN':
            head.bitmap = pygame.image.load('head_down.png')
        head.render()
        
        apple.render()
        #fontwrite
        screen.blit(end.render('Game Over',1 ,(250,0,0)),(80, x))
        screen.blit(again.render ('Try Again(press Space)', 1, (0,200,100)), (60, y))
        screen.blit(again.render(u'Score: '+ str(numeral),1,(0,200,100)), (140, z))
        inf_string.blit(inf_font.render(u'Score: '+ str(numeral) , 1 ,(0,250,200)), (10,0))
        
        #fontshow
        window.blit(inf_string, (0, 0)) 
        window.blit(screen, (0, 30))
        
        
        pygame.display.flip()

        pygame.time.delay(400)
        
GO = True
go = True
while GO:
    for e in pygame.event.get():
        if go:
            game_go()
            go = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                go = True
            if e.key == pygame.K_ESCAPE:
                game.menu()
                go = True
            if e.type == pygame.QUIT:
                GO = False
            
