from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal
from config import Config

class LOGO(Static):
    def render(self):
        return Config.LOGO_TEXT

class Poloska(Static):
    def render(self):
        width = self.app.size.width
        return f"┌{'─' * (width - 2)}┐"


class Poloska2(Static):
    def render(self):
        width = self.app.size.width
        return f"├{'─' * (width - 2)}┤"

class MainMenu(App):
    CSS_PATH = 'styles/main.css'

    def on_mount(self):
        self.title = Config.APP_TITLE

    def compose(self) -> ComposeResult:
        yield Poloska(id='frame')

        with Horizontal(id="top_content"):
            yield LOGO(id='logo')

            with Horizontal(id="os_container") as os_container:
                os_container.styles.margin_left = Config.OS_MARGIN_LEFT

                yield Static(Config.SHOW_OS_LABEL, id='os_text')
                yield Static(Config.get_os_name(), id='os')

        yield Poloska2(id='frame2')


if __name__ == '__main__':
    MainMenu().run()