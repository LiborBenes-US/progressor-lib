Title: Progressor

Python Library Version: 1.0.0

Dependencies: Minimal, no external libraries needed. .py & .toml files.

Author: Dr. Libor Benes, M.A., Creator of Progressor.

This Python Library was developed on Sunday, January 11, 2026.

This README.md is created by Dr. Libor Benes, M.A., on Sunday, January 11, 2026.

This Python Library was developed by Dr. Libor Benes, M.A., using Grok 3 AI and DeepSeek AI for code generation and for this README.md file.

Support E-mail: Benes@iwp.edu

Purpose:
Progressor is a Python library for enhanced progress bars with themes, colors, and custom templates.


![Progressor Demo](https://img.shields.io/badge/demo-see%20below-blue)

Features:
• 15+ Built-in Styles: Block, classic, braille, arrows, circles, squares, triangles, and more.
• Full Color Support: ANSI color themes including gradients and rainbow effects.
• Custom Templates: Create progress bars with any Unicode characters or emojis.
• Unicode Collections: Extensive character sets from blocks, geometric symbols, and emojis.
• Multi-bar Display: Track multiple concurrent processes simultaneously.
• Real-time Metrics: Show percentage, counter, ETA, and speed/throughput.
• Zero Dependencies: Pure Python, works anywhere Python 3.8+ runs.


Installation:

```bash
pip install progressor


Quick Start:

import time
from progressor import get_progress_drawer, ProgressStyle

# Create a progress drawer
draw = get_progress_drawer(
    style=ProgressStyle.BLOCK,
    width=40,
    show_percentage=True,
    show_counter=True,
    color_theme="green_red"
)

# Use it in your loop
for i in range(101):
    progress = i / 100.0
    draw(progress, current=i*10)
    time.sleep(0.05)


Examples:
Multiple Styles:

from progressor import get_progress_drawer, ProgressStyle

# Block style with detailed info
draw1 = get_progress_drawer(
    style=ProgressStyle.BLOCK,
    width=30,
    show_percentage=True,
    show_counter=True,
    show_eta=True,
    show_speed=True
)

# Circle progression
draw2 = get_progress_drawer(
    style=ProgressStyle.CIRCLE,
    width=20,
    color_theme="gradient"
)

# Star rating style
draw3 = get_progress_drawer(
    style=ProgressStyle.STAR,
    width=15,
    show_percentage=True
)


Custom Characters:

from progressor import get_progress_drawer

# Simple custom characters
draw = get_progress_drawer(
    custom_chars=("█", "░"),  # (filled, empty)
    width=25,
    show_percentage=True
)

# Or use Unicode block elements
from progressor import UnicodeBlocks
draw = get_progress_drawer(
    style=UnicodeBlocks.HORIZONTAL,
    width=20,
    color_theme="rainbow"
)


Multi-Bar Display:

from progressor import MultiProgress
import time

# Track 3 concurrent processes
multi = MultiProgress(count=3, style="block", width=25)

# Update each progress independently
multi.update(0, 0.3, "Downloading")
multi.update(1, 0.7, "Processing")
multi.update(2, 0.5, "Compressing")
time.sleep(1)

multi.complete()  # Clean up display


Available Styles:

Style                                                Example                                                   Description
ProgressStyle.BLOCK	               ████████░░░░░░░░	                Smooth block progression
ProgressStyle.CLASSIC	               ■■■■■■■■□□□□□□□□	        Classic filled/empty squares
ProgressStyle.BRAILLE                  ⣿⣿⣿⣿⣀⣀⣀⣀	                                        Braille pattern progression
ProgressStyle.ARROW	               >>>>>>>>--------	                                Arrow forward
ProgressStyle.VERTICAL                ▁▂▃▄▅▆▇█	                                        Vertical height increase
ProgressStyle.CIRCLE	               ○◔◑◕●	                                                Circle filling animation
ProgressStyle.SQUARE	               □◱◲■	                                                Square filling animation
ProgressStyle.GRADIENT	       ░▒▓█	                                                Shade gradient
ProgressStyle.STAR	                       ★★★★☆☆☆☆	                                Star rating
ProgressStyle.TRIANGLE	               ▲▲▲▲▽▽▽▽	                                Triangle progression
ProgressStyle.BOUNCE	               (→ )	                                                        Bouncing animation
Plus spinner variants	                       ⠋⠙⠹⠸⠼⠴	                                        Various spinner styles

Color Themes:
Theme	                                      Description	                                                Best For
None	                                              No coloring (default)	                                Simple terminals
"green_red"	                              Green progress, red remaining	                Success/failure indicators
"blue_yellow"	                              Blue progress, yellow remaining	                Cool/warm contrast
"gradient"	                                      Red→Yellow→Green based on progress	Process completion
"rainbow"	                                      Rainbow colors across the bar	                Fun, colorful displays
"monochrome"	                              Bright white on black	                                Low-color terminals
"terminal"	                                      Default colors with dimmed empty	        Subtle, clean look


Unicode Collections:
The library includes organized character sets:

from progressor import UnicodeBlocks, GeometricSymbols, EmojiThemes

# Block elements (8 levels of fill)
UnicodeBlocks.HORIZONTAL  # ['▏', '▎', '▍', '▌', '▋', '▊', '▉', '█']

# Geometric shapes
GeometricSymbols.CIRCLES["filled"]  # ['○', '◔', '◑', '◕', '●']

# Emoji themes (modern terminals)
EmojiThemes.NATURE["weather"]  # ['🌧️', '🌦️', '⛅', '🌤️', '☀️']

# Create custom sequences
from progressor import CustomTemplate
CustomTemplate.from_string("♩♪♫♬", stages=10)


API Reference:
get_progress_drawer()

def get_progress_drawer(
    style: Union[str, List[str]] = "block",
    width: int = 30,
    show_percentage: bool = True,
    show_counter: bool = False,
    show_eta: bool = False,
    show_speed: bool = False,
    spinner_only: bool = False,
    color_theme: Optional[Union[str, Callable]] = None,
    custom_chars: Optional[Tuple[str, str]] = None
) -> Callable[[float, Optional[int], Optional[float], Optional[float]], None]


MultiProgress Class:

multi = MultiProgress(count=3, style="block", width=30)
multi.update(index, progress, label="")
multi.complete()


progressor/
├── LICENSE                          # MIT License ✓
├── README.md                    # Documentation
├── CHANGELOG.md            # Changes
├── pyproject.toml                    # Build config (version: 1.0.0)
└── src/
    └── progressor/
        ├── __init__.py                # (version: 1.0.0)
        ├── progress.py
        ├── colors.py
        └── themes.py


Requirements:
• Python: 3.8 or higher
• Terminal: UTF-8 support (for Unicode characters)
• Colors: ANSI color support (most modern terminals)


Testing:

# After installation
python -c "from progressor import get_progress_drawer, ProgressStyle; print('Import successful')"

# Run the advanced test
python advanced_test.py


Contributing:
Contributions are welcome! Please feel free to submit a Pull Request.


License:
MIT License - see LICENSE file for details.


Files:

1) LICENSE

MIT License

Copyright (c) 2026 Dr. Libor Benes, M.A.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

--------------------------------------------------------------------------------------------------

2) README.md

This file.

--------------------------------------------------------------------------------------------------

3) CHANGELOG.md

# CHANGELOG.md

All published changes to Progressor to be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[1.0.0] - 2026-01-11
Added:
• Initial public release.
• Progress bar styles: Block, classic, braille, arrow, equal, dot, vertical, circle, square, gradient, hash, star, triangle, bounce.
• Spinner animations: Simple, dots, arrow spinners.
• Color support: 7 color themes (green_red, blue_yellow, gradient, rainbow, monochrome, terminal).
• Unicode collections: Block elements, geometric symbols, emoji themes, ASCII art, fancy symbols.
• Custom templates: Create progress bars with any characters.
• Multi-bar display: Track multiple concurrent processes.
• Real-time metrics: Percentage, counter, ETA, speed/throughput.
• Zero dependencies: Pure Python, uses only standard library.

Technical:
• Full Python type hints.
• Comprehensive error handling.
• MIT License.
• Python 3.8+ compatibility.

--------------------------------------------------------------------------------------------------

4) pyproject.toml

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "progressor"
version = "1.0.0"
description = "Enhanced progress bars with themes, colors, and custom templates"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    {name = "Dr. Libor Benes, M.A.", email = "Benes@iwp.edu"}
]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: User Interfaces",
    "Topic :: Terminals"
]

--------------------------------------------------------------------------------------------------

5) src/progressor/__init__.py

"""
progressor - Enhanced progress bars with themes, colors, and custom templates.
Minimal dependencies, no external libraries needed.
"""

from .progress import get_progress_drawer, ProgressStyle, MultiProgress
from .colors import Colors, ColorTheme, apply_color
from .themes import (
    UnicodeBlocks, GeometricSymbols, EmojiThemes,
    ASCIIArt, FancySymbols, CustomTemplate
)

__version__ = "1.0.0"
__all__ = [
    "get_progress_drawer",
    "ProgressStyle",
    "MultiProgress",
    "Colors",
    "ColorTheme",
    "apply_color",
    "UnicodeBlocks",
    "GeometricSymbols",
    "EmojiThemes",
    "ASCIIArt",
    "FancySymbols",
    "CustomTemplate",
    "__version__"
]

--------------------------------------------------------------------------------------------------

6) src/progressor/progress.py

"""
Main progress bar implementation.
Enhanced with themes, colors, and custom templates.
Minimal dependencies, no external libraries needed.
"""

import sys
import time
from typing import Callable, Optional, Union, List, Tuple

# Import new modules
from .colors import ColorTheme
from .themes import UnicodeBlocks, GeometricSymbols


class ProgressStyle:
    """Predefined progress bar styles (expanded)"""
    
    # Block styles
    BLOCK = "block"             # ████████░░░░░░░░
    CLASSIC = "classic"         # [■■■■■■■■□□□□□□□□]
    BRAILLE = "braille"         # ⣿⣿⣿⣿⣀⣀⣀⣀
    ARROW = "arrow"             # >>>>>>>>--------
    EQUAL = "equal"             # =========-------
    DOT = "dot"                 # ••••••••........
    
    # Spinners
    SPIN_SIMPLE = "spin_simple" # |/-\\|/-\...
    SPIN_DOTS = "spin_dots"     # ⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏
    SPIN_ARROW = "spin_arrow"   # ←↖↑↗→↘↓↙
    
    # New styles
    VERTICAL = "vertical"       # ▁▂▃▄▅▆▇█ (vertical blocks)
    CIRCLE = "circle"           # ○◔◑◕●
    SQUARE = "square"           # □◱◲■
    GRADIENT = "gradient"       # ░▒▓█ (shaded gradient)
    HASH = "hash"               # #####.....
    STAR = "star"               # ★★★★★☆☆☆☆☆
    TRIANGLE = "triangle"       # ▲▲▲▲▽▽▽▽
    BOUNCE = "bounce"           # (→    ) ( →   ) etc.


def get_progress_drawer(
    style: Union[str, List[str]] = "block",
    width: int = 30,
    show_percentage: bool = True,
    show_counter: bool = False,
    show_eta: bool = False,
    show_speed: bool = False,  # NEW: Show operations per second
    spinner_only: bool = False,
    color_theme: Optional[Union[str, Callable]] = None,
    custom_chars: Optional[Tuple[str, str]] = None
) -> Callable[[float, Optional[int], Optional[float], Optional[float]], None]:
    """
    Factory that returns a progress drawing function with selected style.
    
    Enhanced with color support and custom character sets.
    
    The returned function signature:
        def draw(progress: float, current: int | None = None, 
                eta: float | None = None, speed: float | None = None) -> None:
            # progress ∈ [0,1]
            # speed: operations per second (if show_speed=True)
    """

    # Track start time for speed calculation
    start_time = time.time()
    last_update = start_time
    last_value = 0
    
    # Determine style and handle custom inputs
    style_name = ""
    filled_char = ""
    empty_char = ""
    chars = []
    
    if custom_chars is not None:
        # User provided custom characters like ("@", ".")
        filled_char, empty_char = custom_chars
        style_name = "custom"
    elif isinstance(style, list):
        # User provided a list of characters for progressive fill
        chars = style
        if len(chars) < 1:
            raise ValueError("Character list must have at least one character")
        style_name = "custom_list"
    else:
        # Regular style name
        style_name = style.lower()
    
    # Map style names to drawing functions
    if style_name == "block":
        chars = " ▏▎▍▋▊▉"
        def draw_func(p: float):
            filled = int(p * (width * len(chars)-1))
            full = filled // (len(chars)-1)
            part = filled % (len(chars)-1)
            bar = chars[-1] * full + (chars[part] if part else "")
            bar += " " * (width - len(bar))
            return bar, " " * width

    elif style_name == "classic":
        def draw_func(p: float):
            filled = int(p * width)
            return "■" * filled, "□" * (width - filled)

    elif style_name == "braille":
        braille = " ⡀⡄⡆⡇⡏⡟⡿⣿"
        def draw_func(p: float):
            filled = int(p * width * 4)
            full = filled // 4
            part = filled % 4
            bar = braille[7] * full + (braille[part] if part else "")
            bar += " " * (width - len(bar))
            return bar, " " * width

    elif style_name == "arrow":
        def draw_func(p: float):
            filled = int(p * width)
            return ">" * filled, "-" * (width - filled)

    elif style_name == "equal":
        def draw_func(p: float):
            filled = int(p * width)
            return "=" * filled, "-" * (width - filled)

    elif style_name == "dot":
        def draw_func(p: float):
            filled = int(p * width)
            return "•" * filled, "." * (width - filled)

    elif style_name == "vertical":
        vertical_chars = UnicodeBlocks.VERTICAL
        def draw_func(p: float):
            filled = int(p * width)
            bar = ""
            for i in range(width):
                if i < filled:
                    # Use different heights based on position
                    height_idx = min(int(p * len(vertical_chars)), len(vertical_chars)-1)
                    bar += vertical_chars[height_idx]
                else:
                    bar += " "
            return bar, " " * width

    elif style_name == "circle":
        circle_chars = GeometricSymbols.CIRCLES["filled"]
        def draw_func(p: float):
            filled = int(p * width)
            filled_part = ""
            for i in range(filled):
                # Progressively fill circles
                idx = min(int(p * len(circle_chars)), len(circle_chars)-1)
                filled_part += circle_chars[idx]
            empty_part = circle_chars[0] * (width - filled)
            return filled_part, empty_part

    elif style_name == "square":
        square_chars = GeometricSymbols.SQUARES
        def draw_func(p: float):
            filled = int(p * width)
            filled_part = ""
            for i in range(filled):
                # Progressively fill squares
                idx = min(int(p * len(square_chars)), len(square_chars)-1)
                filled_part += square_chars[idx]
            empty_part = square_chars[0] * (width - filled)
            return filled_part, empty_part

    elif style_name == "gradient":
        def draw_func(p: float):
            filled = int(p * width)
            bar = ""
            for i in range(width):
                if i < filled:
                    # More filled = darker shade
                    if p < 0.33:
                        bar += "░"
                    elif p < 0.66:
                        bar += "▒"
                    else:
                        bar += "▓"
                else:
                    bar += " "
            return bar, " " * width

    elif style_name == "hash":
        def draw_func(p: float):
            filled = int(p * width)
            return "#" * filled, "." * (width - filled)

    elif style_name == "star":
        def draw_func(p: float):
            filled = int(p * width)
            return "★" * filled, "☆" * (width - filled)

    elif style_name == "triangle":
        def draw_func(p: float):
            filled = int(p * width)
            return "▲" * filled, "▽" * (width - filled)

    elif style_name == "bounce":
        frames = ["(→    )", "( →   )", "(  →  )", "(   → )", "(    →)", 
                 "(   ← )", "(  ←  )", "( ←   )", "(←    )"]
        def make_bounce():
            i = 0
            def bounce(p: float):
                nonlocal i
                # Scale frame based on progress
                frame_idx = int(p * (len(frames) - 1))
                s = frames[frame_idx]
                i = (i + 1) % len(frames)
                return s, ""
            return bounce
        
        draw_func = make_bounce()

    elif style_name == "spin_arrow":
        frames = ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"]
        def make_spinner():
            i = 0
            def spin(_: float):
                nonlocal i
                s = frames[i % len(frames)]
                i = (i + 1) % len(frames)
                return s * (width // 3) if spinner_only else s, ""
            return spin
        
        draw_func = make_spinner()

    elif style_name in ("spin_simple", "spin_dots"):
        if style_name == "spin_simple":
            frames = r"\|/-"
        else:
            frames = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

        def make_spinner():
            i = 0
            def spin(_: float):
                nonlocal i
                s = frames[i % len(frames)]
                i = (i + 1) % len(frames)
                return s * (width // 3) if spinner_only else s, ""
            return spin
        
        draw_func = make_spinner()

    elif style_name == "custom":
        # Custom characters from user (filled_char, empty_char)
        def draw_func(p: float):
            filled = int(p * width)
            return filled_char * filled, empty_char * (width - filled)

    elif style_name == "custom_list":
        # List of characters for progressive fill
        if len(chars) == 0:
            raise ValueError("Character list cannot be empty")
        def draw_func(p: float):
            filled = int(p * width)
            filled_part = ""
            for i in range(filled):
                # Use character based on position in sequence
                idx = min(int(p * len(chars)), len(chars)-1)
                filled_part += chars[idx]
            empty_part = chars[0] * (width - filled)
            return filled_part, empty_part

    else:
        raise ValueError(f"Unknown style: {style!r}. Available: {', '.join([k for k in ProgressStyle.__dict__.keys() if not k.startswith('_')])}")

    # Color theme handler
    if color_theme is None:
        color_handler = ColorTheme.default
    elif callable(color_theme):
        color_handler = color_theme
    elif color_theme == "green_red":
        color_handler = ColorTheme.green_red
    elif color_theme == "blue_yellow":
        color_handler = ColorTheme.blue_yellow
    elif color_theme == "gradient":
        color_handler = ColorTheme.gradient
    elif color_theme == "rainbow":
        color_handler = ColorTheme.rainbow
    elif color_theme == "monochrome":
        color_handler = ColorTheme.monochrome
    elif color_theme == "terminal":
        color_handler = ColorTheme.terminal
    else:
        color_handler = ColorTheme.default

    def draw(
        progress: float,
        current: Optional[int] = None,
        eta: Optional[float] = None,
        speed: Optional[float] = None
    ):
        """
        Draw progress bar according to selected style
        
        Args:
            progress: 0..1
            current: Current item count (if show_counter=True)
            eta: Estimated time remaining in seconds (if show_eta=True)
            speed: Operations per second (if show_speed=True)
        """
        # Fix variable scope issue
        nonlocal last_update, last_value
        
        if not 0 <= progress <= 1:
            progress = max(0, min(1, progress))
        
        # Calculate speed if not provided but requested
        computed_speed = None
        if show_speed and speed is None and current is not None:
            now = time.time()
            if now > last_update:
                computed_speed = (current - last_value) / (now - last_update)
                last_update = now
                last_value = current
        
        # Draw the bar
        filled_part, empty_part = draw_func(progress)
        
        # Apply color theme
        if color_handler:
            filled_part, empty_part = color_handler(filled_part, empty_part, progress)
        
        bar = filled_part + empty_part
        
        # Build info parts
        parts = []
        
        if show_percentage:
            parts.append(f"{progress:5.1%}")
        
        if show_counter and current is not None:
            parts.append(f"{current:,}")
        
        if show_eta and eta is not None and eta > 0:
            if eta < 60:
                parts.append(f"ETA {eta:.1f}s")
            elif eta < 3600:
                parts.append(f"ETA {eta/60:.1f}m")
            else:
                parts.append(f"ETA {eta/3600:.1f}h")
        
        if show_speed:
            speed_to_show = speed if speed is not None else computed_speed
            if speed_to_show is not None:
                if speed_to_show < 1000:
                    parts.append(f"{speed_to_show:.1f}/s")
                elif speed_to_show < 1_000_000:
                    parts.append(f"{speed_to_show/1000:.1f}K/s")
                else:
                    parts.append(f"{speed_to_show/1_000_000:.1f}M/s")
        
        extra = " │ " + "  ".join(parts) if parts else ""
        
        line = f"\r{bar}{extra}"
        sys.stdout.write(line)
        sys.stdout.flush()
        
        # Print newline when complete
        if progress >= 1:
            sys.stdout.write("\n")
            sys.stdout.flush()

    return draw


# Multi-bar display (simple implementation)
class MultiProgress:
    """
    Simple multi-progress bar display.
    Useful for tracking multiple concurrent processes.
    """
    
    def __init__(self, count: int, style: str = "block", width: int = 30):
        self.count = count
        self.drawers = [get_progress_drawer(style, width, show_percentage=False) 
                       for _ in range(count)]
        self.lines_written = 0
    
    def update(self, index: int, progress: float, label: str = ""):
        """Update a specific progress bar"""
        if index < 0 or index >= self.count:
            raise IndexError(f"Index {index} out of range (0-{self.count-1})")
        
        # Move cursor to the right line
        if self.lines_written:
            sys.stdout.write(f"\033[{self.lines_written}A")  # Move up
        
        # Update all bars
        for i in range(self.count):
            if i == index:
                prefix = f"{label}: " if label else f"Bar {i+1}: "
                sys.stdout.write(prefix)
                self.drawers[i](progress)
                sys.stdout.write("\n")
            else:
                # Just keep existing line
                sys.stdout.write("\n")
        
        self.lines_written = self.count
        sys.stdout.flush()
    
    def complete(self):
        """Complete all progress bars"""
        sys.stdout.write("\n" * self.lines_written)
        sys.stdout.flush()

--------------------------------------------------------------------------------------------------

7) src/progressor/colors.py

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

--------------------------------------------------------------------------------------------------

8) src/progressor/themes.py

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
