import os
import urllib.request
import urllib.response
import sys
import platform

def install_pygame(url,filename):
    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        resp_data = res.read()
        file = open(filename,"wb")
        file.write(resp_data)
        file.close()
        pip.main(['install',filename])
        os.remove(filename)
    except:
        print ("The game cannot run on the current version of python")
        print ("Please download and install Python 2.7 or Python 3.4 or Python 3.5")
        print ("And run the game with that version of python")
    
try:
    import pygame
except:
    import pip
    version = str(sys.version_info.major) + str(sys.version_info.minor)
    arc = platform.architecture()
    arc = arc[0]
    if arc == "64bit":
        print ("Installing pygame")
        filename = "pygame-1.9.2a0-cp"+str(version)+"-none-win_amd64.whl"
        url = "http://dodgethat.co.uk/pygame_files/pygame-1.9.2a0-cp"+str(version)+"-none-win_amd64.whl"
        install_pygame(url,filename)
    if arc == "32bit":
        print ("Installing pygame")
        url = "http://dodgethat.co.uk/pygame_files/pygame-1.9.2a0-cp"+str(version)+"-none-win32.whl"
        filename = "pygame-1.9.2a0-cp"+str(version)+"-none-win32.whl"
        install_pygame(url,filename)
    import pygame

installed = os.path.isfile(".installed")
if not installed:
    pygame.init()
    screen = pygame.display.set_mode((400,200))
    pygame.display.set_caption("Downloading Resources...")

    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    bg = (44,62,80)
    clock = pygame.time.Clock()
    #Function to display text on the screen
    def message_to_screen(msg, color, position, fontsize):
        font = pygame.font.SysFont("comicsansms", fontsize)  # Rendering font
        screen_text = font.render(msg, True, color)  # Inserting message into font and rendering colour
        screen.blit(screen_text, [position, position])  # Displaying text on the screen
    #Funtion to display text ends here
    def get_package_list():
        req = urllib.request.Request("http://dodgethat.co.uk/dep/beta/.package")
        res = urllib.request.urlopen(req)
        resp = res.read()
        file = open(".package","wb")
        file.write(resp)
        file.close()

    if not os.path.isfile(".package"):
        get_package_list()

    if not os.path.isfile(".package"):
        get_package_list()
        
    def get_dep():
        files = []
        file = open(".package","rt")
        for lines in file:
            files.append(lines)
        file.close()
        return files
    def download_dep_file(file_name):
        url = "http://dodgethat.co.uk/dep/beta/"+file_name
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        resp = res.read()
        return resp

    def main():
        global installed
        done = False
        draw = True
        file_no = 0
        percentage = 0
        if not installed: 
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()

                if not draw:
                    files = get_dep()
                    file_len = len(files)
                    file_no = 1
                    for file in files:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit()
                        file = file.split('\n')
                        file = file[0]
                        if not os.path.isfile(file):
                            percentage = file_no / file_len
                            percentage = round (percentage * 100,1)
                            try:
                                if not os.path.exists(os.path.dirname(file)):
                                    os.makedirs(os.path.dirname(file))
                                if not os.path.exists("images/new_bars"):
                                    os.mkdir("images/new_bars")
                            except:
                                pass
                            file_downloaded = download_dep_file(file)
                            file_save = open(file,"wb")
                            file_save.write(file_downloaded)
                            file_save.close()
                            file_no += 1
                            if percentage == 100.0:
                                done = True
                            screen.fill(bg)
                            pygame.draw.rect(screen,white,[50,70,3 * percentage,40])
                            message_to_screen("Downloading Game Resources",white,[25,10],27)
                            message_to_screen(str(percentage)+"% Done",white,[175,120],17)
                            pygame.display.update()
                screen.fill(bg)
                pygame.draw.rect(screen,white,[50,70,0,40])
                message_to_screen("Downloading Game Resources",white,[25,10],27)
                message_to_screen(str(percentage)+"% Done",white,[165,120],17)
                pygame.display.update()
                clock.tick(60)
                draw = False
                if file_no == 1:
                    done = True 
    installed_file = open (".installed","wt")
    installed_file.close()       
    main()
import scripts.main