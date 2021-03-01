"""
The Sims 4 Control Menu is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from pprint import pformat

import sims4.commands
from typing import Any, Union, Callable, Iterator

from protocolbuffers.Localization_pb2 import LocalizedString
from sims.sim_info import SimInfo
from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.mod_support.mod_identity import CommonModIdentity
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.utils.common_function_utils import CommonFunctionUtils
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4controlmenu.commonlib.dialogs.common_choose_response_dialog import CommonChooseResponseDialog
from sims4controlmenu.commonlib.dialogs.option_dialogs.common_choose_response_option_dialog import \
    CommonChooseResponseOptionDialog
from sims4controlmenu.commonlib.dialogs.option_dialogs.options.common_dialog_button_option import \
    CommonDialogButtonOption
from sims4controlmenu.commonlib.dialogs.option_dialogs.options.common_dialog_response_option_context import \
    CommonDialogResponseOptionContext
from ui.ui_dialog import UiDialogBase, UiDialogOption


class CommonChooseButtonOptionDialog(CommonChooseResponseOptionDialog):
    """CommonChooseButtonOptionDialog(\
        mod_identity,\
        title_identifier,\
        description_identifier,\
        title_tokens=(),\
        description_tokens=(),\
        on_previous=CommonFunctionUtils.noop\
        on_previous=CommonFunctionUtils.noop,\
        on_close=CommonFunctionUtils.noop\
    )

    A dialog that displays a list of options.

    .. note:: To see an example dialog, run the command :class:`s4clib_testing.show_choose_button_option_dialog` in the in-game console.

    :Example usage:

    .. highlight:: python
    .. code-block:: python

        def _on_option_chosen(option_identifier: DialogOptionIdentifierType, choice: DialogOptionValueType):
            pass

        def _on_previous_chosen() -> None:
            pass

        def _on_close() -> None:
            pass

        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
                text_color=CommonLocalizedStringColor.GREEN
            ),
        )
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                CommonStringId.TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME,
                tokens=(CommonSimUtils.get_active_sim_info(),),
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        option_dialog = CommonChooseButtonOptionDialog(
            ModInfo.get_identity(),
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            on_previous=_on_previous_chosen,
            on_close=_on_close
        )

        # We add the options, in this case we have three options.
        option_dialog.add_option(
            CommonDialogButtonOption(
                'Option 1',
                'Value 1',
                CommonDialogResponseOptionContext(
                    CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
                    subtext_identifier=CommonStringId.TESTING_TEST_BUTTON_ONE
                ),
                on_chosen=_on_option_chosen
            )
        )

        option_dialog.add_option(
            CommonDialogButtonOption(
                'Option 2',
                'Value 2',
                CommonDialogResponseOptionContext(
                    CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
                    subtext_identifier=CommonStringId.TESTING_TEST_BUTTON_TWO,
                ),
                on_chosen=_on_option_chosen
            )
        )

        option_dialog.add_option(
            CommonDialogButtonOption(
                'Option 3',
                'Value 3',
                CommonDialogResponseOptionContext(
                    CommonLocalizationUtils.create_localized_string('Value 3'),
                    subtext_identifier=CommonStringId.TESTING_TEST_BUTTON_TWO
                ),
                on_chosen=_on_option_chosen
            )
        )

        option_dialog.show(
            sim_info=CommonSimUtils.get_active_sim_info()
        )

    :param mod_identity: The identity of the mod creating the dialog. See :class:`.CommonModIdentity` for more information.
    :type mod_identity: CommonModIdentity
    :param title_identifier: A decimal identifier of the title text.
    :type title_identifier: Union[int, str, LocalizedString, CommonStringId]
    :param description_identifier: A decimal identifier of the description text.
    :type description_identifier: Union[int, str, LocalizedString, CommonStringId]
    :param title_tokens: An iterable of Tokens to format into the title. Default is an empty collection.
    :type title_tokens: Iterator[Any], optional
    :param description_tokens: An iterable of Tokens to format into the description. Default is an empty collection.
    :type description_tokens: Iterator[Any], optional
    :param include_previous_button: If True, the Previous button will be appended to the end of the dialog. Default is True.
    :type include_previous_button: bool, optional
    :param on_previous: A callback invoked upon the the Previous option being chosen. Default is CommonFunctionUtils.noop.
    :type on_previous: Callable[[], None], optional
    :param on_close: A callback invoked upon the dialog closing. Default is CommonFunctionUtils.noop.
    :type on_close: Callable[[], None], optional
    """

    # noinspection PyMissingOrEmptyDocstring
    @property
    def log_identifier(self) -> str:
        return 's4cl_choose_button_option_dialog'

    def __init__(
        self,
        mod_identity: CommonModIdentity,
        title_identifier: Union[int, str, LocalizedString, CommonStringId],
        description_identifier: Union[int, str, LocalizedString, CommonStringId],
        title_tokens: Iterator[Any]=(),
        description_tokens: Iterator[Any]=(),
        include_previous_button: bool=True,
        on_previous: Callable[[], None]=CommonFunctionUtils.noop,
        on_close: Callable[[], None]=CommonFunctionUtils.noop
    ):
        super().__init__(
            CommonChooseResponseDialog(
                mod_identity,
                title_identifier,
                description_identifier,
                tuple(),
                title_tokens=title_tokens,
                description_tokens=description_tokens
            ),
            include_previous_button=include_previous_button,
            on_previous=on_previous,
            on_close=on_close
        )

    def add_option(self, option: CommonDialogButtonOption):
        """add_option(option)

        Add an option to the dialog.

        :param option: The option to add.
        :type option: CommonDialogObjectOption
        """
        return super().add_option(option)

    def _add_response(self, option: CommonDialogButtonOption):
        self._internal_dialog.add_response(option.as_response(len(self._options)))

    def show(
        self,
        dialog_options: UiDialogOption=0,
        sim_info: SimInfo=None
    ):
        """show(\
            dialog_options=0,\
            sim_info=None\
        )

        Show the dialog and invoke the callbacks upon the player making a choice.

        :param dialog_options: Options to apply to the dialog, such as removing the close button. Default is no options.
        :type dialog_options: UiDialogOption, optional
        :param sim_info: The SimInfo of the Sim that will appear in the dialog image. The default Sim is the active Sim. Default is None.
        :type sim_info: SimInfo, optional
        """
        return super().show(
            dialog_options=dialog_options,
            sim_info=sim_info
        )

    def build_dialog(
        self,
        dialog_options: UiDialogOption=0,
        sim_info: SimInfo=None
    ) -> Union[UiDialogBase, None]:
        """build_dialog(\
            dialog_options=0,\
            sim_info=None\
        )

        Build the dialog and invoke the callbacks upon the player making a choice.

        :param dialog_options: Options to apply to the dialog, such as removing the close button. Default is no options.
        :type dialog_options: UiDialogOption, optional
        :param sim_info: The SimInfo of the Sim that will appear in the dialog image. The default Sim is the active Sim. Default is None.
        :type sim_info: SimInfo, optional
        :return: The built dialog or None if a problem occurs.
        :rtype: Union[UiDialogBase, None]
        """
        return super().build_dialog(
            dialog_options=dialog_options,
            sim_info=sim_info
        )


@sims4.commands.Command('s4clib_testing.show_choose_button_option_dialog', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_choose_button_option_dialog(_connection: int=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test choose button option dialog.')

    def _on_option_chosen(option_identifier: str, choice: str):
        output('Chose option {} with value: {}.'.format(pformat(option_identifier), pformat(choice)))

    def _on_previous_chosen() -> None:
        output('Chose previous option.')

    def _on_close() -> None:
        output('Closed dialog.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
                text_color=CommonLocalizedStringColor.GREEN
            ),
        )
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                CommonStringId.TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME,
                tokens=(CommonSimUtils.get_active_sim_info(),),
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        option_dialog = CommonChooseButtonOptionDialog(
            ModInfo.get_identity(),
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            on_previous=_on_previous_chosen,
            on_close=_on_close
        )

        option_dialog.add_option(
            CommonDialogButtonOption(
                'Option 1',
                'Value 1',
                CommonDialogResponseOptionContext(
                    CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
                    subtext_identifier=CommonStringId.TESTING_TEST_BUTTON_ONE
                ),
                on_chosen=_on_option_chosen
            )
        )

        option_dialog.add_option(
            CommonDialogButtonOption(
                'Option 2',
                'Value 2',
                CommonDialogResponseOptionContext(
                    CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
                    subtext_identifier=CommonStringId.TESTING_TEST_BUTTON_TWO,
                ),
                on_chosen=_on_option_chosen
            )
        )

        option_dialog.add_option(
            CommonDialogButtonOption(
                'Option 3',
                'Value 3',
                CommonDialogResponseOptionContext(
                    CommonLocalizationUtils.create_localized_string('Value 3'),
                    subtext_identifier=CommonStringId.TESTING_TEST_BUTTON_TWO
                ),
                on_chosen=_on_option_chosen
            )
        )

        option_dialog.show(
            sim_info=CommonSimUtils.get_active_sim_info()
        )
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show dialog, please locate your exception log file.')
    output('Done showing.')
