#!.venv/bin/python

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace, _SubParsersAction

from src.commands.config.config_command import ConfigCommand
from src.commands.config.config_command_arguments import ConfigCommandArguments
from src.commands.config.config_repository_json import ConfigRepositoryJson
from src.commands.set.set_command_arguments import SetCommandArguments
from src.commands.save.save_command import SaveCommand
from src.commands.set.set_command_provider import SetCommandProvider


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


def parse_args() -> Namespace:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    command_parsers = parser.add_subparsers(dest='command')

    register_set_command(command_parsers)
    register_save_command(command_parsers)
    register_config_command(command_parsers)

    return parser.parse_args()


def run_command(args: Namespace) -> None:
    if args.command == 'set':
        command = SetCommandProvider(ConfigRepositoryJson()).provide()
        command.execute(SetCommandArguments(
            resolution=args.resolution,
            keywords=args.keywords
        ))

    if args.command == 'save':
        command = SaveCommand()
        command.execute()

    if args.command == 'config':
        command = ConfigCommand(ConfigRepositoryJson())

        if args.value:
            command_args = ConfigCommandArguments(
                set=True,
                resolution=args.value[0] if args.param == 'resolution' else None,
                keywords=args.value if args.param == 'keywords' else None
            )
        else:
            command_args = ConfigCommandArguments(set=False)

        command.execute(command_args)


def main():
    args = parse_args()
    run_command(args)


if __name__ == '__main__':
    main()
