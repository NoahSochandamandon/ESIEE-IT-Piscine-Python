import pygame


class JeuControleur:
    def __init__(self, modele, vue):
        self.modele = modele
        self.vue = vue
        self.play = True

    def traiter_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.modele.deplacer_joueur(-10, 0)
                elif event.key == pygame.K_RIGHT:
                    self.modele.deplacer_joueur(10, 0)
                elif event.key == pygame.K_UP:
                    self.modele.deplacer_joueur(0, -10)
                elif event.key == pygame.K_DOWN:
                    self.modele.deplacer_joueur(0, 10)

    def jouer(self):
        while self.play:
            self.traiter_evenements()
            self.modele.mise_a_jour()
            self.vue.afficher(self.modele)
            pygame.time.delay(100)
