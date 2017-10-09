# -*- coding: utf-8 -*-
"""
@author: salimt
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser


def converter(wantedLink, videoQuality):
    #print(wantedLink)
    url = "http://video.genyoutube.net/" + wantedLink
    
    soup = BeautifulSoup(urlopen(url), "lxml")
    #print(soup)
    for link in soup.findAll('h1', attrs={'id':'ytitle'})[-1]:
        print('\x1b[1;31;44m' + "Video Name: \n" + '\x1b[0m' + link + "\n")
    print('\x1b[1;31;44m' + "Video Quality: \n" + '\x1b[0m' + videoQuality + "p\n")

    if videoQuality == '720':   
        #list = soup.findAll('div', attrs={'class':'row'})
        for link in soup.findAll('a', attrs={'data-itag':'22'}, href=True):
            links = link.get('href')
            links = links.replace(links[537:552], "salimt" + "_")            
            webbrowser.open(links)
            print('\x1b[1;31;44m' + 'Link Succesfully Generated: ' + '\x1b[0m')
            #print()
            print (links)
            
    elif videoQuality == '360':   
        #list = soup.findAll('div', attrs={'class':'row'})
        for link in soup.findAll('a', attrs={'data-itag':'18'}, href=True):
            links = link.get('href')
            links = links.replace(links[537:552], "salimt" + "_")
            webbrowser.open(links)
            print('\x1b[1;31;44m' + 'Link Successfully Generated: ' + '\x1b[0m')
            #print()
            print (links)
            #print (link.get('href'))            
            #print(links[537:551])
    print()
    ques = input('Would you like to continue?(y/n)\n> ')
    if ques == 'y' or ques== 'Y':
        youtubeLink()
    else:
        print('Goodbye!')
        return False
        

def youtubeLink():     
    while True:
            videoCode = input('Link: ')
            if videoCode == "e":
                print("Goodbye!")
                break
            videoQuality = input('type "720" for 720p mp4\n' +\
                                 'type "360" for 360p mp4\n> ')
            print()
            #converter(videoCode)
            if videoQuality == "e":
                print("Goodbye!")
                break
            if not (videoQuality == "720" or videoQuality == "360"):
                print("Invalid Input!")
                continue
            elif not 'watch?' in videoCode:
                print('Invalid link!')
                continue
            elif videoCode.startswith('https://www.'):
                videoCode = videoCode[32:]
                converter(videoCode, videoQuality)
                print(videoCode[32:])
                print('Used protocol: https')
                break
            elif videoCode.startswith('http://www.'):
                videoCode = videoCode[31:]
                converter(videoCode, videoQuality)
                print(videoCode[31:])
                print('Used protocol: http')
                break

#            elif videoCode.startswith('https://youtu.be/'):
#                videoCode = videoCode[17:]
#                converter(videoCode, videoQuality)
#                print(videoCode[17:])
#                print('youtu.be')
#                break            
            else:
                print('Invalid input!')
                continue

    

if __name__ == '__main__':
    print('YOUTUBE LINK CONVERTER!\n' +\
      ' "press e for exit".')
    youtubeLink()
    