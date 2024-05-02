from file_manager import FileManager
from command_parser import CommandParser
import config

workdir = config.WORKDIR
file_manager = FileManager(workdir)
parser = CommandParser(file_manager)
while True:
    command = input(f"{file_manager.workdir}> ")
    parser.parse_command(command)