# -*- coding: utf-8 -*-

# Ankjutsu - Gojo Reinforcement Add-on for Anki
# Based on Ankitty by Marvin A. Ruder (originally Puppy Reinforcement by Glutanimate)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

from aqt.gui_hooks import add_cards_did_add_note, reviewer_did_answer_card

from .reinforcer import GojoReinforcer


def initialize_views(reinforcer: GojoReinforcer, config: dict):
    if config.get("count_reviewing", True):
        reviewer_did_answer_card.append(reinforcer.show_gojo)
    if config.get("count_adding", False):
        add_cards_did_add_note.append(reinforcer.show_gojo)
