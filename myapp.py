from physics import vypocet_cas_padu_na_zem, vypocet_cas_padu_na_mesici, doba_prechodu_svetelneho_signalu

cas_padu_zem = vypocet_cas_padu_na_zem(100)
print(f"Čas pádu z výšky 100 metrů na Zemi je: {cas_padu_zem:.2f} sekund.")

cas_padu_mesic = vypocet_cas_padu_na_mesici(100)
print(f"Čas pádu z výšky 100 metrů na Měsíci je: {cas_padu_mesic:.2f} sekund.")

doba_prechodu = doba_prechodu_svetelneho_signalu(1_000_000)
print(f"Doba přechodu světelného signálu vzdáleností 1 milion metrů je: {doba_prechodu:.2f} sekund.")
