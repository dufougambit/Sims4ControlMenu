import sims4
import services


@sims4.commands.Command('clock.set_game_clock')
def set_game_clock(absolute_ticks: int):
    services.game_clock_service().tick_game_clock(absolute_ticks)
