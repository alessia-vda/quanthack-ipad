"""Valeurs chiffrées des exercices QuantHack phase 1, recalculées à chaque build.
Tous les paramètres sont des cas hypothétiques, non des données de marché.
"""
from math import pow

VALUES = {
    'F1': 100 - 88,                # fonds propres banque : actifs - dettes
    'F2': 50_000_000 * 24 / 1e6,  # capitalisation en millions d'euros
    'F3': 1000 / ((1 + .04) ** 2),# zéro-coupon, taux annuel composé
    'F4': 100.08 - 100.02,        # écart achat/vente en euros
    'F5': 113 - 105,              # forward long, payoff à l'échéance
    'F6': 1020 - 950,             # actifs - passifs comptables
    'F7': 120 - 112,              # gap actif/passif simplifié
    'F8': ((1 + .04) / (1 + .025) - 1) * 100,  # rendement réel exact en %
}

if __name__ == '__main__':
    for name, value in VALUES.items():
        print(name, repr(value))
