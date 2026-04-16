# -*- coding: utf-8 -*-

# Ankjutsu - Gojo Reinforcement Add-on for Anki
# Based on Ankitty by Marvin A. Ruder (originally Puppy Reinforcement by Glutanimate)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

from typing import TYPE_CHECKING, Dict, List, Optional

import random
import re
from pathlib import Path

if TYPE_CHECKING:
    from aqt.main import AnkiQt

from .gui.notification import Notification

# Path to this addon's directory
_ADDON_DIR = Path(__file__).parent


class GojoReinforcer:
    _extensions = re.compile(r"\.(jpg|jpeg|png|bmp|gif|webp)$")

    def __init__(self, mw: "AnkiQt", config: dict):
        self._mw = mw
        self._config = config
        self._images: List[str] = []
        self._playlist: List[int] = []

        self._state: Dict = {
            "cnt": 0,
            "last": 0,
            "enc": None,
            "ivl": config.get("encourage_every", 10),
            "cutoff": False,
        }

        self._read_images()
        self._rebuild_playlist()
        self._shuffle_playlist()

    def show_gojo(self, *args, **kwargs):
        config = self._config

        if config.get("reset_counter_on_new_day", False):
            self._maybe_reset_count()

        self._state["cnt"] += 1
        if self._state["cnt"] != self._state["last"] + self._state["ivl"]:
            return

        image_path = self._get_next_image()
        if not image_path:
            return

        encouragement = self._get_encouragement(self._state["cnt"])
        self._show_tooltip(encouragement, image_path)

        self._state["ivl"] = max(
            1,
            config.get("encourage_every", 10)
            + random.randint(
                -config.get("max_spread", 5), config.get("max_spread", 5)
            ),
        )
        self._state["last"] = self._state["cnt"]

    def _show_tooltip(self, encouragement: str, image_path: str):
        config = self._config
        count = self._state["cnt"]

        html = f"""\
<table cellpadding=10>
<tr>
<td><img height={config.get("image_height", 128)} src="{image_path}"></td>
<td valign="middle">
    <center><b>{count} {'cards' if count > 1 else 'card'} done so far!</b><br>
    {encouragement}</center>
</td>
</tr>
</table>"""

        notification = Notification(
            html,
            self._mw.progress,
            duration=config.get("duration", 3000),
            parent=self._mw.app.activeWindow() or self._mw,
            align_horizontal=config.get("tooltip_align_horizontal", "left"),
            align_vertical=config.get("tooltip_align_vertical", "bottom"),
            space_horizontal=config.get("tooltip_space_horizontal", 0),
            space_vertical=config.get("tooltip_space_vertical", 100),
            bg_color=config.get("tooltip_color", "#C5CFFF"),
        )

        notification.show()

    def _read_images(self):
        default_path = _ADDON_DIR / "images"
        user_path = _ADDON_DIR / "user_files"

        images = []

        for path in (user_path, default_path):
            if not path.is_dir():
                continue
            for p in path.iterdir():
                if not self._extensions.search(p.suffix.lower()):
                    continue
                images.append(str(p.resolve()))

            if images and self._config.get("disable_default_images", False):
                break

        self._images = images

    def _maybe_reset_count(self):
        cutoff = self._get_day_cutoff()

        if self._state["cutoff"] is False:
            self._state["cutoff"] = cutoff
        elif self._state["cutoff"] == cutoff:
            return

        self._state["cnt"] = 0
        self._state["cutoff"] = cutoff

    def _get_day_cutoff(self) -> Optional[int]:
        if (collection := self._mw.col) is None:
            return None
        scheduler = collection.sched
        if hasattr(scheduler, "day_cutoff"):
            return scheduler.day_cutoff
        try:
            return scheduler.dayCutoff  # type: ignore[union-attr]
        except AttributeError:
            return None

    def _rebuild_playlist(self):
        self._playlist = list(range(len(self._images)))

    def _shuffle_playlist(self):
        random.shuffle(self._playlist)

    def _get_next_image(self) -> Optional[str]:
        if not self._images:
            return None
        try:
            index = self._playlist.pop()
        except IndexError:
            self._rebuild_playlist()
            self._shuffle_playlist()
            index = self._playlist.pop()
        return self._images[index]

    def _get_encouragement(self, cards: int) -> str:
        config = self._config
        last = self._state["enc"]
        encouragements = config.get("encouragements", {})

        if cards >= config.get("limit_max", 100):
            lst = list(encouragements.get("max", ["Incredible!"]))
        elif cards >= config.get("limit_high", 50):
            lst = list(encouragements.get("high", ["Amazing!"]))
        elif cards >= config.get("limit_middle", 25):
            lst = list(encouragements.get("middle", ["Keep going!"]))
        else:
            lst = list(encouragements.get("low", ["Nice!"]))

        if last and last in lst:
            lst.remove(last)
        if not lst:
            return ""
        idx = random.randrange(len(lst))
        self._state["enc"] = lst[idx]
        return lst[idx]
