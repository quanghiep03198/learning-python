from list_methods.sample import create_list_methods_sample
from array_methods.sample import create_array_sample
from string_methods.sample import create_string_methods_sample
from data_types.sample import create_data_types_sample
from operations.sample import create_operators_sample
from set_methods.sample import create_set_sample

if __name__ == "__main__":

    def main():
        while True:
            print("\n========= MENU =========")
            print("1. Data Types")
            print("2. Operations")
            print("3. String Methods")
            print("4. Number Methods")
            print("5. List Methods")
            print("6. Array Methods")
            print("7. Set Methods")
            print("8. Exit")

            choice = input("\nEnter your choice (1-8): ")

            match choice:
                case "1":
                    create_data_types_sample()
                case "2":
                    create_operators_sample()
                case "3":
                    create_string_methods_sample()
                case "4":
                    create_set_sample()
                case "5":
                    create_list_methods_sample()
                case "6":
                    create_array_sample()
                case "8":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")

    main()
