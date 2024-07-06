from textual.app import App, ComposeResult
from textual.widgets import Header, Button, Static, Digits
from textual.reactive import reactive
from textual import on


class ContadorApp(App):

    puntos = ("0", "15", "30", "40", "AD")
    indice = 0
    numero_a_mostrar = reactive("0")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Sumar uno", id="sumar")
        yield Button("Restar uno", id="restar")
        yield Digits("0", id="id-puntos2")

    @on(Button.Pressed)
    def sumar_uno(self, event: Button.Pressed):
        id_boton = event.button.id
        if id_boton == "sumar":
            if self.indice < 4:
                self.indice += 1
            else:
                self.indice = 0
        elif id_boton == "restar":
            if self.indice > 0:
                self.indice -= 1
            else:
                self.indice = 4

        self.numero_a_mostrar = str(self.puntos[self.indice])

    def watch_numero_a_mostrar(self, nuevo_valor: str) -> None:
        self.query_one("#id-puntos"+"2").update(nuevo_valor)


if __name__ == "__main__":
    app = ContadorApp()
    app.run()
