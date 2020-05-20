dictionary = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

def alan():

    returnvalue = 0
    for x in dictionary:
        if isinstance(dictionary[x], int):
            returnvalue+= dictionary[x]
    
    return returnvalue

print(alan())