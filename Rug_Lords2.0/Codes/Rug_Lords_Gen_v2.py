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
    
    BackGrounds_Rarity = [4,12,4,4,4,12,12,4,4,4,4,4,4,12,12]
    Base_Rarity = [21,22,5,3,22,23,4]
    Torso_Rarity=[5,4,4,6,6,6,6,4,3,6,4,4,4,4,6,6,6,6,6,3,3]
    FacialHair_Rarity=[8,8,8,8,7,50,8,3]
    Mouth_Rarity=[10,10,70,10]
    Facewear_Rarity = [3,3,2,2,3,1,5,55,3,6,8,4]
    Head_Rarity = [4,4,4,4,4,4,3,3,3,2,4,4,4,4,3,4,2,4,5,2,3,3,3,3,4,4,4,4,2,2,1,1]
    WholeBody_Rarity = [1,1,85,1,2,2,2,2,2,2]
    
    
    return BackGrounds_Rarity, Base_Rarity, Torso_Rarity, FacialHair_Rarity, Mouth_Rarity, Facewear_Rarity, Head_Rarity, WholeBody_Rarity


def Get_Rugs ():
    

    special_black_hands = [f for f in listdir(f"{input_path}/9 - Hand/Special_Hands/Black") if isfile(join(f"{input_path}/9 - Hand/Special_Hands/Black", f))]
    special_black_cyborg_hands = [f for f in listdir(f"{input_path}/9 - Hand/Special_Hands/Cyborg") if isfile(join(f"{input_path}/9 - Hand/Special_Hands/Cyborg", f))]
    special_ghost_hands = [f for f in listdir(f"{input_path}/9 - Hand/Special_Hands/Ghost") if isfile(join(f"{input_path}/9 - Hand/Special_Hands/Ghost", f))]
    special_tan_hands = [f for f in listdir(f"{input_path}/9 - Hand/Special_Hands/Tan") if isfile(join(f"{input_path}/9 - Hand/Special_Hands/Tan", f))]
    special_white_hands = [f for f in listdir(f"{input_path}/9 - Hand/Special_Hands/White") if isfile(join(f"{input_path}/9 - Hand/Special_Hands/White", f))]
    special_zombie_hands = [f for f in listdir(f"{input_path}/9 - Hand/Special_Hands/Zombie") if isfile(join(f"{input_path}/9 - Hand/Special_Hands/Zombie", f))]

    return  special_black_hands, special_black_cyborg_hands, special_ghost_hands, special_tan_hands, special_white_hands, special_zombie_hands



def NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity, Torso, Torso_Rarity, Mouth, Mouth_Rarity, FacialHair, FacialHair_Rarity, Facewear, Facewear_Rarity, Head, Head_Rarity, WholeBody, WholeBody_Rarity):
  

    NFT_BackGrounds = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]
    NFT_Base = random.choices(Base,weights=(Base_Rarity))[0]
    NFT_Torso = random.choices(Torso,weights=(Torso_Rarity))[0]
    NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]
    NFT_Mouth = random.choices(Mouth,weights=(Mouth_Rarity))[0]
    NFT_Facewear = random.choices(Facewear,weights=(Facewear_Rarity))[0]
    NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]
    NFT_WholeBody = random.choices(WholeBody,weights=(WholeBody_Rarity))[0]

    
    return NFT_BackGrounds, NFT_Base, NFT_Torso, NFT_FacialHair, NFT_Mouth,  NFT_Facewear, NFT_Head, NFT_WholeBody

def Get_NFT_Hands_Expression(Base):

    Base = Base.split('.')[0]

    Hand_Path = f"{input_path}/9 - Hand/{Base}/"
    Hands = [f for f in listdir(Hand_Path) if isfile(join(Hand_Path, f))]

    if (Base in ['White','Tan','Brown','Black']):

        Hand_Rarity = [4,50,2,6,6,6,6,6,6,6,6,6,6,6]
    else:
        Hand_Rarity = [2,77,2,5,1,1,1,5,4,6,4]
    NFT_Hand = random.choices(Hands,weights=(Hand_Rarity))[0] 
    
    Expression_Path = f"{input_path}/2 - Expression/{Base}/"
    Expression = [f for f in listdir(Expression_Path) if isfile(join(Expression_Path, f))]

    if (Base == 'Black' or Base == 'Tan' or Base == 'White' or Base == 'Brown'):
        Expression_Rarity = [10,10,10,10,10]
    elif (Base == 'Zombie' or Base == 'Ghost'):
        Expression_Rarity = [10,10,10]
    else:
        Expression_Rarity = [10,10]

    NFT_Expression = random.choices(Expression,weights=(Expression_Rarity))[0] 
    
    return NFT_Hand, NFT_Expression
    

def get_special_hand(Base, Special_Hand):

    Base = Base.split('.')[0]

    NFT_Hand = Special_Hand[0]

    Special_Hand.pop(0)

    Image_Hand = f'{input_path}/9 - Hand/Special_Hands/{Base}/'+NFT_Hand

    print (Image_Hand)

    return Image_Hand



def control_ADN(NFT_BackGrounds, NFT_Base, NFT_Expression, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_Hand):
    
    ADN_NFT = NFT_BackGrounds + "&" + NFT_Base + "&" + NFT_Expression + "&" + NFT_Torso + "&" + NFT_Mouth + "&" + NFT_FacialHair + "&" + NFT_Facewear + "&" + NFT_Head + "&" + NFT_WholeBody + "&" + NFT_Hand
    
    if (ADN_NFT in ADN_list):
        control = True
    else:
        control = False
    
    ADN_list.append(ADN_NFT)
    
    return ADN_list, control


def FacialHair_Conflicts (NFT_FacialHair, FacialHair, FacialHair_Rarity, NFT_Head):

    if NFT_Head in ['Flow hair brown.png', 'Mullet brown.png', 'Short hair brown.png', 'Side part hair brown.png', 'Headband.png']:

        conflict_FacialHair = ['Duck tail black.png', 'Full beard black.png','Stubble black']

        for elem in conflict_FacialHair:

            if elem in FacialHair:

                remove_elem = FacialHair.index(elem)
                FacialHair.pop(remove_elem)
                FacialHair_Rarity.pop(remove_elem)

        NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]

    elif NFT_Head in ['Emamah.png', 'Flow hair black.png', 'Mullet black.png', 'Short hair black.png', 'Side part hair black.png','Long.png']:

        conflict_FacialHair = ['Duck tail brown.png', 'Full beard brown.png']

        for elem in conflict_FacialHair:

            if elem in FacialHair:

                remove_elem = FacialHair.index(elem)
                FacialHair.pop(remove_elem)
                FacialHair_Rarity.pop(remove_elem)

        NFT_FacialHair = random.choices(FacialHair,weights=(FacialHair_Rarity))[0]

    else:

        NFT_FacialHair = NFT_FacialHair

    return NFT_FacialHair
    
    
def Facewear_Conflicts (NFT_Head, Head, Head_Rarity, NFT_Facewear, NFT_WholeBody):

    if NFT_Facewear in ['3D Glasses.png', 'Sunglasses.png', 'Reading glasses.png', 'Meme glasses.png']:
        
        conflict_head = ['Thawb black.png', 'Thawb dark red.png', 'Thawb green.png', 'Thawb navy.png', 'Thawb white.png', 'Turban.png', 'Emamah.png', 'Grey & Red turban.png', 'White turban.png', 'Red turban.png']
    
        for elem in conflict_head:
            
            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]      
        NFT_WholeBody = NFT_WholeBody
    
    elif NFT_Facewear in ['Laser eyes red.png', 'Laser eyes orange.png', 'Laser eyes green.png', 'Laser eyes cyan.png']:

        conflict_head = ['Turban.png', 'Emamah.png', 'Grey & Red turban.png', 'White turban.png', 'Red turban.png','Long.png']
    
        for elem in conflict_head:
            
            if elem in Head:

                remove_elem = Head.index(elem)
                Head.pop(remove_elem)
                Head_Rarity.pop(remove_elem)

        NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]    
        NFT_WholeBody = 'None.png'

    elif NFT_Facewear in ['Btc mask.png', 'Pac-Man mask.png', 'Gox mask.png']:
    
        NFT_Head = 'None.png'
        NFT_WholeBody = 'None.png'
       
    elif NFT_Facewear in ['Vision Pro.png']:
        
        NFT_Head = NFT_Head
        NFT_WholeBody = 'None.png'

    else:

        NFT_Head = NFT_Head
        NFT_WholeBody = NFT_WholeBody

    return NFT_Head, NFT_WholeBody

def get_Images (NFT_BackGrounds, NFT_Base, NFT_Expression, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_Hand):
    
    Base = NFT_Base.split('.')[0]

    Image_BackGrounds = f'{input_path}/0 - Backgrounds/'+NFT_BackGrounds
    Image_Base = f'{input_path}/1 - Base/'+NFT_Base
    Image_Expression = f'{input_path}/2 - Expression/{Base}/'+NFT_Expression
    Image_Torso = f'{input_path}/3 - Torso/'+NFT_Torso
    Image_FacialHair = f'{input_path}/4 - Facial Hair/'+NFT_FacialHair
    Image_Mouth = f'{input_path}/5 - Mouth/'+NFT_Mouth
    Image_Facewear = f'{input_path}/6 - Facewear/'+NFT_Facewear
    Image_Head = f'{input_path}/7 - Head/'+NFT_Head
    Image_WholeBody = f'{input_path}/8 - Whole Body/'+NFT_WholeBody
    Image_Hand = f'{input_path}/9 - Hand/{Base}/'+NFT_Hand    

    return Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand


def get_NFT_main (Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand):
    
   
    BackGround_Image = Image.open(Image_BackGrounds).convert("RGBA")
    
    Base_Image = Image.open(Image_Base).convert("RGBA")

    int1 = Image.alpha_composite(BackGround_Image, Base_Image)
    
    Expression_Image = Image.open(Image_Expression).convert("RGBA")

    int2 = Image.alpha_composite(int1, Expression_Image)
    
    Torso_Image = Image.open(Image_Torso).convert("RGBA")

    int3 = Image.alpha_composite(int2, Torso_Image)
    
    FacialHair_Image = Image.open(Image_FacialHair).convert("RGBA")

    int4 = Image.alpha_composite(int3, FacialHair_Image)
    
    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")

    int5 = Image.alpha_composite(int4, Mouth_Image)
    
    Facewear_Image = Image.open(Image_Facewear).convert("RGBA")

    int6 = Image.alpha_composite(int5, Facewear_Image)
    
    Head_Image = Image.open(Image_Head).convert("RGBA")
    
    int7 = Image.alpha_composite(int6, Head_Image)
    
    WholeBody_Image = Image.open(Image_WholeBody).convert("RGBA")    
    
    int8 = Image.alpha_composite(int7, WholeBody_Image)
    
    Hand_Image = Image.open(Image_Hand).convert("RGBA")     

    final = Image.alpha_composite(int8, Hand_Image)

    return final

def get_NFT_hand (Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand):
    
   
    BackGround_Image = Image.open(Image_BackGrounds).convert("RGBA")
    
    Base_Image = Image.open(Image_Base).convert("RGBA")

    int1 = Image.alpha_composite(BackGround_Image, Base_Image)
    
    Expression_Image = Image.open(Image_Expression).convert("RGBA")

    int2 = Image.alpha_composite(int1, Expression_Image)
    
    Torso_Image = Image.open(Image_Torso).convert("RGBA")

    int3 = Image.alpha_composite(int2, Torso_Image)
    
    FacialHair_Image = Image.open(Image_FacialHair).convert("RGBA")

    int4 = Image.alpha_composite(int3, FacialHair_Image)
     
    Facewear_Image = Image.open(Image_Facewear).convert("RGBA")

    int5 = Image.alpha_composite(int4, Facewear_Image)
    
    Head_Image = Image.open(Image_Head).convert("RGBA")
    
    int6 = Image.alpha_composite(int5, Head_Image)
    
    WholeBody_Image = Image.open(Image_WholeBody).convert("RGBA")    
    
    int7 = Image.alpha_composite(int6, WholeBody_Image)
    
    Hand_Image = Image.open(Image_Hand).convert("RGBA")     

    int8 = Image.alpha_composite(int7, Hand_Image)

    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")

    final = Image.alpha_composite(int8, Mouth_Image)

    return final


def get_NFT_mouth (Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand):
    
   
    BackGround_Image = Image.open(Image_BackGrounds).convert("RGBA")
    
    Base_Image = Image.open(Image_Base).convert("RGBA")

    int1 = Image.alpha_composite(BackGround_Image, Base_Image)
    
    Expression_Image = Image.open(Image_Expression).convert("RGBA")

    int2 = Image.alpha_composite(int1, Expression_Image)
    
    Torso_Image = Image.open(Image_Torso).convert("RGBA")

    int3 = Image.alpha_composite(int2, Torso_Image)
    
    FacialHair_Image = Image.open(Image_FacialHair).convert("RGBA")

    int4 = Image.alpha_composite(int3, FacialHair_Image)
    
    Facewear_Image = Image.open(Image_Facewear).convert("RGBA")

    int5 = Image.alpha_composite(int4, Facewear_Image)
    
    Mouth_Image = Image.open(Image_Mouth).convert("RGBA")

    int6 = Image.alpha_composite(int5, Mouth_Image)
    
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
    output_path_resized = base_dir/'Generations_Resized'

    output_path.mkdir(parents=True,exist_ok=True)
    output_path.mkdir(parents=True, exist_ok=True)
    json_out_path.mkdir(parents=True, exist_ok=True)
    
    ## foldering

    ## control
    ADN_list = []
    ## control
    
    ## adding 1on1s
    NFTs = Get_One_on_Ones()
    random.shuffle(NFTs)
    number_of_ones = 0
    collection_number = 2101 
    position_list = random.sample(range(1, collection_number), number_of_ones)
    position_list.sort()
    
    print (input_path)
    ## adding 1on1s
    
    special_Black_hands, special_Cyborg_hands, special_Ghost_hands, special_Tan_hands, special_White_hands, special_Zombie_hands = Get_Rugs ()

    special_hands = {
    'Black': special_Black_hands,
    'Cyborg': special_Cyborg_hands,
    'Ghost': special_Ghost_hands,
    'Tan': special_Tan_hands,
    'White': special_White_hands,
    'Zombie': special_Zombie_hands,
    }

    #number_of_special_hands = len(special_Black_hands) + len(special_Cyborg_hands) + len(special_Ghost_hands) + len(special_Tan_hands) + len(special_White_hands) + len(special_Zombie_hands)
    
    i = 1
    while (i<collection_number):
        
        if (len(position_list)!=0 and i == position_list[0]):
            
            get_One_on_One (NFTs, position_list)

            print (rf"Rug Lord #{i}")
            i+=1
            continue
        
        special_hand_number = random.randint(1,10)
            
        ## getting layers & rarities per run ##
        BackGrounds, Base, Torso, FacialHair, Mouth, Facewear, Head, WholeBody = Get_Layers ()
        BackGrounds_Rarity, Base_Rarity, Torso_Rarity, FacialHair_Rarity, Mouth_Rarity, Facewear_Rarity, Head_Rarity, WholeBody_Rarity = Get_Rarities()
        
        ## getting layers & rarities per run ##


        ##get first layers
        NFT_BackGrounds, NFT_Base, NFT_Torso,  NFT_FacialHair, NFT_Mouth, NFT_Facewear, NFT_Head, NFT_WholeBody = NFT_First_Iteration (BackGrounds, BackGrounds_Rarity,Base,Base_Rarity, Torso, Torso_Rarity,
                                                                                                                                                              Mouth, Mouth_Rarity, FacialHair, FacialHair_Rarity, Facewear, Facewear_Rarity,
                                                                                                                                                                      Head, Head_Rarity, WholeBody, WholeBody_Rarity)
        
        NFT_Hand, NFT_Expression = Get_NFT_Hands_Expression(NFT_Base)

        ##get first layers
        
        NFT_Head_Excluded = []

        #conflicts

        ## control
    
        ADN_List, control = control_ADN(NFT_BackGrounds, NFT_Base, NFT_Expression, NFT_Torso, NFT_Mouth, NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_Hand)
        if control: continue

        

        ## control
        ##full restrictive controls

        if (NFT_Torso == 'Gold jacket.png'):
            
            conflict_head = ['Grey & Red turban.png']

            for elem in conflict_head:

                if elem in Head:

                    remove_elem = Head.index(elem)
                    Head.pop(remove_elem)
                    Head_Rarity.pop(remove_elem)
            
            NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]

            #print('1')
        if (NFT_Mouth != 'None.png'):
            NFT_WholeBody = 'None.png'

            conflict_background = ['Binary code.png','Binary purple.png','Night sky.png','Mosque.png']
            conflict_head = ['Grey & Red turban.png']

            for elem in conflict_head:

                if elem in Head:

                    remove_elem = Head.index(elem)
                    Head.pop(remove_elem)
                    Head_Rarity.pop(remove_elem)
            
            NFT_Head = random.choices(Head,weights=(Head_Rarity))[0]

            for elem in conflict_background:

                if elem in conflict_background:

                    remove_elem_bg = BackGrounds.index(elem)
                    BackGrounds.pop (remove_elem_bg)
                    BackGrounds_Rarity.pop(remove_elem_bg)

            NFT_BackGrounds = random.choices(BackGrounds,weights=(BackGrounds_Rarity))[0]

        if (NFT_Head not in ['Fedora.png', 'Taqiyah beige', 'Taqiyah blue', 'Taqiyah dark green', 'Taqiyah red'] and NFT_Facewear == 'Vision Pro.png'):

            NFT_Facewear = 'None.png'

        
        NFT_Head, NFT_WholeBody = Facewear_Conflicts (NFT_Head, Head, Head_Rarity, NFT_Facewear, NFT_WholeBody)
        NFT_FacialHair = FacialHair_Conflicts (NFT_FacialHair, FacialHair, FacialHair_Rarity, NFT_Head)

        if (NFT_WholeBody != 'None.png'):

            NFT_Head = 'None.png'
            NFT_Torso = 'Bald.png'
            NFT_Facewear = 'None.png'

        if (NFT_Base in ['Cyborg.png','Ghost.png','Zombie.png'] or NFT_Facewear in ['Pac-Man mask.png','Btc mask.png','Gox mask.png']):

            NFT_FacialHair = 'None.png'


        if NFT_Mouth != 'None':
            
            NFT_Hand = random.choices(['OR Rune.png', 'None.png'],weights=(10,30))[0]
        
        if NFT_Facewear in ['Laser eyes red.png', 'Laser eyes orange.png', 'Laser eyes green.png', 'Laser eyes cyan.png']:

            NFT_Hand = random.choices(['OR Rune.png','None.png'],weights=(10,90))[0]
            NFT_Mouth = 'None.png'

        if (NFT_Facewear in ['Pac-Man mask.png','Btc mask.png','Gox mask.png'] and NFT_Expression in ['Smile.png','Wink.png']):

            NFT_Expression = 'Rest.png'
        
        if (NFT_FacialHair in['Duck tail black.png', 'Duck tail brown.png','Full beard black.png','Full beard brown.png'] and NFT_Expression in ['Smile.png', 'Wink.png']):

            NFT_Expression = 'Rest.png'
        
        if (NFT_Base in ['Ghost.png','Cyborg.png'] and NFT_FacialHair != 'None.png'):
            
            NFT_FacialHair = 'None.png'

        if (NFT_Base == 'Ghost.png' and NFT_Mouth != 'None.png'):

            NFT_Mouth = 'None.png'

        ##other controls
        ##import final images

        Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand = get_Images (NFT_BackGrounds, NFT_Base, NFT_Expression, NFT_Torso, NFT_Mouth, 
                                                                                                                                                                                       NFT_FacialHair, NFT_Facewear, NFT_Head, NFT_WholeBody, NFT_Hand)
        ##import final images
        ##image generation



        Base = NFT_Base.split('.')[0]

        if special_hand_number == 2 and Base in special_hands:
            try:
                Image_Hand = get_special_hand(Base, special_hands[Base])
            except:
                pass
        

        if (NFT_Mouth != 'None.png' and NFT_Hand != 'None.png'):
            final = get_NFT_hand(Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand)
        
        elif (NFT_Mouth != 'None.png'):
            final = get_NFT_mouth(Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand)
        else:
            final = get_NFT_main (Image_BackGrounds, Image_Base, Image_Expression, Image_Torso, Image_FacialHair, Image_Mouth, Image_Facewear, Image_Head, Image_WholeBody, Image_Hand)

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
                    'trait_type': 'Expression',
                    'value': NFT_Expression.split('.')[0]
                },
                {
                    'trait_type': 'Torso',
                    'value': NFT_Torso.split('.')[0]
                },
                {
                    'trait_type': 'Facial Hair',
                    'value': NFT_FacialHair.split('.')[0]
                },
                {
                    'trait_type': 'Mouth',
                    'value': NFT_Mouth.split('.')[0]
                },
                {
                    'trait_type': 'Facewear',
                    'value': NFT_Facewear.split('.')[0]
                },
                {
                   'trait_type': 'Head',
                    'value': NFT_Head.split('.')[0]
                },

                {
                    'trait_type': 'Whole Body',  
                    'value': NFT_WholeBody.split('.')[0]
                },
                {
                    'trait_type': '1/1',
                    'value': 'None'
                }]
            }
        

        with open(rf'{json_out_path}/Rug_Lord #{i}.json', 'w') as json_print:  # Nota el uso de 'with', que es una buena práctica para manejar archivos
            json.dump(metadata, json_print, indent=4)
        
        final_resized = final.resize((480, 480), Image.NEAREST)
        final_resized.save(f'{output_path_resized}/Rug_Lord #{i}.png')
        print (rf"Rug Lord #{i}")
        i+=1