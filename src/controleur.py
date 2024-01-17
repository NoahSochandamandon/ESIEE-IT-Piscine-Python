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
        self.clock = pygame.time.Clock()

    def traiter_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            elif event.type == pygame.KEYDOWN and (self.modele.get_ecran() > 4):
                if event.key in self.touche_enfoncee:
                    self.touche_enfoncee[event.key] = True
            elif event.type == pygame.KEYUP and (self.modele.get_ecran() > 4):
                if event.key in self.touche_enfoncee:
                    self.touche_enfoncee[event.key] = False
            # event des menus
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.modele.get_ecran() == 2:
                    self.modele.set_selected_lvl(self.modele.get_selected_lvl() - 1)
                if event.key == pygame.K_DOWN and self.modele.get_ecran() == 2:
                    self.modele.set_selected_lvl(self.modele.get_selected_lvl() + 1)
                if event.key == pygame.K_SPACE and self.modele.get_ecran() == 2:
                    self.modele.set_ecran(self.modele.get_selected_lvl() + 4)
                if event.key == pygame.K_SPACE and self.modele.get_ecran() == 1:
                    self.modele.set_ecran(2)

                # ecran de mort
                if event.key == pygame.K_UP and self.modele.get_ecran() == 3:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() - 1
                    )
                if event.key == pygame.K_DOWN and self.modele.get_ecran() == 3:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() + 1
                    )
                if (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 3
                    and self.modele.get_selected_death_box() == 1
                ):
                    self.modele.set_ecran(self.modele.get_selected_lvl() + 4)
                if (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 3
                    and self.modele.get_selected_death_box() == 2
                ):
                    self.modele.set_ecran(2)

                # ecran de victoire
                if event.key == pygame.K_UP and self.modele.get_ecran() == 4:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() - 1
                    )
                if event.key == pygame.K_DOWN and self.modele.get_ecran() == 4:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() + 1
                    )
                if (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 4
                    and self.modele.get_selected_death_box() == 1
                ):
                    self.modele.set_ecran(self.modele.get_selected_lvl() + 4)
                if (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 4
                    and self.modele.get_selected_death_box() == 2
                ):
                    self.modele.set_ecran(2)

    def jouer(self):
        while self.play:
            self.traiter_evenements()

            # event de jeu
            # if self.touche_enfoncee[pygame.K_LEFT]:
            #     self.modele.perso.set_vitesse_x(-15)
            # if self.touche_enfoncee[pygame.K_RIGHT]:
            #     self.modele.perso.set_vitesse_x(15)
            # else:
            #     self.modele.perso.set_vitesse_x(0)

            # if not self.modele.perso.get_en_saut():
            #     if self.touche_enfoncee[pygame.K_UP]:
            #         self.modele.perso.set_en_saut(True)
            #         self.modele.perso.set_vitesse_saut(
            #             self.modele.perso.get_hauteur_saut()
            #         )

            # if self.modele.get_ecran() >= 3 and self.touche_enfoncee[pygame.K_RIGHT]:
            #     return
            # if self.modele.get_ecran() >= 3 and self.touche_enfoncee[pygame.K_LEFT]:
            #     return
            # else:
            #     return
            # if self.modele.get_ecran() >= 3 and self.touche_enfoncee[pygame.K_SPACE]:
            #     return

            self.modele.mise_a_jour()

            if self.modele.get_ecran() == 1:
                self.vue.afficher_screen_1(self.modele)
            elif self.modele.get_ecran() == 2:
                self.vue.afficher_screen_2(self.modele)
            elif self.modele.get_ecran() == 3:
                self.vue.afficher_screen_death(self.modele)
            elif self.modele.get_ecran() == 4:
                self.vue.afficher_screen_victory(self.modele)
            elif self.modele.get_ecran() == 5:
                self.vue.afficher_screen_3(self.modele)
            elif self.modele.get_ecran() == 6:
                self.vue.afficher_screen_4(self.modele)
            # print(self.modele.get_ecran())

            pygame.display.update()
            self.clock.tick(60)
