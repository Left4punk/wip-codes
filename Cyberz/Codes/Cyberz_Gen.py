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
    
    Background = [f for f in listdir(f"{input_path}/BACKGROUND") if isfile(join(f"{input_path}/BACKGROUND", f))]
    Base = [f for f in listdir(f"{input_path}/BASES") if isfile(join(f"{input_path}/BASES", f))]
    Eyes = [f for f in listdir(f"{input_path}/EYES") if isfile(join(f"{input_path}/EYES", f))]
    Eyewear = [f for f in listdir(f"{input_path}/EYEWEAR") if isfile(join(f"{input_path}/EYEWEAR", f))]
    Headwear = [f for f in listdir(f"{input_path}/HEADWEAR") if isfile(join(f"{input_path}/HEADWEAR", f))]
    Mask = [f for f in listdir(f"{input_path}/MASKS") if isfile(join(f"{input_path}/MASKS", f))]
    Mouth = [f for f in listdir(f"{input_path}/MOUTH") if isfile(join(f"{input_path}/MOUTH", f))]
    Clothing = [f for f in listdir(f"{input_path}/CLOTHING") if isfile(join(f"{input_path}/CLOTHING", f))]
    

    return  Background, Base, Eyes, Eyewear, Headwear, Mask, Mouth, Clothing


def Get_Rarities ():
    
    Background_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10]
    Base_Rarity = [10,10,10,10]
    Eyes_Rarity = [10,10,10,10,10,10]
    Eyewear_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Headwear_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Mask_Rarity = [0,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Mouth_Rarity = [10,10,10,10,10,10,10,10,10]
    Clothing_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

    return Background_Rarity, Base_Rarity, Eyes_Rarity, Eyewear_Rarity, Headwear_Rarity, Mask_Rarity, Mouth_Rarity, Clothing_Rarity

def NFT_First_Iteration(Background, Background_Rarity, Base, Base_Rarity, Eyes, Eyes_Rarity, Eyewear, Eyewear_Rarity, Headwear, Headwear_Rarity, Mask, Mask_Rarity, Mouth, Mouth_Rarity, Clothing, Clothing_Rarity):
  
    NFT_Backgrounds = random.choices(Background,weights=(Background_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Eyes = random.choices(Eyes,weights=(Eyes_Rarity))[0]
    NFT_Eyewear = random.choices(Eyewear,weights=(Eyewear_Rarity))[0]
    NFT_Headwear = random.choices(Headwear,weights=(Headwear_Rarity))[0]
    NFT_Mask = random.choices(Mask,weights=(Mask_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_Clothing = random.choices(Clothing,weights=(Clothing_Rarity))[0]
    
    return NFT_Backgrounds, NFT_Base, NFT_Eyes, NFT_Eyewear, NFT_Headwear, NFT_Mask, NFT_Mouth, NFT_Clothing


def control_ADN(ADN_list, NFT_Backgrounds, NFT_Base, NFT_Eyewear, NFT_Headwear, NFT_Mask, NFT_Mouth, NFT_Clothing, NFT_Hair, NFT_Eyebrow):
    
    ADN_NFT = NFT_Backgrounds + "&" + NFT_Base + "&" + NFT_Eyewear + "&" + NFT_Headwear + "&" + NFT_Mask + "&" + NFT_Mouth + "&" + NFT_Clothing + "&" + NFT_Hair + "&" + NFT_Eyebrow
    
    if (ADN_NFT in ADN_list):
        control = True
    else:
        control = False
    
    ADN_list.append(ADN_NFT)
    
    return ADN_list, control


def get_Images(NFT_Backgrounds, NFT_Base, NFT_Eyes, NFT_Eyewear, NFT_Headwear, NFT_Mask, NFT_Mouth, NFT_Clothing):

    Image_Background = f'{input_path}/BACKGROUND/'+NFT_Backgrounds
    Image_Base = f'{input_path}/BASES/'+NFT_Base
    Image_Eyes = f'{input_path}/EYES/'+NFT_Eyes
    Image_Eyewear = f'{input_path}/EYEWEAR/'+NFT_Eyewear
    Image_Headwear = f'{input_path}/HEADWEAR/'+NFT_Headwear
    Image_Mask = f'{input_path}/MASKS/'+NFT_Mask
    Image_Mouth = f'{input_path}/MOUTH/'+NFT_Mouth
    Image_Clothing = f'{input_path}/CLOTHING/'+NFT_Clothing
 
    return Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing

def get_Images_Hair(NFT_Backgrounds, NFT_Base, NFT_Eyes, NFT_Eyewear, NFT_Headwear, NFT_Mask, NFT_Mouth, NFT_Clothing, NFT_Hair, Color_Hair, NFT_Eyebrow):

    Image_Background = f'{input_path}/BACKGROUND/'+NFT_Backgrounds
    Image_Base = f'{input_path}/BASES/'+NFT_Base
    Image_Eyes = f'{input_path}/EYES/'+NFT_Eyes
    Image_Eyewear = f'{input_path}/EYEWEAR/'+NFT_Eyewear
    Image_Headwear = f'{input_path}/HEADWEAR/'+NFT_Headwear
    Image_Mask = f'{input_path}/MASKS/'+NFT_Mask
    Image_Mouth = f'{input_path}/MOUTH/'+NFT_Mouth
    Image_Clothing = f'{input_path}/CLOTHING/'+NFT_Clothing
    Image_Hair = f'{input_path}/HAIR/{Color_Hair}/'+NFT_Hair
    Image_Eyebrows = f'{input_path}/EYEBROWS/'+NFT_Eyebrow


    return Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing, Image_Hair, Image_Eyebrows

def get_NFT_main (Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing):
    
    Background_Image = Image.open(Image_Background).convert("RGBA")

    Base_Image = Image.open(Image_Base).convert("RGBA")
    
    int0 = Image.alpha_composite(Background_Image, Base_Image)
    
    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")

    int1 = Image.alpha_composite(int0, Eyes_Image)
    
    Clothes_Image = Image.open(Image_Clothing).convert("RGBA")

    int2 = Image.alpha_composite(int1, Clothes_Image)

    Headwear_Image = Image.open(Image_Headwear).convert("RGBA")

    int3 = Image.alpha_composite(int2,Headwear_Image)

    Eyewear_Image = Image.open(Image_Eyewear).convert("RGBA")

    int4 = Image.alpha_composite(int3, Eyewear_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int5 = Image.alpha_composite(int4, Mouth_Image)

    Mask_Image = Image.open(Image_Mask).convert("RGBA")

    final = Image.alpha_composite(int5, Mask_Image)

    return final

def get_NFT_main_Hair (Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing, Image_Hair, Image_Eyebrows):

    Background_Image = Image.open(Image_Background).convert("RGBA")

    Base_Image = Image.open(Image_Base).convert("RGBA")
    
    int0 = Image.alpha_composite(Background_Image, Base_Image)

    Eyes_Image = Image.open(Image_Eyes).convert("RGBA")

    int1 = Image.alpha_composite(int0, Eyes_Image)

    Hair_Image = Image.open(Image_Hair).convert("RGBA")

    int2 = Image.alpha_composite(int1, Hair_Image)

    Eyebrows_Image = Image.open(Image_Eyebrows).convert("RGBA")

    int3 = Image.alpha_composite(int2, Eyebrows_Image)

    Clothes_Image = Image.open(Image_Clothing).convert("RGBA")

    int4 = Image.alpha_composite(int3, Clothes_Image)

    Eyewear_Image = Image.open(Image_Eyewear).convert("RGBA")

    int5 = Image.alpha_composite(int4,Eyewear_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")
    
    int6 = Image.alpha_composite(int5, Mouth_Image)

    Headwear_Image = Image.open(Image_Headwear).convert("RGBA")
    
    int7 = Image.alpha_composite(int6, Headwear_Image)

    Mask_Image = Image.open(Image_Mask).convert("RGBA")

    final = Image.alpha_composite(int7, Mask_Image)

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
    hair_colors = ['Blue','Brown','Green','Grey','Orange','Purple']
    i = 1
    while (i<collection_number):
        
            
        ## getting layers & rarities per run ##
        Background, Base, Eyes, Eyewear, Headwear, Mask, Mouth, Clothing = Get_Layers ()
        Background_Rarity, Base_Rarity, Eyes_Rarity, Eyewear_Rarity, Headwear_Rarity, Mask_Rarity, Mouth_Rarity, Clothing_Rarity = Get_Rarities()
        ## getting layers & rarities per run ##

        
        ##get first layers
        NFT_Backgrounds, NFT_Base, NFT_Eyes, NFT_Eyewear, NFT_Headwear, NFT_Mask, NFT_Mouth, NFT_Clothing = NFT_First_Iteration(Background, Background_Rarity, Base, Base_Rarity, Eyes, Eyes_Rarity, Eyewear, Eyewear_Rarity, 
                                                                                                               Headwear, Headwear_Rarity, Mask, Mask_Rarity, Mouth, Mouth_Rarity, Clothing, Clothing_Rarity)
        ##get hair & eyebrows layers
        print (NFT_Headwear)

        Need_Hair = True

        if ('-' in NFT_Headwear):
            Need_Hair = False
            Color_Hair = NFT_Headwear.split('-')[1].split('.')[0]
            NFT_Hair = Color_Hair + '.png'
            NFT_Eyebrow = Color_Hair + '.png'
            
        
        if (Need_Hair):

            Color_Hair = random.choice(hair_colors)

            Hair = [f for f in listdir(f"{input_path}/HAIR/{Color_Hair}") if isfile(join(f"{input_path}/HAIR/{Color_Hair}", f))]
            Hair_Rarity = [10,10,10,10,10,10,10,10]

            NFT_Hair = random.choices(Hair,weights=(Hair_Rarity))[0]
            NFT_Eyebrow = Color_Hair + '.png'
        
        print (NFT_Hair, NFT_Eyebrow)

        #conflicts

        ## control
    
        ADN_List, control = control_ADN(ADN_list, NFT_Backgrounds, NFT_Base, NFT_Eyewear, NFT_Headwear, NFT_Mask, NFT_Mouth, NFT_Clothing, NFT_Hair, NFT_Eyebrow)
        if control: continue
    
        ## control
    
        ##import final images
        if (Need_Hair):
            Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing, Image_Hair, Image_Eyebrows = get_Images_Hair(NFT_Backgrounds, NFT_Base, NFT_Eyes, NFT_Eyewear, NFT_Headwear, 
                                                                                                                                                                           NFT_Mask, NFT_Mouth, NFT_Clothing, NFT_Hair, Color_Hair, NFT_Eyebrow)
            print (Image_Hair)
        else:
            Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing = get_Images(NFT_Backgrounds, NFT_Base, NFT_Eyes, NFT_Eyewear, NFT_Headwear, NFT_Mask, NFT_Mouth, NFT_Clothing)
            
        ##import final images

        
        ##image generation
        
        if (Need_Hair):

            final = get_NFT_main_Hair (Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing, Image_Hair, Image_Eyebrows)
        
        else:

            final = get_NFT_main (Image_Background, Image_Base, Image_Eyes, Image_Eyewear, Image_Headwear, Image_Mask, Image_Mouth, Image_Clothing)

        final.save (f'{output_path}/Cyberz #{i}.png'),
        sys.exit()
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