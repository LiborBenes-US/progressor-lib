"""
ANSI color support for progress bars.
Works on most modern terminals (Linux, macOS, Windows 10+ with ANSI support).
"""

class Colors:
    """ANSI color codes for terminal output"""
    
    # Basic colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    # Bright background colors
    BG_BRIGHT_BLACK = "\033[100m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_YELLOW = "\033[103m"
    BG_BRIGHT_BLUE = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN = "\033[106m"
    BG_BRIGHT_WHITE = "\033[107m"
    
    # Styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    
    # Reset
    RESET = "\033[0m"
    
    # Color gradients (for smooth transitions)
    GRADIENT_RED_YELLOW = ["\033[38;5;196m", "\033[38;5;202m", "\033[38;5;208m", 
                          "\033[38;5;214m", "\033[38;5;220m"]
    GRADIENT_BLUE_CYAN = ["\033[38;5;21m", "\033[38;5;27m", "\033[38;5;33m",
                         "\033[38;5;39m", "\033[38;5;45m", "\033[38;5;51m"]
    GRADIENT_GREEN = ["\033[38;5;22m", "\033[38;5;28m", "\033[38;5;34m",
                     "\033[38;5;40m", "\033[38;5;46m", "\033[38;5;82m"]
    
    @staticmethod
    def rgb(r: int, g: int, b: int) -> str:
        """Create 24-bit RGB color (if terminal supports it)"""
        return f"\033[38;2;{r};{g};{b}m"
    
    @staticmethod
    def bg_rgb(r: int, g: int, b: int) -> str:
        """Create 24-bit background RGB color"""
        return f"\033[48;2;{r};{g};{b}m"


class ColorTheme:
    """Predefined color themes for progress bars"""
    
    @staticmethod
    def default(filled: str, empty: str, progress: float = 0) -> tuple[str, str]:
        """No coloring"""
        return filled, empty
    
    @staticmethod
    def green_red(filled: str, empty: str, progress: float = 0) -> tuple[str, str]:
        """Green progress, red remaining"""
        return f"{Colors.GREEN}{filled}{Colors.RESET}", f"{Colors.RED}{empty}{Colors.RESET}"
    
    @staticmethod
    def blue_yellow(filled: str, empty: str, progress: float = 0) -> tuple[str, str]:
        """Blue progress, yellow remaining"""
        return f"{Colors.BLUE}{filled}{Colors.RESET}", f"{Colors.YELLOW}{empty}{Colors.RESET}"
    
    @staticmethod
    def gradient(filled: str, empty: str, progress: float) -> tuple[str, str]:
        """Gradient from red to green based on position"""
        if progress < 0.33:
            color = Colors.RED
        elif progress < 0.66:
            color = Colors.YELLOW
        else:
            color = Colors.GREEN
        return f"{color}{filled}{Colors.RESET}", f"{Colors.DIM}{empty}{Colors.RESET}"
    
    @staticmethod
    def rainbow(filled: str, empty: str, progress: float) -> tuple[str, str]:
        """Rainbow gradient across the bar"""
        colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, 
                 Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
        idx = int(progress * (len(colors) - 1))
        return f"{colors[idx]}{filled}{Colors.RESET}", empty
    
    @staticmethod
    def monochrome(filled: str, empty: str, progress: float = 0) -> tuple[str, str]:
        """Simple white on black"""
        return f"{Colors.BRIGHT_WHITE}{filled}{Colors.RESET}", empty
    
    @staticmethod
    def terminal(filled: str, empty: str, progress: float = 0) -> tuple[str, str]:
        """Use terminal's default colors (dim empty part)"""
        return filled, f"{Colors.DIM}{empty}{Colors.RESET}"


def apply_color(text: str, color_code: str, reset: bool = True) -> str:
    """Apply color to text"""
    return f"{color_code}{text}{Colors.RESET if reset else ''}"
