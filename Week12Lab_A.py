import console_gfx
def printMenu():
    print("\nRLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")

    option = input("\nSelect a Menu Option: ")

    return option;

def main():
    image_data = None

    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)

    option = 7

    while option != '0':

        option = printMenu()

        if option == '1':
            filename = input("Enter name of file to load: ")
            try:
                image_data = console_gfx.load_file(filename)
                print("File loaded.")
            except:
                print("Failed to load file.")

        elif option == '2':
            image_data = console_gfx.test_image
            print("Test image data loaded.")

        elif option == '6':
            if image_data is not None:
                console_gfx.display_image(image_data)
            else:
                print("No image loaded.")

        elif option == '0':
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
