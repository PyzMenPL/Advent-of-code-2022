class Filesystem:
    def __init__(self) -> None:
        self.root = Folder('/')
        # List of folder names
        self.current_directory = [self.root.name]

    def command(self, command) -> None:
        command = command.split()

        # This is some type of command
        if command[0] == '$' and command[1] == 'cd':
            if command[2] == '..':
                del self.current_directory[-1]
            else:
                self.cd(command[2])

        # Add directory or file if it doesn't exist
        elif command[0] == 'dir' or command[0].isdigit():
            file = None
            if command[0] == 'dir':
                file = Folder(command[1])
            elif command[0].isdigit():
                file = File(command[1], command[0])

            self.root.add(file, self.current_directory[:])

        # If I check for dir and number I don't have to look for the ls command

    def cd(self, dst_name=None) -> None:
        if dst_name == '/':
            self.current_directory = []
        else:
            self.current_directory.append(dst_name)


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.is_created = False

    def __str__(self):
        return "- {} ({}, size={})".format(self.name, "file", self.size)

    def __repr__(self):
        # Instead of printing out <class 'str'>, it prints out as follows
        return "Plik '{}'".format(self.name)


class Folder(File):
    # Folder is a child of the File class (takes its name and size from it)
    def __init__(self, name: str) -> None:
        # The same as self.name = name and self.size = size
        super().__init__(name=name, size=0)
        self.contains = []

    def __iter__(self):
        # If iteration starts, we start from zero
        self.index = 0
        # We end up with the last item on the list
        self.limit = len(self.contains)
        return self

    def __next__(self):
        # If next() is called we increment the index
        self.index += 1

        # If the index is already out of the list, we abort the iteration
        if self.index == self.limit + 1:
            raise StopIteration

        # If the index is in the range of the list, we return the list element
        return self.contains[self.index - 1]

    def __str__(self) -> str:
        # If we need a folder name
        if self.size == 0:
            return "- {} (dir)".format(self.name)
        else:
            return "- {} (dir, size={})".format(self.name, self.size)

    def __repr__(self):
        # Instead of printing out <class 'str'>, it prints out as follows
        return "'Folder '{}'".format(self.name)

    def add(self, file, dst_folder_path) -> None:
        # If it reaches the destination folder, it saves the file.
        # If the condition did not check if the file was created, it would still be saved in the wrong places
        if dst_folder_path == [] and file.is_created is False:
            self.contains.append(file)

            # Once added, it changes its state so that the file is not saved again
            file.is_created = True
            return None

        # For each item in the folder
        for child_folder in self.contains:
            # Checking whether the pursuit of a folder has been completed
            if len(dst_folder_path) == 0:
                return None

            # If the item in the folder list is a folder
            if isinstance(child_folder, type(Folder(''))) and child_folder.name == dst_folder_path[0]:
                del dst_folder_path[0]
                child_folder.add(file, dst_folder_path)

    def sizes(self):
        for child_folder in self.contains:
            # If I am a folder
            if isinstance(self, type(Folder(''))):
                self.size += int(child_folder.size)

            # If I encounter a folder
            if isinstance(child_folder, type(Folder(''))):
                child_folder.sizes()
                # After the size is calculated add it to self.size
                self.size += int(child_folder.size)

    def print(self, depth=0) -> None:
        """View the contents of subfolders"""
        # We display the directory we started with
        if depth == 0:
            print(depth * '\t', self)
            depth += 1

        # If the folder is empty
        if not self.contains:
            print(depth * '\t', "[Empty]")
            return None

        # For each item in the folder
        for child_folder in self.contains:
            # Display name with proper spacing
            print(depth * '\t', child_folder)

            # If the item from the folder list is a folder
            if isinstance(child_folder, type(Folder(''))):
                # Display the contents of the subfolder
                child_folder.print(depth + 1)

    def solve(self, space_to_free: int, solution=None):
        # PyCharm says that this is better than solution=[] so I will trust it
        if solution is None:
            solution = []

        # Jeżeli jestem folderem o rozmiarze większym niż space_to_delete
        if isinstance(self, type(Folder(''))) and self.size >= space_to_free:
            if not solution:
                solution.append(self)
            elif self.size < solution[0].size:
                solution[0] = self

        for child_folder in self.contains:
            # Jeżeli mój potomek jest folderem
            if isinstance(child_folder, type(Folder(''))):
                child_folder.solve(space_to_free, solution)

        return solution[0]


with open('input.txt', 'r') as oFile:
    fastFS = Filesystem()
    for line in oFile:
        fastFS.command(line)

    fastFS.root.sizes()
    fastFS.root.print()
    print(' ')

    space_to_delete = 30000000 - (70000000 - fastFS.root.size)

    print(fastFS.root.solve(space_to_delete))
