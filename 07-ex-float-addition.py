print(0.1 + 0.3)


print(f"{0.1:.20f}")


"""
les floating points sont des nombres à virgule flottante, ils ne sont pas toujours précis
represented by a binary fraction

comme 1/3 = 0.33333333333

en decimal 0.1 = 0.1

en binaire = 0.00011001100110011... (repeating)


from decimal import Decimal

# Using Decimal to handle precise decimal arithmetic
a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')

print(a + b == c)  # This will print True

"""
