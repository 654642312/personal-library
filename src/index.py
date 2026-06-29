
import questionary

def listBooks(): 
    books = ["1984", "Cien años de soledad", "Dune", "Fahrenheit 451"]

    while True:
        if not books:
            print("no books")
        else:
            options = books + ["-- Exit --"]

            book_selected = questionary.select("Select a book", choices=options).ask()

            if book_selected == "-- Exit --" or book_selected is None:
                print("👋 Leaving...")
                break

def main():
    option_menu = {
        "list the books": listBooks
    }

    option = questionary.select("Personal Library", choices=list(option_menu.keys())).ask()

    if option in option_menu:
        option_selected = option_menu[option]
        option_selected()



if __name__ == '__main__':
    main()