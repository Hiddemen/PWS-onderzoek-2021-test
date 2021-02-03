# input van de gebruiker
review = input("Schrijf hier uw review: ")

# input wordt in kleine letters gezet
review = review.lower()

# lijst met positieve en negatieve woorden
positieveWoorden = ["leuk", "goed", "perfect"]
negatieveWoorden = ["stom", "slecht", "matig", "belabberd"]

# tellers om het aan positieve en negatieve woorden te tellen
positieveWoordenCounter = 0
negatieveWoordenCounter = 0

# loop die opniew gaat voor elk woord in de positieveWoorden lijst
for x in positieveWoorden:

    # Als woord x uit de lijst in de review staat wordt er 1 bij de positieveWoordenCounter opgeteld
    if x in review:
        positieveWoordenCounter = positieveWoordenCounter + 1

# loop die opniew gaat voor elk woord in de negatieveWoorden lijst
for x in negatieveWoorden:

    # Als woord x uit de lijst in de review staat wordt er 1 bij de negatieveWoordenCounter opgeteld
    if x in review:
        negatieveWoordenCounter = negatieveWoordenCounter + 1

# print het aantal positieve ene negatieve woorden
print("Aantal positieve woorden: ", positieveWoordenCounter)
print("Aantal negatieve woorden: ", negatieveWoordenCounter)

# als er meer negatieve woorden dan positieve woorden in review zit wordt er geprint dat het negatief is.
# enzovoort voor positief en neutraal
if negatieveWoordenCounter > positieveWoordenCounter:
    print("De review is negeatief")

elif positieveWoordenCounter > negatieveWoordenCounter:
    print("De review is positief")

elif positieveWoordenCounter == negatieveWoordenCounter:
    print("De review is neutraal")