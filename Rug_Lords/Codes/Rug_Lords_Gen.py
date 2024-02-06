from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import sys
import random
from PIL import Image
from random import randint
from pathlib import Path


def Get_Layers ():
    
    BackGrounds = [f for f in listdir(f"{input_path}/0 - Background") if isfile(join(f"{input_path}/0 - Background", f))]
    Base = [f for f in listdir(f"{input_path}/1 - Base") if isfile(join(f"{input_path}/1 - Base", f))]
    Eyes = [f for f in listdir(f"{input_path}/2 - Eyes") if isfile(join(f"{input_path}/2 - Eyes", f))]
    Torso = [f for f in listdir(f"{input_path}/3 - Torso") if isfile(join(f"{input_path}/3 - Torso", f))]
    Mouth = [f for f in listdir(f"{input_path}/4 - Mouth") if isfile(join(f"{input_path}/4 - Mouth", f))]
    FacialHair = [f for f in listdir(f"{input_path}/5 - Facial Hair") if isfile(join(f"{input_path}/5 - Facial Hair", f))]
    Accesories = [f for f in listdir(f"{input_path}/6 - Accesories") if isfile(join(f"{input_path}/6 - Accesories", f))]
    Head = [f for f in listdir(f"{input_path}/7 - Head") if isfile(join(f"{input_path}/7 - Head", f))]
    Facewear = [f for f in listdir(f"{input_path}/8 - Facewear") if isfile(join(f"{input_path}/8 - Facewear", f))]
    WholeHead = [f for f in listdir(f"{input_path}/9 - Whole Head") if isfile(join(f"{input_path}/9 - Whole Head", f))]


    return  BackGrounds, Base, Eyes, Torso, Mouth, FacialHair, Accesories, Head, Facewear, WholeHead


def Get_Rarities ():
    
    BackGrounds_Rarity = [10,10,10,10,10,10,10,10]
    Base_Rarity = [33,33,33]
    Eyes_Rarity = [10,10,10,10,10,10,10,10]
    Torso_Rarity=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Mouth_Rarity=[10,10,10,10,10,10]
    FacialHair_Rarity=[10,10,10,10,10,10,10,10]
    Accesories_Rarity = [10,10,10,10,10,10]
    Head_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Facewear_Rarity = [10,10,10,10,10,10,10,10,10,10,10]
    WholeHead_Rarity = [10,10,50,10,10]
    
    
    return BackGrounds_Rarity, Base_Rarity, Eyes_Rarity, Torso_Rarity, Mouth_Rarity, FacialHair_Rarity, Accesories_Rarity, Head_Rarity, Facewear_Rarity, WholeHead_Rarity

def NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity,Eyes,Eyes_Rarity,Torso,Torso_Rarity,Mouth,Mouth_Rarity,FacialHair,FacialHair_Rarity,Accesories,Accesories_Rarity,Head,Head_Rarity,Facewear,Facewear_Rarity,WholeHead, WholeHead_Rarity):
  

    NFT_BackGrounds = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Eyes = random.choices(Eyes,weights=(Eyes_Rarity))[0]
    NFT_Torso = random.choices(Torso,weights=(Torso_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]
    NFT_Accesories = random.choices(Accesories,weights=(Accesories_Rarity))[0]
    NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
    NFT_WholeHead = random.choices(WholeHead,weights=(WholeHead_Rarity))[0]  
    
    return NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead

def Get_NFT_Hands(Base):

    Base = Base.split('.')[0]

    Hand_Path = f"{input_path}/10 - Hand/{Base}/"
    Hands = [f for f in listdir(Hand_Path) if isfile(join(Hand_Path, f))]
    
    if (Base == 'Tanned'):
        Hand_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10]
    
    else:
        Hand_Rarity = [100]

    NFT_Hand = random.choices(Hands,weights=(Hand_Rarity))[0] 
    
    return NFT_Hand
    
def control_ADN(ADN_list,NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead, NFT_Hand):
    
    ADN_NFT = NFT_BackGrounds + "&" + NFT_Base + "&" + NFT_Eyes + "&" + NFT_Torso + "&" + NFT_Mouth + "&" + NFT_FacialHair + "&" + NFT_Accesories + "&" + NFT_Head + "&" + NFT_Facewear + "&" + NFT_WholeHead + "&" + NFT_Hand
    
    if (ADN_NFT in ADN_list):
        control = True
    else:
        control = False
    
    ADN_list.append(ADN_NFT)
    
    return ADN_list, control


def Eyes_Conflicts (NFT_Eyes, 
                    NFT_Head, NFT_Facewear, NFT_WholeHead, Facewear,Facewear_Rarity, Head, Head_Rarity):
    
    if (NFT_Eyes == 'Annoyed.png' or NFT_Eyes == 'Smug.png'):

        conflict_facewear = ['Shades.png']
        conflict_heads = []

        for elem in conflict_facewear:

            if elem in Facewear:

                remove_elem = Facewear.index(elem)
                Facewear.pop(remove_elem)
                Facewear_Rarity.pop(remove_elem)

        NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
        NFT_Head = NFT_Head
        NFT_WholeHead = NFT_WholeHead
    
    elif (NFT_Eyes == 'Worried.png'):

        conflict_facewear = ['Round Shades.png']

        for elem in conflict_facewear:

            if elem in Facewear:

                remove_elem = Facewear.index(elem)
                Facewear.pop(remove_elem)
                Facewear_Rarity.pop(remove_elem)

        NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
        NFT_Head = NFT_Head
        NFT_WholeHead = NFT_WholeHead

    elif (NFT_Eyes == 'Bored.png'):

        conflict_facewear = ['Shades.png','Round Shades.png','Monocle.png']

        for elem in conflict_facewear:

            if elem in Facewear:

                remove_elem = Facewear.index(elem)
                Facewear.pop(remove_elem)
                Facewear_Rarity.pop(remove_elem)
            
        NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
        NFT_Head = NFT_Head
        NFT_WholeHead = NFT_WholeHead

    elif (NFT_Eyes == 'Neutral.png'):

        conflict_heads = ['Jafar_s Hat.png','Green Keffiyeh.png','Red Turban.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)
            
        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_Facewear = NFT_Facewear
        NFT_WholeHead = NFT_WholeHead

    elif (NFT_Eyes == 'Blue Laser Eyes.png' or NFT_Eyes == 'Green Laser Eyes.png'):
        
        conflict_heads = ['Emamah.png','Orange Keffiyeh.png','Messy Hair.png','Dreadlocks.png','Brown Quiff.png','Small Dreadlocks.png','Crazy Hair.png']
         
        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)
        
        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_Facewear = 'none.png'
        NFT_WholeHead = 'none.png'
    
    elif (NFT_Eyes == 'Side Eye.png'):

        conflict_heads = ['Panama Hat.png','Red Turban.png','Helmet.png','Red Keffiyeh.png','Boat Cap.png','Emamah.png']
        conflict_facewear = ['Black Glasses.png','Gold Glasses.png','Reading Glasses.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)
                

        for elem in conflict_facewear:
            
            if elem in Facewear:

                remove_elem = Facewear.index(elem)
                Facewear.pop(remove_elem)
                Facewear_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
        NFT_WholeHead = NFT_WholeHead

    return NFT_Head, NFT_Facewear, NFT_WholeHead

def Bandana_Conflicts (NFT_Mouth, 
                       NFT_Head, NFT_FacialHair, Head, Head_Rarity, FacialHair,FacialHair_Rarity,NFT_WholeHead):

    if (NFT_Mouth == 'BTC Bandana.png' or NFT_Mouth == 'Cigar.png' or NFT_Mouth == 'Pipe.png'):
        
        conflict_heads = ['Grey Keffiyeh.png','Brown Bedouin.png','Bedouin.png','Orange Keffiyeh.png','Long Windswept Hair.png','Jafar_s Hat.png','Green Keffiyeh.png','Wavy Black Hair.png','Red Keffiyeh.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_FacialHair = 'none.png'
        NFT_WholeHead = 'none.png'

        
        
    elif (NFT_Mouth == 'Smile.png'):

        conflict_facialhair = ['Light.png','Moustache.png','Red.png','Black.png']
        
        for elem in conflict_facialhair:

            if elem in FacialHair:

                remove_elem = FacialHair.index(elem)
                FacialHair.pop(remove_elem)
                FacialHair_Rarity.pop(remove_elem)
                
        NFT_Head = NFT_Head
        NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]
        NFT_WholeHead = NFT_WholeHead
    
    elif (NFT_Mouth == 'Smirk.png'):

        conflict_facialhair = ['Light.png']
        
        for elem in conflict_facialhair:

            if elem in FacialHair:

                remove_elem = FacialHair.index(elem)
                FacialHair.pop(remove_elem)
                FacialHair_Rarity.pop(remove_elem)
                
        NFT_Head = NFT_Head
        NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]
        NFT_WholeHead = NFT_WholeHead
    else:
        NFT_Head = NFT_Head
        NFT_FacialHair = NFT_FacialHair
        NFT_WholeHead = NFT_WholeHead
    
    return NFT_Head, NFT_FacialHair,NFT_WholeHead

def FacialHair_Conflicts (NFT_FacialHair, 
                          NFT_Head, NFT_WholeHead, Head, Head_Rarity):

    if (NFT_FacialHair == 'Black.png' or NFT_FacialHair == 'Grey.png' or NFT_FacialHair == 'Neck.png' or NFT_FacialHair == 'Red.png' or NFT_FacialHair == 'Thin.png'):
 
        conflict_heads = ['Boudin.png','Orange Keffiyeh.png','Long Windswept Hair.png','Jafar_s Hat.png','Wavy Black Hair.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_WholeHead = 'none.png'

    elif (NFT_FacialHair == 'Bushy.png'):

        conflict_heads = ['Grey Keffiyeh.png','Brown Boudin.png','Boudin.png','Orange Keffiyeh.png','Long Windswept Hair.png','Green Keffiyeh.png','Red Keffiyeh.png','Jafar_s Hat.png','Wavy Black Hair.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_WholeHead = 'none.png'

    else:
        NFT_Head = NFT_Head
        NFT_WholeHead = NFT_WholeHead
    
    return NFT_Head, NFT_WholeHead
    
def Accesories_Conflicts (NFT_Accesories, 
                          NFT_Head, Head, Head_Rarity):

    if (NFT_Accesories == 'Coin Earring.png' or NFT_Accesories == 'Gold Drop.png' or NFT_Accesories == 'Gold Earing.png' or NFT_Accesories == 'Silver Earring.png'):

        conflict_heads = ['Short Slick.png', 'Messy Hair.png','Emamah.png','Hemlet.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)
            
        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    elif (NFT_Accesories == 'Gold Statement.png'):
        
        conflict_heads = ['Short Slick.png', 'Messy Hair.png','Emamah.png','Hemlet.png','Orange Keffiyeh.png','Dreadlock Headband.png','Long Windswept Hair.png','Jafar_s Hat.png','Wavy Black Hair.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)
            
        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]

    else:

        NFT_Head = NFT_Head
    
    return NFT_Head


def Hand_Conflicts (NFT_Hand, 
                    NFT_Mouth, Mouth, Mouth_Rarity, 
                    NFT_FacialHair, 
                    NFT_Head, Head, Head_Rarity,
                    NFT_WholeHead, NFT_Facewear):

    if (NFT_Hand == 'Bundle.png'):

        conflict_mouth = ['BTC Bandana.png','Pipe.png']
        conflict_heads = ['Grey Keffiyeh.png','Brown Bedouin.png','Bedouin.png','Orange Keffiyeh.png','Green Keffiyeh.png','Red Keffiyeh.png','Pharaoh_s Headdress.png','Black Turban.png']

        for elem in conflict_mouth:

            if elem in Mouth:

                remove_elem = Mouth.index(elem)
                Mouth.pop(remove_elem)
                Mouth_Rarity.pop(remove_elem)
        
        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)
        
        NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_FacialHair = 'none.png'
        NFT_WholeHead = 'none.png'
        NFT_Facewear = NFT_Facewear

    elif (NFT_Hand == 'Tea.png'):

        conflict_mouth = ['BTC Bandana.png','Pipe.png','Cigar.png']

        for elem in conflict_mouth:

            if elem in Mouth:

                remove_elem = Mouth.index(elem)
                Mouth.pop(remove_elem)
                Mouth_Rarity.pop(remove_elem)

        NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
        NFT_Head = NFT_Head
        NFT_FacialHair = NFT_FacialHair
        NFT_WholeHead = NFT_WholeHead
        NFT_Facewear = NFT_Facewear

    elif (NFT_Hand == 'Big Pipe.png'):
        
        conflict_mouth = ['BTC Bandana.png','Pipe.png','Cigar.png']

        for elem in conflict_mouth:

            if elem in Mouth:

                remove_elem = Mouth.index(elem)
                Mouth.pop(remove_elem)
                Mouth_Rarity.pop(remove_elem)

        NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
        NFT_Head = NFT_Head
        NFT_FacialHair = NFT_FacialHair
        NFT_WholeHead = 'none.png'

    elif (NFT_Hand == 'Eagle.png'):

        conflict_mouth = ['Pipe.png','Cigar.png']
        
        for elem in conflict_mouth:

            if elem in Mouth:

                remove_elem = Mouth.index(elem)
                Mouth.pop(remove_elem)
                Mouth_Rarity.pop(remove_elem)

        NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
        NFT_Head = NFT_Head
        NFT_FacialHair = NFT_FacialHair
        NFT_WholeHead = NFT_WholeHead
        NFT_Facewear = NFT_Facewear
    
    elif (NFT_Hand == 'Rug.png'):
        
        conflict_mouth = ['BTC Bandana.png','Pipe.png','Cigar.png']
        conflict_heads = ['Grey Keffiyeh.png', 'Fisherman Hat.png', 'Cowboy Hat.png', 'Panama Hat.png', 'Small Dreadlocks.png', 'Messy Hair.png', 'Long Windswept Hair.png', 'Jafar_s Hat.png', 'Wavy Black Hair.png', 
                          'Boat Cap.png', 'Helmet.png', 'Red Turban.png', 'Emamah.png', 'Brown Bedouin.png', 'Bedouin.png', 'Orange Keffiyeh.png', 'Green Keffiyeh.png', 'Red Keffiyeh.png', 'Pharaoh_s Headdress.png', 'Black Turban.png']
        
        for elem in conflict_mouth:

            if elem in Mouth:

                remove_elem = Mouth.index(elem)
                Mouth.pop(remove_elem)
                Mouth_Rarity.pop(remove_elem)   

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)     

        NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]                
        NFT_WholeHead = 'none.png'
        NFT_FacialHair = 'none.png'
        NFT_Facewear = 'none.png'

    return NFT_Mouth, NFT_Head, NFT_FacialHair, NFT_WholeHead, NFT_Facewear


    
def Facewear_Conflicts (NFT_Facewear, 
                          NFT_Head, Head, Head_Rarity,
                          NFT_WholeHead):

    if (NFT_Facewear == 'Black Glasses.png' or NFT_Facewear == 'Gold Glasses.png' or 
        NFT_Facewear == 'Gold Shades.png' or NFT_Facewear == 'Reading Glasses.png' or
        NFT_Facewear == 'Round Shades.png' or NFT_Facewear == 'Shades.png' or NFT_Facewear == 'Sunglasses.png'):
        
        conflict_heads = ['Black Turban.png', 'Red Turban.png', 'Pharaoh_s Headdress.png', 'Red Keffiyeh.png', 'Emamah.png', 'Turban.png',
            'Green Keffiyeh.png', 'Jafar_s Hat.png', 'Long Windswept Hair.png', 
            'Dreadlocks Headband.png', 'Orange Keffiyeh.png', 'Bedouin.png', 'Brown Bedouin.png', 'Cowboy Hat.png',
            'Fisherman Hat.png', 'Grey Keffiyeh.png', 'Prince Turban.png', 'Red Keffiyeh.png', 'Pharaoh_s Headdress.png', 'Black Turban.png']

        for elem in conflict_heads:
            
            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]      
        NFT_WholeHead = 'none.png'

    elif (NFT_Facewear == 'Scanner.png'):
    
        conflict_heads = ['Black Turban.png', 'Red Turban.png', 'Pharaoh_s Headdress.png', 'Boat Cap.png',
            'Crazy Hair.png', 'Panama Hat.png','Ahinese Hat.png', 'Red Keffiyeh.png', 'Emamah.png', 'Turban.png',
            'Green Keffiyeh.png', 'Jafar_s Hat.png', 'Long Windswept Hair.png', 
            'Dreadlocks Headband.png', 'Orange Keffiyeh.png', 'Bedouin.png', 'Brown Bedouin.png', 'Cowboy Hat.png',
            'Fisherman Hat.png', 'Grey Keffiyeh.png', 'Prince Turban.png', 'Red Keffiyeh.png']
        
        for elem in conflict_heads:
            
            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]      
        NFT_WholeHead = 'none.png'

    elif (NFT_Facewear == 'Monocle.png'):
        
        conflict_heads = ['Black Turban.png', 'Red Turban.png', 'Green Keffiyeh.png', 'Jafar_s Hat.png', 'Orange Keffiyeh.png', 'Grey Keffiyeh.png', 'Prince Turban.png']
        
        for elem in conflict_heads:
            
            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]      
        NFT_WholeHead = 'none.png'

    elif (NFT_Facewear == '3D Glasses.png'):
        
        conflict_heads = ['Black Turban.png', 'Red Turban.png', 'Pharaoh_s Headdress.png', 'Red Keffiyeh.png', 'Turban.png',
            'Green Keffiyeh.png', 'Jafar_s Hat.png', 'Long Windswept Hair.png', 
            'Dreadlocks Headband.png', 'Orange Keffiyeh.png', 'Bedouin.png', 'Brown Bedouin.png', 'Cowboy Hat.png',
            'Fisherman Hat.png', 'Grey Keffiyeh.png', 'Prince Turban.png', 'Red Keffiyeh.png', 'Pharaoh_s Headdress.png', 'Black Turban.png']
        
        for elem in conflict_heads:
            
            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]      
        NFT_WholeHead = 'none.png'
    else:
        NFT_Head = NFT_Head
        NFT_WholeHead = NFT_WholeHead

    return NFT_Head, NFT_WholeHead

def get_Images (NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead, NFT_Hand):
    
    Base = NFT_Base.split('.')[0]

    Image_BackGrounds = f'{input_path}/0 - Background/'+NFT_BackGrounds
    Image_Base = f'{input_path}/1 - Base/'+NFT_Base
    Image_Eyes = f'{input_path}/2 - Eyes/'+NFT_Eyes
    Image_Torso = f'{input_path}/3 - Torso/'+NFT_Torso
    Image_Mouth = f'{input_path}/4 - Mouth/'+NFT_Mouth
    Image_FacialHair = f'{input_path}/5 - Facial Hair/'+NFT_FacialHair
    Image_Accesories = f'{input_path}/6 - Accesories/'+NFT_Accesories
    Image_Head = f'{input_path}/7 - Head/'+NFT_Head
    Image_Facewear = f'{input_path}/8 - Facewear/'+NFT_Facewear
    Image_WholeHead = f'{input_path}/9 - Whole Head/'+NFT_WholeHead
    Image_Hand = f'{input_path}/10 - Hand/{Base}/'+NFT_Hand    

    return Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand

def get_NFT_main (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand):
    
   
    BackGround_Image = Image.open(Image_BackGrounds).convert("RGBA")
    
    Base_Image = Image.open(Image_Base).convert("RGBA")

    int1 = Image.alpha_composite(BackGround_Image, Base_Image)
    
    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")

    int2 = Image.alpha_composite(int1, Eyes_Image)

    Torso_Image = Image.open(Image_Torso).convert("RGBA")

    int3 = Image.alpha_composite(int2,Torso_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Mouth_Image)

    FacialHair_Image = Image.open(Image_FacialHair).convert("RGBA")
    
    int5 = Image.alpha_composite(int4, FacialHair_Image)

    Accesories_Image = Image.open(Image_Accesories).convert("RGBA")

    int6 = Image.alpha_composite(int5, Accesories_Image)

    Head_Image = Image.open(Image_Head).convert("RGBA")

    int7 = Image.alpha_composite(int6, Head_Image)
    
    Facewear_Image = Image.open(Image_Facewear).convert("RGBA")
    
    int8 = Image.alpha_composite(int7, Facewear_Image)
    
    WholeHead_Image = Image.open(Image_WholeHead).convert("RGBA")

    int9 = Image.alpha_composite(int8, WholeHead_Image)

    Hand_Image = Image.open(Image_Hand).convert("RGBA")

    final = Image.alpha_composite(int9, Hand_Image)

    return final

def get_NFT_Hand (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand, NFT_Base, NFT_Back):

    
    ## adding back for hand trait ##
    Base = NFT_Base.split('.')[0]
    Image_Back = f'{input_path}/10 - Hand/{Base}/Back/{NFT_Back}'
    ## adding back for hand trait ##

    BackGround_Image = Image.open(Image_BackGrounds).convert("RGBA")
    
    Back_Image = Image.open(Image_Back).convert("RGBA")

    int0 = Image.alpha_composite(BackGround_Image, Back_Image)

    Base_Image = Image.open(Image_Base).convert("RGBA")

    int1 = Image.alpha_composite(int0, Base_Image)
    
    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")

    int2 = Image.alpha_composite(int1, Eyes_Image)

    Torso_Image = Image.open(Image_Torso).convert("RGBA")

    int3 = Image.alpha_composite(int2,Torso_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Mouth_Image)

    FacialHair_Image = Image.open(Image_FacialHair).convert("RGBA")
    
    int5 = Image.alpha_composite(int4, FacialHair_Image)

    Accesories_Image = Image.open(Image_Accesories).convert("RGBA")

    int6 = Image.alpha_composite(int5, Accesories_Image)

    Head_Image = Image.open(Image_Head).convert("RGBA")

    int7 = Image.alpha_composite(int6, Head_Image)
    
    Facewear_Image = Image.open(Image_Facewear).convert("RGBA")
    
    int8 = Image.alpha_composite(int7, Facewear_Image)
    
    WholeHead_Image = Image.open(Image_WholeHead).convert("RGBA")

    int9 = Image.alpha_composite(int8, WholeHead_Image)

    Hand_Image = Image.open(Image_Hand).convert("RGBA")

    final = Image.alpha_composite(int9, Hand_Image)

    return final

if __name__ == '__main__':


    ## foldering
    current_dir = Path(__file__).parent
    
    base_dir = current_dir.parent
    
    input_path = base_dir/'Traits'
    output_path = base_dir/'Generations'
    json_out_path = base_dir/'Metadata'
    
    output_path.mkdir(parents=True, exist_ok=True)
    json_out_path.mkdir(parents=True, exist_ok=True)
    ## foldering

    ## control
    ADN_list = []
    ## control
    
    i = 1

    while (i<1001):
        
        ## getting layers & rarities per run ##
        BackGrounds, Base, Eyes, Torso, Mouth, FacialHair, Accesories, Head, Facewear, WholeHead = Get_Layers ()
        BackGrounds_Rarity, Base_Rarity, Eyes_Rarity, Torso_Rarity, Mouth_Rarity, FacialHair_Rarity, Accesories_Rarity, Head_Rarity, Facewear_Rarity, WholeHead_Rarity = Get_Rarities()
        ## getting layers & rarities per run ##

        
        ##get first layers
        NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead= NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity,Eyes,
                                                                                                                                                                          Eyes_Rarity,Torso,Torso_Rarity,Mouth,Mouth_Rarity,FacialHair,
                                                                                                                                                                          FacialHair_Rarity,Accesories,Accesories_Rarity,Head,Head_Rarity,Facewear,Facewear_Rarity,
                                                                                                                                                                          WholeHead, WholeHead_Rarity)
        NFT_Hand = Get_NFT_Hands(NFT_Base)
        ##get first layers
        
        NFT_Head_Excluded = []

        #conflicts
        NFT_Head, NFT_Facewear, NFT_WholeHead = Eyes_Conflicts (NFT_Eyes, NFT_Head, NFT_Facewear, NFT_WholeHead, Facewear,Facewear_Rarity, Head, Head_Rarity)
        NFT_Head, NFT_FacialHair, NFT_WholeHead = Bandana_Conflicts (NFT_Mouth, NFT_Head, NFT_FacialHair, Head, Head_Rarity, FacialHair,FacialHair_Rarity,NFT_WholeHead)
        NFT_Head = Accesories_Conflicts (NFT_Accesories, NFT_Head, Head, Head_Rarity)
        NFT_Mouth, NFT_Head, NFT_FacialHair, NFT_WholeHead, NFT_Facewear = Hand_Conflicts (NFT_Hand,NFT_Mouth, Mouth, Mouth_Rarity,NFT_FacialHair, NFT_Head, Head, Head_Rarity,NFT_WholeHead, NFT_Facewear)
        NFT_Head, NFT_WholeHead = Facewear_Conflicts (NFT_Facewear,NFT_Head, Head, Head_Rarity,NFT_WholeHead)
        NFT_Head, NFT_WholeHead = FacialHair_Conflicts (NFT_FacialHair, NFT_Head, NFT_WholeHead, Head, Head_Rarity)
        NFT_Head, NFT_FacialHair, NFT_WholeHead = Bandana_Conflicts (NFT_Mouth, NFT_Head, NFT_FacialHair, Head, Head_Rarity, FacialHair,FacialHair_Rarity,NFT_WholeHead)
        ## control
    
        ADN_List, control = control_ADN(ADN_list,NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead, NFT_Hand)
        if control: continue
    
        ## control
    
        ##import final images
        Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand = get_Images (NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead, NFT_Hand)
        ##import final images
    
        ##image generation
        
        if (NFT_Hand != 'Rug.png' and NFT_Hand != 'Bundle.png'):

            final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand)
        
        else:
            
            if (NFT_Hand == 'Rug.png'):
                
                NFT_Back = 'Rug (back).png'
            
            else:
                NFT_Back = 'Bundle (back).png'
            
            final = get_NFT_Hand (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand, NFT_Base, NFT_Back)
        final.save (f'{output_path}/Rug_Lord #{i}.png'),

        metadata = {
            'name': f'Rug_Lord #{i}',
            'attributes': [
                {
                    'trait_type': 'Background',
                    'value': NFT_BackGrounds.split('.')[0]
                },
                {
                    'trait_type': 'Base',
                    'value': NFT_Base.split('.')[0]
                },
                {
                    'trait_type': 'Eyes',
                    'value': NFT_Eyes.split('.')[0]
                },
                {
                    'trait_type': 'Torso',
                    'value': NFT_Torso.split('.')[0]
                },
                {
                    'trait_type': 'Mouth',
                    'value': NFT_Mouth.split('.')[0]
                },
                {
                    'trait_type': 'Facial Hair',
                    'value': NFT_FacialHair.split('.')[0]
                },
                {
                    'trait_type': 'Accesories',
                    'value': NFT_Accesories.split('.')[0]
                },
                {
                   'trait_type': 'Head',
                    'value': NFT_Head.split('.')[0]
                },
                {
                    'trait_type': 'Facewear',  
                    'value': NFT_Facewear.split('.')[0]
                },
                {
                    'trait_type': '1/1',
                    'value': 'None'
                }]
            }
        

        with open(rf'{json_out_path}/Rug_Lord #{i}.json', 'w') as json_print:  # Nota el uso de 'with', que es una buena práctica para manejar archivos
            json.dump(metadata, json_print, indent=4)
        print (rf"Rug Lord #{i}")
        i+=1