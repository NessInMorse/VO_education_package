from bokeh.io import show
from bokeh.palettes import Category10
from bokeh.plotting import figure


def check_valid_input(menu_choice, options):
    if menu_choice in options:
        return menu_choice
    else:
        print("\nJe input was niet geldig, "
              "probeer het opnieuw, je hebt alleen keuze uit de opties: "
              "<1>, <2>, <3> en <x>")
        return menu_choice


def validate_number(n, options):
    if n.isdigit():
        if int(n) in options:
            return int(n)
    return -1


def return_number(n):
    if n.isdigit():
        if int(n) > 0:
            return int(n)
    return -1


class Eindstand:
    def __init__(self):
        self.groups = {}
        self.optie_menu()

    def optie_menu(self):
        print("\nLET OP: MAX 10 GROEPEN, ANDERS Category10 (line 2 en 135) "
              "AANPASSEN NAAR Category20 ")
        menu_choice = ""
        while menu_choice != "x":
            menu_choice = ""
            while not menu_choice:
                menu_choice = input(
                    "\nWelkom, wat voor dingen zou je willen doen?\n"
                    "1) Punten invullen voor opdracht 1\n"
                    "2) Punten invullen voor opdracht 2\n"
                    "3) Een nieuwe groepsnaam invullen\n"
                    "x) Eindig het script\n").lower()
                menu_choice = check_valid_input(menu_choice,
                                                ["1", "2", "3", "x"])
            if menu_choice == "1" and self.groups:
                self.add_exercise_points(0)
            elif menu_choice == "2" and self.groups:
                self.add_exercise_points(1)
            elif menu_choice == "3":
                self.add_group()
            self.plot()
        # self.writeFile()

    def check_valid_group_name(self, new_group):
        if new_group not in self.groups:
            return new_group
        return ""

    def add_group(self):
        new_group = ""
        while not new_group:
            new_group = input("\nTyp x als je terug wilt.\n"
                              "Geef de naam van de groep:\n").lower()
            if new_group == "x":
                return None
            new_group = self.check_valid_group_name(new_group)
            if not new_group:
                print("\n\nHet lijkt erop dat deze groepsnaam al bestaat, "
                      "probeer een andere groepsnaam te bedenken.\n\n")
        self.groups[new_group] = [0, 0]

    def add_exercise_points(self, exercise):
        group_name = ""
        newline = "\n"
        while not group_name:
            print(f"Dit zijn de verschillende groepen:\n"
                  f"{f'{newline}'.join(self.groups.keys())}")
            group_name = input("\nTyp x als je terug wilt.\n"
                               "Geef de naam van de groep:\n").lower()
            if group_name == "x":
                return None
            elif group_name not in self.groups:
                group_name = ""

        # Punten zelf
        score_answers = -1
        while score_answers == -1:
            score_answers = input(
                "Hoeveel punten heeft het groepje in totaal behaald?\n")
            score_answers = return_number(score_answers)

        # Placement
        options = [20, 15, 10, 5, 0]

        p = -1
        while p == -1:
            p = input("Wat is de placement van het groepje? [1-5]\n")
            p = validate_number(p, [1, 2, 3, 4, 5])
            if p == -1:
                print(
                    "\n\nLijkt er op dat je een verkeerde input hebt "
                    "gegeven, probeer het opnieuw\n\n")
        placement = options[p - 1]

        # Bonus (hint kaartjes)
        # 5 * n kaartjes
        # n = -1
        # while n == -1:
        #     n = input("Hoeveel hint kaartjes zijn er nog over? [0-3]\n")
        #     n = validate_number(n, [0, 1, 2, 3])
        #     if n == -1:
        #         print(
        #             "\n\nLijkt er op dat je een verkeerde input hebt "
        #             "gegeven, probeer het opnieuw\n\n")

        # total
        points = score_answers + placement  # + 5 * n

        self.groups[group_name][exercise] = points

    def writeFile(self):
        infile = open("groeps_punten.tsv", "w")
        infile.write("groepsnaam\topdr1\topdr2\n")
        for group in self.groups.keys():
            infile.write(
                f"{group}\t{self.groups[group][0]}\t{self.groups[group][1]}\n")
        infile.close()

    def plot(self):
        scores = sorted([sum(self.groups[key]) for key in self.groups.keys()],
                        reverse=True)
        groupnames = sorted(list(self.groups.keys()),
                            key=lambda x: sum(self.groups[x]), reverse=True)
        colors = {key: Category10[10][i] for i, key in
                  enumerate(self.groups.keys())}
        col_sort = [colors[key] for key in groupnames]

        source = {'x': groupnames, 'y': scores, 'col': col_sort}
        tooltips = [("Aantal punten", "@y")]
        p = figure(x_range=groupnames, height=500, title="Score!",
                   toolbar_location=None, tooltips=tooltips)
        p.vbar(x="x", top="y", width=0.9, color="col", source=source)
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        show(p)


if __name__ == "__main__":
    eindstand = Eindstand()
