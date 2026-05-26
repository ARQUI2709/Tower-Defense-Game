"""
Generates placeholder assets for the Tower Defense Game so the project can be
launched (locally or as a PWA via pygbag) without the original art.

All sprites are colored rectangles with a label baked in. Replace them with the
real assets in `game_assets/` whenever they are available — the file names and
folder layout match exactly what the game tries to load.

Usage:
    pip install Pillow
    python tools/generate_placeholders.py
"""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "game_assets"


def _font(size: int) -> ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ):
        if os.path.exists(candidate):
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_sprite(
    path: Path,
    size: tuple[int, int],
    color: tuple[int, int, int],
    label: str,
    *,
    border: tuple[int, int, int] | None = (20, 20, 20),
    alpha: bool = True,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "RGBA" if alpha else "RGB"
    base_color = (*color, 255) if alpha else color
    img = Image.new(mode, size, base_color)
    draw = ImageDraw.Draw(img)

    if border:
        b = (*border, 255) if alpha else border
        draw.rectangle([0, 0, size[0] - 1, size[1] - 1], outline=b, width=2)

    font = _font(max(10, min(size) // 6))
    text_bbox = draw.textbbox((0, 0), label, font=font)
    tw = text_bbox[2] - text_bbox[0]
    th = text_bbox[3] - text_bbox[1]
    tx = (size[0] - tw) // 2
    ty = (size[1] - th) // 2
    shadow = (0, 0, 0, 200) if alpha else (0, 0, 0)
    draw.text((tx + 1, ty + 1), label, font=font, fill=shadow)
    draw.text((tx, ty), label, font=font, fill=(255, 255, 255, 255) if alpha else (255, 255, 255))

    img.save(path)


def write_silent_mp3(path: Path) -> int:
    """
    Tries to produce a silent music.mp3 placeholder.

    Strategy:
      1) Use ffmpeg if available — best result, real valid MP3.
      2) Otherwise write a minimal MPEG-1 Layer III silent frame (104 bytes).
         Most decoders (including SDL_mixer) accept it; if pygame ever
         complains, drop in any real .mp3 in its place.

    Returns the number of bytes written.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        try:
            subprocess.run(
                [
                    ffmpeg, "-y", "-loglevel", "error",
                    "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
                    "-t", "2", "-b:a", "64k", str(path),
                ],
                check=True,
            )
            return path.stat().st_size
        except subprocess.CalledProcessError:
            pass

    # Fallback: one silent MPEG-1 Layer III frame (32 kbps, 44.1 kHz, mono).
    header = bytes([0xFF, 0xFB, 0x10, 0x64])
    frame = header + b"\x00" * 100
    path.write_bytes(frame * 50)  # 50 frames ≈ 1.3 s of silence
    return path.stat().st_size


ROOT_SPRITES = [
    ("bg.png", (1350, 700), (60, 130, 70), "BACKGROUND", False),
    ("logo.png", (600, 200), (120, 70, 30), "LOGO", True),
    ("side.png", (120, 500), (70, 45, 25), "SIDE PANEL", True),
    ("menu.png", (120, 70), (50, 50, 80), "MENU", True),
    ("wave.png", (225, 75), (180, 40, 40), "WAVE", True),
    ("heart.png", (40, 40), (220, 40, 40), "HP", True),
    ("star.png", (40, 40), (240, 200, 40), "$", True),
    ("button_play.png", (200, 80), (60, 160, 60), "PLAY", True),
    ("button_start.png", (75, 75), (60, 160, 60), "GO", True),
    ("button_pause.png", (75, 75), (200, 160, 40), "II", True),
    ("button_sound.png", (75, 75), (80, 110, 200), "SND", True),
    ("button_sound_off.png", (75, 75), (110, 110, 110), "MUTE", True),
    ("upgrade.png", (50, 50), (40, 180, 40), "UP", True),
    ("buy_archer.png", (75, 75), (140, 90, 50), "ARC1", True),
    ("buy_archer_2.png", (75, 75), (170, 110, 60), "ARC2", True),
    ("buy_damage.png", (75, 75), (200, 60, 60), "DMG", True),
    ("buy_range.png", (75, 75), (60, 140, 200), "RNG", True),
]


def generate_root() -> None:
    for name, size, color, label, alpha in ROOT_SPRITES:
        make_sprite(ASSETS / name, size, color, label, alpha=alpha)


def generate_archer_towers() -> None:
    base = ASSETS / "archer_towers"
    for x in range(7, 10):
        make_sprite(base / "archer_1" / f"{x}.png", (90, 90), (140, 90, 50), f"T1-{x}")
    for x in range(10, 13):
        make_sprite(base / "archer_2" / f"{x}.png", (90, 90), (170, 110, 60), f"T2-{x}")
    for x in range(37, 43):
        make_sprite(base / "archer_top" / f"{x}.png", (60, 80), (40, 80, 160), f"A{x}")
    for x in range(43, 49):
        make_sprite(base / "archer_top_2" / f"{x}.png", (60, 80), (160, 80, 40), f"A{x}")


def generate_support_towers() -> None:
    base = ASSETS / "support_towers"
    for name, color in [("4.png", (60, 140, 200)), ("5.png", (40, 110, 180))]:
        make_sprite(base / name, (90, 90), color, "RNG")
    for name, color in [("8.png", (200, 60, 60)), ("9.png", (170, 40, 40))]:
        make_sprite(base / name, (90, 90), color, "DMG")


ENEMIES = [
    ("1", "scorpion", (200, 140, 40), (64, 64)),
    ("2", "wizard", (140, 80, 200), (64, 64)),
    ("5", "club", (140, 100, 60), (64, 64)),
    ("8", "sword", (200, 60, 80), (100, 100)),
]


def generate_enemies() -> None:
    base = ASSETS / "enemies"
    for folder, label, color, size in ENEMIES:
        for x in range(20):
            suffix = f"0{x}" if x < 10 else str(x)
            name = f"{folder}_enemies_1_run_0{suffix}.png"
            make_sprite(base / folder / name, size, color, label[:4].upper())


def main() -> None:
    print(f"Writing placeholders to {ASSETS}")
    generate_root()
    generate_archer_towers()
    generate_support_towers()
    generate_enemies()
    music_bytes = write_silent_mp3(ASSETS / "music.mp3")
    total = sum(1 for _ in ASSETS.rglob("*") if _.is_file())
    print(f"music.mp3 = {music_bytes} bytes")
    print(f"Done. {total} files in game_assets/")


if __name__ == "__main__":
    main()
