# GUI PART OF THIS TASK
# Yes, I did use the example as I am running low on time and learning tkinter will take a while
from data_module import (
    display_dataset_preview,
    display_visualisation,
    search_data
)

def main_menu():
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. View datasets")
        print("2. View visualisations")
        print("3. Search or filter data")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            display_dataset_preview()
        elif choice == '2':
            display_visualisation()
        elif choice == '3':
            search_data()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()