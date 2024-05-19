#!/usr/bin/python3
"""
This code provides a way to interact with a powerful storage system using a command-line interface.

It defines a class named HBNBCommand that lets you use commands to manage data.
This code allows you to easily switch between different storage methods (like files or databases) without changing the core functionality.
You can use this tool to:
Define the structure of your data (create a data model)
Manage your data through commands (create, update, delete, etc.)
Save your data to a file (JSON format) for persistence
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class."""

    intro = "Welcome to the HBNB command interpreter. Type 'help' for a list of commands.\n"
    prompt = "(hbnb) "

    def do_quit(self, inp):
        """Quit the command interpreter."""
        print("Exiting HBNB command interpreter.")
        exit()

    def emptyline(self):
        """Handle empty lines by passing control."""
        pass  # Do nothing for empty lines

    def do_help(self, inp):
        """Get help on commands."""
        print("Type 'help <command>' to get specific help on a command.")
        print("Available commands:")
        super().do_help(inp)  # Inherit help from cmd module for other commands

if __name__ == '__main__':
    HBNBCommand().cmdloop()
