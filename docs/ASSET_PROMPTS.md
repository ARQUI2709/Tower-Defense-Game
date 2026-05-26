# Prompts de generación de assets (Gemini / Imagen / Nano Banana)

Este documento contiene prompts listos para usar con **Gemini 2.5 Flash Image (Nano Banana)** o **Imagen 4** para generar los ~120 assets que necesita el juego, manteniendo una estética coherente inspirada en juegos móviles tipo *Kingshot*, *Clash Royale* y *Rush Royale* (cartoon 3D vista cenital, colores muy saturados, sombras suaves y siluetas claras).

> **Tip:** Genera todo a 4× la resolución final y luego reescala con un tool. Eso da mejor antialiasing y permite reutilizar el master en pantallas retina.

---

## 0. Estilo base (péguelo como prefijo en TODOS los prompts)

```
STYLE: Mobile game cartoon-3D rendering, top-down 3/4 isometric view, soft
cel-shading with subtle ambient occlusion, vivid saturated colors, chunky
stylized proportions, clean silhouette readable at small sizes, smooth gradients,
slight rim light, no text, no watermark, no UI, flat shadow underneath.
PALETTE: bright grass green #4FA94D, warm wood brown #8B5A2B, gold #F2C84B,
royal blue #2D6CDF, alarm red #D63B3B, parchment cream #F4E4B8.
REFERENCE: art direction similar to Kingshot / Rush Royale / Clash Royale.
BACKGROUND: pure transparent (PNG alpha) unless stated otherwise.
```

---

## 1. Fondos (no transparentes)

### `game_assets/bg.png` — 1350×700
```
Top-down view of a grassy battlefield map for a tower defense game. A winding
dirt path snakes from the left edge across the screen and exits on the right,
forming a single continuous lane with smooth curves. The path is light sandy
beige with subtle pebble texture. Surrounding terrain is lush cartoon grass
with small flower clusters, scattered bushes, a few stylized pine trees in the
corners, and a wooden palisade fence framing the playable area. Soft warm
midday lighting, no characters, no UI overlay, no text. Resolution 1350x700.
```

### `main_menu/main_menu` reuses the same `bg.png`.

---

## 2. UI raíz (`game_assets/`)

### `logo.png` — 600×200 (transparent)
```
A bold cartoon game logo reading "TOWER DEFENSE" in chunky 3D extruded letters,
golden yellow with a thick dark brown outline, slight inner highlight and
drop shadow, slightly tilted in 3/4 perspective, on transparent background.
Mobile game title aesthetic, hyper-readable.
```

### `side.png` — 120×500 (transparent)
```
Vertical wooden side panel for a game HUD, made of stacked horizontal wooden
planks with visible grain, dark iron rivets in the corners, slightly worn
edges, rich brown #8B5A2B color. Standalone panel with transparent background,
no buttons drawn on top, leaving the interior empty for UI.
```

### `menu.png` — 120×70 (transparent)
```
Small rectangular wooden plaque / signpost in cartoon style, horizontal
orientation, rounded corners, dark wood grain with a lighter inset center,
gold trim on the border, transparent background. Used as a tooltip / menu
background.
```

### `wave.png` — 225×75 (transparent)
```
Banner ribbon for a wave counter, deep red fabric with golden trim,
slight wave-like curl at both ends, cartoon-3D style, plenty of flat
central space to overlay text later, transparent background.
```

### `heart.png` — 40×40 (transparent)
```
Glossy cartoon red heart icon, slightly 3D with a soft highlight on the top
left and a darker red rim. Plump rounded shape, clean silhouette, transparent
background. Mobile game HUD style.
```

### `star.png` — 40×40 (transparent)
```
Glossy cartoon gold coin viewed almost head-on, with a star symbol embossed
in the center, slight 3D depth, warm golden gradient #F2C84B, dark gold rim,
soft top highlight. Transparent background.
```

### Botones (todos transparentes)

#### `button_play.png` — 600×200 → reescalar
```
Large rounded rectangular cartoon button labeled "PLAY", green body
(#4FA94D), thick dark green outline, white play triangle icon to the left of
the text, glossy top highlight, soft drop shadow. Transparent background.
Mobile game main-menu button style.
```

#### `button_start.png` — 256×256 → reescalar a 75×75
```
Circular cartoon button with a green body and dark green outline, white play
triangle (▶) centered, glossy top highlight, slight bevel. Transparent
background.
```

#### `button_pause.png` — 256×256
```
Circular cartoon button, yellow-orange body (#F2A93B) with dark brown outline,
two white vertical bars centered (pause icon), glossy top highlight.
Transparent background.
```

#### `button_sound.png` — 256×256
```
Circular cartoon button, blue body (#2D6CDF) with dark navy outline, white
speaker icon with sound waves centered. Glossy top highlight. Transparent
background.
```

#### `button_sound_off.png` — 256×256
```
Same as button_sound.png but the speaker has a red diagonal slash through it,
indicating muted. Same dimensions and styling.
```

#### `upgrade.png` — 256×256 → reescalar a 50×50
```
Circular cartoon button, vivid green body, white upward arrow (↑) centered,
small plus sign (+) overlapping the arrow tail, thick dark outline, glossy
highlight. Transparent background.
```

#### `buy_archer.png` — 256×256 → reescalar a 75×75
```
Square rounded card for a shop item, parchment cream background with brown
border, showing a small cartoon archer tower (wooden tower with thatched
roof and a tiny archer on top, blue tunic) in the center. Top-down 3/4 view.
Transparent background outside the card.
```

#### `buy_archer_2.png` — 256×256 → reescalar a 75×75
```
Same shop-card frame as buy_archer.png, but containing a stone-based archer
tower with a red-tunic archer on top, slightly taller and more fortified.
Transparent background.
```

#### `buy_damage.png` — 256×256 → reescalar a 75×75
```
Same shop-card frame, containing a small red crystal totem tower glowing
warmly, representing a damage-boost support tower. Cartoon 3D, transparent
background.
```

#### `buy_range.png` — 256×256 → reescalar a 75×75
```
Same shop-card frame, containing a small blue crystal totem tower glowing
cyan, representing a range-boost support tower. Cartoon 3D, transparent
background.
```

---

## 3. Torres de arquero (`game_assets/archer_towers/`)

Las torres tienen **dos partes**: la base (`archer_1/`, `archer_2/`) y el arquero animado encima (`archer_top/`, `archer_top_2/`). El arquero se anima por frames.

### `archer_1/7.png`, `8.png`, `9.png` — 360×360 → 90×90 (transparent)
```
A cartoon-3D wooden archer tower in top-down 3/4 view, three upgrade tiers
shown side by side as separate images:
- Tier 1 (7.png): small wooden tower with thatched roof, single floor.
- Tier 2 (8.png): same tower with reinforced wooden beams, a small balcony.
- Tier 3 (9.png): tall fortified wooden tower with iron banding and a flag
  on top.
All three sit on the same cobblestone base, viewed from a top-down 3/4
angle, transparent background, no characters on top (the archer is rendered
separately). Save each tier as a separate PNG with the same camera framing.
```

### `archer_2/10.png`, `11.png`, `12.png` — 360×360 → 90×90 (transparent)
```
Same as archer_1 but built from gray stone instead of wood:
- Tier 1 (10.png): short stone turret with crenellations.
- Tier 2 (11.png): two-story stone turret with arrow slits.
- Tier 3 (12.png): tall stone keep with a blue conical roof and a flag.
Top-down 3/4 view, identical camera, transparent background, no archer on
top.
```

### `archer_top/37.png` … `42.png` — 240×320 → ~60×80 (transparent)
**6 frames de animación**
```
A cartoon archer character viewed from a top-down 3/4 angle (looking down
onto the head and shoulders), wearing a green hood and brown leather armor.
Generate a 6-frame shooting animation sequence:
- 37.png: idle, bow held loosely.
- 38.png: drawing the arrow back, string tensioning.
- 39.png: full draw, aiming to the right.
- 40.png: arrow released, bow vibrating slightly.
- 41.png: follow-through, arm extended.
- 42.png: returning to idle.
Consistent character design across all frames, transparent background,
identical canvas size and centering. Facing right by default (the game flips
horizontally for the other direction).
```

### `archer_top_2/43.png` … `48.png` — 240×320 → ~60×80 (transparent)
**6 frames de animación** (versión 2)
```
Same as archer_top but for an elite archer: red hood and steel scale armor,
a more ornate bow with golden inlays. Same 6-frame draw-aim-release-recover
sequence, consistent character, transparent background, facing right.
Frames 43–48.
```

---

## 4. Torres de soporte (`game_assets/support_towers/`)

### `4.png`, `5.png` — 360×360 → 90×90 (transparent) — RANGE
```
A cartoon-3D magical range-boost totem, two upgrade tiers:
- 4.png: a small wooden pillar topped with a glowing CYAN crystal sphere,
  faint blue particles around it, runes carved on the base.
- 5.png: a taller obsidian pillar with a larger faceted CYAN crystal,
  brighter aura, more particles, golden bands around the base.
Top-down 3/4 view, transparent background, identical camera.
```

### `8.png`, `9.png` — 360×360 → 90×90 (transparent) — DAMAGE
```
A cartoon-3D magical damage-boost totem, two upgrade tiers:
- 8.png: a small wooden pillar topped with a glowing RED crystal sphere,
  faint red embers around it, runes carved on the base.
- 9.png: a taller obsidian pillar with a larger faceted RED crystal,
  brighter aura, more embers, golden bands around the base.
Top-down 3/4 view, transparent background, identical camera.
```

---

## 5. Enemigos animados (`game_assets/enemies/`)

Cada enemigo tiene **20 frames de animación de carrera (run cycle)**, numerados `000` a `019`. La cámara es top-down 3/4 cenital (vista desde arriba ligeramente inclinada), igual que en la imagen de referencia *Kingshot*.

> **Estrategia recomendada con Nano Banana:** genera el frame 000 primero como turnaround base, luego pídele "iterate this character into a 20-frame run cycle, keeping silhouette, colors and proportions identical". Sirve para mantener consistencia.

### `enemies/1/` — SCORPION (64×64 final, 20 frames)
```
A small cartoon desert scorpion with a glossy orange-brown carapace, two
oversized claws and a curled tail with a yellow stinger. Top-down 3/4 view.
Generate a 20-frame run-cycle animation (000 to 019) of the scorpion
scuttling forward toward the right of the frame. Maintain identical
coloring, proportions, and camera in every frame. Cartoon-3D style,
transparent background, flat shadow on the ground.
```

### `enemies/2/` — WIZARD (64×64 final, 20 frames)
```
A small cartoon evil wizard with a tall pointed purple hat, long white
beard, dark purple robe with golden trim, holding a glowing magical staff.
Top-down 3/4 view. Generate a 20-frame walk-cycle animation (000 to 019)
showing the wizard hovering / striding forward toward the right, robe
billowing, staff bobbing. Consistent design across all frames, transparent
background, soft purple glow around the staff.
```

### `enemies/5/` — CLUB (64×64 final, 20 frames)
```
A burly cartoon orc warrior with green skin, tusks, leather harness and a
massive wooden club resting on his shoulder. Top-down 3/4 view. Generate a
20-frame heavy-walk animation (000 to 019) showing the orc lumbering
forward toward the right, club bouncing on the shoulder. Consistent
character, transparent background, flat ground shadow.
```

### `enemies/8/` — SWORD (100×100 final, 20 frames — BIGGER)
```
A heavily armored cartoon knight boss, larger than other enemies, wearing
ornate red-and-silver plate armor, plumed helmet, holding a huge two-handed
broadsword resting on his shoulder. Top-down 3/4 view. Generate a 20-frame
slow-march animation (000 to 019) showing the knight stomping forward
toward the right with imposing weight. Consistent design across all frames,
transparent background, flat ground shadow. Render larger than other enemies.
```

---

## 6. Audio

### `music.mp3`
```
Background music loop is NOT generated by image models. Use any of these
sources:
- pixabay.com/music/search/medieval+loop  (CC0, drop-in safe)
- opengameart.org "tower defense"          (CC-BY, attribute the author)
- Suno / Udio prompt: "epic medieval tower defense battle music loop,
  orchestral percussion and brass, mid-tempo, seamless loop, 90 seconds,
  uplifting heroic mood, no vocals"
Convert to MP3, 128 kbps, mono or stereo, exactly looping (no silence at
edges).
```

---

## 7. Convenciones de exportación

| Aspecto | Valor |
|---|---|
| Formato | PNG con alpha (excepto `bg.png`) |
| Color profile | sRGB |
| Bit depth | 8-bit por canal |
| Padding | Sin padding extra; el sprite debe llenar el frame |
| Pivote | Centro geométrico, para que `pygame.transform.flip` quede simétrico |
| Naming | Respetar EXACTAMENTE los nombres de la sección anterior |

## 8. Flujo sugerido con Nano Banana

1. Genera todos los fondos y UI estáticos primero (~20 prompts independientes).
2. Para cada **torre y enemigo** genera primero un frame de referencia y luego usa "iterate to N-frame animation cycle, same character" para los frames restantes — esto mantiene consistencia visual.
3. Pasa todo por `tools/check_assets.py` (si lo añadimos) para verificar que coincidan tamaños y rutas.
4. Reemplaza los placeholders generados por `tools/generate_placeholders.py`.

---

## 9. Checklist rápido

- [ ] 17 sprites en `game_assets/` (raíz)
- [ ] 6 sprites en `archer_towers/archer_1` y `archer_2`
- [ ] 12 frames en `archer_towers/archer_top` y `archer_top_2`
- [ ] 4 sprites en `support_towers/`
- [ ] 80 frames en `enemies/{1,2,5,8}/`
- [ ] 1 archivo `music.mp3`
- [ ] **Total: ~120 archivos**
