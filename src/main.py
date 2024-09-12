import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import random

# Define the Project class to handle the GUI and its functionalities
class Project:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Scripting with Python")

        # Set up the main label for the application
        self.label = tk.Label(root, text="Scripting with Python", foreground="black", border="2", borderwidth='20',
                              font=("Helvetica", 18), background="#5f85db")
        self.label.pack(padx=10, pady=10, fill=tk.BOTH)

        # Label to show the current file being used in the application
        self.FileLabel = tk.Label(root, text="Current File : No File Selected", foreground="white", background="#90b8f8")
        self.FileLabel.pack(padx=10, pady=10, fill=tk.BOTH)

        # Initialize filename, numbers list, and encryption shift key
        self.filename = ""
        self.numbers = []
        self.ENKey = 5

        # Set the size of the main window and its background color
        self.root.geometry("700x600")
        self.root.config(background="#90b8f8")

        # Buttons for various functionalities: File selection, display, sort, search, find largest, append, encrypt, decrypt, and exit
        self.SelectFileButton = tk.Button(root, text="Select / Create File", command=self.SelectFile,
                                          activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.SelectFileButton.pack(padx=10, pady=10, fill=tk.BOTH)

        self.DisplayAllButton = tk.Button(root, text="Display All", command=self.DisplayAll,
                                          activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.DisplayAllButton.pack(padx=10, pady=10, fill=tk.BOTH)

        self.SortButton = tk.Button(root, text="Sort Number", command=self.SortNum,
                                    activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.SortButton.pack(padx=10, pady=10, fill=tk.BOTH)

        self.SearchButton = tk.Button(root, text="Search Number", command=self.SearchNum,
                                      activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.SearchButton.pack(padx=10, pady=10, fill=tk.BOTH)

        self.LargestButton = tk.Button(root, text="Largest Number", command=self.LargestN,
                                       activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.LargestButton.pack(padx=10, pady=10, fill=tk.BOTH)

        self.AppendButton = tk.Button(root, text="Append Random Number", command=self.AppendNumber,
                                      activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.AppendButton.pack(padx=10, pady=10, fill=tk.BOTH)

        self.EncryptButton = tk.Button(root, text="Encrypt File", command=self.EncryptFile,
                                       activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.EncryptButton.pack(padx=10, pady=10, fill=tk.BOTH)

        self.DecryptButton = tk.Button(root, text="Decrypt File", command=self.DecryptFile,
                                       activebackground="grey51", height=1, width=20, font=("Helvetica", 12))
        self.DecryptButton.pack(padx=10, pady=10, fill=tk.BOTH)

        # Exit button to close the application
        Exit_button = tk.Button(root, text='Exit', command=root.destroy, activebackground="Red",
                                height=1, width=20, font=("Helvetica", 12))
        Exit_button.pack(padx=10, pady=10, fill=tk.BOTH)

    # Function to update the file label when a file is selected
    def FileLabelUpdate(self):
        self.FileLabel.config(text=f"Current File: {self.filename}", background="black")

    # Function to select an existing file or create a new one
    def SelectFile(self):
        # Flag to check if a new file needs to be created
        CreateFile = False
        messagebox.showinfo("File Information", "To Create New File\nPlease Click CANCEL BUTTON on next pop-up")

        # Open file dialog to select a file
        self.filename = filedialog.askopenfilename(defaultextension=".txt")

        # If no file is selected, offer to create a new file
        if not self.filename:
            messagebox.showinfo("Create File", "Create New file to proceed with the program")
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
            if not self.filename:
                return
            messagebox.showinfo("File Created", "An Empty file is Created\nPlease Add data into the File")
            CreateFile = True

        # Update the file label to show the selected or created file
        self.FileLabelUpdate()

        try:
            # Read the content of the selected file
            Infile = open(self.filename, "r")
            Content = Infile.read()
            ContentString = Content.split()

            # Convert file content to a list of integers
            for num in ContentString:
                self.numbers.append(int(num))

            Infile.close()

            # Show a success message depending on whether a new file was created or an existing one was selected
            if not CreateFile:
                messagebox.showinfo("SUCCESS", f"The {self.filename}.txt Selected Successfully")
            else:
                messagebox.showinfo("New File Created", f"The {self.filename}.txt created and selected Successfully")
        except TypeError:
            messagebox.showerror("Error", "File not Selected")
        except FileNotFoundError:
            if not CreateFile:
                messagebox.showinfo("Error", "File Not Found")

    # Function to display all numbers in the file, along with their sum and average
    def DisplayAll(self):
        try:
            # Check if a file is selected and contains data
            if not self.filename:
                messagebox.showerror("Error", "File not selected")
                return

            if not self.numbers:
                messagebox.showerror("Error", "No data in the file")
                return

            # Display numbers, their sum, and their average
            NumDis = self.numbers
            NumTotal = sum(self.numbers)
            NumAverage = NumTotal / len(self.numbers)
            messagebox.showinfo("Number Operation", f"The Numbers in file : {NumDis}\n"
                                                    f"The sum of Numbers : {NumTotal}\n"
                                                    f"The Average of Numbers : {NumAverage:.2f}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No data in the file")

    # Function to sort numbers in the file
    def SortNum(self):
        try:
            # Check if a file is selected and contains data
            if not self.filename:
                messagebox.showerror("Error", "File not selected")
                return

            if not self.numbers:
                messagebox.showerror("Error", "No data in the file")
                return

            # Sort the numbers in ascending order
            NumSort = sorted(self.numbers)
            messagebox.showinfo("Sorted Number", f"Numbers in the file in Ascending order:\n{NumSort}")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

    # Function to search for a number in the file
    def SearchNum(self):
        try:
            # Check if a file is selected and contains data
            if not self.filename:
                messagebox.showerror("Error", "File not selected")
                return

            if not self.numbers:
                messagebox.showerror("Error", "No data in the file")
                return

            # Prompt user for the number to search
            SearchN = int(simpledialog.askstring("Search", "Enter the number to search in the file "))
            if SearchN is None:
                messagebox.showwarning("Cancel search", "Search Cancelled")
                return
            elif SearchN < 0:
                messagebox.showerror("Error", "Search Number must be positive")
                return

            # Count occurrences of the searched number in the file
            Infile = open(self.filename, "r")
            Content = Infile.read()
            ContentString = Content.split()
            CountNum = ContentString.count(str(SearchN))

            # Display search results
            if CountNum == 0:
                messagebox.showinfo("Search", f"Number {SearchN} is not found in the file")
            else:
                messagebox.showinfo("Search", f"Number {SearchN} appears {CountNum} times in the file")

            Infile.close()

        except TypeError:
            messagebox.showinfo("Search End", "Search aborted")
        except IOError:
            messagebox.showerror("Error", "File Not Selected OR\nNO Data in File")
        except ValueError:
            messagebox.showerror("Search", "Invalid Input")

    # Function to find the largest number in the file
    def LargestN(self):
        try:
            # Check if a file is selected and contains data
            if not self.filename:
                messagebox.showerror("Error", "File not selected")
                return

            if not self.numbers:
                messagebox.showerror("Error", "No data in the file")
                return

            # Find and display the largest number
            LargestNum = max(self.numbers)
            messagebox.showinfo("Largest Number", f"The Largest Number is : {LargestNum}")
        except FileNotFoundError:
            messagebox.showerror("Error", "File Not Selected OR\nNO Data in File")
        except ValueError:
            messagebox.showerror("Error", "File has No Data")

    # Function to append a random number between 1 and 1000 to the file
    def AppendNumber(self):
        try:
            # Check if a file is selected
            if not self.filename:
                messagebox.showerror("Error", "File not selected")
                return

            # Generate a random number and append it to the file
            new_number = random.randint(1, 1000)
            with open(self.filename, 'a') as file:
                file.write(f"{new_number}\n")
                self.numbers.append(new_number)
            messagebox.showinfo("Success", f"{new_number} appended to the file.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

    # Function to encrypt the file using a Caesar cipher with a shift key of 5
    def EncryptFile(self):
        try:
            # Check if a file is selected
            if not self.filename:
                messagebox.showerror("Error", "File not selected")
                return

            # Read the file and apply encryption
            with open(self.filename, "r") as file:
                content = file.read()

            encrypted_content = "".join([chr((ord(char) + self.ENKey - 32) % 95 + 32) for char in content])

            # Save the encrypted content to the file
            with open(self.filename, "w") as file:
                file.write(encrypted_content)

            messagebox.showinfo("Success", f"{self.filename} is encrypted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

    # Function to decrypt the file using a Caesar cipher with a shift key of 5
    def DecryptFile(self):
        try:
            # Check if a file is selected
            if not self.filename:
                messagebox.showerror("Error", "File not selected")
                return

            # Read the file and apply decryption
            with open(self.filename, "r") as file:
                content = file.read()

            decrypted_content = "".join([chr((ord(char) - self.ENKey - 32) % 95 + 32) for char in content])

            # Save the decrypted content to the file
            with open(self.filename, "w") as file:
                file.write(decrypted_content)

            messagebox.showinfo("Success", f"{self.filename} is decrypted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

# Main function to run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    project = Project(root)
    root.mainloop()
