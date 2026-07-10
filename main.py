from textual.app import App, ComposeResult
from textual.events import Compose
from textual.widgets import Static
import platform
from textual.containers import Horizontal

try:
    info = platform.freedesktop_os_release()
    os_name = info.get("NAME", "Linux")
except AttributeError:
    os_name = platform.system()

class LOGO(Static):
    def render(self):
        return '''
    ██   ██ ██    ██ ██████   ██████ 
    ██  ██  ██    ██ ██   ██ ██    ██
    █████   ██    ██ ██   ██ ██    ██
    ██  ██  ██    ██ ██   ██ ██    ██
    ██   ██  ██████  ██████   ██████


    '''


class Poloska(Static):
    def render(self):
        width = self.app.size.width
        return f"┌{'─' * (width - 2)}┐"

class Poloska2(Static):
    def render(self):
        width = self.app.size.width
        return f"└{'─' * (width - 2)}┘"

class MainMenu(App):
    CSS_PATH = 'styles/main.css'

    def on_mount(self):
        self.title = 'Kudo'

    def compose(self) -> ComposeResult:
        yield Poloska(id='frame')
        with Horizontal(id="top_content"):
            yield LOGO(id='logo')
            with Horizontal(id="os_container"):
                yield Static("OS name: ", id='os_text')
                yield Static(os_name, id='os')





if __name__ == '__main__':
    MainMenu().run()
