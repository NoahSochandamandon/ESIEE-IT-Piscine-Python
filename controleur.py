import pygame


class JeuControleur:
    def __init__(self, modele, vue):
        self.modele = modele
        self.vue = vue
        self.play = True
        self.touche_enfoncee = {
            pygame.K_LEFT: False,
            pygame.K_RIGHT: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False,
        }

    def traiter_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            elif event.type == pygame.KEYDOWN:
                if event.key in self.touche_enfoncee:
                    self.touche_enfoncee[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in self.touche_enfoncee:
                    self.touche_enfoncee[event.key] = False

    def jouer(self):
        while self.play:
            self.traiter_evenements()
            if self.touche_enfoncee[pygame.K_LEFT]:
                self.modele.deplacer_joueur(-10, 0)
            if self.touche_enfoncee[pygame.K_RIGHT]:
                self.modele.deplacer_joueur(10, 0)
            if self.touche_enfoncee[pygame.K_UP]:
                self.modele.deplacer_joueur(0, -10)
            if self.touche_enfoncee[pygame.K_DOWN]:
                self.modele.deplacer_joueur(0, 10)

            self.modele.mise_a_jour()

            if self.modele.get_ecran() == 1:
                self.vue.afficher_screen_1(self.modele)
            elif self.modele.get_ecran() == 2:
                self.vue.afficher_screen_2(self.modele)
            self.vue.set_clock(60)
