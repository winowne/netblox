from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from config import Config, check_models_folder
from textual.widgets import OptionList, Label
from textual.widgets.option_list import Option
models = check_models_folder()

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

        with Vertical(id="models_container"):
            if not models:
                yield Label("Локальные модели не установлены!", id='error_models')
                
                yield OptionList(
                    Option("Скачать модели", id="opt_download"),
                    Option("Открыть папку с моделями", id="opt_open_folder"),
                    Option("Выйти", id="opt_exit"),
                    id="menu_options"
                )
            else:
                yield Static(f"Обнаружено локальных моделей: {len(models)}")
                for model in models:
                    yield Static(f"      {model}")

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        option_id = event.option_id

        if option_id == "opt_download":
            self.notify("Запуск процесса скачивания моделей...")

        elif option_id == "opt_open_folder":
            import os
            import subprocess
            import sys
            
            models_path = "./models"
            try:
                if sys.platform == "win32":
                    os.startfile(models_path)
                elif sys.platform == "darwin":
                    subprocess.Popen(["open", models_path])
                else:
                    subprocess.Popen(["xdg-open", models_path])
            except Exception as e:
                self.notify(f"Не удалось открыть папку: {e}", severity="error")

        elif option_id == "opt_exit":
            self.exit()


if __name__ == '__main__':
    MainMenu().run()