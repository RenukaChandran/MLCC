import random


class Vehicle:

    def __init__(self, id, type):
        self.vehicle_id = id
        self.vehicle_type = type

    def check_space(self):
        small_slot = medium_slot = large_slot = -1
        for slot in ParkingSpace.not_assigned:
            if list_slots[slot].parking_size == "small":
                small_slot = slot
                break
        for slot in ParkingSpace.not_assigned:
            if list_slots[slot].parking_size == "medium":
                medium_slot = slot
                break
        for slot in ParkingSpace.not_assigned:
            if list_slots[slot].parking_size == "large":
                large_slot = slot
                break

        if self.vehicle_type == "bus":
            if large_slot != -1:
                list_slots[large_slot].parked(self)
            else:
                list_slots[large_slot].no_space()

        elif self.vehicle_type == "car":
            if medium_slot != -1:
                list_slots[medium_slot].parked(self)
            elif large_slot != -1:
                list_slots[large_slot].parked(self)
            else:
                list_slots[large_slot].no_space()

        elif self.vehicle_type == "motorcycle":
            if small_slot != -1:
                list_slots[small_slot].parked(self)
            elif medium_slot != -1:
                list_slots[medium_slot].parked(self)
            elif large_slot != -1:
                list_slots[large_slot].parked(self)
            else:
                list_slots[large_slot].no_space()
        else:
                list_slots[0].no_space()


class ParkingSpace():
    not_assigned = [i for i in range(0, 20)]

    def __init__(self, id, size):
        self.parking_id = id
        self.parking_size = size
        self.parked_vehicle = Vehicle(0, "free")

    def __str__(self):
        return str(self.parking_id) + " " + str(self.parking_size) + " " + str(self.parked_vehicle.vehicle_id) + " " + str(self.parked_vehicle.vehicle_type)

    def parked(self,vehicle_park):
        self.parked_vehicle.__dict__ = vehicle_park.__dict__.copy()
        ParkingSpace.not_assigned.remove(self.parking_id - 1)
        print("parked your vehicle \n vehicle id {} \n parking slot id {}".format(self.parked_vehicle.vehicle_id, self.parking_id))

    def no_space(self):
        print("parking slot not available for vehicle type")


list_slots = []
sizes = ["small"] * 10 + ["medium"] * 7 + ["large"] * 3
random.shuffle(sizes)

for i in range(0, 20):
    list_slots.append(ParkingSpace(i+1, sizes[i]))

while len(ParkingSpace.not_assigned)>0:
    print("enter your vehicle id and type(motorcycle, car, bus)")
    id = input()
    size = input()
    to_be_parked = Vehicle(id, size)
    to_be_parked.check_space()