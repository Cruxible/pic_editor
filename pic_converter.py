#!/usr/bin/env python3
import getpass
import platform
from rich.tree import Tree
from rich import print
from rich.console import Console
from PIL import Image
import os
import sys

class main_logo:
    def logo():
        print(" [red1]___  _   _ ____ ____\n |__]  \\_/  |__/ |__|\n |      |   |  \\ |  |[/red1]")

class HonerableMentions:
    old_filename = "\n Filename?"
    new_filename = "\n New filename?"
    save_pic_where = "\n Save on Desktop or Pictures?"
    exit_program = "\n Exiting the program"

class MySexyVariables:
    pics_dir = os.path.join(os.path.expanduser("~"), "Pictures")
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    desktop_list = os.listdir(desktop_dir)
    pics_list = os.listdir(pics_dir)
    calls_list = [
                "jpg to png",
                "webp to png",
                "exit"
                ]

class Input:
    @staticmethod
    def get_string_input():
        user = getpass.getuser()
        curdir = os.getcwd()
        console = Console()
        return console.input(" [white]_______________________________________________[/white]" + "[red]\n  __ [/red]" + "[white]" + curdir + " [/white]" + "[red]\n (__[/red]" + "[white]" + user + "[/white]" + "[red]__: [/red]")

class calls:
    @staticmethod
    def call_list():
        tree = Tree("[white]" + " Editing Tools", guide_style= "red")
        for i in MySexyVariables.calls_list:
            tree.add("[white]" + str(i))
        print(" ", tree)

    @staticmethod
    def picture_list_jpg():
        os.chdir(MySexyVariables.pics_dir)
        tree = Tree("[white]" + MySexyVariables.pics_dir, guide_style="red")
        for file in MySexyVariables.pics_list:
            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
                tree.add("[white]" + str(file))
        print(" ", tree)

    @staticmethod
    def picture_list_webp():
        os.chdir(MySexyVariables.pics_dir)
        tree = Tree("[white]" + MySexyVariables.pics_dir, guide_style="red")
        for file in MySexyVariables.pics_list:
            if file.lower().endswith('.webp'):
                tree.add("[white]" + str(file))
        print(" ", tree)

class main_functions:
    @staticmethod
    def get_pixel_size(image_file_path):
      img = Image.open(image_file_path)
      width, height = img.size
      return (width, height)


    @staticmethod
    def jpg_to_png():
        calls.picture_list_jpg()
        print(HonerableMentions.old_filename)
        jpg_name = Input.get_string_input()
        if jpg_name == 'exit':
            print(HonerableMentions.exit_program)
            sys.exit()
        elif jpg_name.lower().endswith('.jpg') or jpg_name.lower().endswith('.jpeg'):
            pixel_size = main_functions.get_pixel_size(f'{jpg_name}')
            print(f' Pixel size is: {pixel_size}')
            os.chdir(MySexyVariables.pics_dir)
            img = Image.open(jpg_name)
            print(HonerableMentions.new_filename)
            new_name = Input.get_string_input()
            if new_name.lower() == "exit":
                print(HonerableMentions.exit_program)
                sys.exit()
            elif new_name.lower().endswith('.png'):
                print(HonerableMentions.save_pic_where)
                save_dir = Input.get_string_input()
                if save_dir.lower() == "desktop":
                    os.chdir(MySexyVariables.desktop_dir)
                    img.save(new_name, 'PNG')
                elif save_dir.lower() == "pictures":
                    os.chdir(MySexyVariables.pics_dir)
                    img.save(new_name, 'PNG')
                elif save_dir.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                print(" Conversion finished")
            else:
                print(" New name must end in png")
                Main.main()
        else:
            print(" New name must end in jpg")
            Main.main()
    
    def webp_to_png():
        calls.picture_list_webp()
        print(HonerableMentions.old_filename)
        webp_name = Input.get_string_input()
        if webp_name == 'exit':
            print(HonerableMentions.exit_program)
            sys.exit()
        elif webp_name.lower().endswith('.webp'):
            pixel_size = main_functions.get_pixel_size(f'{webp_name}')
            print(f' Pixel size is: {pixel_size}')
            os.chdir(MySexyVariables.pics_dir)
            img = Image.open(webp_name)
            print(HonerableMentions.new_filename)
            new_name = Input.get_string_input()
            if new_name.lower() == "exit":
                print(HonerableMentions.exit_program)
                sys.exit()
            elif new_name.lower().endswith('.png'):
                print(HonerableMentions.save_pic_where)
                save_dir = Input.get_string_input()
                if save_dir.lower() == "desktop":
                    os.chdir(MySexyVariables.desktop_dir)
                    img.save(new_name, 'PNG')
                elif save_dir.lower() == "pictures":
                    os.chdir(MySexyVariables.pics_dir)
                    img.save(new_name, 'PNG')
                elif save_dir.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                print(" Conversion finished")
            else:
                print(" New name must end in png")
                Main.main()
        else:
            print(" New name must end in jpg")
            Main.main()

class Main:
    @staticmethod
    def main():
        while True:
            main_logo.logo()
            calls.call_list()
            command = Input.get_string_input()
            if command == MySexyVariables.calls_list[0]:
                main_functions.jpg_to_png()
            elif command == MySexyVariables.calls_list[1]:
                main_functions.webp_to_png()
            elif command == MySexyVariables.calls_list[2]:
                sys.exit()

if __name__ == '__main__':
    print(f" [white]System: {platform.system()}\n Node Name: {platform.node()}\n Release: {platform.release()}[/white]")
    print(f" [white]Version: {platform.version()}\n Machine: {platform.machine()}\n Python version: {platform.python_version()}[/white]")
    print(" [red1]All that we see or seem is but a dream within a dream\n ~ Edgar Allen Poe[/red1]")
    if platform.system() == 'Linux':
        Main.main()
