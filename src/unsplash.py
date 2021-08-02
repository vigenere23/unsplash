from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace, _SubParsersAction
from typing import Tuple

from client.resolution import ResolutionFactory
from commands.logs.logs_command import LogsCommand
from commands.upgrade.upgrade_command_provider import UpgradeCommandProvider
from commands.uninstall.uninstall_command_provider import UninstallCommandProvider
from commands.config.config_command import ConfigCommand
from commands.config.config_command_arguments import ConfigCommandArguments
from commands.config.config_repository_json import ConfigRepositoryJson
from commands.set.set_command_arguments import SetCommandArguments
from commands.save.save_command import SaveCommand
from commands.set.set_command_provider import SetCommandProvider


def register_set_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('set', help='Change the wallpaper')
    parser.add_argument('type', nargs='?', choices=['new', 'saved'])
    parser.add_argument('-r', '--resolution', type=str, help='Override default resolution')
    parser.add_argument('-k', '--keywords', type=str, nargs='*', help="Override kwywords selection")

    return parser


def register_save_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('save', help='Save the current wallpaper')

    return parser


def register_config_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('config', help='Get or set the current config')
    parser.add_argument('subcommand', choices=['get', 'set'])
    parser.add_argument('param', choices=['resolution', 'keywords', 'type'], help='Config param to get or set')
    parser.add_argument('value', nargs='*', help='Value to set to the config parameter')

    return parser


def register_uninstall_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('uninstall', help='Uninstall this program')

    return parser


def register_upgrade_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('upgrade', help='Upgrade/reinstall this program with latest version')

    return parser


def register_logs_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('logs', help='Show program logs')

    return parser


def parse_args() -> Tuple[ArgumentParser, Namespace]:
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        prog='unsplash')
    command_parsers = parser.add_subparsers(dest='command')

    register_set_command(command_parsers)
    register_save_command(command_parsers)
    register_config_command(command_parsers)
    register_uninstall_command(command_parsers)
    register_upgrade_command(command_parsers)
    register_logs_command(command_parsers)

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()

    if args.command == 'set':
        command = SetCommandProvider(ConfigRepositoryJson()).provide()
        command.execute(SetCommandArguments(
            type=args.type,
            resolution=args.resolution,
            keywords=args.keywords
        ))

    elif args.command == 'save':
        command = SaveCommand()
        command.execute()

    elif args.command == 'config':
        command = ConfigCommand(ConfigRepositoryJson(), ResolutionFactory())

        if args.subcommand == 'get':
            command.get(args.param)

        if args.subcommand == 'set':
            command_args = ConfigCommandArguments(
                resolution=args.value[0] if args.param == 'resolution' and len(args.value) > 0 else None,
                keywords=args.value if args.param == 'keywords' else None,
                type=args.value[0] if args.param == 'type' else None
            )
            command.set(command_args)

    elif args.command == 'uninstall':
        command = UninstallCommandProvider().provide()
        command.execute()

    elif args.command == 'upgrade':
        command = UpgradeCommandProvider().provide()
        command.execute()

    elif args.command == 'logs':
        command = LogsCommand()
        command.execute()

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
