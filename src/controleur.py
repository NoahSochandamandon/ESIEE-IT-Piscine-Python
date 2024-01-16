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
            pygame.K_SPACE: False,
        }

    def traiter_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            elif event.type == pygame.KEYDOWN and (self.modele.get_ecran() > 2):
                if event.key in self.touche_enfoncee:
                    self.touche_enfoncee[event.key] = True
            elif event.type == pygame.KEYUP and (self.modele.get_ecran() > 2):
                if event.key in self.touche_enfoncee:
                    self.touche_enfoncee[event.key] = False
            # event des menus
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.modele.get_ecran() == 2:
                    self.modele.set_selected_lvl(self.modele.get_selected_lvl() - 1)
                if event.key == pygame.K_DOWN and self.modele.get_ecran() == 2:
                    self.modele.set_selected_lvl(self.modele.get_selected_lvl() + 1)
                if event.key == pygame.K_SPACE and self.modele.get_ecran() == 2:
                    self.modele.set_ecran(self.modele.get_selected_lvl() + 2)
                if event.key == pygame.K_SPACE and self.modele.get_ecran() == 1:
                    self.modele.set_ecran(2)

    def jouer(self):
        while self.play:
            self.traiter_evenements()
            # event de jeu
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
            elif self.modele.get_ecran() == 3:
                self.vue.afficher_screen_3(self.modele)
            elif self.modele.get_ecran() == 4:
                self.vue.afficher_screen_3(self.modele)
            self.vue.set_clock(60)
