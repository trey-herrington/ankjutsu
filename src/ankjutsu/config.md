**Ankjutsu** supports the following config values:

<div style="color: #ff8080; font-weight: bold;">Please note that you will have to restart Anki for some of these options to apply (e.g. toggling the add-on for reviews / adding cards)</div>

- **count_adding** [true/false]: count added cards towards Gojo tally; default: `false`
- **count_reviewing** [true/false]: count reviews towards Gojo tally; default: `true`
- **duration** [integer]: duration in msec; default: `3000`
- **encourage_every** [integer]: show encouragement about every n cards; default: `10`
- **encouragements** [dict]: JJK-themed encouragements by level
- **image_height** [integer]: image height in px, tooltip is automatically scaled; default: `128`
- **limit_high** [integer]: lower card limit for high encouragement level; default: `50`
- **limit_max** [integer]: lower card limit for max encouragement level; default: `100`
- **limit_middle** [integer]: lower card limit for middle encouragement level; default: `25`
- **max_spread** [integer]: max spread around interval; default: `5`
- **tooltip_color** [string]: HTML color code; default: `#C5CFFF` (light blue/purple)
- **tooltip_align_vertical** [enum]: `top`, `center`, or `bottom`. Default: `bottom`.
- **tooltip_align_horizontal** [enum]: `right`, `center`, or `left`. Default: `left`.
- **tooltip_space_vertical** [integer]: distance from top/bottom edge. Default: `100`.
- **tooltip_space_horizontal** [integer]: distance from left/right edge. Default: `0`.
- **disable_default_images** [true/false]: if you add custom images to the `user_files` directory, set this to `true` to only use those. Default: `false`.
- **reset_counter_on_new_day** [true/false]: reset the card counter on day change. Default: `false`.
