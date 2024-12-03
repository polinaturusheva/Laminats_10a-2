def aprekinat_laminatu(plaksnes_garums, plaksnes_platums, istabas_garums, istabas_platums):
    kopejas_plaksnes = 0
    atlikusais_platums = istabas_platums
    rindas_numurs = 1

    while atlikusais_platums > 0:
        rindas_plaksnes = 0
        rindas_garums = istabas_garums

        if rindas_numurs % 2 == 1:
            # Nepāra rinda
            while rindas_garums > 0:
                rindas_plaksnes += 1
                rindas_garums -= plaksnes_garums
        else:
            # Pāra rinda
            rindas_plaksnes += 0.5
            rindas_garums -= plaksnes_garums / 2
            while rindas_garums > 0:
                rindas_plaksnes += 1
                rindas_garums -= plaksnes_garums

        kopejas_plaksnes += rindas_plaksnes
        atlikusais_platums -= plaksnes_platums
        rindas_numurs += 1

    return kopejas_plaksnes


print(aprekinat_laminatu(1, .5, 3, 2))

import math

room_length = float(input("Istabas garums (m): "))
room_width = float(input("Istabas platums (m): "))
package_price = float(input("Lamināta pakas cena (EUR): "))
package_area = float(input("Lamināta pakas sedzošā platība (m²): "))
plank_length = float(input("Plāksnes garums (m): "))
plank_width = float(input("Plāksnes platums (m): "))

longest_wall = max(room_length, room_width)
plank_area = plank_length * plank_width
planks_per_package = package_area / plank_area
room_area = room_length * room_width
required_planks = room_area / plank_area
required_packages = math.ceil(required_planks / planks_per_package)

print(f"Istabas garākā siena: {longest_wall:.2f} m")
print(f"Plāksnes vienā pakā: {math.floor(planks_per_package)} gab.")
print(f"Nepieciešamais plākšņu skaits: {math.ceil(required_planks)} gab.")
print(f"Nepieciešamais paku skaits: {required_packages} gab.")
