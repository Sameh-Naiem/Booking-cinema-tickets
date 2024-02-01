import admin
import Client


def main_fn():
    print("Press 1 if you are an admin\nor\nPress 2 if you are a client")
    admin_or_client_choice = int(input())
    if admin_or_client_choice == 1:
        admin.admin_code_fn()

    elif admin_or_client_choice == 2:
        Client.client_register_login()

    else:
        print("Wrong choice.\nPlease try again.")
        main_fn()


print("Welcome to CinemaHub")

main_fn()
