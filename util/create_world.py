
from adventure.models import Player, Room
Room.objects.all().delete()


def create_rooms():
    for i in range(10):
        for j in range(10):
            new_room= Room(title="title", description="something",x=j,y=i)
            new_room.save()


create_rooms()


rooms_list = Room.objects.all()
print(rooms_list)
print(rooms_list[0].x)


def generate_connection():
    for i in range(99):
        for j in range(100):
            if not rooms_list[i] == rooms_list[j]:
                if rooms_list[i].x == rooms_list[j].x and rooms_list[i].y - rooms_list[j].y == 1:
                    rooms_list[i].connectRooms(rooms_list[j],"s")
                if rooms_list[i].x == rooms_list[j].x and rooms_list[j].y - rooms_list[i].y == 1:
                    rooms_list[i].connectRooms(rooms_list[j],"n")
                if rooms_list[i].y == rooms_list[j].y and rooms_list[i].x - rooms_list[j].x == 1:
                    rooms_list[i].connectRooms(rooms_list[j], "w")
                if rooms_list[i].y == rooms_list[j].y and rooms_list[j].x - rooms_list[i].x == 1:
                    rooms_list[i].connectRooms(rooms_list[j],"e")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

generate_connection()