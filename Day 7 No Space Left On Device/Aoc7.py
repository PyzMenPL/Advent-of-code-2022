class Filesystem:
    def __init__(self) -> None:
        self.root = Folder('/')
        # Lista nazw folderów
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
        # Zamiast wypisywać się <class 'str'>, wypisuje się tak jak poniżej
        return "Plik '{}'".format(self.name)


class Folder(File):
    # Folder jest dziedzicem klasy File (bierze od niej imię i rozmiar)
    def __init__(self, name: str) -> None:
        # To samo co self.name = name i self.size = size
        super().__init__(name=name, size=0)
        self.contains = []

    def __iter__(self):
        # Jeżeli rozpocznie się iteracja
        # Zaczynamy od zera
        self.index = 0
        # Kończymy na ostatnim elemencie z listy
        self.limit = len(self.contains)
        return self

    def __next__(self):
        # Jeżeli zostanie wywołane next() zwiększamy index
        self.index += 1

        # Jeżeli index jest już poza listą, przerywamy iterację
        if self.index == self.limit + 1:
            raise StopIteration

        # Jeżeli index znajduje się w zasięgu listy, zwracamy element listy
        return self.contains[self.index - 1]

    def __str__(self) -> str:
        # Jeżeli potrzebujemy nazwy folderu
        if self.size == 0:
            return "- {} (dir)".format(self.name)
        else:
            return "- {} (dir, size={})".format(self.name, self.size)

    def __repr__(self):
        # Zamiast wypisywać się <class 'str'>, wypisuje się tak jak poniżej
        return "'Folder '{}'".format(self.name)

    def add(self, file, dst_folder_path) -> None:
        # Jeżeli dotrze do folderu docelowego, zapisuje plik.
        # Gdyby warunek nie sprawdzał, czy plik ma nazwę, zostałby jeszcze zapisany w nieodpowiednich miejscach
        if dst_folder_path == [] and file.is_created is False:
            self.contains.append(file)

            # Po dodaniu usuwa nazwę, aby plik nie został ponownie zapisany
            file.is_created = True
            return None

        # Dla każdego elementu w folderze
        for child_folder in self.contains:
            # Sprawdzanie, czy dążenie do folderu zostało zakończone
            if len(dst_folder_path) == 0:
                return None

            # Jeżeli element z listy folderu jest folderem
            if isinstance(child_folder, type(Folder(''))) and child_folder.name == dst_folder_path[0]:
                del dst_folder_path[0]
                child_folder.add(file, dst_folder_path)

    def sizes(self):
        for child_folder in self.contains:
            # Jeżeli jestem folderem
            if isinstance(self, type(Folder(''))):
                self.size += int(child_folder.size)

            # Jeżeli napotkam na folder
            if isinstance(child_folder, type(Folder(''))):
                child_folder.sizes()
                # After the size is calculated add it to self.size
                self.size += int(child_folder.size)

    def print(self, depth=0) -> None:
        """Wyświetlenie zawartości podfolderów"""
        # Wyświetlamy katalog, od którego zaczynamy
        if depth == 0:
            print(depth * '\t', self)
            depth += 1

        # Jeżeli folder jest pusty
        if not self.contains:
            print(depth * '\t', "[Empty]")
            return None

        # Dla każdego elementu w folderze
        for child_folder in self.contains:
            # Wyświetl nazwę z zachowaniem odpowiedniego odstępu
            print(depth * '\t', child_folder)

            # Jeżeli element z listy folderu jest folderem
            if isinstance(child_folder, type(Folder(''))):
                # Wyświetl zawartość podfolderu
                child_folder.print(depth + 1)

    def solve(self, suma: int = 0) -> int:
        # Jeżeli jestem folderem o rozmiarze mniejszym niż 100000
        if isinstance(self, type(Folder(''))) and self.size <= 100000:
            suma += self.size

        for child_folder in self.contains:
            # Jeżeli mój potomek jest folderem
            if isinstance(child_folder, type(Folder(''))):
                suma = child_folder.solve(suma)

        return suma


with open('input.txt', 'r') as oFile:
    fastFS = Filesystem()
    for line in oFile:
        fastFS.command(line)

    fastFS.root.sizes()
    print(fastFS.root.solve())
