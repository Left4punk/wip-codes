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
    
    
    BackGrounds = [f for f in listdir(f"{input_path}/1.background") if isfile(join(f"{input_path}/1.background", f))]
    Base = [f for f in listdir(f"{input_path}/2.body") if isfile(join(f"{input_path}/2.body", f))]
    Clothes = [f for f in listdir(f"{input_path}/3.clothes") if isfile(join(f"{input_path}/3.clothes", f))]
    Eyes = [f for f in listdir(f"{input_path}/4.eyes") if isfile(join(f"{input_path}/4.eyes", f))]
    Mouth = [f for f in listdir(f"{input_path}/5.mouth") if isfile(join(f"{input_path}/5.mouth", f))]
    Head = [f for f in listdir(f"{input_path}/6.head") if isfile(join(f"{input_path}/6.head", f))]
    Mask = [f for f in listdir(f"{input_path}/7.mask") if isfile(join(f"{input_path}/7.mask", f))]

    return  BackGrounds, Base, Clothes, Eyes, Mouth, Head, Mask


def Get_Rarities ():
    
    BackGrounds_Rarity = [10,10,10,10,10,10,10,10,10]
    Base_Rarity = [10,10,10,10]
    Clothes_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Eyes_Rarity=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Mouth_Rarity=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Head_Rarity=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Mask_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    
    return BackGrounds_Rarity, Base_Rarity, Clothes_Rarity, Eyes_Rarity, Mouth_Rarity, Head_Rarity, Mask_Rarity

def NFT_First_Iteration(BackGrounds, BackGrounds_Rarity,Base,Base_Rarity,Clothes,Clothes_Rarity,Eyes,Eyes_Rarity,Mouth,Mouth_Rarity,Head,Head_Rarity,Mask,Mask_Rarity):
  

    NFT_BackGrounds = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Clothes = random.choices(Clothes,weights=(Clothes_Rarity))[0]
    NFT_Eyes = random.choices(Eyes,weights=(Eyes_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    NFT_Mask = random.choices(Mask,weights=(Mask_Rarity))[0]
    
    return NFT_BackGrounds, NFT_Base, NFT_Clothes, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Mask 

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
    
def control_ADN(ADN_list,NFT_BackGrounds, NFT_Base, NFT_Clothes, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Mask):
    
    ADN_NFT = NFT_BackGrounds + "&" + NFT_Base + "&" + NFT_Clothes + "&" + NFT_Eyes + "&" + NFT_Mouth + "&" + NFT_Head + "&" + NFT_Mask
    
    if (ADN_NFT in ADN_list):
        control = True
    else:
        control = False
    
    ADN_list.append(ADN_NFT)
    
    return ADN_list, control


def get_Images (NFT_BackGrounds, NFT_Base, NFT_Clothes, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Mask):

    Image_BackGrounds = f'{input_path}/1.background/'+NFT_BackGrounds
    Image_Base = f'{input_path}/2.body/'+NFT_Base
    Image_Clothes = f'{input_path}/3.clothes/'+NFT_Clothes
    Image_Eyes = f'{input_path}/4.eyes/'+NFT_Eyes
    Image_Mouth = f'{input_path}/5.mouth/'+NFT_Mouth
    Image_Head = f'{input_path}/6.head/'+NFT_Head
    Image_Mask = f'{input_path}/7.mask/'+NFT_Mask
 
    return Image_BackGrounds, Image_Base, Image_Clothes, Image_Eyes, Image_Mouth, Image_Head, Image_Mask

def get_NFT_main (Image_BackGrounds, Image_Base, Image_Clothes, Image_Eyes, Image_Mouth, Image_Head, Image_Mask):
    
   
    BackGround_Image = Image.open(Image_BackGrounds).convert("RGBA")
    
    Base_Image = Image.open(Image_Base).convert("RGBA")

    int1 = Image.alpha_composite(BackGround_Image, Base_Image)
    
    Clothes_Image = Image.open(Image_Clothes).convert("RGBA")

    int2 = Image.alpha_composite(int1, Clothes_Image)

    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")

    int3 = Image.alpha_composite(int2,Eyes_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int4 = Image.alpha_composite(int3, Mouth_Image)

    Head_Image = Image.open(Image_Head).convert("RGBA")
    
    int5 = Image.alpha_composite(int4, Head_Image)

    Mask_Image = Image.open(Image_Mask).convert("RGBA")

    final = Image.alpha_composite(int5, Mask_Image)

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
    
    ## adding 1on1s


    collection_number = 501  

    ## adding 1on1s
    
    i = 1
    while (i<collection_number):
        
            
        ## getting layers & rarities per run ##
        BackGrounds, Base, Clothes, Eyes, Mouth, Head, Mask = Get_Layers ()
        BackGrounds_Rarity, Base_Rarity, Clothes_Rarity, Eyes_Rarity, Mouth_Rarity, Head_Rarity, Mask_Rarity = Get_Rarities()
        ## getting layers & rarities per run ##

        
        ##get first layers
        NFT_BackGrounds, NFT_Base, NFT_Clothes, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Mask = NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity,Clothes,Clothes_Rarity,
                                                                                                               Eyes,Eyes_Rarity,Mouth,Mouth_Rarity,Head,Head_Rarity,Mask,Mask_Rarity)

        ##get first layers
        
        NFT_Head_Excluded = []

        #conflicts

        ## control
    
        ADN_List, control = control_ADN(ADN_list,NFT_BackGrounds, NFT_Base, NFT_Clothes, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Mask)
        if control: continue
    
        ## control
    
        ##import final images
        Image_BackGrounds, Image_Base, Image_Clothes, Image_Eyes, Image_Mouth, Image_Head, Image_Mask = get_Images (NFT_BackGrounds, NFT_Base, NFT_Clothes, NFT_Eyes, NFT_Mouth, NFT_Head, NFT_Mask)
            
        ##import final images
    
        ##image generation
        

        final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Clothes, Image_Eyes, Image_Mouth, Image_Head, Image_Mask)
        

        final.save (f'{output_path}/Cyberz #{i}.png'),

        metadata = {
            'name': f'Cyberz #{i}',
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
                    'trait_type': 'Clothes',
                    'value': NFT_Clothes.split('.')[0]
                },
                {
                    'trait_type': 'Eyes',
                    'value': NFT_Eyes.split('.')[0]
                },
                {
                    'trait_type': 'Mouth',
                    'value': NFT_Mouth.split('.')[0]
                },
                {
                    'trait_type': 'Head',
                    'value': NFT_Head.split('.')[0]
                },
                {
                    'trait_type': 'Mask',
                    'value': NFT_Mask.split('.')[0]
                }]
            }
        

        with open(rf'{json_out_path}/Cyberz #{i}.json', 'w') as json_print: 
            json.dump(metadata, json_print, indent=4)
        print (rf"Cyberz #{i}")
        i+=1