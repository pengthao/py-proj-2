import csv
from project import app
from project.models import Cupcake
from flask import render_template, redirect, request

app.app_context().push()


def cupcakes_list():
    cupcake_list = []
    with open("sample.csv") as csvfile:
        for line in csvfile:
            values = line.strip().split(", ")

            size = values[0] if len(values) > 0 else "regular"
            name = values[1] if len(values) > 1 else "classic"
            price = float(values[2]) if len(values) > 2 else 0.0
            flavor = values[3] if len(values) > 3 else "vanilla"
            frosting = values[4] if len(values) > 4 else "whip"
            sprinkles = eval(values[5]) if len(values) > 5 else []
            filling = values[6] if len(values) > 6 else "none"
            description = values[7] if len(values) > 7 else ""

            try:
                cupcake = Cupcake(
                    size=size,
                    name=name,
                    price=price,
                    flavor=flavor,
                    frosting=frosting,
                    sprinkles=sprinkles,
                    filling=filling,
                    description=description
                )
                cupcake_list.append(cupcake)
            except ValueError:
                print(f"Error processing line: {line}")

    return cupcake_list

def write_cupcakes(cupcakes, filepath="sample.csv"):
    with open(filepath, mode='w', newline='') as csvfile:
        for cupcake in cupcakes:

            size = cupcake.size if cupcake.size else "n/a"
            name = cupcake.name if cupcake.name else "n/a"
            price = cupcake.price if cupcake.price else "n/a"
            flavor = cupcake.flavor if cupcake.flavor else "n/a"
            sprinkles = str(cupcake.sprinkles) if cupcake.sprinkles else "n/a"
            filling = cupcake.filling if cupcake.filling else "n/a"
            description = cupcake.description if cupcake.description else "n/a"

            csv.write(f"{size}, {name}, {price}, {flavor}, {sprinkles}, {filling}, {description}\n")




@app.route('/')
def home():
    return render_template('home.html')




if __name__=='__main__':
    app.run(debug=True)