# Applications using lists - Menu Driven Program

def student_marks_analyzer():
    marks = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        m = int(input(f"Enter mark for subject {i+1}: "))
        marks.append(m)

    print("\n--- Student Marks Report ---")
    print("Marks:", marks)
    print("Total =", sum(marks))
    print("Average =", sum(marks)/n)
    print("Highest mark =", max(marks))
    print("Lowest mark =", min(marks))


def matrix_addition():
    print("\nMatrix A and B are 2x2 fixed matrices")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    C = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] + B[i][j]

    print("\n--- Matrix Addition Result ---")
    for row in C:
        print(row)


def word_occurrence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Words:", words)

    search = input("Enter a word to search: ")
    print("Occurrences:", words.count(search))


def shopping_cart():
    cart = []
    while True:
        print("\n1. Add Item\n2. Remove Item\n3. View Cart\n4. Exit Cart")
        ch = int(input("Enter choice: "))

        if ch == 1:
            item = input("Enter item to add: ")
            cart.append(item)
        elif ch == 2:
            item = input("Enter item to remove: ")
            if item in cart:
                cart.remove(item)
            else:
                print("Item not found!")
        elif ch == 3:
            print("Cart Items:", cart)
        elif ch == 4:
            break


def even_number_extractor():
    numbers = list(range(1, 21))
    evens = [x for x in numbers if x % 2 == 0]

    print("All Numbers:", numbers)
    print("Even Numbers:", evens)


# ---------------- MAIN MENU -------------------

while True:
    print("\n====== LIST APPLICATIONS MENU ======")
    print("1. Student Marks Analyzer")
    print("2. Matrix Addition using Nested Lists")
    print("3. Word Occurrence Counter")
    print("4. Shopping Cart Application")
    print("5. Even Number Extractor using List Comprehension")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_marks_analyzer()
    elif choice == 2:
        matrix_addition()
    elif choice == 3:
        word_occurrence()
    elif choice == 4:
        shopping_cart()
    elif choice == 5:
        even_number_extractor()
    elif choice == 6:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.")
