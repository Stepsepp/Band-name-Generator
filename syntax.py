# Printimisfunktsiooni näide: prindib ekraanile "Hello World".
print("Hello World")

# Kasutades '\n' uue rea loomiseks ühe printimiskäsu sees.
print("Hello world! \nHello world")

# Stringide liitmine tühikuga, et luua terviklik lause.
print("Hello" + " " + "Riho")

# Kasutaja nime küsimine ja tervitus. Siin küsitakse nimi ja prinditakse tervitus ühe käsu sees.
# See võib olla segadusttekitav, kuna kasutaja sisendit ei salvestata.
print("Hello " + input("What is your name? "))

# Optimeerimine: Küsime kasutaja nime üks kord ja salvestame selle muutujasse.
nimi = input("What is your name? ")
print("Hello",
      nimi)  # Muudetud stringide liitmise viisi, et vältida '+' kasutamist.

# Kasutades len() funktsiooni stringi pikkuse leidmiseks ja selle pikkuse printimiseks.
# See on näide selle kohta, kuidas leida ja printida stringi pikkust.
name_length = len(
    input("What is your name? "))  # Küsime nime uuesti, mis pole optimaalne.
print(name_length)

# Optimeerimine: Kuna me juba küsisime kasutaja nime varem, kasutame seda nime pikkuse leidmiseks.
print(len(nimi))
