
element = rzeczy.pop(0)# FIFO
# kolejka
rzeczy = ["doniczka", "kwiatek", "ziemia", "woda"]

rzeczy.append("grabie")
print(element)
element = rzeczy.pop(0)
print(element)
element = rzeczy.pop(0)
print(element)
element = rzeczy.pop(0)
print(element)
print("---------------\n")

# lifo - stos
rzeczy = ["doniczka", "kwiatek", "ziemia", "woda"]
rzeczy.append("łopata")
element = rzeczy.pop()
print(element)
element = rzeczy.pop()
print(element)
element = rzeczy.pop()
print(element)