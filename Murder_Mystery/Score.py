from bokeh.io import show
from bokeh.plotting import figure


class Eindstand:
    def __init__(self):
        self.groups = {}
        self.optie_menu()

    def check_valid_input(self, menu_choice, options):
        if menu_choice in options:
            return menu_choice
        print("\n\nJe input was niet geldig, "
              "probeer het opnieuw, je hebt alleen keuze uit de opties: "
              "<1>, <2>, <3> en <x>\n\n")
        return menu_choice

    def optie_menu(self):
        menu_choice = ""
        while menu_choice != "x":
            menu_choice = ""
            while not menu_choice:
                menu_choice = input(
                    "Welkom, wat voor dingen zou je willen doen?\n"
                    "1) Een nieuwe groepsnaam invullen\n"
                    "2) Punten invullen voor opdracht 1\n"
                    "3) Punten invullen voor opdracht 2\n"
                    "x) Eindig het script\n").lower()
                menu_choice = self.check_valid_input(menu_choice,
                                                     ["1", "2", "3", "x"])
            if menu_choice == "1":
                self.add_group()
            elif menu_choice == "2" and self.groups:
                self.add_exercise_points(0)
            elif menu_choice == "3" and self.groups:
                self.add_exercise_points(1)
            self.plot()
        # self.writeFile()

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
                print(
                    "\n\nHet lijkt erop dat deze groepsnaam al bestaat, "
                    "probeer een andere groepsnaam te bedenken.\n\n")
        self.groups[new_group] = [0, 0]

    def add_exercise_points(self, exercise):
        group_name = ""
        newline = "\n"
        while not group_name:
            print(
                f"Dit zijn de verschillende groepen:\n"
                f"{f'{newline}'.join(self.groups.keys())}")
            group_name = input("\nGeef de naam van jullie groep:\n").lower()
            if group_name not in self.groups:
                group_name = ""

        points = 0

        # Punten zelf
        score_answers = -1

        while score_answers == -1:
                score_answers = input("Hoeveel punten heeft het groepje in totaal behaald?\n")
                score_answers = self.return_number(score_answers)

        # Placement
        options = [20, 15, 10, 5, 0]

        p = -1
        while p == -1:
                p = input("Wat is de placement van het groepje? [1-5]\n")
                p = self.validate_number(n, [1, 2, 3, 4, 5])
                if p == -1:
                        print("\n\nLijkt er op dat je een verkeerde input hebt gegeven, probeer het opnieuw\n\n")
        placement = options[p - 1]

        # Bonus (hint kaartjes)
        # 5 * n kaartjes
        n = -1
        while n == -1:
                n = input("Hoeveel hint kaartjes zijn er nog over? [0-3]\n")
                n = self.validate_number(n, [0, 1, 2, 3])
                if n == -1:
                        print("\n\nLijkt er op dat je een verkeerde input hebt gegeven, probeer het opnieuw\n\n")

        # total
        points = score_answers + placement + 5 * n

        self.groups[group_name][exercise] = points



    def validate_number(self, n, options):
        if n.isdigit():
                if int(n) in options:
                        return int(n)
        return -1

    def return_number(self, n):
        if n.isdigit():
                if int(n) > 0:
                        return int(n)
        return -1


    def writeFile(self):
        infile = open("groeps_punten.tsv", "w")
        infile.write("groepsnaam\topdr1\topdr2\n")
        for group in self.groups.keys():
            infile.write(
                f"{group}\t{self.groups[group][0]}\t{self.groups[group][1]}\n")
        infile.close()

    def plot(self):
        scores = [sum(self.groups[key]) for key in self.groups.keys()]
        groupnames = list(self.groups.keys())
        source = {'x': groupnames, 'y': scores}
        p = figure(x_range=groupnames, height=350, title="Score!",
                   toolbar_location=None, tools="")
        p.vbar(x=source["x"], top=source["y"], width=0.9)
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        show(p)


if __name__ == "__main__":
    eindstand = Eindstand()
