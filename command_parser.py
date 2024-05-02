class CommandParser:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def parse_command(self, user_command):
        command_parts = user_command.split()
        if command_parts:
            command = command_parts[0]
            args = command_parts[1:]
            if hasattr(self.file_manager, command):
                func = getattr(self.file_manager, command)
                func(*args)
            else:
                print("Неизвестная команда")