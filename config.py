import platform


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