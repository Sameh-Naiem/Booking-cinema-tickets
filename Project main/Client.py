import os
import re
import datetime
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
i = 5
cart = []
canceled_film = None
first_name = ""  # Define first_name as a global variable
email = ""  # Define email as a global variable
num_tickets = 0
film_counts = {}
def master_card():
    ID = str(input("Enter the visa number which contains 16 digits: "))
    month = str
    year = str
    cvv = str
    if len(ID) == 16:
        print("Enter the expire date like 8/25.")
        month = (input("month:"))
        year = (input("year: "))
        if year > '23' and 1 <= int(month) <= 12:
            cvv = (input("Enter the CVV consisting of 3 digits:"))
            if len(cvv) == 3:
                with open('money.txt', 'a') as x:
                    x.write('\n' + 'ID:' + ID + '\n')
                with open('money.txt', 'a') as y:
                    y.write(month + '/' + year + '\n')
                with open('money.txt', 'a') as z:
                    z.write('cvv:' + cvv + '\n')
            while len(cvv) != 3:
                print("you entered a wrong cvv, try another one.")
                cvv = (input("Enter the CVV consisting of 3 digits:"))
                if len(cvv) == 3:
                    with open('money.txt', 'a') as x:
                        x.write('\n' + 'ID:' + ID + '\n')
                    with open('money.txt', 'a') as y:
                        y.write(month + '/' + year + '\n')
                    with open('money.txt', 'a') as z:
                        z.write('cvv:' + cvv + '\n')
            print("your information was added successfully.")
            print("thank you for your visit.")
            ff = open("cart.txt", "r+")
            ff.seek(0)
            ff.truncate()
            tt = open("booked_tickets.txt", "r+")
            tt.seek(0)
            tt.truncate()
            ll = open("remaining_tickets.txt", "r+")
            ll.seek(0)
            ll.truncate()
            exit()
        else:
            while year <= '23' or int(month) >= 13:
                print("you entered wrong data, try again.")
                print("Enter the expire date like 8/25.")
                month = (input("month:"))
                year = (input("year: "))
                if year > '23' and 1 <= int(month) <= 12:
                    cvv = (input("Enter the CVV consisting of 3 digits:"))
                    if len(cvv) == 3:
                        with open('money.txt', 'a') as x:
                            x.write('\n' + 'ID:' + ID + '\n')
                        with open('money.txt', 'a') as y:
                            y.write(month + '/' + year + '\n')
                        with open('money.txt', 'a') as z:
                            z.write('cvv:' + cvv + '\n')
                    while len(cvv) != 3:
                        print("you entered a wrong cvv, try another one.")
                        cvv = (input("Enter the CVV consisting of 3 digits:"))
                        if len(cvv) == 3:
                            with open('money.txt', 'a') as x:
                                x.write('\n' + 'ID:' + ID + '\n')
                            with open('money.txt', 'a') as y:
                                y.write(month + '/' + year + '\n')
                            with open('money.txt', 'a') as z:
                                z.write('cvv:' + cvv + '\n')
                    print("your information was added successfully.")
                    print("thank you for your visit.")
                    ff = open("cart.txt", "r+")
                    ff.seek(0)
                    ff.truncate()
                    tt = open("booked_tickets.txt", "r+")
                    tt.seek(0)
                    tt.truncate()
                    ll = open("remaining_tickets.txt", "r+")
                    ll.seek(0)
                    ll.truncate()
                    exit()
    else:
        while len(ID) != 16:
            print("you Enter a wrong ID, enter another one")
            master_card()
            break



def on_delivery():
    address = (input("Enter your address: "))
    with open('money.txt', 'a') as o:
        o.write(address + '\n')
    print("Your information was added successfully.")
    print("Your tickets will arrive soon :) .")
    ff = open("cart.txt", "r+")
    ff.seek(0)
    ff.truncate()
    tt = open("booked_tickets.txt", "r+")
    tt.seek(0)
    tt.truncate()
    ll = open("remaining_tickets.txt", "r+")
    ll.seek(0)
    ll.truncate()
    exit()



def pay():
    choice = int(input("Enter 1 if you want to pay by master card or 2 if you want to pay on delivery: "))
    if choice == 1:
        master_card()
    elif choice == 2:
        on_delivery()
    ff = open("cart.txt", "r+")
    ff.truncate()


def conf_or_cancel(total_money, first_name, canceled_film=None):
    global email
    choice = int(input("Press 1 to confirm or press 2 to cancel: "))
    if choice == 1:
        total_money = total_payment(cart, canceled_film=None)
        booking_date = datetime.date.today()

        # with open('cart.txt', 'r') as firstfile, open('booked_tickets.txt', 'w') as secondfile:
        #     # read content from the first file
        #     for line in firstfile:
        #         # write content to the second file
        #         secondfile.write(line)
        with open('cart.txt', 'r') as cart_file, open('booked_tickets.txt', 'a') as booked_file:
            films = cart_file.readlines()
            for film in set(films):
                film = film.strip()
                num_tickets = get_num_tickets_from_remaining(film)
                booked_file.write(f"{film}({num_tickets}),")

        search_text = "\n"
        replace_text = ","

        with open(r'booked_tickets.txt', 'r') as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r'booked_tickets.txt', 'w') as file:
            file.write(data)

        with open('booked_tickets.txt', 'r') as file:
            contents = file.read()

        contents = contents[:-1]
        with open('booked_tickets.txt', 'w') as file:
            file.write(contents)

        with open('booked_tickets.txt', 'r') as book:
            booked_ticket = book.read()

        with open("client_info.txt", "r") as cr:
            client_info = [line.strip().split() for line in cr.readlines()]


        if total_money != 0:

            for info in client_info:
                if info[3] == email:
                    first_name = info[0]
                    with open('Transactions.txt', 'a') as info_w:
                        info_w.write(first_name + "  " + booked_ticket + "  $" + str(total_money) + "  " + str(
                            booking_date) + "\n")

            pay()
        else:
            print("total payment is 0")

        # Prompt the user for the number of tickets for each film in the cart
        # for film_name in cart:
        #     num_tickets = int(input(f"Enter the number of tickets for {film_name}: "))
        #     update_ticket_count(film_name, num_tickets)

    elif choice == 2:
        if os.path.getsize('cart.txt') == 0:
            print("Your cart is empty")
            print("Press 1 to add another film\nor\nPress 0 to end")
            choice_2 = int(input())

            if choice_2 == 1:
                cart_modify(total_money, first_name)
            elif choice_2 == 0:
                print("Exiting the program. Goodbye!")
        else:
            choice_1 = int(input("Press 1 to cancel all cart or press 2 to cancel specific film\n"))
            if choice_1 == 1:
                erase_cart()
            elif choice_1 == 2:
                delete_specific_items()
            else:
                while True:
                    print("You entered a wrong choice\nPlease try again")
                    conf_or_cancel(total_money, first_name, canceled_film)


def get_num_tickets_from_remaining(film_name):
    try:
        with open("remaining_tickets.txt", "r") as remaining_tickets_file:
            remaining_lines = remaining_tickets_file.readlines()

        for remaining_line in remaining_lines:
            remaining_elements = remaining_line.strip().split()
            if len(remaining_elements) == 2:
                remaining_film, remaining_ticket = remaining_elements
                if film_name == remaining_film:
                    return int(remaining_ticket)

        # Return 0 if film_name not found in remaining_tickets.txt
        return 0

    except FileNotFoundError:
        print("Error: File not found.")
        return 0


def cart_modify(total_money,first_name):
    global email, num_of_tickets, cart, film_counts
    with open('prices.txt', 'r') as film:
        print(film.read())

    total_money = cart_limit(first_name)
    conf_or_cancel(total_money, first_name, canceled_film=None)

    # Use a dictionary to store the number of tickets bought for each film
    tickets_bought_dict = {}


    for FilmName in cart:
        num_tickets = int(input(f"Enter the number of tickets for {FilmName}: "))
        update_ticket_count(FilmName, num_tickets)

        # Update the dictionary with the number of tickets bought for the current film
        tickets_bought_dict[FilmName] = tickets_bought_dict.get(FilmName, 0) + num_tickets

    # Display the number of tickets bought for each film
    for film, num_tickets_bought in tickets_bought_dict.items():
        print(f"You have bought {num_tickets_bought} tickets for {film} so far.")


def update_ticket_count(FilmName, num_tickets, refund=False):
    global num_of_tickets
    try:
        with open("tickets.txt", "r") as prices_file:
            lines = prices_file.readlines()

        films_remaining_tickets = {}
        found_film = False

        for i, line in enumerate(lines):
            elements = line.strip().split()
            if len(elements) == 2:
                file_film, file_ticket = elements
                ticketfilm = int(file_ticket)
                if refund:
                    remaining_tickets = ticketfilm + num_tickets
                else:
                    remaining_tickets = max(ticketfilm - num_tickets, 0)  # Ensure remaining_tickets is not negative

                films_remaining_tickets[file_film] = remaining_tickets

                if FilmName == file_film:
                    if refund or remaining_tickets >= 0:
                        # print(f"{FilmName}: {remaining_tickets} tickets remaining")
                        lines[i] = f"{file_film} {remaining_tickets}\n"
                        found_film = True
                    else:
                        print(f"Tickets available for {FilmName} are {ticketfilm} tickets and that is less than your needs .")
                        return False
            else:
                print(f"Warning: Ignoring invalid line in prices.txt: {line}")

        if not found_film:
            print(f"{FilmName} is not available right now .\nPlease try again.")
            cart_limit_function(first_name)

        with open("tickets.txt", "w") as updated_file:
            updated_file.writelines(lines)

        ## Update the remaining tickets information in remaining_tickets.txt
        with open("remaining_tickets.txt", "r") as remaining_tickets_file:
            remaining_lines = remaining_tickets_file.readlines()

        found_remaining_ticket = False
        for j, remaining_line in enumerate(remaining_lines):
            remaining_elements = remaining_line.strip().split()
            if len(remaining_elements) == 2:
                remaining_film, remaining_ticket = remaining_elements
                if FilmName == remaining_film:
                    remaining_tickets = int(remaining_ticket) + num_tickets
                    remaining_lines[j] = f"{FilmName} {remaining_tickets}\n"
                    found_remaining_ticket = True

        if not found_remaining_ticket:
            remaining_lines.append(f"{FilmName} {num_tickets}\n")

        with open("remaining_tickets.txt", "w") as remaining_tickets_file:
            remaining_tickets_file.writelines(remaining_lines)

        return True

    except FileNotFoundError:
        print("File not found: tickets.txt")
        return False

# def cart_modify(total_money, first_name):
#     global email, num_of_tickets, cart, film_counts
#     with open('prices.txt', 'r') as film:
#         print(film.read())
#     total_money = cart_limit(first_name)
#     conf_or_cancel(total_money, first_name, canceled_film=None)
#     tickets_bought_dict = {}
#     for FilmName in cart:
#         num_tickets = int(input(f"Enter the number of tickets for {FilmName}: "))
#         update_ticket_count(FilmName, num_tickets)
#         tickets_bought_dict[FilmName] = tickets_bought_dict.get(FilmName, 0) + num_tickets
#     for film, num_tickets_bought in tickets_bought_dict.items():
#         print(f"You have bought {num_tickets_bought} tickets for {film} so far.")

def cart_limit_function(first_name, max_cart_size=5):
    global search_text, cart, film_counts, i, num_of_tickets
    while i < max_cart_size:
        FilmName = input("Enter film name you want : ")
        num_of_tickets = int(input("Enter number of tickets you want to buy: "))

        # # Check if the film is in the remaining_tickets.txt file
        # with open("remaining_tickets.txt", "r") as remaining_tickets_file:
        #     remaining_lines = remaining_tickets_file.readlines()
        #
        # found_remaining_ticket = False
        # for remaining_line in remaining_lines:
        #     remaining_elements = remaining_line.strip().split()
        #     if len(remaining_elements) == 2:
        #         remaining_film, remaining_ticket = remaining_elements
        #         if FilmName == remaining_film:
        #             found_remaining_ticket = True
        #             print(f"You have bought {remaining_ticket} tickets for {FilmName} so far.")
        #             break
        #
        # if not found_remaining_ticket:
        #     print(f"{FilmName} is added to the cart.")
        # Check if the film is in the prices.txt file
        with open("prices.txt", "r") as prices_file:
            prices = [line.strip().split() for line in prices_file.readlines()]

        film_exists = any(film == FilmName for film, _ in prices)

        if not film_exists:
            print(f"{FilmName} is not in the list of available films.\nPlease choose another film.")
            continue


        if update_ticket_count(FilmName, num_of_tickets):
            # Check if the film is in the remaining_tickets.txt file
            with open("remaining_tickets.txt", "r") as remaining_tickets_file:
                remaining_lines = remaining_tickets_file.readlines()

            found_remaining_ticket = False
            for remaining_line in remaining_lines:
                remaining_elements = remaining_line.strip().split()
                if len(remaining_elements) == 2:
                    remaining_film, remaining_ticket = remaining_elements
                    if FilmName == remaining_film:
                        found_remaining_ticket = True
                        if FilmName in cart:
                            print(f"You have bought {remaining_ticket} tickets for {FilmName} so far.")
                            i -= 1
                            break
                        elif FilmName not in cart:
                            print(f"You have bought {remaining_ticket} tickets for {FilmName} so far.")
                            break

            if not found_remaining_ticket:
                print(f"{FilmName} is added to the cart.")

            with open('cart.txt', 'r') as cart_file:
                line1 = cart_file.read()

            if FilmName not in line1.strip():
                with open('prices.txt', 'r') as prices_file:
                    prices = [line.strip().split() for line in prices_file.readlines()]

                film_exists = any(film == FilmName for film, _ in prices)
                if film_exists:
                    with open('cart.txt', 'a') as cart_file:
                        cart_file.write(FilmName + "\n")
                    #print("The film is added.")############################

                    cart.append(FilmName)
            # else:
            #     print("The film is added.")
                # print(
                #     f"You added this film before. You have bought {(cart.count(FilmName) * num_of_tickets) + tickets_bought_sum } tickets for {FilmName} so far.")
                #
                # update_ticket_count(FilmName, num_tickets, refund=True)###############################################################################################################

        FilmName1 = int(input("To add another film press 1 or Press 0 to (confirm/cancel).\n"))
        if i == max_cart_size - 1:
            # print("Your cart is full.")
            # total_payment_value = calculate_total_payment(cart)
            while True:
                print(
                    "Your cart is full.\nPress 1 to increase tickets for a film from the cart, or Press 0 to (confirm/cancel).")
                choice = int(input())
                if choice == 0:
                    total_money = 0
                    conf_or_cancel(total_money, first_name, canceled_film=None)
                    break
                elif choice == 1:
                    print("Films in your cart:")
                    for film in cart:
                        print(f"- {film}")
                    FilmName = input("Enter a film from the cart to increase its tickets: ")
                    if FilmName in cart:
                        num_of_tickets = int(input(f"Enter additional tickets for {FilmName}: "))
                        update_ticket_count(FilmName, num_of_tickets)

                        with open("remaining_tickets.txt", "r") as remaining_tickets_file:
                            remaining_lines = remaining_tickets_file.readlines()

                        for remaining_line in remaining_lines:
                            remaining_elements = remaining_line.strip().split()
                            if len(remaining_elements) == 2:
                                remaining_film, remaining_ticket = remaining_elements
                                if FilmName == remaining_film:
                                    if FilmName in cart:
                                        print(f"You have bought {remaining_ticket} tickets for {FilmName} so far.")
                                    elif FilmName not in cart:
                                        print(f"You have bought {remaining_ticket} tickets for {FilmName} so far.")
                        # print(f"You have bought {remaining_ticket} tickets for {FilmName} so far.")
                    else:
                        print("Invalid film choice. Please try again.")
                else:
                    print("Invalid choice. Please try again.")
            if choice == 0:
                break
        if FilmName1 == 0:
            total_money = 0
            conf_or_cancel(total_money, first_name, canceled_film=None)
            break
        i += 1
        # else:
        #     print(" Not enough tickets available. Please try again.")


def cart_limit(first_name, max_cart_size=5):
    global search_text, cart, film_counts
    global email, num_of_tickets, i  # Add global declaration for num_of_tickets
    i = 0
    total_payment_value = 0.0
    # tickets_bought_sum = 0
    cart_limit_function(first_name, max_cart_size=5)

    return total_payment_value


def calculate_total_payment(cart, canceled_film=None):
    total_money = 0

    try:
        with open("prices.txt", "r") as prices_file:
            prices = {}
            for line in prices_file:
                elements = line.strip().split()
                if len(elements) == 2:
                    film, price = elements
                    prices[film] = float(price)
                else:
                    print(f"Warning: Ignoring invalid line in prices.txt: {line}")

        if not cart:
            return total_money  # Return 0 if the cart is empty

        # cart_counts = {film: cart.count(film) for film in set(cart)}
        #
        # for film in cart_counts:
        #     if film in prices and film != canceled_film:
        #         total_money += prices[film] * cart_counts[film] * num_of_tickets#####################
        #
        # return total_money

        # Read remaining tickets from remaining_tickets.txt
        remaining_tickets = {}
        with open("remaining_tickets.txt", "r") as remaining_tickets_file:
            for line in remaining_tickets_file:
                elements = line.strip().split()
                if len(elements) == 2:
                    film, num_tickets = elements
                    remaining_tickets[film] = int(num_tickets)

        # Calculate total payment based on prices and remaining tickets
        for film in cart:
            if film in prices and film in remaining_tickets and film != canceled_film:
                total_money += prices[film] * remaining_tickets[film]

        return total_money

    except FileNotFoundError:
        print("Error: File not found.")
        return None


def total_payment(cart, canceled_film):#####################################################
    total_money = calculate_total_payment(cart, canceled_film)
    if not cart or (canceled_film is not None and canceled_film in cart):
        print(f"Total Payment: ${total_money:.2f}")
        return 0.0

    total_payment = calculate_total_payment(cart, canceled_film=None)

    if total_money is not None:
        print(f"Total Payment: ${total_money:.2f}")
        return total_money
    else:
        return None


def conf_erase_cart():
    print("Type 1 to add another film or Type 0 to exit")

    choice = int(input())
    if choice == 1:
        cart_modify(first_name)
    elif choice == 0:
        print("Thank you for your visit :)")
        exit()
    else:
        print("Invalid choice.\nTry again.")
        conf_erase_cart()
        # Add appropriate exit logic if needed


def erase_cart():
    global cart
    global num_of_tickets  # Assuming num_of_tickets is a global variable
    # Retrieve the initial state of tickets from a backup file
    try:
        with open("tickets_backup.txt", "r") as backup_file:
            lines = backup_file.readlines()

        # Write the initial state back to the tickets.txt file
        with open("tickets.txt", "w") as tickets_file:
            tickets_file.writelines(lines)

        # Update the num_of_tickets variable
        num_of_tickets = 0

        # Empty the cart
        cart = []

        # Clear the remaining_tickets.txt file
        with open("remaining_tickets.txt", "w") as remaining_tickets_file:
            remaining_tickets_file.write("")

        print("Cart is now empty")
        conf_erase_cart()

    except FileNotFoundError:
        print("Backup file not found. Please make sure to create a backup file.")


def delete_specific_items():
    global email,canceled_film
    # total_payment(cart)  # Initial calculation before any film is deleted

    while True:
        canceled_film = input("Enter the name of the film to cancel (or type 'done' to finish): ")
        if canceled_film.lower() == 'done':
            print("Press 1 to add another film or 2 to (conf/cancel)")
            del_specific_choice = int(input())
            if del_specific_choice == 1:
                cart_limit_function(first_name)
            elif del_specific_choice == 2:
                total_money = 0
                conf_or_cancel(total_money, canceled_film)
            else:
                print("Wrong choice.\nPlease try again.")
                delete_specific_items()
            break
        # update_ticket_count(canceled_film, num_of_tickets, refund=True)
        try:
            with open("remaining_tickets.txt", "r") as remaining_tickets_file:
                remaining_lines = remaining_tickets_file.readlines()

            for remaining_line in remaining_lines:
                remaining_elements = remaining_line.strip().split()
                if len(remaining_elements) == 2:
                    remaining_film, remaining_ticket = remaining_elements
                    if canceled_film == remaining_film:
                        # Add the tickets back to tickets.txt
                        update_ticket_count(canceled_film, int(remaining_ticket), refund=True)
                        break


            with open('cart.txt', 'r') as fr:
                contents = fr.read()

            if canceled_film in contents:
                try:
                    with open('cart.txt', 'r') as fr:
                        films_names = fr.readlines()
                        with open('cart.txt', 'w') as fw:
                            canceled = False
                            for line in films_names:
                                if line.strip('\n') == canceled_film and not canceled:
                                    print(f"Film '{canceled_film}' has been canceled successfully.")
                                    canceled = True
                                else:
                                    fw.write(line)

                    if canceled:
                        cart.remove(canceled_film)  # Update the cart list
                        total_payment(cart, canceled_film)  # Calculate total payment after film is deleted

                        # Update the remaining_tickets.txt file
                        # with open("remaining_tickets.txt", "r") as remaining_tickets_file:
                        #     remaining_lines = remaining_tickets_file.readlines()

                        new_remaining_lines = [line for line in remaining_lines if
                                               not line.startswith(f"{canceled_film} ")]

                        with open("remaining_tickets.txt", "w") as remaining_tickets_file:
                            remaining_tickets_file.writelines(new_remaining_lines)
                    else:
                        print(f"Film '{canceled_film}' doesn't exist in the cart")

                except Exception as e:
                    print(f"There is an error: {e}")
            else:
                print(f"Film '{canceled_film}' doesn't exist in the cart")

        except FileNotFoundError:
            print("Error: Cart file not found.")

        if not cart:
            print("Your cart is empty.")
            total_money = 0
            conf_or_cancel(total_money, first_name, canceled_film=None)
            break

def client_login():
    global first_name,email
    print("Please enter your E-mail : ")
    email = str(input())
    print("Please enter your password : ")
    password = str(input())

    with open("client_info.txt", "r") as cr:
        client_info = [line.strip().split() for line in cr.readlines()]

    # Check if the entered email and password combination exists in client_info
    if [email, password] in [info[3:5] for info in client_info]:
        print("Welcome")
        total_money = 0
        cart_modify(total_money, first_name)
    else:
        print("E-mail or password is not correct. Please try again.")
        client_login()


def client_register_login():
    global first_name,email
    while True:
        print("Press 1 to login\nor\nPress 2 to register\nor\nPress 0 to exit")
        choice = int(input())

        if choice == 0:
            print("See you later :)")
            break
        elif choice == 1:
            client_login()
            break
        elif choice == 2:
            print("E-mail must contain @ and . like (test@gmail.com).")
            print("Phone number must contain only digits.")
            print("Password must be between 8 and 20 characters.\n")
            print("Please enter your first name : ")
            first_name = str(input())
            print("Please enter your last name : ")
            last_name = str(input())
            while True:
                print("Please enter your phone number : ")
                phone_num = str(input())
                if phone_num.isdigit():
                    break
                else:
                    print("Phone number must contain only digits")
                    print("Please try again")
            while True:
                print("Please enter your E-mail : ")
                email = str(input())
                if (re.fullmatch(regex, email)):
                    break
                else:
                    print("E-mail must contain @ and .\nLike (test@gmail.com)")
                    print("Please try again")
            while True:
                print("Please enter your password : ")
                password = str(input())
                if len(password) > 7 and len(password) < 21:
                    break
                else:
                    print("Password must be between 8 and 20 characters")
                    print("Please try again")
            with open("client_info.txt", "r") as cr:
                client_info = cr.read()
            if email not in client_info:
                with open("client_info.txt", "a") as cw:
                    cw.write(
                        first_name + "  " + last_name + "  " + phone_num + "  " + email + "  " + password + "\n")
                print("Welcome")
                total_money = 0
                cart_modify(total_money, first_name)
                break
            else:
                print("E-mail already registered")
                print("Press any number to try again\nor\nPress 2 to go back")
                back_choice = int(input())
                if back_choice == 0:
                    print("See you later :)")
                    break
                elif back_choice != 2:
                    print("Invalid choice. Exiting.")
                    break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    client_register_login()











