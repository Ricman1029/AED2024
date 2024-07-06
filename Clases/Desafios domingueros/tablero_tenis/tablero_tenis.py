from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Header, Button, Static, Digits
from textual import on
from textual.reactive import reactive


class Columnas(Static):
    # Indicador de columnas

    def compose(self) -> ComposeResult:
        yield Digits("Primer Set", id="primer_set")
        yield Digits("Segundo Set", id="segundo_set")
        yield Digits("Tercer Set", id="tercer_set")
        yield Digits("Jugador", id="jugador")
        yield Digits("Puntos", id="puntos")


class PuntosRicardo(Static):
    # Los puntos de los jugadores y los sets

    def compose(self) -> ComposeResult:
        yield Digits("0", id="set_1_r")
        yield Digits("0", id="set_2_r")
        yield Digits("0", id="set_3_r")
        yield Digits("Ricardo", id="ricardo")
        yield Digits("0", id="puntos_r")


class PuntosPablo(Static):
    # Los puntos de los jugadores y los sets

    def compose(self) -> ComposeResult:
        yield Digits("0", id="set_1_p")
        yield Digits("0", id="set_2_p")
        yield Digits("0", id="set_3_p")
        yield Digits("Pablo", id="pablo")
        yield Digits("0", id="puntos_p")


class Tablero(Static):
    # El tablero entero

    def compose(self) -> ComposeResult:
        yield Center(Columnas(), PuntosRicardo(), PuntosPablo())


class Anotador(Static):
    # El widget del anotador

    def compose(self) -> ComposeResult:
        # Creamos los dos botones
        yield Button("Ricardo", id="btn_ricardo")
        yield Button("Pablo", id="btn_pablo")


class TableroTenisApp(App):
    # Un tablero de tenis
    CSS_PATH = "tablero_tenis.tcss"

    # Variables Games
    puntos = ("0", "15", "30", "40", "AD")
    puntos_R = reactive("0")
    puntos_P = reactive("0")
    cont_R = cont_P = 0
    game_1_R = reactive("0")
    game_1_P = reactive("0")
    game_2_R = reactive("0")
    game_2_P = reactive("0")
    game_3_R = reactive("0")
    game_3_P = reactive("0")
    cont_game_R = cont_game_P = 0

    # Funciones auxiliares
    def game_ricardo_1(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_R += 1
        self.game_1_R = str(self.cont_game_R)

    def game_pablo_1(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_P += 1
        self.game_1_P = str(self.cont_game_P)

    def game_ricardo_2(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_R += 1
        self.game_2_R = str(self.cont_game_R)

    def game_pablo_2(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_P += 1
        self.game_2_P = str(self.cont_game_P)

    def game_ricardo_3(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_R += 1
        self.game_3_R = str(self.cont_game_R)

    def game_pablo_3(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_P += 1
        self.game_3_P = str(self.cont_game_P)

    def punto_ricardo(self):
        # Actualizo el índice de puntos de la tupla para Ricardo
        self.cont_R += 1
        # Si ganó 3 puntos y tiene una diferencia de 2 con el oponente, gana el game
        if self.cont_R >= 3 and self.cont_R - self.cont_P >= 2:
            # Vamos sumando los games al set que corresponda
            # Set 3
            if int(self.game_2_R) >= 6 and int(self.game_2_R) - int(self.game_2_P) >= 2:
                self.cont_game_R = self.cont_game_P = 0
                self.game_ricardo_3()
            # Set 2
            if int(self.game_1_R) >= 6 and int(self.game_1_R) - int(self.game_1_P) >= 2:
                self.cont_game_R = self.cont_game_P = 0
                self.game_ricardo_2()
            # Set 1
            else:
                self.game_ricardo_1()
        else:
            indice = self.cont_R % 5
            self.puntos_R = str(self.puntos[indice])

    def punto_pablo(self):
        # Actualizo el índice de puntos de la tupla para Pablo
        self.cont_P += 1
        # Si ganó 3 puntos y tiene una diferencia de 2 con el oponente, gana el game
        if self.cont_P >= 3 and self.cont_P - self.cont_R >= 2:
            # Vamos sumando los games al set que corresponda
            # Set 3
            if int(self.game_2_P) >= 6 and int(self.game_2_P) - int(self.game_2_R) >= 2:
                self.game_pablo_3()
            # Set 2
            elif int(self.game_1_P) >= 6 and int(self.game_1_P) - int(self.game_1_R) >= 2:

                self.game_pablo_2()
            # Set 1
            else:
                self.game_pablo_1()
        else:
            indice = self.cont_P % 5
            self.puntos_P = str(self.puntos[indice])

    # Widgets
    def compose(self) -> ComposeResult:
        # Creo los botones
        yield Header()
        yield Center(Tablero(), Anotador())

    # Cambios de los puntos
    @on(Button.Pressed)
    def sumar_puntos(self, event: Button.Pressed):
        id_boton = event.button.id
        if id_boton == "btn_ricardo":
            self.punto_ricardo()
        else:
            self.punto_pablo()

    def watch_puntos_R(self, nuevo_valor: str) -> None:
        self.query_one("#puntos_r").update(nuevo_valor)

    def watch_puntos_P(self, nuevo_valor: str) -> None:
        self.query_one("#puntos_p").update(nuevo_valor)

    def watch_game_1_R(self, nuevo_valor: str) -> None:
        self.query_one("#set_1_r").update(nuevo_valor)

    def watch_game_1_P(self, nuevo_valor: str) -> None:
        self.query_one("#set_1_p").update(nuevo_valor)

    def watch_game_2_R(self, nuevo_valor: str) -> None:
        self.query_one("#set_2_r").update(nuevo_valor)

    def watch_game_2_P(self, nuevo_valor: str) -> None:
        self.query_one("#set_2_p").update(nuevo_valor)

    def watch_game_3_R(self, nuevo_valor: str) -> None:
        self.query_one("#set_3_r").update(nuevo_valor)

    def watch_game_3_P(self, nuevo_valor: str) -> None:
        self.query_one("#set_3_p").update(nuevo_valor)


if __name__ == "__main__":
    app = TableroTenisApp()
    app.run()
