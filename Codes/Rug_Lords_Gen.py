from os import listdir
from os.path import isfile, join
import json
import pandas as pd
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

    return  BackGrounds, Base, Eyes, Torso, Mouth, FacialHair, Accesories, Head, Facewear

def Get_Rarities ():
    
    BackGrounds_Rarity = [10,10,10,10,10,10,10,10]
    Base_Rarity = [33,33,33]
    Eyes_Rarity = [10,10,10,10,10,10,10,10]
    Torso_Rarity=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Mouth_Rarity=[10,10,10,10,10,10]
    FacialHair_Rarity=[10,10,10,10,10,10,10,10]
    Accesories_Rarity = [10,10,10,10,10]
    Head_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    Facewear_Rarity = [10,10,10,10,10,10,10,10,10,10]
    
    return BackGrounds_Rarity, Base_Rarity, Eyes_Rarity, Torso_Rarity, Mouth_Rarity, FacialHair_Rarity, Accesories_Rarity, Head_Rarity, Facewear_Rarity

def NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity,Eyes,Eyes_Rarity,Torso,Torso_Rarity,Mouth,Mouth_Rarity,FacialHair,FacialHair_Rarity,Accesories,Accesories_Rarity,Head,Head_Rarity,Facewear,Facewear_Rarity):
  

    NFT_BackGrounds = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Eyes = random.choices(Eyes,weights=(Eyes_Rarity))[0]
    NFT_Torso = random.choices(Torso,weights=(Torso_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]
    NFT_Accesories = random.choices(Accesories,weights=(Accesories_Rarity))[0]
    NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
    
    
    return NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear

    
def control_ADN(ADN_list,NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear):
    
    ADN_NFT = NFT_BackGrounds + "&" + NFT_Base + "&" + NFT_Eyes + "&" + NFT_Torso + "&" + NFT_Mouth + "&" + NFT_FacialHair + "&" + NFT_Accesories + "&" + NFT_Head + "&" + NFT_Facewear
    
    if (ADN_NFT in ADN_list):
        control = True
    else:
        control = False
    
    ADN_list.append(ADN_NFT)
    
    return ADN_list, control


def get_Images (NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear):
    
    Image_BackGrounds = f'{input_path}/0 - Background/'+NFT_BackGrounds
    Image_Base = f'{input_path}/1 - Base/'+NFT_Base
    Image_Eyes = f'{input_path}/2 - Eyes/'+NFT_Eyes
    Image_Torso = f'{input_path}/3 - Torso/'+NFT_Torso
    Image_Mouth = f'{input_path}/4 - Mouth/'+NFT_Mouth
    Image_FacialHair = f'{input_path}/5 - Facial Hair/'+NFT_FacialHair
    Image_Accesories = f'{input_path}/6 - Accesories/'+NFT_Accesories
    Image_Head = f'{input_path}/7 - Head/'+NFT_Head
    Image_Facewear = f'{input_path}/8 - Facewear/'+NFT_Facewear
    
    return Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear

def get_NFT_main (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear):
    
   
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
    
    final = Image.alpha_composite(int7, Facewear_Image)

    return final



if __name__ == '__main__':


    current_dir = Path(__file__).parent
    
    
    base_dir = current_dir.parent
    
    input_path = base_dir/'Traits'
    output_path = base_dir/'Generations'
    json_out = base_dir/'Metadata'
    
    output_path.mkdir(parents=True, exist_ok=True)
    json_out.mkdir(parents=True, exist_ok=True)
    
    BackGrounds, Base, Eyes, Torso, Mouth, FacialHair, Accesories, Head, Facewear  = Get_Layers ()
    BackGrounds_Rarity, Base_Rarity, Eyes_Rarity, Torso_Rarity, Mouth_Rarity, FacialHair_Rarity, Accesories_Rarity, Head_Rarity, Facewear_Rarity  = Get_Rarities()


    ## control
    ADN_list = []
    ## control
    
    i = 1

    while (i<1001):
        
        NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear = NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity,Eyes,Eyes_Rarity,Torso,Torso_Rarity,Mouth,Mouth_Rarity,FacialHair,FacialHair_Rarity,Accesories,Accesories_Rarity,Head,Head_Rarity,Facewear,Facewear_Rarity)

        print (NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear)
    #conflicts

    ## control
    
        ADN_List, control = control_ADN(ADN_list,NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear)
        if control: continue
    
    ## control
    
    ##import images

        #print (NFT_Head)
        Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear = get_Images (NFT_BackGrounds, NFT_Base, NFT_Eyes, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Accesories, NFT_Head, NFT_Facewear)

    
        ##image generation
        
        final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Eyes, Image_Torso, Image_Mouth, Image_FacialHair, Image_Accesories, Image_Head, Image_Facewear) 

        final.save (f'{output_path}/Rug_Lord #{i}.png')

        #print (f'Rug_Lord #{i}')
        
        
        # df = pd.concat([append_df,df])

        
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
        

        json_out = open(rf'{json_out}\Rug_Lord #{i}.json','w')
        json.dump(metadata, json_out, indent=4)
        json_out.close()
       
        i+=1