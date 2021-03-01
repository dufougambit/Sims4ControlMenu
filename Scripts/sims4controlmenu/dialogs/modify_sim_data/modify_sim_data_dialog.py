"""
The Sims 4 Control Menu is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from typing import Callable
from sims4controlmenu.commonlib.dialogs.option_dialogs.common_choose_button_option_dialog import \
    CommonChooseButtonOptionDialog
from sims4controlmenu.commonlib.dialogs.option_dialogs.options.common_dialog_button_option import \
    CommonDialogButtonOption
from sims4controlmenu.commonlib.dialogs.option_dialogs.options.common_dialog_response_option_context import \
    CommonDialogResponseOptionContext
from sims4controlmenu.dialogs.modify_sim_data.enums.string_identifiers import S4CMSimControlMenuStringId
from sims4controlmenu.dialogs.modify_sim_data.modify_occult.modify_occult_dialog import S4CMModifyOccultDialog
from sims4controlmenu.dialogs.modify_sim_data.control_dialog_base import S4CMSimControlDialogBase
from sims4controlmenu.enums.string_identifiers import S4CMStringId


class S4CMModifySimDataDialog(S4CMSimControlDialogBase):
    """ The control dialog for Sims. """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 's4cm_modify_sim_data_dialog'

    # noinspection PyMissingOrEmptyDocstring
    @property
    def title(self) -> int:
        return S4CMStringId.MODIFY_SIM_DATA

    def _setup_dialog(
        self,
        option_dialog: CommonChooseButtonOptionDialog,
        on_close: Callable[[], None],
        on_previous: Callable[[], None],
        reopen: Callable[[], None]
    ) -> bool:
        option_dialog.add_option(
            CommonDialogButtonOption(
                'ModifyOccult',
                None,
                CommonDialogResponseOptionContext(
                    S4CMSimControlMenuStringId.MODIFY_OCCULT,
                ),
                on_chosen=lambda *_, **__: S4CMModifyOccultDialog(self._sim_info, on_previous=reopen).open()
            )
        )
        return True
