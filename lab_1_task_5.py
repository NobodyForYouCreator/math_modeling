text = """Шляпка гриба, покрытая ... кожиц...й, держится на ... ножк... . 
Снизу шляпка затянута ... плёнкой. 
Когда её уберёшь, откроется нижняя ... сторона шляпк... ."""

print(text)
for _ in range(1, text.count("...")+1):
    text = text.replace("...", input(), 1)
print(text)