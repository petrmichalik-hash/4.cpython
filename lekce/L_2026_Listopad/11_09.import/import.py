import math

print(f"Číslo PI: {math.pi}")
print(f"Sinus 90 stupnu: {math.sin(math.pi/2)}")

def bezpecne_deleni(a,b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(f"chyba: {zde}")
        return None
    except Exception as e:
        zprava = f"nelze dělit objekt {a} / {b}: {e}"
    finally:
        print("Dělení bylo provedeno.")
        print("tento blok se provede vždy")
    return vysledek

print(bezpecne_deleni(10,2))
