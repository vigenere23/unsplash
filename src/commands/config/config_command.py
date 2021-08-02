from client.resolution import ResolutionFactory
from commands.set.set_command_arguments import SetCommandType
from commands.config.config_command_arguments import ConfigCommandArguments
from commands.config.config_repository import ConfigRepository


class ConfigCommand:
    def __init__(self, config_repo: ConfigRepository, resolution_factory: ResolutionFactory):
        self.__config_repo = config_repo
        self.__resolution_factory = resolution_factory

    def get(self, param: str):
        config = self.__config_repo.get()
        print(config[param])

    def set(self, args: ConfigCommandArguments):
        config = self.__config_repo.get()

        if args.resolution:
            config.resolution = self.__resolution_factory.create(args.resolution).print()

        if args.type:
            config.type = SetCommandType.parse(args.type).print()

        if args.keywords:
            if not isinstance(args.keywords, list) or len(args.keywords) == 0:
                raise ValueError("keywords should be a list of strings")

            config.keywords = args.keywords

        self.__config_repo.save(config)
