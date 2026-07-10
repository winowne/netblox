import platform
from pathlib import Path

def check_models_folder():
    models_dir = Path("models")

    if not models_dir.exists():
        models_dir.mkdir(parents=True, exist_ok=True)
        return []

    models = [f.name for f in models_dir.iterdir() if not f.name.startswith('.')]

    return models

class Config:
    APP_TITLE = 'Kudo'
    SHOW_OS_LABEL = "OS name: "

    COLOR_BACKGROUND = "#1d1d20"
    COLOR_PRIMARY = "#7331ff"
    COLOR_TEXT_LIGHT = "#f5f5f4"
    

    OS_MARGIN_LEFT = 5

    LOGO_TEXT = '''
    ██   ██ ██    ██ ██████   ██████ 
    ██  ██  ██    ██ ██   ██ ██    ██
    █████   ██    ██ ██   ██ ██    ██
    ██  ██  ██    ██ ██   ██ ██    ██
    ██   ██  ██████  ██████   ██████
    '''

    @classmethod
    def get_os_name(cls) -> str:
        try:
            info = platform.freedesktop_os_release()
            return info.get("NAME", "Linux")
        except AttributeError:
            return platform.system()