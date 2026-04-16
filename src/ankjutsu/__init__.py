# -*- coding: utf-8 -*-

# Ankjutsu - Gojo Reinforcement Add-on for Anki
# Based on Ankitty by Marvin A. Ruder (originally Puppy Reinforcement by Glutanimate)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

"""
Ankjutsu: Satoru Gojo reinforcement for Anki
Shows Gojo images as positive reinforcement while studying.
"""

from typing import TYPE_CHECKING

from aqt import mw as main_window

from .reinforcer import GojoReinforcer
from .views import initialize_views

if TYPE_CHECKING:
    assert main_window is not None

# Load config using Anki's built-in config manager
config = main_window.addonManager.getConfig(__name__) or {}

gojo_reinforcer = GojoReinforcer(main_window, config)

main_window._gojo_reinforcer = gojo_reinforcer  # type: ignore[attr-defined]

initialize_views(gojo_reinforcer, config)
