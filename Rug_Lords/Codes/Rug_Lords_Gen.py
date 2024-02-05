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
        Hand_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    
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


def Eyes_Conflicts (NFT_Eyes,excluded_traits):
    
    if (NFT_Eyes == 'Blue Laser Eyes.png'):

        
        conflict_hairs = ['Emamah.png','Orange Keffiyeh.png','Messy Hair.png','Dreadlocks.png','Brown Quiff.png','Small Dreadlocks.png','Crazy Hair.png']
         
        #for elem in excluded_traits:
        #    if elem in available_heads:
        #        remove = available_heads.index(elem)
        #        available_heads.pop(remove)
        #        available_rarity.pop(remove)
                # print (elem)
        NFT_Facewear = 'none.png'
        NFT_Wholehead = 'none.png'
        #NFT_Head = random.choices(available_heads,weights=(available_rarity))[0] #'Non La.png'


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



if __name__ == '__main__':


    current_dir = Path(__file__).parent
    
    
    base_dir = current_dir.parent
    
    input_path = base_dir/'Traits'
    output_path = base_dir/'Generations'
    json_out_path = base_dir/'Metadata'
    
    output_path.mkdir(parents=True, exist_ok=True)
    json_out_path.mkdir(parents=True, exist_ok=True)
    
    


    ## control
    ADN_list = []
    ## control
    
    i = 1

    while (i<1001):
        
        ## getting rarities per run ##
        BackGrounds, Base, Eyes, Torso, Mouth, FacialHair, Accesories, Head, Facewear, WholeHead = Get_Layers ()
        BackGrounds_Rarity, Base_Rarity, Eyes_Rarity, Torso_Rarity, Mouth_Rarity, FacialHair_Rarity, Accesories_Rarity, Head_Rarity, Facewear_Rarity, WholeHead_Rarity = Get_Rarities()
        ## getting rarities per run ##

        
        ##get first layers
        NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead= NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity,Eyes,
                                                                                                                                                                          Eyes_Rarity,Torso,Torso_Rarity,Mouth,Mouth_Rarity,FacialHair,
                                                                                                                                                                          FacialHair_Rarity,Accesories,Accesories_Rarity,Head,Head_Rarity,Facewear,Facewear_Rarity,
                                                                                                                                                                          WholeHead, WholeHead_Rarity)
        print(NFT_Base)

        NFT_Hand = Get_NFT_Hands(NFT_Base)
        ##get first layers
        
        #conflicts

        ## control
    
        ADN_List, control = control_ADN(ADN_list,NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead, NFT_Hand)
        if control: continue
    
        ## control
    
    
        ##import final images
        Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand = get_Images (NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear, NFT_WholeHead, NFT_Hand)
        ##import final images
    
        ##image generation
        
        final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear, Image_WholeHead, Image_Hand)

        final.save (f'{output_path}/Rug_Lord #{i}.png')

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