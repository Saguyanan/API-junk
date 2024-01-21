import json
import re
import requests as req


def Main():
    User_input = input('Name?(include spaces)')
    Name = {'name': User_input}


    Res = req.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?', params= Name)
    Get_Desc(Res)

def Get_Desc(Card_Data):
    Desc_Precedence = True
    Desc = ''
    try:
        Pretty_JM = Card_Data.json()['data']
        for x in Pretty_JM:
            Desc = x['desc']
            if x['type'] == 'Normal Monster':
                Desc_Precedence = False
    except:
        print('Invalid name')
        Main()    
    if Desc_Precedence:
        Graveyard_Grabber(Desc)


def Graveyard_Grabber(Effects):
    findallGY =  lambda x,y: re.findall(x, y)
    if findallGY('GY', Effects):
        for effect in re.split(r'\.', Effects):
            if findallGY('GY', effect):
                print(effect)        
    
    



if __name__ == '__main__':
    Main()

