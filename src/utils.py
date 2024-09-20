
def calcul_renta(dic_appart):
    prix = dic_appart["prix"]
    frais_agence = dic_appart["frais_agence"] 
    apport = dic_appart["apport"]
    taux_emprunt = dic_appart["taux_emprunt"]
    surface = dic_appart["surface"]
    charges_copro = dic_appart["charges_copro"]
    travaux = dic_appart["travaux"]
    meubles = dic_appart["meubles"]
    assurance_emprunt = dic_appart["assurance_emprunt"]
    n_annees = dic_appart["n_annees"]
    internet = dic_appart["internet"]
    assurance_proprio = dic_appart["assurance_proprio"]
    #edf = dic_appart["edf"]
    taxe_fonciere = dic_appart["taxe_fonciere"]

    # Cout d'achat et aménagement, 
    droits_enregistrements = 0.08*prix
    prix_travaux = travaux*1000*surface
    COUT_ACHAT = prix +  prix_travaux + meubles + frais_agence

    # Emprunt
    montant_pret = COUT_ACHAT-apport
    assur_emprunt = assurance_emprunt

    n_mois = n_annees * 12
    mensualité = (montant_pret*taux_emprunt/1200) / (1-(1+(taux_emprunt/1200))**(-n_mois))
    mensualité_avec_assurance = mensualité + assur_emprunt/12
    cout_credit = mensualité_avec_assurance * n_mois - montant_pret
    cout_credit_annuel = cout_credit / n_annees


    #charges annuelles 
    if taxe_fonciere == 0:
        taxe_fonciere = 34*surface 
    charge_copro_annuelle = 12*charges_copro
    edf = 50 * surface
    CHARGES_ANNUELLES = taxe_fonciere + charge_copro_annuelle + internet + assurance_proprio + edf

    # Cashflow annuel
    if surface <= 14 :
        loyer  = 65 * surface
    elif surface <= 19:
        loyer = 55 * surface
    else : # rajouter une composant localisation
        loyer = 45*surface

    revenus = loyer * 12
    decaissement =  mensualité_avec_assurance * 12
    CASHFLOW_ANNUEL = revenus-decaissement

    # Profitabilité Annuelle
    revenus_net = revenus - CHARGES_ANNUELLES
    profitabilite_hors_frais_financiers = revenus_net / COUT_ACHAT * 100
    profitabilite_avec_frais_financiers = (revenus_net - cout_credit_annuel) / COUT_ACHAT * 100

    dic = {
        "Cout d'achat et aménagement" : {
            "droits_enregistrements" : droits_enregistrements,
            "prix_travaux" : prix_travaux,
            "COUT_ACHAT" : COUT_ACHAT,
            "apport" : apport
        },
        "Emprunt" : {
            "montant_pret" : montant_pret,
            "assur_emprunt" : assur_emprunt,
            "n_mois" : n_mois,
            "mensualité" : mensualité,
            "mensualité_avec_assurance" : mensualité_avec_assurance,
            "cout_credit" : cout_credit,
            "cout_credit_annuel" : cout_credit_annuel
        },
        "charges annuelles" : {
            "taxe_fonciere" : taxe_fonciere,
            "charge_copro_annuelle" : charge_copro_annuelle,
            "CHARGES_ANNUELLES" : CHARGES_ANNUELLES
        },
        "Cashflow annuel" : {
            "loyer" : loyer,
            "revenus" : revenus,
            "decaissement" :  decaissement,
            "CASHFLOW_ANNUEL" : CASHFLOW_ANNUEL
        },
        "Profitabilité Annuelle" : {
            "revenus_net" : revenus_net,
            "profitabilite_hors_frais_financiers" : round(profitabilite_hors_frais_financiers, 3),
            "profitabilite_avec_frais_financiers" : round(profitabilite_avec_frais_financiers, 3),
        }
    }

    return dic


def display_simul(dic):
    for key in dic:
        print(key, ":")
        for key_bis in dic[key]:
            if key_bis == "profitabilite_hors_frais_financiers" or key_bis == "profitabilite_avec_frais_financiers" :
                print("\t ", key_bis ," : ", dic[key][key_bis], "%")
            elif key_bis == "n_mois" :
                print("\t ", key_bis ," : ", dic[key][key_bis], "mois")
            else :
                print("\t ", key_bis ," : ", dic[key][key_bis], "€")
        print(" ")
    return 0
    