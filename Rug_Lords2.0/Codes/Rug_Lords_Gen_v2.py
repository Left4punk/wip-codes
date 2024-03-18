from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import sys
import random
from PIL import Image
from random import randint
from pathlib import Path

def Get_One_on_Ones ():

    NFTs = [f for f in listdir(f"{input_path}/Honoraries") if isfile(join(f"{input_path}/Honoraries", f))]

    return NFTs

def Get_Layers ():
    
    
    BackGrounds = [f for f in listdir(f"{input_path}/0 - Background") if isfile(join(f"{input_path}/0 - Background", f))]
    Base = [f for f in listdir(f"{input_path}/1 - Base") if isfile(join(f"{input_path}/1 - Base", f))]
    Torso = [f for f in listdir(f"{input_path}/2 - Torso") if isfile(join(f"{input_path}/2 - Torso", f))]
    Mouth = [f for f in listdir(f"{input_path}/3 - Mouth") if isfile(join(f"{input_path}/3 - Mouth", f))]
    Eyes = [f for f in listdir(f"{input_path}/4 - Eyes") if isfile(join(f"{input_path}/4 - Eyes", f))]
    FacialHair = [f for f in listdir(f"{input_path}/5 - Facial Hair") if isfile(join(f"{input_path}/5 - Facial Hair", f))]
    Facewear = [f for f in listdir(f"{input_path}/6 - Facewear") if isfile(join(f"{input_path}/6 - Facewear", f))]
    Head = [f for f in listdir(f"{input_path}/7 - Head") if isfile(join(f"{input_path}/7 - Head", f))]
    WholeBody = [f for f in listdir(f"{input_path}/8 - Whole Body") if isfile(join(f"{input_path}/8 - Whole Body", f))]
    WholeHead = [f for f in listdir(f"{input_path}/9 - Whole Head") if isfile(join(f"{input_path}/9 - Whole Head", f))]

    return  BackGrounds, Base, Torso, Mouth, Eyes, FacialHair, Facewear, Head, WholeBody, WholeHead


def Get_Rarities ():
    
    BackGrounds_Rarity = [10,10,10,10,10,10,10,10,10]
    Base_Rarity = [10,10,10,10,10]
    Torso_Rarity=[10,10,10,10,10,10,10,10,10,10,10]
    Mouth_Rarity=[10,10,50,10,10]
    Eyes_Rarity = [10,10,10,10,10,10]
    FacialHair_Rarity=[10,10,10,10,10,50,10]
    Facewear_Rarity = [10,10,50,10,10]
    Head_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,40,10,10,10,10,10,10,10]
    WholeBody_Rarity = [10,60,10,10,10]
    WholeHead_Rarity = [10,10,10,10,60]
    
    
    return BackGrounds_Rarity, Base_Rarity, Torso_Rarity, Mouth_Rarity, Eyes_Rarity, FacialHair_Rarity, Facewear_Rarity, Head_Rarity, WholeBody_Rarity, WholeHead_Rarity

def NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity, Torso, Torso_Rarity, Mouth, Mouth_Rarity, Eyes, Eyes_Rarity, FacialHair, FacialHair_Rarity, Facewear, Facewear_Rarity, Head, Head_Rarity, WholeBody, WholeBody_Rarity, WholeHead, WholeHead_Rarity):
  

    NFT_BackGrounds = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Torso = random.choices(Torso,weights=(Torso_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_Eyes = random.choices(Eyes,weights=(Eyes_Rarity))[0]
    NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]
    NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
    NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    NFT_WholeBody = random.choices(WholeBody,weights=(WholeBody_Rarity))[0]
    NFT_WholeHead = random.choices(WholeHead,weights=(WholeHead_Rarity))[0]  
    
    return NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_WholeHead

def Get_NFT_Hands(Base):

    Base = Base.split('.')[0]

    Hand_Path = f"{input_path}/10 - Hand/{Base}/"
    Hands = [f for f in listdir(Hand_Path) if isfile(join(Hand_Path, f))]
    if (Base == 'Black' or Base == 'Tan' or Base == 'White'):
        Hand_Rarity = [10,10,10,10,10,50,10,10,10,10,10,10]
    else:
        Hand_Rarity = [10,50,10,10,10,10,10,10]
    NFT_Hand = random.choices(Hands,weights=(Hand_Rarity))[0] 
    
    return NFT_Hand
    
def control_ADN(NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_WholeHead, NFT_Hand):
    
    ADN_NFT = NFT_BackGrounds + "&" + NFT_Base + "&" + NFT_Torso + "&" + NFT_Mouth + "&" + NFT_Eyes + "&" + NFT_FacialHair + "&" + NFT_Facewear + "&" + NFT_Head + "&" + NFT_WholeBody + "&" + NFT_WholeHead + "&" + NFT_Hand
    
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
                       NFT_Head, NFT_FacialHair, Head, Head_Rarity, FacialHair,FacialHair_Rarity,NFT_WholeHead,NFT_Facewear):

    if (NFT_Mouth == 'BTC Bandana.png'):
        
        conflict_heads = ['Grey Keffiyeh.png','Brown Bedouin.png','Bedouin.png','Orange Keffiyeh.png','Long Windswept Hair.png','Jafar_s Hat.png','Green Keffiyeh.png','Wavy Black Hair.png','Red Keffiyeh.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_FacialHair = 'none.png'
        NFT_WholeHead = 'none.png'
        NFT_Facewear = 'none.png'

    if (NFT_Mouth == 'Cigar.png' or NFT_Mouth == 'Pipe.png'):
        
        conflict_heads = ['Grey Keffiyeh.png','Brown Bedouin.png','Bedouin.png','Orange Keffiyeh.png','Long Windswept Hair.png','Jafar_s Hat.png','Green Keffiyeh.png','Wavy Black Hair.png','Red Keffiyeh.png']

        for elem in conflict_heads:

            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
        NFT_FacialHair = 'none.png'
        NFT_WholeHead = 'none.png'
        NFT_Facewear = NFT_Facewear
        
        
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
        NFT_Facewear = NFT_Facewear
    else:
        NFT_Head = NFT_Head
        NFT_FacialHair = NFT_FacialHair
        NFT_WholeHead = NFT_WholeHead
        NFT_Facewear = NFT_Facewear
    
    return NFT_Head, NFT_FacialHair,NFT_WholeHead, NFT_Facewear

def FacialHair_Conflicts (NFT_Mouth, NFT_FacialHair, FacialHair, FacialHair_Rarity):

    if (NFT_Mouth == 'Smirk.png'):
 
        conflict_FacialHair = ['Goatee.png']

        for elem in conflict_FacialHair:

            if elem in FacialHair:

                remove_elem = FacialHair.index(elem)
                FacialHair.pop(remove_elem)
                FacialHair_Rarity.pop(remove_elem)

        NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]

    else:

        NFT_FacialHair = NFT_FacialHair
    return NFT_FacialHair
    
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

def Head_Conflicts (NFT_Eyes, NFT_Head, Head, Head_Rarity):

    if (NFT_Eyes == 'Bored.png'):

        conflict_head = ['Black Turban.png', 'Fez.png']

        for elem in conflict_head:

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


    
def Facewear_Conflicts (NFT_Head,NFT_Facewear, Facewear, Facewear_Rarity):

    if (NFT_Head == 'Ice Cap.png' or NFT_Head == 'Tattoo.png'):
        
        conflict_facewear = ['Shades.png', 'Vision Pro.png']

        for elem in conflict_facewear:
            
            if elem in Facewear:

                remove_elem = Facewear.index(elem)
                Facewear.pop(remove_elem)
                Facewear_Rarity.pop(remove_elem)

        NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]      
    
    elif (NFT_Head == 'Headband.png'):
        
        conflict_facewear = ['Gold.png', 'Vision Pro.png']

        for elem in conflict_facewear:
            
            if elem in Facewear:

                remove_elem = Facewear.index(elem)
                Facewear.pop(remove_elem)
                Facewear_Rarity.pop(remove_elem)

        NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]  
    
    elif (NFT_Head == 'Fez.png'):
        
        conflict_facewear = ['Vision Pro.png']

        for elem in conflict_facewear:
            
            if elem in Facewear:

                remove_elem = Facewear.index(elem)
                Facewear.pop(remove_elem)
                Facewear_Rarity.pop(remove_elem)

        NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]  

    elif (NFT_Head == 'Windswept.png'):
        
        NFT_Facewear = 'None.png'

    else:

        NFT_Facewear = NFT_Facewear
    
    return NFT_Facewear
##
def get_Images (NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_WholeHead,NFT_Hand):
    
    Base = NFT_Base.split('.')[0]

    Image_BackGrounds = f'{input_path}/0 - Background/'+NFT_BackGrounds
    Image_Base = f'{input_path}/1 - Base/'+NFT_Base
    Image_Torso = f'{input_path}/2 - Torso/'+NFT_Torso
    Image_Mouth = f'{input_path}/3 - Mouth/'+NFT_Mouth
    Image_Eyes = f'{input_path}/4 - Eyes/'+NFT_Eyes
    Image_FacialHair = f'{input_path}/5 - Facial Hair/'+NFT_FacialHair
    Image_Facewear = f'{input_path}/6 - Facewear/'+NFT_Facewear
    Image_Head = f'{input_path}/7 - Head/'+NFT_Head
    Image_WholeBody = f'{input_path}/8 - Whole Body/'+NFT_WholeBody
    Image_WholeHead = f'{input_path}/9 - Whole Head/'+NFT_WholeHead
    Image_Hand = f'{input_path}/10 - Hand/{Base}/'+NFT_Hand    

    return Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_WholeHead, Image_Hand


def get_NFT_main2 (Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_WholeHead, Image_Hand):
    
   
    BackGround_Image = Image.open(Image_BackGrounds).convert("RGBA")
    
    Base_Image = Image.open(Image_Base).convert("RGBA")

    int1 = Image.alpha_composite(BackGround_Image, Base_Image)
    
    Torso_Image = Image.open(Image_Torso).convert("RGBA")

    int2 = Image.alpha_composite(int1, Torso_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")

    int3 = Image.alpha_composite(int2,Mouth_Image)

    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Eyes_Image)

    FacialHair_Image = Image.open(Image_FacialHair).convert("RGBA")
    
    int5 = Image.alpha_composite(int4, FacialHair_Image)

    Facewear_Image = Image.open(Image_Facewear).convert("RGBA")

    int6 = Image.alpha_composite(int5, Facewear_Image)

    Head_Image = Image.open(Image_Head).convert("RGBA")

    int7 = Image.alpha_composite(int6, Head_Image)
    
    WholeBody_Image = Image.open(Image_WholeBody).convert("RGBA")
    
    int8 = Image.alpha_composite(int7, WholeBody_Image)
    
    WholeHead_Image = Image.open(Image_WholeHead).convert("RGBA")

    int9 = Image.alpha_composite(int8, WholeHead_Image)

    Hand_Image = Image.open(Image_Hand).convert("RGBA")
    
    final = Image.alpha_composite(int9, Hand_Image)

    return final


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

def  get_One_on_One (NFTs, position_list):
        
    NFT_Name = NFTs[0]
    One_On_One_NFT_Image = rf'{input_path}/Honoraries/'+NFT_Name
    NFT_One_On_One = Image.open(One_On_One_NFT_Image).convert("RGBA")
    NFT_One_On_One.save (f'{output_path}/Rug_Lord #{i}.png')
    position_list.pop(0)
    NFTs.pop(0)

    metadata = {
            'name': f'Rug_Lord #{i}',
            'attributes': [
                {
                    'trait_type': 'Background',
                    'value': '1/1'
                },
                {
                    'trait_type': 'Base',
                    'value': '1/1'
                },
                {
                    'trait_type': 'Eyes',
                    'value': '1/1'
                },
                {
                    'trait_type': 'Torso',
                    'value': '1/1'
                },
                {
                    'trait_type': 'Mouth',
                    'value': '1/1'
                },
                {
                    'trait_type': 'Facial Hair',
                    'value': '1/1'
                },
                {
                    'trait_type': 'Accesories',
                    'value': '1/1'
                },
                {
                   'trait_type': 'Head',
                    'value': '1/1'
                },
                {
                    'trait_type': 'Facewear',  
                    'value': '1/1'
                },
                {
                    'trait_type': 'Whole Head',  
                    'value': '1/1'
                },
                {
                    'trait_type': 'Hand',  
                    'value': '1/1'
                },
                {
                    'trait_type': '1/1',
                    'value': NFT_Name.split('.')[0]
                }]
            }
    with open(rf'{json_out_path}/Rug_Lord #{i}.json', 'w') as json_print:  # Nota el uso de 'with', que es una buena práctica para manejar archivos
            json.dump(metadata, json_print, indent=4)

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
    
    ## adding 1on1s
    NFTs = Get_One_on_Ones()
    random.shuffle(NFTs)
    number_of_ones = 9
    collection_number = 1001 
    position_list = random.sample(range(1, collection_number), number_of_ones)
    position_list.sort()
    
    print (position_list)
    ## adding 1on1s
    
    i = 1
    while (i<collection_number):
        
        if (len(position_list)!=0 and i == position_list[0]):
            
            get_One_on_One (NFTs, position_list)

            print (rf"Rug Lord #{i}")
            i+=1
            continue

            
        ## getting layers & rarities per run ##
        BackGrounds, Base, Torso, Mouth, Eyes, FacialHair, Facewear, Head, WholeBody, WholeHead = Get_Layers ()
        BackGrounds_Rarity, Base_Rarity, Torso_Rarity, Mouth_Rarity, Eyes_Rarity, FacialHair_Rarity, Facewear_Rarity, Head_Rarity, WholeBody_Rarity, WholeHead_Rarity = Get_Rarities()
        ## getting layers & rarities per run ##

        ##get first layers
        NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_WholeHead = NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity, Torso, Torso_Rarity,
                                                                                                                                                              Mouth, Mouth_Rarity, Eyes, Eyes_Rarity, FacialHair, FacialHair_Rarity, Facewear, Facewear_Rarity,
                                                                                                                                                                      Head, Head_Rarity, WholeBody, WholeBody_Rarity, WholeHead, WholeHead_Rarity
                                                                                                                                                                          )

        NFT_Hand = Get_NFT_Hands(NFT_Base)
        ##get first layers
        
        NFT_Head_Excluded = []

        #conflicts
        #NFT_Head, NFT_Facewear, NFT_WholeHead = Eyes_Conflicts (NFT_Eyes, NFT_Head, NFT_Facewear, NFT_WholeHead, Facewear,Facewear_Rarity, Head, Head_Rarity)
        #NFT_Head = Accesories_Conflicts (NFT_Accesories, NFT_Head, Head, Head_Rarity)
        #NFT_Mouth, NFT_Head, NFT_FacialHair, NFT_WholeHead, NFT_Facewear = Hand_Conflicts (NFT_Hand,NFT_Mouth, Mouth, Mouth_Rarity,NFT_FacialHair, NFT_Head, Head, Head_Rarity,NFT_WholeHead, NFT_Facewear)
        #NFT_Head, NFT_WholeHead = Facewear_Conflicts (NFT_Facewear,NFT_Head, Head, Head_Rarity,NFT_WholeHead)
        NFT_Facewear = Facewear_Conflicts (NFT_Head,NFT_Facewear, Facewear, Facewear_Rarity)
        NFT_FacialHair  = FacialHair_Conflicts (NFT_Mouth, NFT_FacialHair, FacialHair, FacialHair_Rarity)
        #NFT_Head, NFT_FacialHair, NFT_WholeHead,NFT_Facewear = Bandana_Conflicts (NFT_Mouth, NFT_Head, NFT_FacialHair, Head, Head_Rarity, FacialHair,FacialHair_Rarity,NFT_WholeHead,NFT_Facewear)
        NFT_Head = Head_Conflicts (NFT_Eyes, NFT_Head, Head, Head_Rarity)
        ## control
    
        ADN_List, control = control_ADN(NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_WholeHead, NFT_Hand)
        if control: continue

        ## control
        ##full restrictive controls

        if (NFT_Mouth == 'Pipe.png' or NFT_Mouth == 'Cigar.png' or NFT_Mouth == 'Cigarrette.png'):
            
            NFT_FacialHair = 'None.png'
            NFT_WholeBody = 'None.png'
            NFT_WholeHead = 'None.png'
            conflict_head = ['Windswept.png', 'Long.png', 'Keffiyeh.png', 'Boudin.png']

            for elem in conflict_head:

                if elem in Head:

                    remove_elem = Head.index(elem)
                    Head.pop(remove_elem)
                    Head_Rarity.pop(remove_elem)
            
            NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]

            #print('1')
        elif (NFT_Mouth == 'Smirk.png'):

            NFT_FacialHair = random.choices(['Brown.png','Bushy.png','Grey.png','Grey.png','None.png','Stubble.png'],weights=(50,50,50,50,50,50))[0]
            #print('2')

        if (NFT_Eyes == 'Blue Laser.png' or NFT_Eyes == 'Green Laser.png'):

            NFT_Facewear = 'None.png'
            NFT_WholeHead = 'None.png'
            conflict_head = ['Mt Gox.png', 'Ghost.png', 'BTC.png', 'Black Turban.png']

            for elem in conflict_head:

                if elem in Head:

                    remove_elem = Head.index(elem)
                    Head.pop(remove_elem)
                    Head_Rarity.pop(remove_elem)
            
            NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
            #print('3')
        
        if (NFT_Head == 'Black Turban.png' or NFT_Head == 'Boudin.png' or NFT_Head == 'BTC.png' or NFT_Head == 'Crown.png' or NFT_Head == 'Emamah.png' or NFT_Head == 'Ghost.png' or
            NFT_Head == 'Helmet.png' or NFT_Head == 'Keffiyeh.png' or NFT_Head == 'Long.png' or NFT_Head == 'Mt Gox.png' or NFT_Head == 'Pablo.png' or NFT_Head == 'Short.png' or 
            NFT_Head == 'Turban.png' or NFT_Head == 'White Bordir.png' or NFT_Head == 'Windswept'):

            NFT_Facewear = 'None.png'
            #print('4')
        
        if (NFT_WholeBody != 'None.png'):
            
            #NFT_Torso = 'None.png'
            NFT_Head = 'None.png'
            NFT_WholeHead = 'None.png'
            NFT_Facewear = 'None.png'
            NFT_Mouth = random.choices(['Smirk.png','Neutral.png'],weights=(50,50))[0]
            #print('5')

        if (NFT_WholeHead != 'None.png'):

            NFT_Head = 'None.png'
            NFT_Mouth = 'Neutral.png'
            NFT_Facewear = 'None.png'
            #print('6')

        if (NFT_Mouth == 'Pipe.png' or NFT_Mouth == 'Cigar.png' or NFT_Mouth == 'Cigarrette.png'):

            NFT_FacialHair = 'None.png'

        ##other controls
        ##import final images
        ##change el import ficant la hand
        #Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_WholeHead = get_Images (NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, 
        #                                                                                                                                                                               NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_WholeHead)
        Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_WholeHead, Image_Hand = get_Images (NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, 
                                                                                                                                                                                       NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_WholeHead,NFT_Hand)
        ##import final images
        ##image generation
        
        #if (NFT_Hand != 'Rug.png' and NFT_Hand != 'Bundle.png'):

        #    final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand)
        
        #else:
            
        #    if (NFT_Hand == 'Rug.png'):
                
        #        NFT_Back = 'Rug (back).png'
            
        #    else:
        #        NFT_Back = 'Bundle (back).png'
        #        final = get_NFT_Hand (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand, NFT_Base, NFT_Back)
        final = get_NFT_main2 (Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_WholeHead, Image_Hand)
        #final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand)
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
                    'value': Image_WholeBody.split('.')[0]
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
                    'trait_type': 'Whole Head',  
                    'value': NFT_WholeHead.split('.')[0]
                },
                #{
                #    'trait_type': 'Hand',  
                #    'value': NFT_Hand.split('.')[0]
                #},
                {
                    'trait_type': '1/1',
                    'value': 'None'
                }]
            }
        

        with open(rf'{json_out_path}/Rug_Lord #{i}.json', 'w') as json_print:  # Nota el uso de 'with', que es una buena práctica para manejar archivos
            json.dump(metadata, json_print, indent=4)
        print (rf"Rug Lord #{i}")
        i+=1