# imports for needed assets
import json
import time

# this is so we can see when new addresses are added to teh database
from datetime import datetime

# this open the external database
with open('addressDB.json', 'r') as data_file:
    data = json.load(data_file)

# input for the users address, with ui for messing it up and not having to re-run the code. Nice!
print("Please enter your address below (if you mess up enter 'Q' to restart) \n")
while True:
    line1 = input("Address Line 1: ")
    if line1.upper() == "Q":
        print('Please try again!')
        continue

    line2 = input("Apartment #: ")
    if line2.upper() == "Q":
        print('Please try again!')
        continue

    city = input("City: ")
    if city.upper() == "Q":
        print('Please try again!')
        continue

    state = input("State (i.e. GA): ")
    if state.upper() == 'Q':
        print('Please try again!')
        continue

    zipcode = input("Zip Code: ")
    if zipcode.upper() == "Q":
        print('Please try again!')
        continue

    else:
        break


def correctAddy():
    print("\nThe address you address you put in is: \n\n" + line1.upper() + '\n' + city.upper() + '\n' + state.upper()
          + '\n' + zipcode + '\n')
    print("This address matches the database and is verified, thank you for using our Address Verification Service")

    # UI checks the data, it is in there, so it spits out a correct address line


def fixAddy():
    # this is for the NEW address
    print("\nPlease enter your FIXED address below (if you mess up enter 'Q' to restart) \n")
    while True:
        line12 = input("Address Line 1: ")
        if line12.upper() == "Q":
            print('Please try again!')
            continue

        line22 = input("Apartment #: ")
        if line22.upper() == "Q":
            print('Please try again!')
            continue

        city2 = input("City: ")
        if city2.upper() == "Q":
            print('Please try again!')
            continue

        state2 = input("State (i.e. GA): ")
        if state2.upper() == 'Q':
            print('Please try again!')
            continue

        zipcode2 = input("Zip Code: ")
        if zipcode2.upper() == "Q":
            print('Please try again!')
            continue

        corw = input('Is this edited address correct? (Y or N) ')

        if corw.upper() == "N":
            print('Please try again!')
            continue

        elif corw.upper() == "Y":
            print('Thank you for the correct address!')
            break
    # this verifies the new address that the user put in
    while True:
        print('\nVerification in progress...\n')
        time.sleep(1)
        if line12.upper() in str(data).upper():
            print('Address Line 1: pass')
            time.sleep(.5)
            if line22.upper() in str(data).upper():
                print('Apartment #: pass')
                time.sleep(.5)
                if city2.upper() in str(data).upper():
                    print('City: pass')
                    time.sleep(.5)
                    if state2.upper() in str(data).upper():
                        print('State: pass')
                        time.sleep(.5)
                        if zipcode2 in str(data):
                            print('Zip Code: pass')
                            time.sleep(1)
                            print("\n\nThe fixed address you put in is: \n\n" + line12.upper() + '\n' +
                                  city2.upper() + '\n' + state2.upper()
                                  + '\n' + zipcode2 + '\n')
                            print("This address matches the database and is verified, thank you for using our Address "
                                  "Verification Service\nGoodbye!")
                            print(data)
                            break
                        # if fail, takes the user to a choice of what adddress to use
                        else:
                            print('\nZip Code: fail')
                            time.sleep(1)
                            wrongline = zipcode2
                            print("Invalid input: " + wrongline + '\n')

                    else:
                        print('\nState: fail')
                        time.sleep(1)
                        wrongline = state2
                        print("Invalid input: " + wrongline + '\n')

                else:
                    print('\nCity: fail')
                    time.sleep(1)
                    wrongline = city2
                    print("Invalid input: " + wrongline + '\n')

            else:
                print('\nApartment #: fail')
                time.sleep(1)
                wrongline = line22
                print("Invalid input: " + wrongline + '\n')

        else:
            print('Address Line 1: fail')
            time.sleep(1)
            wrongline = line12
            print("Invalid input: " + wrongline + '\n')

        print("Verification failed, please continue to the next steps:")

        print('\nThe FIXED address you put in is: \n'
              + line12.upper() + '\n' + city2.upper() + '\n' + state2.upper() + '\n' + zipcode2 + '\n')
        print('\nThe ORIGINAL address you put in is: \n\n'
              + line1.upper() + '\n' + city.upper() + '\n' + state.upper() + '\n' + zipcode + '\n')

        choice = input('Which address would you like to use? (O)riginal or (F)ixed: ')
        # if you choose fixed address
        if choice.upper() == 'F':
            while True:
                print('\nYour choice was:\n'
                      + line12.upper() + '\n' + city2.upper() + '\n' + state2.upper() + '\n' + zipcode2 + '\n')
                addyor = input("Would you like to add this address to the database? (Y or N) ")

                if addyor.upper() == "Y":

                    admin = input("What is your Admin UserID? (ie email address) ")

                    print('\nAddress will now be added to the database!')
                    print('\nThank you for using our Address Verification Service! \n\nGoodbye.')

                    newadd = {
                        "entryNumber": None,
                        "addressLine1": line12.upper(),
                        "addressLine2": line22,
                        "city": city2.upper(),
                        "state": state2.upper(),
                        "postalCode": zipcode2,
                        "_version": 0,
                        "_created": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                        "_createdby": admin,
                        "_changed": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                    }

                    print('json version of the address: ' + str(newadd))

                    # this appends the new address to the json file EXTERNAL
                    with open("addressDB.json", "r+") as append:
                        file_data = json.load(append)

                        file_data.append(newadd)
                        append.seek(0)

                        json.dump(file_data, append, indent=4)

                elif addyor.upper() == "N":
                    print('You have Chosen No. \n\nThank you for using our Address Verification Service! \n\nGoodbye.')

                    break

                # if you put in a wrong letter
                else:
                    print('Incorrect Input! please try again... ')

                break

            break
        # if you choose your original address
        elif choice.upper() == 'O':
            while True:
                print('\nThe choice was:\n'
                      + line1.upper() + '\n' + city.upper() + '\n' + state.upper() + '\n' + zipcode + '\n')
                addyor = input("Would you like to add this address to the database? (Y or N) ")

                if addyor.upper() == "Y":

                    admin = input("What is your Admin UserID? (ie email address) ")

                    print('\nAddress will now be added to the database!')
                    print('\nThank you for using our Address Verification Service! \n\nGoodbye.')

                    # takes the input and makes a new data entry!
                    newadd = {
                        "entryNumber": None,
                        "addressLine1": line12.upper(),
                        "addressLine2": line22,
                        "city": city2.upper(),
                        "state": state2.upper(),
                        "postalCode": zipcode2,
                        "_version": 0,
                        "_created": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                        "_createdby": admin,
                        "_changed": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                    }

                    print('json version of the address: ' + str(newadd))

                    # this appends the new address to the json file EXTERNAL
                    with open("addressDB.json", "r+") as append:
                        file_data = json.load(append)

                        file_data.append(newadd)
                        append.seek(0)

                        json.dump(file_data, append, indent=4)

                    break

                elif addyor.upper() == "N":
                    print('You have Chosen No. \n\nThank you for using our Address Verification Service! \n\nGoodbye.')

                    break

                # if you put in a wrong letter
                else:
                    print('Incorrect Input! please try again... ')

                break

        else:
            print('Incorrect Input! please try again... ')

        break


def wrongAddy():
    while True:
        print('\nAddress is not found in the database.\n\nThe address you address you put in is: \n\n'
              + line1.upper() + '\n' + city.upper() + '\n' + state.upper() + '\n' + zipcode + '\n')
        addyor = input("Would you like to add this address to the database? (Y or N) ")

        if addyor.upper() == "Y":

            admin = input("What is your Admin UserID? (ie email address) ")

            print('Address will now be added to the database!')
            print('\nThank you for using our Address Verification Service! \n\nGoodbye.')

            # converts the user input into a dict
            newadd = {
                "entryNumber": None,
                "addressLine1": line1.upper(),
                "addressLine2": line2,
                "city": city.upper(),
                "state": state.upper(),
                "postalCode": zipcode,
                "_version": 0,
                "_created": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                "_createdby": admin,
                "_changed": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
            }

            print('json version of the address: ' + str(newadd))

            # this appends the new address to the json file EXTERNAL
            with open("addressDB.json", "r+") as append:
                file_data = json.load(append)

                file_data.append(newadd)
                append.seek(0)

                json.dump(file_data, append, indent=4)

            break

        elif addyor.upper() == "N":
            print('You have Chosen No. \n\nThank you for using our Address Verification Service! \n\nGoodbye.')

            break

        # if you put in a wrong letter
        else:
            print('Incorrect Input! please try again... ')

        break


# IF statements that run through every input line by line to check teh database. if any pass, they say so and send the
# user to the correct address function,
# if one fails it will tell you which one fails and and send you to the wrong address function
def verifyAPI():
    print('\nVerification in progress...')
    time.sleep(1)
    if line1.upper() in str(data).upper():
        print('\nAddress Line 1: pass')
        time.sleep(.5)
        if line2.upper() in str(data).upper():
            print('Apartment #: pass')
            time.sleep(.5)
            if city.upper() in str(data).upper():
                print('City: pass')
                time.sleep(.5)
                if state.upper() in str(data).upper():
                    print('State: pass')
                    time.sleep(.5)
                    if zipcode in str(data).upper():
                        print('Zip Code: pass')
                        time.sleep(1)
                        correctAddy()
                    # the fails start here,
                    # if one fails it prompts the user if the failed addres is entered correctly or if they made a
                    # mistake inputting it, ei. is te address just not in the database or did you make a typo.
                    # i could not get the system to individually check addresses for partial correctness.~~~
                    else:
                        print('\nZip Code: fail')
                        time.sleep(1)
                        wrongline = zipcode
                        print("\nThis address is partially incorrect.\nSome of your address passed, but this part was "
                              "incorrect:\nInvalid input: " + wrongline)
                        fixornot = input('\nIs this Zipcode correct(C) or would you like to fix it(F)? (C or F) ')
                        while True:
                            if fixornot.upper() == "C":
                                wrongAddy()
                                break
                            elif fixornot.upper() == "F":
                                fixAddy()
                                break
                            else:
                                print('Incorrect Input! please try again... ')

                            break
                else:
                    print('\nState: fail')
                    time.sleep(1)
                    wrongline = state
                    print("\nThis address is partially incorrect.\nSome of your address passed, but this part was "
                          "incorrect:\nInvalid input: " + wrongline)
                    fixornot = input('\nIs this State correct(C) or would you like to fix it(F)? (C or F) ')
                    while True:
                        if fixornot.upper() == "C":
                            wrongAddy()
                            break
                        elif fixornot.upper() == "F":
                            fixAddy()
                            break
                        else:
                            print('Incorrect Input! please try again... ')

                        break
            else:
                print('\nCity: fail')
                time.sleep(1)
                wrongline = city
                print("\nThis address is partially incorrect.\nSome of your address passed, but this part was "
                      "incorrect:\nInvalid input: " + wrongline)
                fixornot = input('\nIs this city correct(C) or would you like to fix it(F)? (C or F) ')
                while True:
                    if fixornot.upper() == "C":
                        wrongAddy()
                        break
                    elif fixornot.upper() == "F":
                        fixAddy()
                        break
                    else:
                        print('Incorrect Input! please try again... ')

                    break
        else:
            print('\nApartment #: fail')
            time.sleep(1)
            wrongline = line2
            print("\nThis address is partially incorrect.\nSome of your address passed, but this part was "
                  "incorrect:\nInvalid input: " + wrongline)
            fixornot = input('\nIs this Apartment # correct(C) or would you like to fix it(F)? (C or F) ')
            while True:
                if fixornot.upper() == "C":
                    wrongAddy()
                    break
                elif fixornot.upper() == "F":
                    fixAddy()
                    break
                else:
                    print('Incorrect Input! please try again... ')

                break
    else:
        time.sleep(1)
        print('\nAddress Line 1: fail')
        time.sleep(1)
        wrongline = line1
        print("\nThe first line of your address did not pass.\n\nInvalid input: " + wrongline)
        fixornot = input('\nIs this Address line correct(C) or would you like to fix it(F)? (C or F) ')
        while True:
            if fixornot.upper() == "C":
                wrongAddy()
                break
            elif fixornot.upper() == "F":
                fixAddy()
                break
            else:
                print('Incorrect Input! please try again... ')

            break


verifyAPI()

while True:
    clse = input('Would you like to close the program? (Y or N) ')

    if clse.upper() == "Y":
        break
    else:
        continue
