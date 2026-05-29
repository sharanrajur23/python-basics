class Item:
    def __init__(self,name,weight,value):
        self.name=name
        self.weight=weight
        self.value=value

class Player:
    def __init__(self,name,max_carry_weight,inventory=None,gold=0):
        self.name = name
        self.max_carry_weight=max_carry_weight
        if inventory is None:
            self.inventory=[]
        else :
            self.inventory=inventory
        self.gold=gold
        Total_inventory_weight=0
        for i in self.inventory:
            Total_inventory_weight=Total_inventory_weight+i

    def pick_up(self,item_object):
        self.item_object=item_object
        if (self.item_object+Total_inventory_weight)>self.max_carry_weight:
            print("You are carrying too much.")
        else :
            self.inventory.append(self.item_object)

    def sell_item(self,item_name):
        self.item_name=item_name
        for self.item_name in self.inventory:
            self.inventory.remove(self.item_name)
            self.gold = self.gold+self.value
            print("Successfully Removed")
        else:
            print("item Not in inventory")

    def view_inventory(self):
        print(f"Players current gold : {self.gold}")
        print(f"Total current weight :{Total_inventory_weight}")
        for self.item_name in self.inventory:
            print(self.item_name)
