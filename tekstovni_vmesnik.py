import model

def izpis_igre(igra):
    teskt = """
Število preostalih poskusov: {0}
Neuspeli poskusi: {1}
    """.format(
        model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        igra.stevilo_napak()
    )
    return teskt

def izpis_zmage(igra):
    tekst = """
###### BRAVO! Uganil si geslo '{0}' #######
""".format(
        igra.geslo
)

def izpis_poraza(igra):
    tekst = """
!!!!!! JOOOOJ! Porabil si vse poskuse. Geslo je '{0}' !!!!!!!
""".format(
    igra.geslo
)
    return tekst

###########

igra = model.nova_igra()
print(izpis_igre(igra))
print(izpis_zmage(igra))