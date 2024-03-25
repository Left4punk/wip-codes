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
    
    
    BackGrounds = [f for f in listdir(f"{input_path}/0 - Backgrounds") if isfile(join(f"{input_path}/0 - Backgrounds", f))]
    Base = [f for f in listdir(f"{input_path}/1 - Base") if isfile(join(f"{input_path}/1 - Base", f))]
    Torso = [f for f in listdir(f"{input_path}/3 - Torso") if isfile(join(f"{input_path}/3 - Torso", f))]
    FacialHair = [f for f in listdir(f"{input_path}/4 - Facial Hair") if isfile(join(f"{input_path}/4 - Facial Hair", f))]
    Mouth = [f for f in listdir(f"{input_path}/5 - Mouth") if isfile(join(f"{input_path}/5 - Mouth", f))]
    Facewear = [f for f in listdir(f"{input_path}/6 - Facewear") if isfile(join(f"{input_path}/6 - Facewear", f))]
    Head = [f for f in listdir(f"{input_path}/7 - Head") if isfile(join(f"{input_path}/7 - Head", f))]
    WholeBody = [f for f in listdir(f"{input_path}/8 - Whole Body") if isfile(join(f"{input_path}/8 - Whole Body", f))]

    return  BackGrounds, Base, Torso, FacialHair, Mouth,Facewear, Head, WholeBody

def Get_Rarities ():
    
    BackGrounds_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10]
    Base_Rarity = [10,10,10,10,10,10]
    Torso_Rarity=[10,10,10,10,10,10,10,10,10,10,10]
    FacialHair_Rarity=[10,10,10,10,10,50,10]
    Mouth_Rarity=[10,10,50,10,10]
    Facewear_Rarity = [10,10,50,10,10]
    Head_Rarity = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,40,10,10,10,10,10,10,10]
    WholeBody_Rarity = [10,60,10,10,10]
    
    
    return BackGrounds_Rarity, Base_Rarity, Torso_Rarity, FacialHair_Rarity, Mouth_Rarity, Facewear_Rarity, Head_Rarity, WholeBody_Rarity

def NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity, Torso, Torso_Rarity, Mouth, Mouth_Rarity, FacialHair, FacialHair_Rarity, Facewear, Facewear_Rarity, Head, Head_Rarity, WholeBody, WholeBody_Rarity):
  

    NFT_BackGrounds = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Torso = random.choices(Torso,weights=(Torso_Rarity))[0]
    NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
    NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    NFT_WholeBody = random.choices(WholeBody,weights=(WholeBody_Rarity))[0]

    
    return NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody

def Get_NFT_Hands_Expression(Base):

    Base = Base.split('.')[0]

    Hand_Path = f"{input_path}/9 - Hand/{Base}/"
    Hands = [f for f in listdir(Hand_Path) if isfile(join(Hand_Path, f))]
    Hand_Rarity = [10,50,10,10,10,10,10]
    NFT_Hand = random.choices(Hands,weights=(Hand_Rarity))[0] 

    Expression_Path = f"{input_path}/2 - Expression/{Base}/"
    Expression = [f for f in listdir(Expression_Path) if isfile(join(Expression_Path, f))]
    if (Base == 'Black' or Base == 'Tan' or Base == 'White'):
        Expression_Rarity = [10,10,10,10,10]
    elif (Base == 'Zombie' or Base == 'Ghost'):
        Expression_Rarity = [10,10,10]
    else:
        Expression_Rarity = [10,10]

    NFT_Expression = random.choices(Expression,weights=(Expression_Rarity))[0] 
    
    return NFT_Hand, NFT_Expression
    
def control_ADN(NFT_BackGrounds, NFT_Base, NFT_Expression, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_Hand):
    
    ADN_NFT = NFT_BackGrounds + "&" + NFT_Base + "&" + NFT_Expression + "&" + NFT_Torso + "&" + NFT_Mouth + "&" + NFT_FacialHair + "&" + NFT_Facewear + "&" + NFT_Head + "&" + NFT_WholeBody + "&" + NFT_Hand
    
    if (ADN_NFT in ADN_list):
        control = True
    else:
        control = False
    
    ADN_list.append(ADN_NFT)
    
    return ADN_list, control


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
def get_Images (NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody,NFT_Hand):
    
    Base = NFT_Base.split('.')[0]

    Image_BackGrounds = f'{input_path}/0 - Background/'+NFT_BackGrounds
    Image_Base = f'{input_path}/1 - Base/'+NFT_Base
    Image_Torso = f'{input_path}/3 - Torso/'+NFT_Torso
    Image_Mouth = f'{input_path}/3 - Mouth/'+NFT_Mouth
    Image_FacialHair = f'{input_path}/5 - Facial Hair/'+NFT_FacialHair
    Image_Facewear = f'{input_path}/6 - Facewear/'+NFT_Facewear
    Image_Head = f'{input_path}/7 - Head/'+NFT_Head
    Image_WholeBody = f'{input_path}/8 - Whole Body/'+NFT_WholeBody
    Image_Hand = f'{input_path}/9 - Hand/{Base}/'+NFT_Hand    

    return Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand


def get_NFT_main (Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand):
    
   
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

    Hand_Image = Image.open(Image_Hand).convert("RGBA")
    
    final = Image.alpha_composite(int8, Hand_Image)

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
        BackGrounds, Base, Torso, Mouth, Eyes, FacialHair, Facewear, Head, WholeBody = Get_Layers ()
        BackGrounds_Rarity, Base_Rarity, Torso_Rarity, Mouth_Rarity, Eyes_Rarity, FacialHair_Rarity, Facewear_Rarity, Head_Rarity, WholeBody_Rarity = Get_Rarities()
        
        ## getting layers & rarities per run ##

        ##get first layers
        NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody = NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity, Torso, Torso_Rarity,
                                                                                                                                                              Mouth, Mouth_Rarity, Eyes, Eyes_Rarity, FacialHair, FacialHair_Rarity, Facewear, Facewear_Rarity,
                                                                                                                                                                      Head, Head_Rarity, WholeBody, WholeBody_Rarity)

        NFT_Hand, NFT_Expression = Get_NFT_Hands_Expression(NFT_Base)
        ##get first layers
        
        NFT_Head_Excluded = []

        #conflicts
        NFT_Facewear = Facewear_Conflicts (NFT_Head,NFT_Facewear, Facewear, Facewear_Rarity)
        NFT_FacialHair  = FacialHair_Conflicts (NFT_Mouth, NFT_FacialHair, FacialHair, FacialHair_Rarity)

        NFT_Head = Head_Conflicts (NFT_Eyes, NFT_Head, Head, Head_Rarity)
        ## control
    
        ADN_List, control = control_ADN(NFT_BackGrounds, NFT_Base, NFT_Expression, NFT_Torso, NFT_Mouth, NFT_Eyes, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_Hand)
        if control: continue

        ## control
        ##full restrictive controls

        if (NFT_Mouth == 'Pipe.png' or NFT_Mouth == 'Cigar.png' or NFT_Mouth == 'Cigarrette.png'):
            
            NFT_FacialHair = 'None.png'
            NFT_WholeBody = 'None.png'
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
            NFT_Facewear = 'None.png'
            NFT_Mouth = random.choices(['Smirk.png','Neutral.png'],weights=(50,50))[0]
            #print('5')


        if (NFT_Mouth == 'Pipe.png' or NFT_Mouth == 'Cigar.png' or NFT_Mouth == 'Cigarrette.png'):

            NFT_FacialHair = 'None.png'

        ##other controls
        ##import final images

        Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand = get_Images (NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_Mouth, NFT_Eyes, 
                                                                                                                                                                                       NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_Hand)
        ##import final images
        ##image generation

        final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Torso, Image_Mouth, Image_Eyes, Image_FacialHair, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand)

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
                    'trait_type': 'Whole Body',  
                    'value': NFT_WholeBody.split('.')[0]
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