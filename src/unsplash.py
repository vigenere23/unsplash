from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace, _SubParsersAction
from typing import Tuple

from client.resolution import ResolutionFactory
from commands.uninstall.uninstall_command_provider import UninstallCommandProvider
from commands.config.config_command import ConfigCommand
from commands.config.config_command_arguments import ConfigCommandArguments
from commands.config.config_repository_json import ConfigRepositoryJson
from commands.set.set_command_arguments import SetCommandArguments
from commands.save.save_command import SaveCommand
from commands.set.set_command_provider import SetCommandProvider


def register_set_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('set', help='Change the wallpaper')

    parser.add_argument('-r', '--resolution', type=str, help='Override default resolution')
    parser.add_argument('-k', '--keywords', type=str, nargs='*', help="Override kwywords selection")

    return parser


def register_save_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('save', help='Save the current wallpaper')

    return parser


def register_config_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('config', help='Get or set the current config')
    parser.add_argument('param', nargs='?', default=None, help='Config param to get or set (None = get all config)')
    parser.add_argument('--value', type=str, nargs='*', help='Value to set to the config parameter')

    return parser


def register_uninstall_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('uninstall', help='Uninstall this program')

    return parser


def parse_args() -> Tuple[ArgumentParser, Namespace]:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    command_parsers = parser.add_subparsers(dest='command')

    register_set_command(command_parsers)
    register_save_command(command_parsers)
    register_config_command(command_parsers)
    register_uninstall_command(command_parsers)

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()

    if args.command == 'set':
        command = SetCommandProvider(ConfigRepositoryJson()).provide()
        command.execute(SetCommandArguments(
            resolution=args.resolution,
            keywords=args.keywords
        ))

    elif args.command == 'save':
        command = SaveCommand()
        command.execute()

    elif args.command == 'config':
        command = ConfigCommand(ConfigRepositoryJson(), ResolutionFactory())

        if args.value:
            command_args = ConfigCommandArguments(
                set=True,
                resolution=args.value[0] if args.param == 'resolution' else None,
                keywords=args.value if args.param == 'keywords' else None
            )
        else:
            command_args = ConfigCommandArguments(set=False)

        command.execute(command_args)

    elif args.command == 'uninstall':
        command = UninstallCommandProvider().provide()
        command.execute()

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
