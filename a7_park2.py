class Park:
    def __init__(self, name):
        self.name = name
        self.maxNum = 3
        self.parkingSpaces = {}

    def add_parking_space(self, space_id):
            return self.parkingSpaces.append(space_id)

    def __str__(self):
        total_spaces = len(self.parkingSpaces)
        return f"The car park {self.name} has a total of {total_spaces} parking spaces."


    def add(self, spaces):
        for space in spaces:

            if space.startswith("eLot"):
                print("This is an Elot.")
            else:
                print("This is not an Elot.")
            #     if len(self.parkingSpaces) >= self.maxNum:
            #         raise MaxNumError("Maximum number of eLots reached.")
            #     else:
            #         self.add_parking_space(space)
            # else:
            #     self.add_parking_space(space)

    def remove(self, space_id):
        if space_id in self.parkingSpaces:
            del self.parkingSpaces[space_id]
            return True
        else:
            return False

    def numFreeLots(self):
        count = 0
        for space_id in self.parkingSpaces:
            if self.parkingSpaces[space_id] is None:
                count += 1
        return count

    def toFile(carparkspaces):
        with open(carparkspaces, 'w') as file:
            for space_id, space_info in self.parkingSpaces.items():
                space_type = space_info['type']
                space_status = space_info['status']
                total_duration = space_info['total_duration']
                line = f"{space_id} {space_type} {space_status} {total_duration}\n"
                file.write(line)
        file.close()

class MaxNumError(Exception):
    def __init__(self, error):
        self.error = error 
    
    def __str__(self):
        return f"The maximum number of allocated IDs have been used: {self.error}"
    

#A method called add that receives a list containing parking spaces (both stallsand eLots) and adds the spaces in the list to the car park.

class CarPark:
    def __init__(self):
        self.stalls = []
        self.eLots = []
    
    def add(self, parking_spaces):
       
        for space in parking_spaces:
            if space["type"] == "stall":
                self.stalls.append(space)
            elif space["type"] == "eLot":
                self.eLots.append(space)
        
        self.stalls.sort(key=lambda x: x["id"])
        self.eLots.sort(key=lambda x: x["id"])
        
        
        