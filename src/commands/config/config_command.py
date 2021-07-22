from src.commands.config.config_command_arguments import ConfigCommandArguments
from src.commands.config.config_repository import ConfigRepository


class ConfigCommand:
    def __init__(self, config_repo: ConfigRepository):
        self.__config_repo = config_repo

    def execute(self, args: ConfigCommandArguments):
        config = self.__config_repo.get()

        if not args.set:
            print(config)
            return

        if args.resolution:
            config.resolution = args.resolution

        if args.keywords:
            config.keywords = args.keywords

        self.__config_repo.save(config)
        print(config)
