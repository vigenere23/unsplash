from commands.command_executor import CommandExecutor
from commands.executor_macos import ExecutorMacOS


class ExecutorProvider:
    def provide(self) -> CommandExecutor:
        return ExecutorMacOS()
