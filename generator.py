from itertools import permutations
from PIL import Image
import random
import os

all_images = []
traits_counter = {}


def choost_traits(path):
    file_name = []
    file_rarity = []
    for filename in os.listdir(os.getcwd() + '\\traits\\' + path):
        file_name.append(filename)
        file_rarity.append(int(os.path.splitext(filename)[0].split('_')[0]))
    chosen = random.choices(file_name, file_rarity, k=1)[0]
    return chosen, Image.open(os.getcwd() + '\\traits\\' + path + '\\' + chosen)


def traits_count(key):
    if key in traits_counter:
        traits_counter[key] += 1
    else:
        traits_counter[key] = 1

def charater_generator(file_name):
    current_image = {}
    background_name, background_image= choost_traits('background')
    skin_name, skin_image = choost_traits('skin')
    mouth_name, mouth_image = choost_traits('mouth')
    eyes_name,  eyes_image= choost_traits('eyes')
    decoration_name, decoration_image = choost_traits('decoration')
    # current_image['background'] = background_name
    current_image['skin'] = skin_name
    current_image['mouth'] = mouth_name
    current_image['eyes'] = eyes_name
    current_image['decoration'] = decoration_name
    if current_image in all_images:
        print('same')
        return charater_generator(file_name)
    else:
        background_image = Image.alpha_composite(background_image, skin_image)
        background_image = Image.alpha_composite(background_image, eyes_image)
        background_image = Image.alpha_composite(background_image, mouth_image)
        background_image = Image.alpha_composite(background_image, decoration_image)
        background_image = background_image.resize((500, 500), resample = Image.BOX)
        background_image = background_image.save(os.getcwd() + '\\results4\\#' + file_name + '.png')
        all_images.append(current_image)
        traits_count(background_name)
        traits_count(skin_name)
        traits_count(mouth_name)
        traits_count(eyes_name)
        traits_count(decoration_name)

for i in range(1, 51):
    charater_generator(str(i))

print(traits_counter)
