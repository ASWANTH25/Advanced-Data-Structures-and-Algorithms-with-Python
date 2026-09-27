from collections import deque
import heapq

# ------------------ STACK: Transaction Undo/Redo ------------------
class TransactionManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.balance = 0

    def deposit(self):
        amt = int(input("Enter amount to deposit: "))
        self.undo_stack.append(self.balance)
        self.balance += amt
        self.redo_stack.clear()
        print(f"Deposited {amt}. Balance = {self.balance}")

    def withdraw(self):
        amt = int(input("Enter amount to withdraw: "))
        if amt > self.balance:
            print("Insufficient balance!")
            return
        self.undo_stack.append(self.balance)
        self.balance -= amt
        self.redo_stack.clear()
        print(f"Withdrawn {amt}. Balance = {self.balance}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        self.redo_stack.append(self.balance)
        self.balance = self.undo_stack.pop()
        print("Undo successful. Balance =", self.balance)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        self.undo_stack.append(self.balance)
        self.balance = self.redo_stack.pop()
        print("Redo successful. Balance =", self.balance)

    def show(self):
        print("Current Balance:", self.balance)


# ------------------ NORMAL QUEUE: Customer Tokens ------------------
class CustomerQueue:
    def __init__(self):
        self.q = deque()

    def take_token(self):
        name = input("Enter customer name: ")
        self.q.append(name)
        print(f"Token issued to {name}")

    def serve_customer(self):
        if not self.q:
            print("No customers in queue.")
            return
        print("Serving customer:", self.q.popleft())

    def show_queue(self):
        print("Normal Queue:", list(self.q))


# ------------ PRIORITY QUEUE: Senior Citizens / VIP Customers ------------
class PriorityCustomerQueue:
    def __init__(self):
        self.pq = []  # (priority, name)

    def add_priority_customer(self):
        name = input("Enter customer name: ")
        print("Choose priority:")
        print("1. Senior Citizen (Highest)")
        print("2. VIP")
        print("3. Regular Priority")

        p = int(input("Enter priority (1-3): "))
        heapq.heappush(self.pq, (p, name))
        print(f"{name} added with priority {p}")

    def serve_priority_customer(self):
        if not self.pq:
            print("No priority customers.")
            return

        p, name = heapq.heappop(self.pq)
        print(f"Serving Priority Customer: {name} (Priority {p})")

    def show_priority_queue(self):
        if not self.pq:
            print("No priority customers.")
        else:
            print("\nPriority Queue (sorted):")
            for p, name in sorted(self.pq):
                print(f" - {name} (Priority {p})")


# ------------------ MAIN MENU ------------------
def main():
    trans = TransactionManager()
    normal_q = CustomerQueue()
    priority_q = PriorityCustomerQueue()

    while True:
        print("\n========== BANK SERVICE SYSTEM ==========")
        print("1. Bank Account Transactions (Stack - Undo/Redo)")
        print("2. Normal Customer Queue (FIFO)")
        print("3. Priority Customer Queue (Senior/VIP)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # ------- TRANSACTION MENU -------
        if choice == "1":
            while True:
                print("\n--- Transactions ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Undo Last Transaction")
                print("4. Redo Last Transaction")
                print("5. Show Balance")
                print("6. Back")

                c = input("Choose: ")

                if c == "1":
                    trans.deposit()
                elif c == "2":
                    trans.withdraw()
                elif c == "3":
                    trans.undo()
                elif c == "4":
                    trans.redo()
                elif c == "5":
                    trans.show()
                elif c == "6":
                    break
                else:
                    print("Invalid choice!")

        # ------- NORMAL CUSTOMER QUEUE -------
        elif choice == "2":
            while True:
                print("\n--- Normal Customer Queue ---")
                print("1. Take Token")
                print("2. Serve Customer")
                print("3. Show Queue")
                print("4. Back")

                c = input("Choose: ")

                if c == "1":
                    normal_q.take_token()
                elif c == "2":
                    normal_q.serve_customer()
                elif c == "3":
                    normal_q.show_queue()
                elif c == "4":
                    break
                else:
                    print("Invalid choice!")

        # ------- PRIORITY CUSTOMER QUEUE -------
        elif choice == "3":
            while True:
                print("\n--- Priority Customer Queue ---")
                print("1. Add Priority Customer")
                print("2. Serve Priority Customer")
                print("3. Show Priority Queue")
                print("4. Back")

                c = input("Choose: ")

                if c == "1":
                    priority_q.add_priority_customer()
                elif c == "2":
                    priority_q.serve_priority_customer()
                elif c == "3":
                    priority_q.show_priority_queue()
                elif c == "4":
                    break
                else:
                    print("Invalid choice!")

        elif choice == "4":
            print("Exiting Bank Service System…")
            break

        else:
            print("Invalid input! Try again.")


main()
