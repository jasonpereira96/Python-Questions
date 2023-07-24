class Appliance:
    def __init__(self, id):
        # code to load the appliance from disk is necessary
        pass

    def save(self):
        # write the appliance to disk
        pass
    
    def set_type(self, type):
        pass
    # and other setters


class ApplianceManager:
    def __init__(self):
        self.app1 = None
        self.app2 = None
        self.app3 = None

    def set_current_appliance(self, aid):
        if self.current_appliance == aid:
            return

        if self.app1 != None and self.app1.id == aid:
            self.current_appliance = self.app1
            return
        elif self.app2 != None and self.app2.id == aid:
            self.current_appliance = self.app2
            return
        elif self.app3 != None and self.app3.id == aid:
            self.current_appliance = self.app3
            return

        self.app1.save() # save the current appliance to disk
        self.app1 = Appliance(aid) # create new appliance
        
        self.current_appliance = self.app1


    def get_current_appliance_type(self):
        if self.current_appliance == None:
            print("no current appliance")
        return self.current_appliance.type    