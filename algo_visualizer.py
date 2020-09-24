import pygame
import time
import random
import pygame.freetype
pygame.freetype.init()


pygame.init()

display_width=800
display_height=600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Algo Visualizer')
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
blue=(0,0,255)
light_blue=(0,191,255)
light_green=(102,255,102)
purple=(255,0,255)
deep_red=(204,0,0)
light_red=(255,51,51)
deep_orange=(255,128,0)
light_orange=(255,178,102)

clock= pygame.time.Clock()


def text_objects(msg,color,sizi):
    font = pygame.font.Font("ka1.ttf", sizi)
    textSurface= font.render(msg, True,color)
    return textSurface,textSurface.get_rect()


def message_to_screen(msg,color,y_displace=0,sizi=0):

    textSurf,textRect= text_objects(msg,color,sizi)
    textRect.center= (display_width/2,display_height/2  + y_displace)
    gameDisplay.blit(textSurf,textRect)


def message_to_screen_2(msg,color,x_position,y_position,size):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (x_position,y_position)
    gameDisplay.blit(textSurf, textRect)





import pygame as pg


sort_start_x = 100
sort_length_x = 600
sort_height = 350


def draw_outline_sort(x,y,width,block_size,color):
        pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, width, block_size),3)

def draw_fill_sort(x,y,width,block_size,color):
        pygame.draw.rect(gameDisplay,color,[x,y,width,block_size])


def draw_sort_algo(steps,swaps,list,green_1=-1,green_2=-1,red_1=-1,red_2=-1):
    block_size = sort_length_x / len(list)
    current_x_position = sort_start_x
    gameDisplay.fill(white)

    for i in range( len(list) ):
        if(i==green_1 or i==green_2):
            draw_fill_sort(current_x_position, sort_height-list[i],block_size,list[i],blue)
            position=current_x_position+ block_size/2
            message_to_screen_2(str(list[i]),blue,position,sort_height+10,15)

        elif (i==red_1 or i==red_2):
            draw_fill_sort(current_x_position, sort_height - list[i], block_size, list[i], red)
            position = current_x_position + block_size / 2
            message_to_screen_2(str(list[i]), red, position, sort_height + 10, 15)
        else:
            draw_outline_sort(current_x_position, sort_height - list[i], block_size, list[i], green)
            position = current_x_position + block_size / 2
            message_to_screen_2(str(list[i]), green, position, sort_height + 10, 15)
        current_x_position+=block_size


    message_to_screen_2("Swaps "+str(swaps),red,100,500,25)
    message_to_screen_2("Counts " + str(steps), red, 100, 550,25)








def bubble_sort(list):
        #gameDisplay.fill(white)
        steps=0
        swaps=0
        for i in range(len(list)-1):
            for j in range(len(list)-i-1):
                steps+=1
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        pygame.quit()
                        quit()
                draw_sort_algo(steps,swaps,list,i,j)
                if list[j]>list[j+1]:
                    swaps+=1
                    draw_sort_algo(steps,swaps,list,-1,-1,j+1,j)
                    pygame.display.update()
                    clock.tick(2)

                    temp=list[j]
                    list[j]=list[j+1]
                    list[j+1]=temp
                    draw_sort_algo(steps,swaps,list,j+1,j)

                pygame.display.update()
                clock.tick(2)

        draw_sort_algo(steps,swaps,list, -1, -1, -1, -1)
        pygame.display.update()



        while(True):
            #print(list)

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    quit()



def input_value():
    screen = gameDisplay
    font = pg.font.Font("ka1.ttf", 20)
    font_2 = pg.font.Font("ka1.ttf", 15)
    present=0

    clock = pg.time.Clock()
    input_box_1 = pg.Rect(350, 200, 1, 32)
    input_box_2 = pg.Rect(20,340,1,32)
    input_box_3 = pg.Rect(350, 450, 1, 32)
    input_box_4 = pg.Rect(350, 500, 1, 32)

    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    color_2 = color_inactive



    active_1 = False
    active_2 = False
    text_1 = ''
    text_2 = ''
    text_3 = 'Redo'
    text_4 = 'Start'
    size_of_list=0
    number_flag=0
    number_list=[]
    button_color_1 = color_inactive
    button_color_2 = color_inactive


    done = False

    while not done:
        screen.fill(white)

        message_to_screen("Values", red,  -130, 20)
        message_to_screen("Numbers", red, 10, 20)

        for event in pg.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box_1.collidepoint(event.pos):
                    # Toggle the active variable.
                    if number_flag==0:
                        active_1 = not active_1
                elif input_box_2.collidepoint(event.pos):

                    if number_flag==1:
                        active_2 = not active_2

                elif input_box_3.collidepoint(event.pos):
                    input_value()

                elif input_box_4.collidepoint(event.pos):
                    if( size_of_list==len(number_list)):
                        bubble_sort(number_list)

                else:
                    active_1 = False
                # Change the current color of the input box.
                color = color_active if active_1 else color_inactive
                color_2 = color_active if active_2 else color_inactive
            if event.type == pg.KEYDOWN:
                if active_1:
                    if event.key == pg.K_RETURN:
                        if active_1 == True:
                            #print(text_1)
                            size_of_list = int(text_1)
                            number_flag=1
                            active_1= False
                            color=color_inactive
                            #text_1 = ''
                    elif event.key == pg.K_BACKSPACE:
                            if active_1==True:
                                text_1 = text_1[:-1]
                    else:
                        if active_1==True:
                            text_1 += event.unicode
                            if int(text_1)>20:
                                text_1 = text_1[:-1]

                if active_2:
                    if event.key == pg.K_RETURN:
                        if active_2 == True:
                            if text_2[ len(text_2)-1 ] ==' ':
                                continue
                            else:
                                add_number=''
                                if( text_2[len(text_2)-2]!=' '):
                                    add_number+=text_2[len(text_2)-2]
                                if text_2[len(text_2)-1]!=' ':
                                    add_number += text_2[len(text_2) - 1]

                                number_list.append(int(add_number))
                                text_2 += '  '
                                present+=1
                    elif event.key == pg.K_BACKSPACE:
                            if active_2== True:
                                if  text_2[len(text_2)-1]==' ':
                                    continue
                                else:
                                    text_2 = text_2[:-1]
                    else:
                        if active_2==True:
                            if present == size_of_list:
                                continue
                            elif len(text_2)>1 and  text_2[len(text_2)-1] != ' ' and text_2[len(text_2)-2] != ' ':
                                continue
                            text_2 += event.unicode

        width = 200
        width_2 = 200

        input_box_1.w = width - 100
        input_box_2.w = width_2 + 550
        input_box_3.w = width - 100
        input_box_4.w = width - 100

        mouse=pg.mouse.get_pos()

        if(mouse[0]>350 and mouse[0]<450 and mouse[1]>450 and mouse[1]<482):
            button_color_1=color_active
        else:
            button_color_1=color_inactive

        if (mouse[0] > 350 and mouse[0] < 450 and mouse[1] > 500 and mouse[1] < 532):
            button_color_2 = color_active
        else:
            button_color_2 = color_inactive



        # Render the current text.
        txt_surface = font.render(text_1, True, color_active)
        txt_surface_2 = font_2.render(text_2, True, color_active)
        txt_surface_3= font.render(text_3, True, button_color_1)
        txt_surface_4= font.render(text_4, True, button_color_2)


        #print(size_of_list)

        add_ons = (770 - (770 * size_of_list)/20)/2

        # Blit the text.
        screen.blit(txt_surface, (input_box_1.x+35, input_box_1.y+5))
        screen.blit(txt_surface_2, (input_box_2.x + 10 +add_ons , input_box_2.y + 5))
        screen.blit(txt_surface_3, (input_box_3.x + 13, input_box_3.y + 5))
        screen.blit(txt_surface_4, (input_box_4.x + 8, input_box_4.y + 5))

        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box_1, 5)
        pg.draw.rect(screen, color_2, input_box_2, 5)
        pg.draw.rect(screen, button_color_1, input_box_3, 5)
        pg.draw.rect(screen, button_color_2, input_box_4, 5)

        pg.display.flip()

        #print(number_list)

        clock.tick(30)


def menu():
    intro=1
    choice=1
    while(intro):
        gameDisplay.fill(white)
        message_to_screen("Algorithm Visualizer", light_blue, -140, 40)
        message_to_screen("Sorting", red, -10, 30)
        message_to_screen("Grid", red, 40, 30)
        message_to_screen("Tree", red, 90, 30)
        if (choice == 1):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 45, display_height / 2 + 10, 90, 5])
        elif (choice == 2):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 140, display_height / 2 + 60, 280, 5])
        elif (choice == 3):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 45, display_height / 2 + 110, 90, 5])

        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_DOWN):
                    if (choice == 3):
                        choice = 1
                    else:
                        choice += 1
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    if (choice == 1):
                        choice = 3
                    else:
                        choice -= 1
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    if (choice == 1):
                         sort_menu()
                    elif (choice == 3):
                        continue




def sort_menu():
    intro = 1
    choice = 1
    while (intro):
        gameDisplay.fill(white)
        message_to_screen("Insertion", red, -40, 30)
        message_to_screen("Bubble", red, 10, 30)
        message_to_screen("Quick", red, 60, 30)
        if (choice == 1):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 45, display_height / 2 + -20, 90, 5])
        elif (choice == 2):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 140, display_height / 2 + 30, 280, 5])
        elif (choice == 3):
            pygame.draw.rect(gameDisplay, red, [display_width / 2 - 45, display_height / 2 + 80, 90, 5])

        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_DOWN):
                    if (choice == 3):
                        choice = 1
                    else:
                        choice += 1
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    if (choice == 1):
                        choice = 3
                    else:
                        choice -= 1
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    if (choice == 1):
                        input_value()
                    elif (choice == 3):
                        continue









#list_values=[43,65,45,87,45,34,87,65,34,34,22,98,66]
#bubble_sort(list_values)
menu()
sort_menu()
input_value()