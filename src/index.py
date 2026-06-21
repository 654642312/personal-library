
import questionary
def main():
    option = questionary.select("Personal Library", choices=["List books", "Add new book"]).ask()

if __name__ == '__main__':
    main()