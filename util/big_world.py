
from django.contrib.auth.models import User
from adventure.models import Player, Room
from random import randint

Room.objects.all().delete()
names = [
            [
                'Dark', 'Grimy', 'Dirty', 'Narrow', 'Large', 'Dusty', 'Dimly Lit', 'Musty', "Cold", 'Repulsive', 'Decaying', 'Secret', 'Gloomy', 'Crumbling', 'Forgotten', 'Legendary', 'Forbidden', 'Ancient', 'Hidden', 'Eerie'
            ],
            [
                'Great Room', 'Hallway', 'Library', 'Quarters', 'Den', 'Armory', 'Barracks', 'Tower', 'Workshop', 'Pit', 'Dungeon', 'Hall', 'Cave', 'Ruins', 'Fortress', 'Labyrinth', 'Tomb', 'Mine', 'Academy', 'Vault', 'Asylum', 'Lair', 'Forge', 'Arena', 'Observatory', 'Barrow', 'Gallery', 'Refuge', 'Manor', 'Abbey', 'Garrison', 'Cathedral', 'Citadel', 'Shrine', 'Embassy'
            ],
            [
                'Destruction', 'Misery', 'Anguish', 'Malaise', 'Agony', 'Dread', 'Despair', 'Fury', 'Judgement', 'Fire', 'Death', 'Demise', 'Desolation', 'Doom', 'Devastation', 'Silence', 'Isolation', 'Lost Dreams', 'the Dragon', 'the Inferno', 'the Ancient Ones', 'Torment', 'Corrupted Souls', 'the Abyss', 'Chaos', 'the Skulls', 'the Apocalypse', 'the Banished Sect'
            ]
        ]
​
descs = [
                [
                    'Beams of light pierce through the clouds of dirt and dust lingering in the air.',
                    'Every surface is covered in a thick layer of dust and grime.',
                    'The warm air feels like it is sticking to your skin.', 
                    'The surface of the walls are chipping away.',
                    'The room is oppressively humid, making it hard to breathe.',
                    'A musty smell permeates the air around you.',
                    'The smell of mold and mildew lingers in the air.',
                    'The surroundings are adorned with offerings and honorific art, as if in preparation for a wake.',
                    'You feel as though there is an ominous aura about this place.',
                    'The room is filled with shadows, making it difficult to tell what you are looking at.',
                    'The scale and adornment of this room is beyond anything you have seen before.',
                    'This room looks as though it has not been used for anything in decades.',
                    'It is as though this room has not been used in centuries.',
                    'The room is filled with terrifying idols and symbols.',
                    'The room is filled with ancient armor and weapons, all of them forgotten and slowly rusting away.',
                    'It is as if the room itself is rotting away. The furniture, walls, floor, and everything else is falling to pieces.', 
                    'You have to hold your nose as soon as you enter. The stench in this room is overwhelming.'
                ],
                [
                    'You are in a massive room. Each footstep echoes off distant walls.',
                    'There is an altar in the room, covered in symbols you cannot read and idols you do not recognize.',
                    'You are in a hallway, most doors are blocked.',
                    'You have entered a large chambers, filled wall to wall with seating. It must have been used for grand debates.',
                    'Your surroundings do not resemble those of a room. There are stalactites hanging from the ceiling, as if you are in a cavern.',
                    'You have entered an absolutely massive room. It reaches out in every direction.',
                    'You are on an overarching balcony that looks down on a great arena.',
                    'The smell of old paper fills the room, and rows of bookshelves neatly go from wall to wall.',
                    'Beakers and burners litter a series of desks. Terrifying experiments sit inside jars on shelves.',
                    'The room is lined with stone coffins, each engraved with names in an unknown language.',
                    'The walls themselves hold countless graves, each marked with the names of the dead.',
                    'In the center of the room stands a grand statue of an ancient goddess.',
                    'The room is peaceful. You get the feeling that all is right in the world.',
                    'A serpentene decoration addorns the room. Gold and treasure is piled in the corner.',
                    'A broken altar sits in the corner. Melted and lit candles line the walls.',
                    'You have entered a series of halls. Most doors are blocked.',
                    'Your surroundings do not resemble those of a room. There are stalactites hanging from the ceiling, as if you are in a cave.'
                ],
                [
                    'A feeling of death hangs over the room, and decaying bodies lie in the corner.',
                    'An oppressive feeling of the annihilation comes over you.',
                    'A rack and stretching tools sit in the corner next to a pile of bones.',
                    'An inner peace settles over you.', 
                    'There is a massive X in the middle of the room. Echoes of ancient secrets bounce off the walls.',
                    'You find it hard to think. Which way was out, again?',
                    'Angry red writing covers the walls, and the adornments seem out of place.',
                    'There is blood splattered around the room.', 
                    'The ground is broken up beneath your feet.',
                    'You begin to feel despair that this is all you will ever know.',
                    'Soft choir chanting drifts down from somewhere.', 
                    'The oppressive air feeds your feeling of impending doom.'
                ]
            ]




def create_rooms():
    for i in range(10):
        for j in range(10):
            # Create room title and description
            title = ""
            desc = ""
            for z in range(3):
                num = randint(0, len(names[z])-1)
                num2 = randint(0, len(descs[z])-1)
                if len(title) == 0:
                    title += names[z][num] + " "
                    desc += descs[z][num2] + " "
                elif z == 1:
                    title += names[z][num] + " of "
                    desc += descs[z][num2] + " "
                else:
                    title += names[z][num]
                    desc += descs[z][num2]
            new_room = Room(title=title, description=desc, x=j, y=i)
            new_room.save()

create_rooms()

rooms_list = Room.objects.all()
print(rooms_list)
print(rooms_list[0].x)

# def generate_connection():

#     for i in range(100):
#         for j in range(100):
#             if rooms_list[i].x == rooms_list[j].x :
#                 if rooms_list[i].y - rooms_list[j].y == 1:
#                     print("x,y",rooms_list[i].x,rooms_list[i].y )
#                     print("s",rooms_list[i].x,rooms_list[j].x, (rooms_list[i].y - rooms_list[j].y))
#                     rooms_list[i].connectRooms(rooms_list[j], "s")
#                     rooms_list[j].connectRooms(rooms_list[i], "n")
                    
#                 elif rooms_list[j].y - rooms_list[i].y == 1:
#                     print("x,y",rooms_list[i].x,rooms_list[i].y )
#                     print("n",rooms_list[i].x,rooms_list[j].x, (rooms_list[i].y - rooms_list[j].y))
#                     rooms_list[i].connectRooms(rooms_list[j], "n")
#                     rooms_list[j].connectRooms(rooms_list[i], "s")
                    
#             elif rooms_list[i].y == rooms_list[j].y :
#                 if rooms_list[i].x - rooms_list[j].x == 1:
#                     print("x,y",rooms_list[i].x,rooms_list[i].y )
#                     print("w",rooms_list[i].y,rooms_list[j].y, (rooms_list[i].x - rooms_list[j].x))
#                     rooms_list[i].connectRooms(rooms_list[j], "w")
#                     rooms_list[j].connectRooms(rooms_list[i], "e")
                    
#                 elif rooms_list[j].x - rooms_list[i].x == 1:
#                     print("x,y",rooms_list[i].x,rooms_list[i].y )
#                     print("e",rooms_list[i].y,rooms_list[j].y, (rooms_list[i].x - rooms_list[j].x))
#                     rooms_list[i].connectRooms(rooms_list[j], "e")
#                     rooms_list[j].connectRooms(rooms_list[i], "w")


def generate_connection():
    for i in range(100):
        print(rooms_list[i].x,rooms_list[i].y)
        if rooms_list[i].x == 0 :
            if rooms_list[i].y == 0:
                rooms_list[i].connectRooms(rooms_list[i + 10], "n")
                rooms_list[i].connectRooms(rooms_list[i + 1], "e")
            elif rooms_list[i].y == 9:
                rooms_list[i].connectRooms(rooms_list[i - 10], "s")
                rooms_list[i].connectRooms(rooms_list[i + 1], "e")
            else:
                rooms_list[i].connectRooms(rooms_list[i + 10], "n")
                rooms_list[i].connectRooms(rooms_list[i + 1], "e")
                rooms_list[i].connectRooms(rooms_list[i - 10], "s")
        elif rooms_list[i].x == 9:
            if rooms_list[i].y == 0:
                rooms_list[i].connectRooms(rooms_list[i + 10], "n")
                rooms_list[i].connectRooms(rooms_list[i - 1], "w")
            elif rooms_list[i].y == 9:
                rooms_list[i].connectRooms(rooms_list[i - 10], "s")
                rooms_list[i].connectRooms(rooms_list[i - 1], "w")
            else:
                rooms_list[i].connectRooms(rooms_list[i + 10], "n")
                rooms_list[i].connectRooms(rooms_list[i - 1], "w")
                rooms_list[i].connectRooms(rooms_list[i - 10], "s")
        elif rooms_list[i].y == 0:
            rooms_list[i].connectRooms(rooms_list[i + 10], "n")
            rooms_list[i].connectRooms(rooms_list[i + 1], "e")
            rooms_list[i].connectRooms(rooms_list[i - 1], "w")
        elif rooms_list[i].y == 9:
            rooms_list[i].connectRooms(rooms_list[i - 10], "s")
            rooms_list[i].connectRooms(rooms_list[i + 1], "e")
            rooms_list[i].connectRooms(rooms_list[i - 1], "w")
        else:
            rooms_list[i].connectRooms(rooms_list[i+10], "n")
            rooms_list[i].connectRooms(rooms_list[i-10], "s")
            rooms_list[i].connectRooms(rooms_list[i + 1], "e")
            rooms_list[i].connectRooms(rooms_list[i-1], "w")
            




generate_connection()

players=Player.objects.all()
for p in players:
  p.currentRoom=Room.objects.first().id
  p.save()


