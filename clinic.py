class Clinic:
    patients={}
    appointemnts ={}

    def registeration(self,name,email,phone):
        """
        Registeration of patient.

        Parameters
        ----------
        name (str):  patient's name

        email (str): patient's email

        phone (str): patient's phone number
        
        Returns
        -------      
            True if registeration is sucessfull False otherwise,

        """
        if name not in self.patients:
            self.patients[name] = [email,phone]
            return True
        else:
            print("Patient already exisits")
            return False
        
    def getAllPatients(self):
        """
        Prints a list of patients registered in the clinic..

        """
        for key in self.patients.keys():
            print(key)

    def delete(self,name):
        """
        deletes specified patient.

        Parameters
        ----------
        name (str):  patient's name
        
        Returns
        -------      
            True if record is deleted sucessfully False otherwise,
        """
        try:
            self.patients.pop(name)
            print("sucessful")
            return True
        except:
            print('failed')
            return False
        
    def bookAppointment(self,name,date,slot_number):
        """
        Registeration of patient.

        Parameters
        ----------
        name (str):  patient's name
        
        date (str):  date of appointment format (YYYY-MM-DD)

        slot_number (int):   enum 1, 2, 3, 4 or 5
        
                    slot: 1 => 09:30 AM to 10:00 AM
                    
                    slot: 2 => 10:01 AM to 10:30 AM
                    
                    slot: 3 => 10:31 AM to 11:00 AM
                    
                    slot: 4 => 11:01 AM to 11:30 AM
                    
                    slot: 5 => 11:31 AM to 12:00 PM
        
        Returns
        -------      
            True, if Appointment is sucessfully reserved otherwise False

        """
        
        time = None
        if slot_number==1:
            time = "09:30 AM to 10:00 AM"
        elif slot_number==2:
            time = "10:01 AM to 10:30 AM"
        elif slot_number==3:
            time = "10:31 AM to 11:00 AM"
        elif slot_number==4:
            time = "11:01 AM to 11:30 AM"
        elif slot_number==5:
            time = "11:31 AM to 12:00 PM"
        else:
            print('invalid input for time')
            return False
            
        
        if date not in self.appointemnts:
            self.appointemnts[date] = {
                name : time            
            }
            return True
        else:
            if len(self.appointemnts[date].keys())==4:
                print("All slots are booked")
                return False
            temp = self.appointemnts[date].items()
            for key,value in temp:
                if value==time:
                    print("This slot is already booked")
                    return False
                
            self.appointemnts[date][name]=time
            return True 
        
    def view_appointemnts(self):
        """
        view all appointments
        """
        get_all_values(self.appointemnts)
        
    def get_all_values(self,nested_dictionary):
        for key, value in nested_dictionary.items():
            if type(value) is dict:
                get_all_values(value)
            else:
                print(key, ":", value)