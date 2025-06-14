#WAP Guest list
guest_list=[]
while(True):
    print("------MENU------")
    print("1.Add the Guest")
    print("2.Remove the guest who cancels")
    print("3.Check if a guest is attending the party or not")
    print("4.View the final guest list")
    print("5.Exit")
    print("*****************")
    choice=int(input("Enter your choice:"))
    if (choice>=1 and choice<=5):
        if (choice==1):
            Guest_Name=input("Enter the name of the guest:")
            guest_list.append(Guest_Name)
            print(f"{Guest_Name} is added to the guestlist")
        elif (choice==2):
            Cancelled_guest= input("Enter the name of the Cancelled guest:")
            if Cancelled_guest in guest_list:
                guest_list.remove(Cancelled_guest)
                print(f"{Cancelled_guest} is removed from the Guest list")
            else:
                print(f"{Cancelled_guest} is not in the guest list")
        elif(choice==3):
            Check_Guest=input("Enter the Guest Name to check:")
            if Check_Guest in Check_Guest:
                print(f"{Check_Guest} is attending the party:")
            else:
                print(f"{Check_Guest} is not attending the party:")
        elif(choice==4):
            if (len(guest_list)==0):
                print("Guest List is empty, enter the guest names")
            else:
                guest_list.sort()
                print("Here is your final Guest list:")
                print(guest_list)
        else:
            print("Enjoy the party...!!!")
            break
    else:
        print("Invalid-Input")