#!.venv/bin/python

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, Namespace, _SubParsersAction

from src.commands.set.set_command_arguments import SetCommandArguments
from src.commands.save.save_command import SaveCommand
from src.commands.set.set_command_provider import SetCommandProvider


def register_set_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('set', help='Change the wallpaper')

    return parser


def register_save_command(main_parser: _SubParsersAction) -> ArgumentParser:
    parser: ArgumentParser = main_parser.add_parser('save', help='Save the current wallpaper')

    return parser


def parse_args() -> Namespace:
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    command_parsers = parser.add_subparsers(dest='command')

    register_set_command(command_parsers)
    register_save_command(command_parsers)

    return parser.parse_args()


def run_command(args: Namespace) -> None:
    if args.command == 'set':
        command = SetCommandProvider().provide()
        # TODO send args instead
        command.execute(SetCommandArguments())

    if args.command == 'save':
        command = SaveCommand()
        command.execute()


def main():
    args = parse_args()
    run_command(args)


if __name__ == '__main__':
    main()
