
import questionary

class Book:
    def __init__(self, id, title, synopsis):
        self.id = id
        self.title = title
        self.synopsis = synopsis

def exit():
    print("👋 Leaving...")

def listBooks(): 
    books = [Book(1, "1984", "synopsis"), Book(2, "Cien años de soledad", "synopsis"), Book(3, "Dune", "synopsis"), Book(4, "Fahrenheit 451", "synopsis")]

    while True:
        if len(books) == 0:
            print("no books")
        else:
            options = [book.title for book in books] + ["-- Exit --"]

            book_selected = questionary.select("Select a book", choices=options).ask()

            if book_selected == "-- Exit --" or book_selected is None:
                exit()
                break

def addNewBook():
    while True:
        print("-- Adding new book --")
        new_title = questionary.text("Enter a book title").ask()

        if new_title is None:
            exit()
            return

        if not new_title:
            print("⚠️ The book title is required")
        
        new_synopsis = questionary.text("Enter a book synopsis").ask()

        if new_synopsis is None:
            exit()
            return

        if not new_synopsis:
            print("⚠️ The book synopsis is required")
        
        print(f"✅ '{new_title}' book added successfully")
        break

def main():
    option_menu = {
        "List the books": listBooks,
        "Add new book": addNewBook,
        "-- Exit --": exit,
    }

    while True:
        option = questionary.select("Personal Library", choices=list(option_menu.keys())).ask()

        if option is None:
            exit()
            break

        if option in option_menu:
            option_selected = option_menu[option]
            if option == '-- Exit --':
                option_selected()
                break
            else:
                option_selected()

            



if __name__ == '__main__':
    main()