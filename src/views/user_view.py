"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.user import User
from controllers.user_controller import UserController

class UserView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """
        controller = UserController()
        while True:
            print("\n1. Montrer la liste d'utilisateurs\n2. Ajouter un utilisateur\n3. Effacer Un utillisateur\n4. Changer Un utilisateur\n5. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                users = controller.list_users()
                UserView.show_users(users)
            elif choice == '2':
                name, email = UserView.get_inputs()
                user = User(None, name, email)
                controller.create_user(user)
            elif choice == '3':
                user_id = int(input("Quel est l'ID de l'utilisateur? "))
                controller.delete_user(user_id)
            elif choice == '4':
                user_name = input("Quel est le nom de l'utilisateur? ")

                user = controller.list_user(user_name)

                print("Changer l'utilisateur")

                name, email = UserView.get_inputs()

                

                user.name = name
                user.email = email

                controller.update_user(user)
            elif choice == '5':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_users(users):
        """ List users """
        print("\n".join(f"{user.id}: {user.name} ({user.email})" for user in users))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a new user """
        name = input("Nom d'utilisateur : ").strip()
        email = input("Adresse courriel : ").strip()
        return name, email