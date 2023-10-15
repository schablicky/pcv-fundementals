'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81
MOON_GRAVITY = 1.625
SPEED_OF_LIGHT = 299792458
SPEED_OF_SOUND = 343 

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def vypocet_cas_padu_na_zem(vyska: float) -> float:
    """
    Vypočte čas volného pádu na Zemi z dané výšky.
    """
    return (2 * vyska / EARTH_GRAVITY) ** 0.5

def vypocet_cas_padu_na_mesici(vyska: float) -> float:
    """
    Vypočte čas volného pádu na Měsíci z dané výšky.
    """
    return (2 * vyska / MOON_GRAVITY) ** 0.5

def doba_prechodu_svetelneho_signalu(vzdalenost: float) -> float:
    """
    Vypočte dobu, kterou potřebuje světelný signál k přechodu danou vzdáleností ve vakuu.
    """
    return vzdalenost / SPEED_OF_LIGHT