"""
Control Menu is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
import date_and_time
from sims4communitylib.utils.common_time_utils import CommonTimeUtils
import sims4
from scheduler import ScheduleEntry
import services


class CMTimeUtils:
    EA_REAL_MILLISECONDS_PER_SIM_SECOND = 25
    EA_SECONDS_PER_MINUTE = 60
    EA_SECONDS_PER_HOUR = EA_SECONDS_PER_MINUTE * 60
    EA_SECONDS_PER_DAY = EA_SECONDS_PER_HOUR * 24
    EA_SECONDS_PER_WEEK = EA_SECONDS_PER_DAY * 7

    @classmethod
    def compute_second_per_period(cls, new_real_milliseconds_per_sim_second):

        """
        with sims4.reload.protected(globals()):
            # date_and_time.TICKS_PER_REAL_WORLD_SECOND = 1000
            date_and_time.REAL_MILLISECONDS_PER_SIM_SECOND = real_milliseconds_per_sim_second
        """

        real_milliseconds_per_sim_second = date_and_time.REAL_MILLISECONDS_PER_SIM_SECOND

        date_and_time.REAL_MILLISECONDS_PER_SIM_SECOND = new_real_milliseconds_per_sim_second
        ScheduleEntry.FACTORY_TUNABLES['start_time']._default = date_and_time.create_date_and_time(hours=9, minutes=0)

        absolute_ticks = services.server_clock_service().ticks()
        new_ticks = absolute_ticks * new_real_milliseconds_per_sim_second // real_milliseconds_per_sim_second

        if new_real_milliseconds_per_sim_second < real_milliseconds_per_sim_second:
            time_delta = date_and_time.TimeSpan(new_ticks - absolute_ticks)
            delta_seconds = time_delta.in_seconds()
            sims4.commands.execute(f'clock.advance_game_time 0 0 {delta_seconds}', None)

        sims4.commands.execute('clock._set_milliseconds_per_sim_second {0}'.format(new_real_milliseconds_per_sim_second),
                               None)

        if new_real_milliseconds_per_sim_second > real_milliseconds_per_sim_second:
            time_delta = date_and_time.TimeSpan(absolute_ticks - new_ticks)
            delta_seconds = time_delta.in_seconds()
            sims4.commands.execute(f'clock.advance_game_time 0 0 {delta_seconds}', None)
