import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img=pg.image.load("fig/pg_bg.jpg")
    kk_img=pg.image.load("fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)
    kk_img=pg.transform.rotozoom(kk_img,10,1.0)
    bg_img2=pg.transform.flip(bg_img,True,False)

    kk_rct = kk_img.get_rect() 
    kk_rct.center = 300, 200 
    
    key_lst = pg.key.get_pressed() 


    tmr = 0
    

    while True:
        hensutate=0
        hensuyoko=0
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst=pg.key.get_pressed() 
        if key_lst[pg.K_UP]:
            hensutate-=1
        if key_lst[pg.K_DOWN]:
            hensutate+=1
        if key_lst[pg.K_LEFT]:
            hensuyoko-=1
        if key_lst[pg.K_RIGHT]:
            hensuyoko+=2
        else:
            hensuyoko-=1
            

        

        kk_rct.move_ip((hensuyoko,hensutate))

        x=tmr%3200
        screen.blit(bg_img, [-x,0])
        screen.blit(bg_img, [-x+3200,0])
        screen.blit(bg_img2, [-x+1600,0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1     
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()