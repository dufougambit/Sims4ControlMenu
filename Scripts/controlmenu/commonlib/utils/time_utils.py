"""
Control Menu is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
import date_and_time


class CMTimeUtils:
    EA_REAL_MILLISECONDS_PER_SIM_SECOND = 25
    EA_SECONDS_PER_MINUTE = 60
    EA_SECONDS_PER_HOUR = EA_SECONDS_PER_MINUTE * 60
    EA_SECONDS_PER_DAY = EA_SECONDS_PER_HOUR * 24
    EA_SECONDS_PER_WEEK = EA_SECONDS_PER_DAY * 7

    @classmethod
    def compute_second_per_period(cls, real_milliseconds_per_sim_second):
        ratio = cls.EA_REAL_MILLISECONDS_PER_SIM_SECOND / real_milliseconds_per_sim_second
        date_and_time.SECONDS_PER_MINUTE = cls.EA_SECONDS_PER_MINUTE // ratio
        date_and_time.SECONDS_PER_HOUR = cls.EA_SECONDS_PER_HOUR // ratio
        date_and_time.SECONDS_PER_DAY = cls.EA_SECONDS_PER_DAY // ratio
        date_and_time.SECONDS_PER_WEEK = cls.EA_SECONDS_PER_WEEK // ratio

