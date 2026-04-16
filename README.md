# Ankjutsu

Satoru Gojo reinforcement add-on for Anki. Get motivated by the strongest sorcerer while studying your flashcards.

Based on [Ankitty](https://github.com/marvinruder/ankitty) / [Puppy Reinforcement](https://github.com/glutanimate/puppy-reinforcement) by Glutanimate.

## How It Works

Every ~10 cards (configurable), a random Gojo image pops up with a JJK-themed encouragement message like "Nah, I'd study." or "Domain Expansion: Infinite Knowledge!" Uses intermittent reinforcement to keep you motivated without being annoying.

**Images are not included.** You need to supply your own Gojo images due to copyright. See below.

## Installation

1. Install the add-on (via AnkiWeb or manually — see below)
2. **Add your own Gojo images** to the add-on's `images/` folder (see [Adding Images](#adding-images))
3. Restart Anki

### Via AnkiWeb

1. In Anki, go to **Tools > Add-ons > Get Add-ons...**
2. Paste the add-on code: `TODO` (update after publishing)

### Manual Install

1. Copy or symlink the `src/ankjutsu/` directory into your Anki addons folder:
   - Linux: `~/.local/share/Anki2/addons21/ankjutsu`
   - macOS: `~/Library/Application Support/Anki2/addons21/ankjutsu`
   - Windows: `%APPDATA%\Anki2\addons21\ankjutsu`

## Adding Images

This add-on does **not** ship with images. You need to add your own Satoru Gojo images.

1. Find the add-on folder:
   - In Anki, go to **Tools > Add-ons**, select Ankjutsu, and click **View Files**
2. Place your images (`.jpg`, `.png`, `.gif`, `.bmp`, `.webp`) in the `images/` subfolder
3. Restart Anki

You can also place images in a `user_files/` subfolder instead. If you set `"disable_default_images": true` in the config, only images from `user_files/` will be used.

## Configuration

Go to **Tools > Add-ons > Ankjutsu > Config** in Anki to customize settings. See `config.md` for all options.

## License

GNU AGPLv3
