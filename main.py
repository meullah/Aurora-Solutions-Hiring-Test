import clinic
import warnings
myClinic = clinic.Clinic()

help = """
=================================\n
Enter 1 for registeration\n
Enter 2 for booking appointment\n
Enter 3 to view patients\n
Enter 4 to view appointments\n
Enter 5 to delete patient\n
=================================\n
"""
if __name__ == "__main__":
    while(1):
        print(help)
        choice = int(input("Enter Choice: "))
        if choice==1:
            name = input("Enter patient's name: ")
            email = input("Enter patient's email: ")
            ph = input("Enter patient's phone number: ")
            myClinic.registeration(name,email,ph)
        elif choice==2:
            name = input("Enter patient's name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            print("""slot: 1 => 09:30 AM to 10:00 AM\n
                     slot: 2 => 10:01 AM to 10:30 AM\n                    
                     slot: 3 => 10:31 AM to 11:00 AM\n                    
                     slot: 4 => 11:01 AM to 11:30 AM\n
                     slot: 5 => 11:31 AM to 12:00 PM\n""")
            slot = input("Enter slot number: ")
            myClinic.bookAppointment(name,date,slot)
            
        elif choice==3:
            myClinic.getAllPatients()
        elif choice==4:
            myClinic.view_appointemnts()
        elif choice==5:
            name = input("Enter patient's name to delete: ")
            myClinic.delete(name)
        else:
            warnings.warn("INVALID INPUT")
            print(help)

        