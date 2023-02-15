#Kardo-Tamm_IS22
 #Avage fail lugemiseks
#with open("sammud.txt", "r") as f:
    # Read the lines of the file into a list of integers
#    steps_data = [int(line.strip()) for line in f.readlines()]

 #Arvutab sammude koguarvu
#total_steps = sum(steps_data)
#print("Total number of steps for the week:", total_steps)

 #Arvutab keskmise sammude arvu päevas
#average_steps = total_steps / len(steps_data)
#print("Average number of steps per day:", average_steps)

 #Leidke kõige suurema ja väikseima sammuga päev
#max_steps = max(steps_data)
#min_steps = min(steps_data)
#max_day = steps_data.index(max_steps) + 1
#min_day = steps_data.index(min_steps) + 1

 #Kirjutab tulemused
#print("Day with the most steps:", max_day, "with", max_steps, "steps")
#print("Day with the least steps:", min_day, "with", min_steps, "steps")


#import turtle

# Avame faili
#with open("kilpkonn.txt", "r") as f:
    # Loeme failist kaks rida
#    line1 = f.readline().strip()
#    line2 = f.readline().strip()

    # Tõlgime andmed kilpkonnale arusaadavaks
#    length = int(line1)
#    angle = int(line2)

    # Loome kilpkonna
#    t = turtle.Turtle()

    # Liigutame kilpkonna vastavalt andmetele
#    t.forward()
#    t.left(angle)

    # Ootame, kuni kasutaja sulgeb akna
  #  turtle.done()


# Avame faili
#with open("kilpkonn.txt", "r") as f:
    # Loeme failist ühe rea
#    line = f.readline().strip()

    # Tõlgime andmed kilpkonnale arusaadavaks
#    side_length = int(line)

    # Loome kilpkonna
#    t = turtle.Turtle()

    # Joonistame ruudu
#    for i in range(4):
#        t.forward(side_length)
 #       t.left(90)

    # Ootame, kuni kasutaja sulgeb akna
#    turtle.done()

    # Küsime kasutajalt arvu kujundeid
#    num_shapes = int(input("Sisesta arv kujundeid: "))

    # Avame faili
 #   with open("kilpkonn.txt", "r") as f:
        # Loeme failist ühe rea
#        line = f.readline().strip()

        # Tõlgime andmed kilpkonnale arusaadavaks
#        side_length = int(line)

        # Loome kilpkonna
 #       t = turtle.Turtle()

        # Joonistame ruudud
#        for i in range(num_shapes):
#            for j in range(4):
#                t.left(90)
#            t.penup()
#            t.forward(2 * side_length)
#            t.pendown()

        # Ootame, kuni kasutaja sulgeb akna
#        turtle.done()

