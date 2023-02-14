class Eindstand:
        def __init__(self):
                self.groups = {}
                self.optie_menu()


        def check_valid_input(self, menu_choice):
                options = ["1", "2", "3", "x"]
                if menu_choice in options:
                        return menu_choice
                print("\n\nJe input was niet geldig, " +\
                "probeer het opnieuw, je hebt alleen keuze uit de opties: " +\
                "<1>, <2>, <3> en <x>\n\n")
                return menu_choice


        def optie_menu(self):
                menu_choice = ""
                while menu_choice != "x":
                        menu_choice = ""
                        while not menu_choice:
                                menu_choice = input("Welkom, wat voor dingen zou je willen doen?\n" +\
                                                "1) Een nieuwe groepsnaam invullen\n" +\
                                                "2) Punten invullen voor opdracht 1\n" +\
                                                "3) Punten invullen voor opdracht 2\n" +\
                                                "x) Eindig het script\n").lower()
                                menu_choice = self.check_valid_input(menu_choice)
                        if menu_choice == "1":
                                print("Komt nu uit bij 1")
                        elif menu_choice == "2":
                                print("Komt nu uit bij 2")
                        elif menu_choice == "3":
                                print("Komt nu uit bij 3")
                self.writeFile()
        
        def add_group(self):
                self.groups

        def writeFile(self):
                infile = open("groeps_punten.tsv", "w")
                infile.write("groepsnaam\topdr1\topdr2\n")
                for group in self.groups.keys():
                        infile.write(f"{group}\t{self.groups[group][0]}\t{self.groups[group][1]}")
                infile.close()
                        






if __name__ == "__main__":
        eindstand = Eindstand()
        
