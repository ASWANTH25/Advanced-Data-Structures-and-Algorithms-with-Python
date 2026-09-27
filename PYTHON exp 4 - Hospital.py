from collections import deque
import heapq

# ---------------- STACK APPLICATION (Undo/Redo Editor) ----------------
class UndoRedoEditor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.text = ""

    def type_text(self):
        new = input("Enter text to add: ")
        self.undo_stack.append(self.text)
        self.text += new
        self.redo_stack.clear()
        print("Current Text:", self.text)

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo!")
            return
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        print("After Undo:", self.text)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo!")
            return
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        print("After Redo:", self.text)

    def show(self):
        print("Current Text:", self.text)


# ---------------- NORMAL QUEUE (Customer Service) ----------------
class CustomerQueue:
    def __init__(self):
        self.q = deque()

    def arrive(self):
        name = input("Enter customer name: ")
        self.q.append(name)
        print(name, "joined the queue.")

    def serve(self):
        if not self.q:
            print("No customers to serve.")
            return
        print("Serving:", self.q.popleft())

    def show(self):
        print("Queue:", list(self.q))


# ---------------- PRIORITY QUEUE (Emergency Patients) ----------------
class PriorityPatientQueue:
    def __init__(self):
        self.pq = []     # (priority, name)

    def add_patient(self):
        name = input("Enter patient name: ")
        print("Choose priority:")
        print("1. Emergency")
        print("2. High")
        print("3. Normal")
        p = int(input("Enter priority (1-3): "))

        heapq.heappush(self.pq, (p, name))
        print(f"{name} added with priority {p}")

    def serve_patient(self):
        if not self.pq:
            print("No patients to serve.")
            return
            
        p, name = heapq.heappop(self.pq)
        print(f"Serving: {name} (Priority {p})")

    def show_queue(self):
        if not self.pq:
            print("Queue is empty.")
        else:
            print("\nPatients (by priority):")
            for p, name in sorted(self.pq):
                print(f" - {name} (Priority {p})")


# ---------------- MAIN MENU ----------------
def main():
    editor = UndoRedoEditor()
    customer_queue = CustomerQueue()
    priority_queue = PriorityPatientQueue()

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Stack App (Undo/Redo Editor)")
        print("2. Queue App (Customer Service)")
        print("3. Priority Queue (Emergency Patients)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # -------- Stack Menu --------
        if choice == "1":
            while True:
                print("\n--- Stack Menu (Undo/Redo) ---")
                print("1. Type Text")
                print("2. Undo")
                print("3. Redo")
                print("4. Show Text")
                print("5. Back")

                c = input("Choose option: ")
                if c == "1":
                    editor.type_text()
                elif c == "2":
                    editor.undo()
                elif c == "3":
                    editor.redo()
                elif c == "4":
                    editor.show()
                elif c == "5":
                    break
                else:
                    print("Invalid input!")

        # -------- Normal Queue Menu --------
        elif choice == "2":
            while True:
                print("\n--- Queue Menu (Customer Service) ---")
                print("1. Add Customer")
                print("2. Serve Customer")
                print("3. Show Queue")
                print("4. Back")

                c = input("Choose option: ")
                if c == "1":
                    customer_queue.arrive()
                elif c == "2":
                    customer_queue.serve()
                elif c == "3":
                    customer_queue.show()
                elif c == "4":
                    break
                else:
                    print("Invalid input!")

        # -------- Priority Queue Menu --------
        elif choice == "3":
            while True:
                print("\n--- Priority Queue (Patients) ---")
                print("1. Add Patient")
                print("2. Serve Patient")
                print("3. Show Queue")
                print("4. Back")

                c = input("Choose option: ")
                if c == "1":
                    priority_queue.add_patient()
                elif c == "2":
                    priority_queue.serve_patient()
                elif c == "3":
                    priority_queue.show_queue()
                elif c == "4":
                    break
                else:
                    print("Invalid input!")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")


main()
