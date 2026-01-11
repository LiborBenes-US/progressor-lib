"""
Expanded collection of Unicode characters and patterns for progress bars.
Organized by category for easy discovery and use.
"""

class UnicodeBlocks:
    """Block elements from Unicode with varying fill levels"""
    
    # Full block elements
    FULL = {
        "standard": "█",
        "light": "▓",
        "medium": "▒",
        "light_shade": "░",
        "dark_shade": "█",
        "seven_eighths": "▉",
        "three_quarters": "▊",
        "five_eighths": "▋",
        "half": "▌",
        "three_eighths": "▍",
        "quarter": "▎",
        "one_eighth": "▏",
    }
    
    # Vertical blocks (for vertical progress)
    VERTICAL = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    
    # Horizontal blocks
    HORIZONTAL = ["▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
    
    # Braille patterns (8-dot)
    BRAILLE = {
        "full": "⣿",
        "stages": [" ", "⡀", "⡄", "⡆", "⡇", "⡏", "⡟", "⡿", "⣿"],
        "dots": ["⠀", "⠁", "⠃", "⠇", "⡇", "⡏", "⡟", "⡿", "⣿"]
    }
    
    # Box drawing elements
    BOXES = {
        "solid": "█",
        "double": "═",
        "rounded": "●",
        "square": "■",
        "diamond": "◆",
        "triangle": "▲"
    }


class GeometricSymbols:
    """Geometric shapes and symbols"""
    
    CIRCLES = {
        "filled": ["○", "◔", "◑", "◕", "●"],
        "outlined": ["○", "◑", "●"],
        "concentric": ["◎", "◉", "●"],
        "dot_centered": ["◌", "◍", "◎"]
    }
    
    SQUARES = ["□", "◱", "◲", "■"]
    
    TRIANGLES = {
        "up": ["△", "▲"],
        "down": ["▽", "▼"],
        "right": ["▷", "▶"],
        "left": ["◁", "◀"]
    }
    
    STARS = ["☆", "★", "✪", "✯", "✦", "✧", "✩", "✰"]
    
    ARROWS = {
        "forward": [">", "»", "›", "➔", "➙", "➛", "➜"],
        "backward": ["<", "«", "‹", "➔", "➙", "➛", "➜"][::-1],
        "bouncing": ["(→    )", "( →   )", "(  →  )", "(   → )", "(    →)", 
                    "(   ← )", "(  ←  )", "( ←   )", "(←    )"]
    }


class EmojiThemes:
    """Emoji-based progress indicators (for modern terminals)"""
    
    TECH = {
        "computers": ["🖥️", "💻", "📱", "⌚", "🎮"],
        "loading": ["⏳", "⌛", "⏰", "🕐", "🕑", "🕒", "🕓", "🕔"],
        "network": ["📡", "📶", "🌐", "🛰️", "📶"],
        "battery": ["🔋", "🪫", "🔌", "⚡", "💡"]
    }
    
    NATURE = {
        "weather": ["🌧️", "🌦️", "⛅", "🌤️", "☀️"],
        "growth": ["🌱", "🌿", "🍃", "🌳", "🎄"],
        "water": ["💧", "🌊", "🌨️", "❄️", "☃️"],
        "day_night": ["🌑", "🌒", "🌓", "🌔", "🌕"]
    }
    
    CONSTRUCTION = {
        "build": ["🚧", "👷", "🔨", "🏗️", "🏢"],
        "tools": ["🛠️", "⚒️", "🔧", "🔩", "⛏️"]
    }
    
    FOOD = {
        "cooking": ["🥚", "🍳", "🥓", "🍖", "🍗"],
        "baking": ["🌾", "🍞", "🥖", "🥨", "🥐"],
        "drinks": ["☕", "🍵", "🥤", "🍹", "🍷"]
    }


class ASCIIArt:
    """Classic ASCII art patterns"""
    
    SIMPLE = {
        "equals": ["=", "-"],
        "hash": ["#", "."],
        "asterisk": ["*", " "],
        "plus": ["+", "-"],
        "at": ["@", "."]
    }
    
    RETRO = {
        "pong": ["( ●    )", "(  ●   )", "(   ●  )", "(    ● )", "(     ●)", 
                "(    ● )", "(   ●  )", "(  ●   )", "( ●    )"],
        "pacman": ["C", "c", "ᴐ", "o", "O"],
        "space_invaders": ["👾", "💀", "🤖", "👽", "🛸"]
    }


class FancySymbols:
    """Miscellaneous fancy Unicode symbols"""
    
    MUSICAL = ["♩", "♪", "♫", "♬", "♭", "♯", "🎵", "🎶"]
    
    CHESS = ["♔", "♕", "♖", "♗", "♘", "♙", "♚", "♛"]
    
    CURRENCY = ["$", "€", "£", "¥", "₿", "💎", "💵", "💰"]
    
    ZODIAC = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"]
    
    PLANETS = ["☉", "☿", "♀", "♁", "♂", "♃", "♄", "♅", "♆", "♇"]


class CustomTemplate:
    """Utilities for creating custom progress bar templates"""
    
    @staticmethod
    def from_string(chars: str, stages: int = 8) -> list[str]:
        """
        Create a progress sequence from a string of characters.
        
        Args:
            chars: String where each character is a fill level
            stages: How many discrete stages to create
            
        Returns:
            List of characters for each stage
        """
        if len(chars) < 2:
            raise ValueError("Need at least 2 characters for filled/empty")
        
        if stages <= len(chars):
            return list(chars[:stages])
        
        # Interpolate if we need more stages than characters
        result = []
        for i in range(stages):
            idx = int(i * (len(chars) - 1) / (stages - 1))
            result.append(chars[idx])
        return result  # FIXED: Actually return the result!
    
    @staticmethod
    def gradient(filled_char: str, empty_char: str, steps: int = 10) -> list[str]:
        """
        Create a gradient from empty to filled character.
        
        Args:
            filled_char: Character for 100% filled
            empty_char: Character for 0% filled
            steps: Number of gradient steps
            
        Returns:
            List of gradient characters
        """
        result = [empty_char]
        for i in range(1, steps - 1):
            # Mix characters for gradient effect
            if i < steps // 2:
                result.append(empty_char)
            else:
                result.append(filled_char)
        result.append(filled_char)
        return result
    
    @staticmethod
    def pattern(pattern: str, width: int = 30) -> str:
        """
        Create a repeating pattern progress bar.
        
        Args:
            pattern: Pattern string (e.g., "=-", "◐◑", "⠋⠙")
            width: Width of the progress bar
            
        Returns:
            Pattern repeated to fit width
        """
        repeats = (width // len(pattern)) + 1
        return (pattern * repeats)[:width]
