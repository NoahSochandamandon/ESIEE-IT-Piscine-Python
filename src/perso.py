import pygame


class Personnage:
    def __init__(self):
        self.x = 100  # Position horizontale initiale
        self.y = 300  # Position verticale initiale (au sol, par exemple)
        self.vitesse_x = 0  # Vitesse horizontale
        self.vitesse_y = 0  # Vitesse verticale
        self.en_saut = False
        self.hauteur_saut = 10  # Hauteur maximale du saut
        self.vitesse_saut = self.hauteur_saut  # Vitesse initiale du saut
        self.gravite = 1  # Force de gravité
        self.sprite_actuel = "./sprites/skin/skin_1.png"

    # setter and getter
    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = value

    def get_vitesse_x(self):
        return self.vitesse_x

    def set_vitesse_x(self, value):
        self.vitesse_x = value

    def get_vitesse_y(self):
        return self.vitesse_y

    def set_vitesse_y(self, value):
        self.vitesse_y = value

    def get_en_saut(self):
        return self.en_saut

    def set_en_saut(self, value):
        self.en_saut = value

    def get_hauteur_saut(self):
        return self.hauteur_saut

    def set_hauteur_saut(self, value):
        self.hauteur_saut = value

    def get_vitesse_saut(self):
        return self.vitesse_saut

    def set_vitesse_saut(self, value):
        self.vitesse_saut = value

    def get_gravite(self):
        return self.gravite

    def set_gravite(self, value):
        self.gravite = value

    def get_sprite_actuel(self):
        return self.sprite_actuel

    def set_sprite_actuel(self, value):
        self.sprite_actuel = value

    def mise_a_jour(self):
        # Mise à jour de la position horizontale
        self.x += self.vitesse_x

        # Si le personnage est en train de sauter
        if self.en_saut:
            # Calculer la vitesse de saut et la position y
            if self.vitesse_saut >= -self.hauteur_saut:
                neg = 1
                if self.vitesse_saut < 0:
                    neg = -1
                self.y -= (self.vitesse_saut**2) * 0.5 * neg
                self.vitesse_saut -= self.gravite
            else:
                # Fin du saut
                self.en_saut = False
                self.vitesse_saut = self.hauteur_saut

        # Appliquer la gravité si le personnage n'est pas sur le sol
        self.y += self.vitesse_y
        if self.y > 300:  # Supposons que 300 est la position du sol
            self.y = 300
            self.vitesse_y = 0

        # S'assurer que le personnage ne traverse pas le sol
        if self.y < 300:
            self.vitesse_y += self.gravite
        else:
            self.vitesse_y = 0
            if not self.en_saut:
                # Réinitialiser la vitesse de saut si le personnage est sur le sol
                self.vitesse_saut = self.hauteur_saut
