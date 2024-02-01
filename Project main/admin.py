def admin():
    print("Press 1 to add or remove films in the system")
    print("Press 2 to set or edit price of tickets and available tickets for every film")
    print("Press 3 to  remove or add client on system")
    print("Press 4 to see all transactions that happened on the system")
    print("Press 0 to exit")
    admin_choice = int(input())

    if admin_choice == 1:
        def film_add():
            print("Please enter the film you want to add:")
            the_film_name = str(input())
            with open('films.txt', 'r') as fr:
                contents = fr.read()
            if the_film_name not in contents:
                with open('films.txt', 'a') as f:
                    f.writelines(the_film_name + '\n')
                print("Film added successfully\n")
            else:
                print("This film already exists\n")

        def view_films():
            with open('films.txt', 'r') as fr:
                read = fr.read()
                print("-List of films-")
                print(read)
                print("---------------")

        def film_delete():
            view_films()
            print("Please enter the name of film you want to delete:")
            df = str(input())
            with open('films.txt', 'r') as fr:
                contents = fr.read()
            if df in contents:
                try:
                    with open('films.txt', 'r') as fr:
                        films_names = fr.readlines()
                        with open('films.txt', 'w') as fw:
                            for line in films_names:
                                if line.strip('\n') != df:
                                    fw.write(line)
                    print("Deleted successfully\n")
                except:
                    print("Their is an error check the code")
            elif df not in contents:
                print("Film doesn't exist\n")

        def film_modify():
            print("Press 1 to add a film\nor\nPress 2 to remove a film\nor\nPress 3 to view list of films\nor\nPress "
                  "0 to return")
            choice = int(input())
            if choice == 0:
                admin()
            while choice != 0:

                if choice == 1:
                    film_add()
                    print("Press 1 to add a film\nor\nPress 2 to remove a film\nor\nPress 0 to return")
                    choice = int(input())
                    if choice == 0:
                        film_modify()
                        break
                    elif choice == 3:
                        print("Wrong choice try again")
                        print("Press 1 to add a film\nor\nPress 2 to remove a film\nor\nPress 3 to view list of "
                              "films\nor\nPress0 to exit")
                        choice = int(input())
                        continue
                elif choice == 2:
                    film_delete()
                    print("Press 1 to add a film\nor\nPress 2 to remove a film\nor\nPress 0 to return")
                    choice = int(input())
                    if choice == 0:
                        film_modify()
                    elif choice == 3:
                        print("Wrong choice try again")
                        print("Press 1 to add a film\nor\nPress 2 to remove a film\nor\nPress 3 to view list of "
                              "films\nor\nPress"
                              "0 to return")
                        choice = int(input())
                        continue
                elif choice == 3:
                    view_films()
                    print(
                        "Press 1 to add a film\nor\nPress 2 to remove a film\nor\nPress 3 to view list of films\nor\nPress "
                        "0 to return")
                    choice = int(input())
                    if choice == 0:
                        admin()
                    continue

                elif choice == 0:
                    admin()
                else:
                    print("You entered a wrong number\nPlease try again")
                    print(
                        "Press 1 to add a film\nor\nPress 2 to remove a film\nor\nPress 3 to view list of films\nor\nPress "
                        "0 to return")
                    choice = int(input())
                    continue

        film_modify()
    elif admin_choice == 2:
        def mod_price_ticket():
            global film_name
            choice = int(input("Press 1 to modify prices\nPress 2 to modify available tickets\n"))
            if choice == 1:
                prices_fun()
            elif choice == 2:
                tic_fun()
            else:
                print("Wrong choice\nPlease try again")
                mod_price_ticket()

        def modify_prices_AvTickets():
            global film_name
            film_name = input("Please enter the film name you want to modify or press 0 to return:\n")
            if film_name == "0":
                admin()
            else:
                try:
                    with open('films.txt', 'r') as d:
                        lines = d.read()
                    if film_name in lines:
                        print('Film already exists')
                    elif film_name not in lines:
                        print("invalid film\nplease try again")
                        modify_prices_AvTickets()
                        return
                except FileNotFoundError:
                    print("Error reading from films.txt")
                mod_price_ticket()

        def set_price():
            global film_name
            film_price = input("please enter the film price:")
            with open('prices.txt', 'r') as b:
                lines = b.read()
            if film_name in lines:
                print("you are already set the price for this film before")
            elif film_name not in lines:
                try:
                    with open('prices.txt', 'a') as f:
                        f.writelines(film_name + "  " + film_price + '\n')
                        print("the price added successfully")
                except FileNotFoundError:
                    print("Error writing to prices.txt")

        def edit_price():
            global film_name
            try:
                with open('prices.txt', 'r+') as b:
                    content = b.read()
                    if film_name in content:
                        new_price = input("Enter the new price: ")
                        for i in range(len(content)):
                            if film_name in content[i]:
                                content[i] = film_name + ' ' + str(new_price) + '\n'
                                break
                        b.seek(0)
                        b.writelines(content)
                        print("the price edited successfully")
                    elif film_name not in content:
                        print("film's price haven't been set before\nplease try again")
                        prices_fun()
            except FileNotFoundError:
                print("Error reading or writing to prices.txt")

        def set_tickets():
            global film_name
            tickets = input("Please enter the available tickets: ")
            with open('tickets.txt', 'r') as b:
                lines = b.read()
            if film_name in lines:
                print("you are already set the available tickets for this film before")
            elif film_name not in lines:
                try:
                    with open('tickets.txt', 'a') as f:
                        f.writelines(film_name + '  ' + tickets + '\n')
                        print("the available tickets have been added successfully")
                except FileNotFoundError:
                    print("Error writing to tickets.txt")

        def edit_tickets():
            global film_name
            try:
                with open('tickets.txt', 'r+') as c:
                    content = c.read()
                    print(film_name)
                    if film_name in content:
                        new_tickets = input("Enter the new available tickets: ")
                        for i in range(len(content)):
                            if film_name in content[i]:
                                content[i] = film_name + ' ' + str(new_tickets) + '\n'
                                break
                        c.seek(0)
                        c.writelines(content)
                        print("the available tickets edited successfully")
                    elif film_name not in content:
                        print("Film's ticket haven't been set before\nPlease try again")
                        tic_fun()
            except FileNotFoundError:
                print("Error reading or writing to tickets.txt")

        def prices_fun():
            global film_name
            while True:
                choice_2 = input(
                    "Press 1 to set the price\nPress 2 to edit the price\nPress 3 to return to price and tickets\nPress 0 to return to main menu\n")
                if choice_2 == '1':
                    set_price()
                elif choice_2 == '2':
                    edit_price()
                elif choice_2 == '3':
                    modify_prices_AvTickets()
                    break
                elif choice_2 == '0':
                    admin()
                else:
                    print("Invalid choice.\nPlease enter a valid option.")

        def tic_fun():
            global film_name
            while True:
                choice_3 = input(
                    "Press 1 to set the available tickets\nPress 2 to edit the available tickets\nPress 3 to return to price and tickets\nPress 0 to return to main menu\n")
                if choice_3 == '1':
                    set_tickets()
                elif choice_3 == '2':
                    edit_tickets()
                elif choice_3 == '3':
                    modify_prices_AvTickets()
                    return
                elif choice_3 == '0':
                    admin()
                else:
                    print("Invalid choice.\nPlease enter a valid option.")

        modify_prices_AvTickets()


    elif admin_choice == 3:
        def add_client():
            with open('blocked_clients.txt', 'r') as f:
                f_content = f.read()
                print(f_content)
            email_to_search = str
            while (email_to_search != '0'):
                email_to_search = str(input("Enter the email of the client you want to unblock or 0 to return : "))
                if email_to_search != '0':
                    if email_to_search not in f_content:
                        print("this client isn't blocked.")
                    elif email_to_search in f_content:
                        lines = f_content.split('\n')
                        for line in lines:
                            if email_to_search in line:
                                with open("client_info.txt", "a") as bc:
                                    bc.write(line + "\n")
                                lines = [line for line in lines if email_to_search not in line]
                                f_content = '\n'.join(lines)
                                with open("blocked_clients.txt", "w") as del_cl:
                                    del_cl.write(f_content)
                                print("client unblocked successfully")
                        # with open('blocked_clients.txt','r') as f:
                        #         f.write(email_to_search+'\n')
                        #         print("name added successfully")
                elif email_to_search == '0':
                    client_add_delete()
                    break

        def delete_client():
            with open('client_info.txt', 'r') as o:
                o_content = o.read()
                print(o_content)
            email_to_search = str
            while (email_to_search != '0'):
                email_to_search = str(input("Enter the email of the client you want to delete or 0 to return : "))
                if email_to_search != '0':
                    if email_to_search not in o_content:
                        print("this client does not exist.")
                    elif email_to_search in o_content:
                        lines = o_content.split('\n')
                        for line in lines:
                            if email_to_search in line:
                                with open("blocked_clients.txt", "a") as bc:
                                    bc.write(line + "\n")
                                lines = [line for line in lines if email_to_search not in line]
                                o_content = '\n'.join(lines)
                                with open("client_info.txt", "w") as del_cl:
                                    del_cl.write(o_content)
                                print("client deleted successfully")
                        # with open("client_info.txt", "r") as cr:
                        #     client_info = [line.strip().split() for line in cr.readlines()]
                        # for info in client_info:
                        #     if info[3] == email_to_search:
                        #         client = info[]
                        #         print(client)

                        # with open('client.txt','r') as z:
                        #     lines=z.readlines()
                        # with open('client.txt','w') as z:
                        #     for line in lines:
                        #         if line.strip("\n")!=name:
                        #             z.write(line)
                        #     print("name deleted successfully")
                elif email_to_search == '0':
                    client_add_delete()
                    break

        def client_add_delete():
            x = int(input(
                "Enter 1 if you want to unblock a client\nor\nEnter 2 if you want to block a client\nor\nEnter 0 to return to main menu\n"))
            if x == 1:
                add_client()
            elif x == 2:
                delete_client()
            elif x == 0:
                admin()

        client_add_delete()

    elif admin_choice == 4:
        def main_trans():
            show_trans()
            update_or_return()

        def show_trans():
            with open("Transactions.txt", 'r') as tr:
                trans_info = tr.read()
                print(trans_info)

        def update_or_return():
            print("Press 1 to update list\nor\nPress 0 to return")
            trans_choice = int(input())
            if trans_choice == 1:
                main_trans()
            elif trans_choice == 0:
                admin()
            else:
                print("You entered a wrong choice\nPlease try again")
                update_or_return()

        main_trans()


    elif admin_choice == 0:
        print("thank you for using our program :)")
        exit()


    else:
        print("Wrong choice\nPlease try again")
        admin()


def admin_code_fn():
    print("Please enter your admin code:")
    admin_code_str = str(input())
    with open("admin_code.txt", "r") as a:
        ad_cd = a.readlines()
    if admin_code_str in ad_cd:
        admin()
    else:
        print("This code is invalid in case you forgot your code contact your supervisor.\nPlease try again.")
        admin_code_fn()


if __name__ == "__main__":
    admin_code_fn()
