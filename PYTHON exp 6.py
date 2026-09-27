class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

class Node:
    def __init__(self, employee):
        self.employee = employee
        self.left = None
        self.right = None

class EmployeeTree:
    def __init__(self):
        self.root = None

    # ---- INSERT ---- #
    def insert(self, employee):
        if not self.root:
            self.root = Node(employee)
        else:
            self._insert(self.root, employee)

    def _insert(self, current, employee):
        if employee.emp_id < current.employee.emp_id:
            if current.left:
                self._insert(current.left, employee)
            else:
                current.left = Node(employee)
        else:
            if current.right:
                self._insert(current.right, employee)
            else:
                current.right = Node(employee)

    # ---- SEARCH ---- #
    def search(self, emp_id):
        return self._search(self.root, emp_id)

    def _search(self, current, emp_id):
        if not current:
            return None
        if current.employee.emp_id == emp_id:
            return current.employee
        return self._search(current.left, emp_id) if emp_id < current.employee.emp_id else self._search(current.right, emp_id)

    # ---- DELETE ---- #
    def delete(self, emp_id):
        self.root = self._delete(self.root, emp_id)

    def _delete(self, current, emp_id):
        if not current:
            return current
        if emp_id < current.employee.emp_id:
            current.left = self._delete(current.left, emp_id)
        elif emp_id > current.employee.emp_id:
            current.right = self._delete(current.right, emp_id)
        else:
            if not current.left:  # No left child
                return current.right
            elif not current.right:  # No right child
                return current.left
            else:
                # Node with 2 children: find inorder successor
                temp = self._min_value_node(current.right)
                current.employee = temp.employee
                current.right = self._delete(current.right, temp.employee.emp_id)
        return current

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    # ---- DISPLAY TREE STRUCTURE ---- #
    def visualize(self, node, level=0, prefix="Root: "):
        if node:
            print(" " * (level * 4) + prefix + f"[{node.employee.emp_id}, {node.employee.name}]")
            if node.left:
                self.visualize(node.left, level + 1, "L---")
            if node.right:
                self.visualize(node.right, level + 1, "R---")

    # ---- INORDER DISPLAY ---- #
    def display_inorder(self):
        self._display_inorder(self.root)

    def _display_inorder(self, current):
        if current:
            self._display_inorder(current.left)
            emp = current.employee
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Salary: {emp.salary}")
            self._display_inorder(current.right)


# ---------- MAIN PROGRAM ----------
tree = EmployeeTree()

while True:
    print("\n1. Insert Employee\n2. Search Employee\n3. Delete Employee\n4. Display All Employees (Inorder)")
    print("5. Visualize Tree Structure\n6. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        tree.insert(Employee(emp_id, name, salary))
        print("Employee inserted successfully!")

    elif choice == 2:
        emp_id = int(input("Enter Employee ID to search: "))
        emp = tree.search(emp_id)
        print(f"Employee Found -> ID: {emp.emp_id}, Name: {emp.name}, Salary: {emp.salary}") if emp else print("Employee not found.")

    elif choice == 3:
        emp_id = int(input("Enter Employee ID to delete: "))
        tree.delete(emp_id)
        print("Employee deleted (if existed).")

    elif choice == 4:
        print("\nEmployee records (Inorder Traversal):")
        tree.display_inorder()

    elif choice == 5:
        print("\nBinary Tree Structure:")
        if tree.root:
            tree.visualize(tree.root)
        else:
            print("Tree is empty.")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
