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
from sims4communitylib.logging import vanilla_logging
from controlmenu.logging.has_cm_log import HasCMLog
from sims4communitylib.utils.common_time_utils import CommonTimeUtils

class CMTimeUtils(HasCMLog):
    EA_REAL_MILLISECONDS_PER_SIM_SECOND = 25
    EA_SECONDS_PER_MINUTE = 60
    EA_SECONDS_PER_HOUR = EA_SECONDS_PER_MINUTE * 60
    EA_SECONDS_PER_DAY = EA_SECONDS_PER_HOUR * 24
    EA_SECONDS_PER_WEEK = EA_SECONDS_PER_DAY * 7

    # noinspection PyMissingOrEmptyDocstring
    @property
    def log_identifier(self) -> str:
        return 'cm_time_utils'

    def adjust_game_clock(self, real_milliseconds_per_sim_second, new_real_milliseconds_per_sim_second):
        self.log.enable()

        #sims4.commands.execute(f'clock.setspeed zero', None)

        self.log.info(f"Changing 'real milliseconds per sim second' from {real_milliseconds_per_sim_second} "
                      f"to {new_real_milliseconds_per_sim_second}.")

        '''actual_date = services.game_clock_service().now()
        #absolute_clicks = actual.absolute_ticks()
        if new_real_milliseconds_per_sim_second < real_milliseconds_per_sim_second:
            self._adjust_date_in_the_futur(actual_date, real_milliseconds_per_sim_second,
                                           new_real_milliseconds_per_sim_second)'''

        self.log.info(f"Executing 'clock._set_milliseconds_per_sim_second {new_real_milliseconds_per_sim_second}'"
                      f" command.")
        sims4.commands.execute(f'clock._set_milliseconds_per_sim_second {new_real_milliseconds_per_sim_second}', None)

        '''if new_real_milliseconds_per_sim_second > real_milliseconds_per_sim_second:
            self.log.info(f"Executing 'clock.set_game_clock {actual_date.absolute_ticks()}'  command.")
            sims4.commands.execute(f'clock.set_game_clock {actual_date.absolute_ticks()}', None)'''

    '''
    def _adjust_date_in_the_futur(self, actual_date: date_and_time, real_milliseconds_per_sim_second,
                                  new_real_milliseconds_per_sim_second):
        base_ticks = actual_date.absolute_ticks()
        new_ticks = int(base_ticks * new_real_milliseconds_per_sim_second / real_milliseconds_per_sim_second)
        self.log.info(f"Going from {base_ticks} clicks to {new_ticks} clicks")
        delta_clicks = abs(new_ticks - base_ticks)
        delta_seconds = int(date_and_time.TimeSpan(delta_clicks).in_seconds())

        actual_date_in_second = actual_date.absolute_seconds()

        self.log.info(f"Executing 'clock.set_game_clock {base_ticks + delta_clicks}'  command.")
        #CommonTimeUtils.set_current_time(0, 0, delta_seconds + actual_date_in_second)
        sims4.commands.execute(f'clock.set_game_clock {base_ticks + delta_clicks}', None)
    '''
