import sys
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
                # écran de selection des niveaux
                if event.key == pygame.K_UP and self.modele.get_ecran() == 2:
                    self.modele.set_selected_lvl(self.modele.get_selected_lvl() - 1)
                elif event.key == pygame.K_DOWN and self.modele.get_ecran() == 2:
                    self.modele.set_selected_lvl(self.modele.get_selected_lvl() + 1)
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 2
                    and not self.modele.get_selected_lvl()
                    == self.modele.get_LVL_MAX() + 1
                ):
                    self.modele.set_ecran(self.modele.get_selected_lvl() + 4)
                    self.vue.launch_music_duo("spawn.mp3", "main.mp3")
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 2
                    and self.modele.get_selected_lvl() == self.modele.get_LVL_MAX() + 1
                ):
                    self.play = False

                # écran de démarrage
                elif event.key == pygame.K_SPACE and self.modele.get_ecran() == 1:
                    self.modele.set_ecran(2)

                # ecran de mort
                elif event.key == pygame.K_UP and self.modele.get_ecran() == 3:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() - 1
                    )
                elif event.key == pygame.K_DOWN and self.modele.get_ecran() == 3:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() + 1
                    )
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 3
                    and self.modele.get_selected_death_box() == 1
                ):
                    self.modele.set_ecran(self.modele.get_selected_lvl() + 4)
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 3
                    and self.modele.get_selected_death_box() == 2
                ):
                    self.modele.set_ecran(2)
                    self.modele.set_selected_lvl(1)
                    self.modele.set_selected_death_box(1)
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 3
                    and self.modele.get_selected_death_box() == 3
                ):
                    self.play = False

                # ecran de victoire
                elif event.key == pygame.K_UP and self.modele.get_ecran() == 4:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() - 1
                    )
                elif event.key == pygame.K_DOWN and self.modele.get_ecran() == 4:
                    self.modele.set_selected_death_box(
                        self.modele.get_selected_death_box() + 1
                    )
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 4
                    and self.modele.get_selected_death_box() == 1
                ):
                    self.modele.set_ecran(self.modele.get_selected_lvl() + 4)
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 4
                    and self.modele.get_selected_death_box() == 2
                ):
                    self.modele.set_ecran(2)
                    self.modele.set_selected_lvl(1)
                    self.modele.set_selected_death_box(1)
                elif (
                    event.key == pygame.K_SPACE
                    and self.modele.get_ecran() == 4
                    and self.modele.get_selected_death_box() == 3
                ):
                    self.play = False

    def jouer(self):
        while self.play:
            self.traiter_evenements()

            # event de jeu
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
                self.vue.afficher_screen_5(self.modele)
            elif self.modele.get_ecran() == 6:
                self.vue.afficher_screen_6(self.modele)

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()
