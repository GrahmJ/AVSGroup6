# these need to be downloaded before you can run the system properly
# i recommend you run this using PyCharm!
import requests
import json
import time

from datetime import datetime

# grabs the user input w/ an option to restart
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

# GET of the address from our online database on restdb.io
url = "https://addresses-a445.restdb.io/rest/avs-addresses"

headers = {
    'content-type': "application/json",
    'x-apikey': "1682b9bc011cea7e87c1ce2d68dbd762e9c9d",
    'cache-control': "no-cache"
}

data = requests.request("GET", url, headers=headers)


# Function for correct address
def correctAddy():
    print("\nThe address you put in is: \n\n" + line1.upper() + '\n' + city.upper() + '\n' + state.upper()
          + '\n' + zipcode + '\n')
    print("This address matches the database and is verified, thank you for using our Address Verification "
          "Service\nGoodbye!")
    print(data)


# Function for fixing the user input + verifying it once fixed
# also prompts the user if they want to add their address to the database
# lets the user have a choice between addresses
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
        if line12.upper() in str(data.text).upper():
            print('Address Line 1: pass')
            time.sleep(.5)
            if line22.upper() in str(data.text).upper():
                print('Apartment #: pass')
                time.sleep(.5)
                if city2.upper() in str(data.text).upper():
                    print('City: pass')
                    time.sleep(.5)
                    if state2.upper() in str(data.text).upper():
                        print('State: pass')
                        time.sleep(.5)
                        if zipcode2 in str(data.text):
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

        print('\nThe FIXED address you put in is: \n\n'
              + line12.upper() + '\n' + city2.upper() + '\n' + state2.upper() + '\n' + zipcode2 + '\n')
        print('\nThe ORIGINAL address you put in is: \n\n'
              + line1.upper() + '\n' + city.upper() + '\n' + state.upper() + '\n' + zipcode + '\n')

        # user chooses between their fixed address or the first one they put in.
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

                    urlpost = "https://addresses-a445.restdb.io/rest/avs-addresses"

                    # takes the input and makes a new json data entry!
                    payload = json.dumps(
                        {"Address 1": line12, "Address 2": line22, "City": city2, "State": state2,
                         "Zip": zipcode2, "_version": 0, "_created": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                         "_createdby": admin, "_changed": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')})
                    headers2 = {
                        'content-type': "application/json",
                        'x-apikey': "1682b9bc011cea7e87c1ce2d68dbd762e9c9d",
                        'cache-control': "no-cache"
                    }

                    # sends data to restdb.io
                    response = requests.request("POST", urlpost, data=payload, headers=headers2)

                    print(response)

                # this ends the program
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

                    urlpost = "https://addresses-a445.restdb.io/rest/avs-addresses"

                    # takes the input and makes a new data entry!
                    payload = json.dumps(
                        {"Address 1": line1, "Address 2": line2, "City": city, "State": state,
                         "Zip": zipcode, "_version": 0, "_created": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                         "_createdby": admin, "_changed": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')})
                    headers2 = {
                        'content-type': "application/json",
                        'x-apikey': "1682b9bc011cea7e87c1ce2d68dbd762e9c9d",
                        'cache-control': "no-cache"
                    }

                    # sends data to restdb.io
                    response = requests.request("POST", urlpost, data=payload, headers=headers2)

                    print(response)

                    break

                # this ends the program
                elif addyor.upper() == "N":
                    print('You have Chosen No. \n\nThank you for using our Address Verification Service! \n\nGoodbye.')

                    break

                # if user puts in a wrong letter
                else:
                    print('Incorrect Input! please try again... ')

                break

        # if user puts in a wrong letter
        else:
            print('Incorrect Input! please try again... ')

        break


# Function for incorrect address with an option to add it to the online database
def wrongAddy():
    while True:
        print('\nAddress is not found in the database.\n\nThe address you put in is: \n\n'
              + line1.upper() + '\n' + city.upper() + '\n' + state.upper() + '\n' + zipcode + '\n')
        addyor = input("Would you like to add this address to the database? (Y or N) ")

        if addyor.upper() == "Y":

            adminuser = input("What is your Admin UserID? (ie email address) ")

            print('\nAddress will now be added to the database!')
            print('\nThank you for using our Address Verification Service! \n\nGoodbye.')

            urlpost = "https://addresses-a445.restdb.io/rest/avs-addresses"

            # takes the input and makes a new data entry!
            payload = json.dumps(
                {"Address 1": line1, "Address 2": line2, "City": city, "State": state,
                 "Zip": zipcode, "_version": 0, "_created": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                 "_createdby": adminuser, "_changed": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')})
            headers2 = {
                'content-type': "application/json",
                'x-apikey': "1682b9bc011cea7e87c1ce2d68dbd762e9c9d",
                'cache-control': "no-cache"
            }

            # sends data to restdb.io
            response = requests.request("POST", urlpost, data=payload, headers=headers2)

            print(response)

            break

        # end the program
        elif addyor.upper() == "N":
            print('You have Chosen No. \n\nThank you for using our Address Verification Service! \n\nGoodbye.')

            break

        # if you put in a wrong letter
        else:
            print('Incorrect Input! please try again... ')

        break


# IF statements that run through every input line by line to check teh database. if any pass, they say so and send the
# user to the correct address function,
# if one fails it will tell you which one fails and and send you to the wrong/fix address function

# this function takes the input and checks if it is in the database file i have pulled from restdb.io
def verifyAPI():
    print('\nVerification in progress...')
    time.sleep(1)
    if line1.upper() in str(data.text).upper():
        print('\nAddress Line 1: pass')
        time.sleep(.5)
        if line2.upper() in str(data.text).upper():
            print('Apartment #: pass')
            time.sleep(.5)
            if city.upper() in str(data.text).upper():
                print('City: pass')
                time.sleep(.5)
                if state.upper() in str(data.text).upper():
                    print('State: pass')
                    time.sleep(.5)
                    if zipcode in str(data.text).upper():
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

# this is just for the .exe file so it doent auto-close the console window.
while True:
    close = input('Would you like to close the program? (Y or N) ')

    if close.upper() == "Y":
        break
    else:
        continue
