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
        yield Digits("0", id="set_r_1")
        yield Digits("0", id="set_r_2")
        yield Digits("0", id="set_r_3")
        yield Digits("Ricardo", id="ricardo")
        yield Digits("0", id="puntos_r")


class PuntosPablo(Static):
    # Los puntos de los jugadores y los sets

    def compose(self) -> ComposeResult:
        yield Digits("0", id="set_p_1")
        yield Digits("0", id="set_p_2")
        yield Digits("0", id="set_p_3")
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

    # Variables Puntos
    puntos = ("0", "15", "30", "40", "AD")
    puntos_R = reactive("0")
    puntos_P = reactive("0")
    cont_R = cont_P = 0
    # Variables Games
    game_R = reactive("0")
    game_P = reactive("0")
    cont_game_R = cont_game_P = 0
    # Variables Sets
    set = 1
    set_r = set_p = 0
    # Indica si hay tiebreak o no
    hay_tiebreak = False

    def game_ricardo(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_R += 1
        self.game_R = str(self.cont_game_R)

    def game_pablo(self):
        # Empieza un nuevo game asi que los puntos se resetean
        self.cont_R = self.cont_P = 0
        self.puntos_R = self.puntos_P = "0"
        self.cont_game_P += 1
        self.game_P = str(self.cont_game_P)

    def punto_ricardo(self):
        # Actualizo el índice de puntos de la tupla para Ricardo
        self.cont_R += 1
        # Si están 40 a 40, hay que ganar dos puntos seguidos para el game
        if self.puntos_P == "AD" and self.puntos_R == "40":
            self.cont_R -= 1
            self.cont_P -= 1
            indice = self.cont_P % 5
            self.puntos_P = str(self.puntos[indice])
        # Si ganó 3 puntos y tiene una diferencia de 2 con el oponente, gana el game
        elif self.cont_R >= 4 and self.cont_R - self.cont_P >= 2:
            # Vamos sumando los games al set que corresponda
            self.game_ricardo()
        # Sino, sumamos normal
        else:
            indice = self.cont_R % 5
            self.puntos_R = str(self.puntos[indice])

    def punto_pablo(self):
        # Actualizo el índice de puntos de la tupla para Pablo
        self.cont_P += 1
        # Si están 40 a 40, hay que ganar dos puntos seguidos para el game
        if self.puntos_R == "AD" and self.puntos_P == "40":
            self.cont_P -= 1
            self.cont_R -= 1
            indice = self.cont_R % 5
            self.puntos_R = str(self.puntos[indice])
        # Si ganó 3 puntos y tiene una diferencia de 2 con el oponente, gana el game
        elif self.cont_P >= 4 and self.cont_P - self.cont_R >= 2:
            self.game_pablo()
        else:
            indice = self.cont_P % 5
            self.puntos_P = str(self.puntos[indice])

    def reset_variables(self):
        self.game_R = "0"
        self.game_P = "0"
        self.cont_game_R = 0
        self.cont_game_P = 0

    def nuevo_set(self):
        # Sumamos un set y reseteamos todas las variables
        self.set += 1
        self.reset_variables()

    def tiebreak(self, boton):
        if not self.hay_tiebreak:
            # Si recién entramos al tiebreak, reseteamos las variables
            self.reset_variables()
        # Indicamos que hay tiebreak
        self.hay_tiebreak = True

        # Para ganar el tiebreak se necesita llegar a 7 o mas con 2 puntos de ventaja
        if boton == "btn_ricardo":
            # Suma punto ricardo
            self.punto_ricardo()
            if int(self.game_R) >= 7 and int(self.game_R) - int(self.game_P) >= 2:
                # Si ganó el tiebreak, empieza un nuevo set y termina el tiebreak
                self.nuevo_set()
                self.set_r += 1
                self.hay_tiebreak = False

        else:
            # Suma punto pablo
            self.punto_pablo()
            if int(self.game_P) >= 7 and int(self.game_P) - int(self.game_R) >= 2:
                # Si ganó el tiebreak, empieza un nuevo set y termina el tiebreak
                self.nuevo_set()
                self.set_p += 1
                self.hay_tiebreak = False

    # Widgets
    def compose(self) -> ComposeResult:
        # Creo los botones
        yield Header()
        yield Center(Tablero(), Anotador())

    # Cambios de los puntos
    @on(Button.Pressed)
    def sumar_puntos(self, event: Button.Pressed):
        id_boton = event.button.id
        if self.set != 3 and ((int(self.game_P) == 6 and int(self.game_R) == 6) or self.hay_tiebreak):
            # Si están empatados 6 a 6, hay tiebreak
            self.tiebreak(id_boton)

        elif self.set > 3 or self.set_r == 2 or self.set_p == 2:
            # Si alguien ganó el tercer set, ya no hacemos nada con los botones
            pass

        elif id_boton == "btn_ricardo":
            # Suma punto ricardo
            self.punto_ricardo()
            if int(self.game_R) >= 6 and int(self.game_R) - int(self.game_P) >= 2:
                # Si ganó el set, empieza uno nuevo
                self.nuevo_set()
                self.set_r += 1

        else:
            # Suma punto pablo
            self.punto_pablo()
            if int(self.game_P) >= 6 and int(self.game_P) - int(self.game_R) >= 2:
                # Si ganó el set, empieza uno nuevo
                self.nuevo_set()
                self.set_p += 1

    def watch_puntos_R(self, nuevo_valor: str) -> None:
        self.query_one("#puntos_r").update(nuevo_valor)

    def watch_puntos_P(self, nuevo_valor: str) -> None:
        self.query_one("#puntos_p").update(nuevo_valor)

    def watch_game_R(self, nuevo_valor: str) -> None:
        if self.set <= 3:
            self.query_one("#set_r_" + str(self.set)).update(nuevo_valor)

    def watch_game_P(self, nuevo_valor: str) -> None:
        if self.set <= 3:
            self.query_one("#set_p_" + str(self.set)).update(nuevo_valor)


if __name__ == "__main__":
    app = TableroTenisApp()
    app.run()
