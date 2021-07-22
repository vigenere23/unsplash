from src.config.config import Config
from src.config.config_repository_json import ConfigRepositoryJson


repo = ConfigRepositoryJson()


config = Config(
    resolution='1440x960',
    keyword='mountains'
)

repo.save(config)

config = repo.get()
print(config)
