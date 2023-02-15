class Eindstand:
        def __init__(self):
                self.groups = {}
                self.optie_menu()


        def check_valid_input(self, menu_choice, options):
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
                                menu_choice = self.check_valid_input(menu_choice, ["1", "2", "3", "x"])
                        if menu_choice == "1":
                                self.add_group()
                        elif menu_choice == "2" and self.groups:
                                self.add_exercise_points(0)
                        elif menu_choice == "3" and self.groups:
                                self.add_exercise_points(1)
                self.writeFile()
        
        def check_valid_group_name(self, new_group):
                if new_group not in self.groups:
                        return new_group
                return ""
                

        def add_group(self):
                new_group = ""
                while not new_group:
                        new_group = input("\nGeef de naam van jullie groep:\n").lower()
                        new_group = self.check_valid_group_name(new_group)
                        if not new_group:
                                print("\n\nHet lijkt erop dat deze groepsnaam al bestaat, probeer een andere groepsnaam te bedenken.\n\n")
                self.groups[new_group] = [0, 0]



        def add_exercise_points(self, exercise):
                group_name = ""
                newline = "\n"
                while not group_name:
                        print(f"Dit zijn de verschillende groepen:\n{f'{newline}'.join(self.groups.keys())}")
                        group_name = input("\nGeef de naam van jullie groep:\n").lower()
                        if group_name not in self.groups:
                                group_name = ""
                
                points = 0
                # Punten zelf
                score_answers = int(input("Hoeveel punten heeft het groepje in totaal behaald?"))


                # Placement
                # [20, 15, 10, 5, 0]
                options = [20, 15, 10, 5, 0]
                placement = 0

                # Bonus (hint kaartjes)
                # 5 * n kaartjes


                # total
                points = score_answers + placement + 0


                print("Yo lekker gedaan")

        def writeFile(self):
                infile = open("groeps_punten.tsv", "w")
                infile.write("groepsnaam\topdr1\topdr2\n")
                for group in self.groups.keys():
                        infile.write(f"{group}\t{self.groups[group][0]}\t{self.groups[group][1]}\n")
                infile.close()
                        






if __name__ == "__main__":
        eindstand = Eindstand()
