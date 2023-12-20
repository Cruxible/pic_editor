#!/usr/bin/env python3
#Creator: Ioannes Cruxibulum
#Created on: Dec 19, 2023
import getpass
import platform
from rich.tree import Tree
from rich import print
from rich.console import Console
import moviepy.editor as mpy
import moviepy.video.fx.all as vfx
from PIL import Image, ImageEnhance
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
                "png to jpg",
                "webp to png",
                "check size",
                "resize image",
                "filters",
                "exit"
                ]
    filter_list = [
                "greyscale",
                "saturation",
                "contrast",
                "brightness",
                "negative"
                ]

class Input:
    @staticmethod
    def get_string_input():
        user = getpass.getuser()
        curdir = os.getcwd()
        console = Console()
        return console.input(" [white]_______________________________________________[/white]" + "[red]\n  __ [/red]" + "[white]" + curdir + " [/white]" + "[red]\n (__[/red]" + "[white]" + user + "[/white]" + "[red]__: [/red]")

    @staticmethod
    def get_integer_input():
        user = getpass.getuser()
        curdir = os.getcwd()
        console = Console()
        return int(console.input(" [white]_______________________________________________[/white]" + "[red]\n  __ [/red]" + "[white]" + curdir + " [/white]" + "[red]\n (__[/red]" + "[white]" + user + "[/white]" + "[red]__: [/red]"))

    @staticmethod
    def get_float_input():
        user = getpass.getuser()
        curdir = os.getcwd()
        console = Console()
        return float(console.input(" [white]_______________________________________________[/white]" + "[red]\n  __ [/red]" + "[white]" + curdir + " [/white]" + "[red]\n (__[/red]" + "[white]" + user + "[/white]" + "[red]__: [/red]"))


class calls:
    @staticmethod
    def call_list():
        tree = Tree("[white]" + " Editing Tools", guide_style= "red")
        for i in MySexyVariables.calls_list:
            tree.add("[white]" + str(i))
        print(" ", tree)

    @staticmethod
    def list_filters():
        tree = Tree("[white]" + " Image Filters", guide_style= "red")
        for i in MySexyVariables.filter_list:
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

    @staticmethod
    def picture_list_png():
        os.chdir(MySexyVariables.pics_dir)
        tree = Tree("[white]" + MySexyVariables.pics_dir, guide_style="red")
        for file in MySexyVariables.pics_list:
            if file.lower().endswith('.png'):
                tree.add("[white]" + str(file))
        print(" ", tree)

    @staticmethod
    def picture_list():
        os.chdir(MySexyVariables.pics_dir)
        tree = Tree("[white]" + MySexyVariables.pics_dir, guide_style="red")
        for file in MySexyVariables.pics_list:
            if file.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
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
    
    def png_to_jpg():
        calls.picture_list_png()
        print(HonerableMentions.old_filename)
        png_name = Input.get_string_input()
        if png_name == 'exit':
            print(HonerableMentions.exit_program)
            sys.exit()
        elif png_name.lower().endswith('.png'):
            pixel_size = main_functions.get_pixel_size(f'{png_name}')
            print(f' Pixel size is: {pixel_size}')
            os.chdir(MySexyVariables.pics_dir)
            img = Image.open(png_name)
            # Convert the image to RGB
            rgb_img = img.convert('RGB')
            print(HonerableMentions.new_filename)
            new_name = Input.get_string_input()
            if new_name.lower() == "exit":
                print(HonerableMentions.exit_program)
                sys.exit()
            elif new_name.lower().endswith('.jpg'):
                print(HonerableMentions.save_pic_where)
                save_dir = Input.get_string_input()
                if save_dir.lower() == "desktop":
                    os.chdir(MySexyVariables.desktop_dir)
                    rgb_img.save(new_name, 'JPEG')
                elif save_dir.lower() == "pictures":
                    os.chdir(MySexyVariables.pics_dir)
                    rgb_img.save(new_name, 'JPEG')
                elif save_dir.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                print(" Conversion finished")
            else:
                print(" New name must end in jpg")
                Main.main()
        else:
            print(" File name must end in png")
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
            # Convert webp to rgb mode
            img = img.convert("RGB")
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

    def get_size():
        calls.picture_list()
        print(HonerableMentions.old_filename)
        pic_name = Input.get_string_input()
        if pic_name == 'exit':
            print(HonerableMentions.exit_program)
            sys.exit()
        elif pic_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
            pixel_size = main_functions.get_pixel_size(f'{pic_name}')
            os.chdir(MySexyVariables.pics_dir)
            main_functions.get_pixel_size(pic_name)
            print(f' Pixel size is: {pixel_size}')
        else:
            print(" Please choose a file.")

    def resize_image():
        calls.picture_list()
        print(HonerableMentions.old_filename)
        pic_name = Input.get_string_input()
        if pic_name == 'exit':
            print(HonerableMentions.exit_program)
            sys.exit()
        elif pic_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
            print(' 1080 or 720 format?')
            pic_format = Input.get_string_input()
            if pic_format == 'exit':
                print(HonerableMentions.exit_program)
                sys.exit()
            elif pic_format == '720':
                original_image = Image.open(pic_name)
                width, height = original_image.size
                new_width = 1280
                new_height = 720
                resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
                print(HonerableMentions.new_filename)
                new_name = Input.get_string_input()
                if new_name.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                elif new_name:
                    print(HonerableMentions.save_pic_where)
                    save_dir = Input.get_string_input()
                    if save_dir.lower() == "desktop":
                        os.chdir(MySexyVariables.desktop_dir)
                        print(f"The original image size is {width} wide x {height} tall")
                        print(f"The resized image size is {new_width} wide x {new_height} tall")
                        resized_image.show()
                        resized_image.save(new_name)
                    elif save_dir.lower() == "pictures":
                        os.chdir(MySexyVariables.pics_dir)
                        print(f"The original image size is {width} wide x {height} tall")
                        print(f"The resized image size is {new_width} wide x {new_height} tall")
                        resized_image.show()
                        resized_image.save(new_name)
                    elif save_dir.lower() == "exit":
                        print(HonerableMentions.exit_program)
                        sys.exit()
                    print(" Resize Finished")
                else:
                    print(' not a valide format')
            
            elif pic_format == '1080':
                original_image = Image.open(pic_name)
                width, height = original_image.size
                new_width = 1920
                new_height = 1080
                resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
                print(HonerableMentions.new_filename)
                new_name = Input.get_string_input()
                if new_name.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                elif new_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                    print(HonerableMentions.save_pic_where)
                    save_dir = Input.get_string_input()
                    if save_dir.lower() == "desktop":
                        os.chdir(MySexyVariables.desktop_dir)
                        print(f"The original image size is {width} wide x {height} tall")
                        print(f"The resized image size is {new_width} wide x {new_height} tall")
                        resized_image.show()
                        resized_image.save(new_name)
                    elif save_dir.lower() == "pictures":
                        os.chdir(MySexyVariables.pics_dir)
                        print(f"The original image size is {width} wide x {height} tall")
                        print(f"The resized image size is {new_width} wide x {new_height} tall")
                        resized_image.show()
                        resized_image.save(new_name)
                    elif save_dir.lower() == "exit":
                        print(HonerableMentions.exit_program)
                        sys.exit()
                    print(" Resize Finished.")
                else:
                    print(' Not a valide format.')

    def pic_filters():
        calls.list_filters()
        print(' Enter a filter option.')
        filter_command = Input.get_string_input()
        if filter_command == 'exit':
            print(HonerableMentions.exit_program)
            sys.exit()
        elif filter_command == 'greyscale':
            calls.picture_list()
            print(HonerableMentions.old_filename)
            image_path = Input.get_string_input()
            if image_path == 'exit':
                print(HonerableMentions.exit_program)
                sys.exit()
            elif image_path.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                print(HonerableMentions.new_filename)
                new_name = Input.get_string_input()
                if new_name.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                elif new_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                    clip = mpy.ImageClip(image_path)
                    grey_clip = clip.fx(vfx.blackwhite)
                    print(HonerableMentions.save_pic_where)
                    save_dir = Input.get_string_input()
                    if save_dir.lower() == "desktop":
                        os.chdir(MySexyVariables.desktop_dir)
                        grey_clip.save_frame(new_name)
                        print(" Filter Applied")
                    elif save_dir.lower() == "pictures":
                        os.chdir(MySexyVariables.pics_dir)
                        grey_clip.save_frame(new_name)
                        print(" Filter Applied")
                    else:
                        print(' Not a valid directory.')
                else:
                    print(' New filename must end in:\n .jpeg, .jpg, .png, .webp.')
            else:
                print(' Filename must end in:\n .jpeg, .jpg, .png, .webp.')
        
        elif filter_command == 'saturation':
            calls.picture_list()
            print(HonerableMentions.old_filename)
            image_path = Input.get_string_input()
            if image_path == 'exit':
                print(HonerableMentions.exit_program)
                sys.exit()
            elif image_path.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                print(' Enter above 1 for more color\n less than 1 for less color\n Example: .75 or 1.5')
                multiplier = Input.get_float_input()
                print(HonerableMentions.new_filename)
                new_name = Input.get_string_input()
                if new_name.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                elif new_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                    clip = mpy.ImageClip(image_path)
                    color_adjusted_clip = clip.fx(vfx.colorx, multiplier)
                    print(HonerableMentions.save_pic_where)
                    save_dir = Input.get_string_input()
                    if save_dir.lower() == "desktop":
                        os.chdir(MySexyVariables.desktop_dir)
                        color_adjusted_clip.save_frame(new_name)
                        print(" Filter Applied")
                    elif save_dir.lower() == "pictures":
                        os.chdir(MySexyVariables.pics_dir)
                        color_adjusted_clip.save_frame(new_name)
                        print(" Filter Applied")
                    else:
                        print(' Not a valid directory.')
                else:
                    print(' New filename must end in:\n .jpeg, .jpg, .png, .webp.')
            else:
                print(' Filename must end in:\n .jpeg, .jpg, .png, .webp.')
        
        elif filter_command == 'contrast':
            calls.picture_list()
            print(HonerableMentions.old_filename)
            image_path = Input.get_string_input()
            if image_path == 'exit':
                print(HonerableMentions.exit_program)
                sys.exit()
            elif image_path.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                print(' Enter above 1 for more color\n less than 1 for less color\n Example: .75 or 1.5')
                lum = Input.get_float_input()  # Get luminance value from user input
                print(' Enter above 1 for more color\n less than 1 for less color\n Example: .75 or 1.5')
                contrast = Input.get_float_input()  # Get contrast value from user input
                clip = mpy.ImageClip(image_path)
                contrast_adjusted_clip = clip.fx(vfx.lum_contrast, lum=lum, contrast=contrast)
                print(HonerableMentions.new_filename)
                new_name = Input.get_string_input()
                if new_name.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                elif new_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                    print(HonerableMentions.save_pic_where)
                    save_dir = Input.get_string_input()
                    if save_dir.lower() == "desktop":
                        os.chdir(MySexyVariables.desktop_dir)
                        contrast_adjusted_clip.save_frame(new_name)
                        print(" Filter Applied")
                    elif save_dir.lower() == "pictures":
                        os.chdir(MySexyVariables.pics_dir)
                        contrast_adjusted_clip.save_frame(new_name)
                        print(" Filter Applied")
                    else:
                        print(' Not a valid directory.')
                else:
                    print(' New filename must end in:\n .jpeg, .jpg, .png, .webp.')
            else:
                print(' Filename must end in:\n .jpeg, .jpg, .png, .webp.')
        
        elif filter_command == 'brightness':
            calls.picture_list()
            print(HonerableMentions.old_filename)
            image_path = Input.get_string_input()
            if image_path == 'exit':
                print(HonerableMentions.exit_program)
                sys.exit()
            elif image_path.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                print(' Enter above 1 for more brightness\n less than 1 for less brightness\n Example: .75 or 1.5')
                brightness_factor = Input.get_float_input()  # Get brightness factor from user input
                image = Image.open(image_path)
                enhancer = ImageEnhance.Brightness(image)
                brightness_adjusted_image = enhancer.enhance(brightness_factor)
                print(HonerableMentions.new_filename)
                new_name = Input.get_string_input()
                if new_name.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                elif new_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                    print(HonerableMentions.save_pic_where)
                    save_dir = Input.get_string_input()
                    if save_dir.lower() == "desktop":
                        os.chdir(MySexyVariables.desktop_dir)
                        brightness_adjusted_image.save(new_name)
                        print(" Filter Applied")
                    elif save_dir.lower() == "pictures":
                        os.chdir(MySexyVariables.pics_dir)
                        brightness_adjusted_image.save(new_name)
                        print(" Filter Applied")
                    else:
                        print(' Not a valid directory.')
                else:
                    print(' New filename must end in:\n .jpeg, .jpg, .png, .webp.')
            else:
                print(' Filename must end in:\n .jpeg, .jpg, .png, .webp.')

        elif filter_command == 'negative':
            calls.picture_list()
            print(HonerableMentions.old_filename)
            image_path = Input.get_string_input()
            if image_path == 'exit':
                print(HonerableMentions.exit_program)
                sys.exit()
            elif image_path.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                clip = mpy.ImageClip(image_path)
                inverted_clip = clip.fx(vfx.invert_colors)
                print(HonerableMentions.new_filename)
                new_name = Input.get_string_input()
                if new_name.lower() == "exit":
                    print(HonerableMentions.exit_program)
                    sys.exit()
                elif new_name.lower().endswith(('.webp', '.png', 'jpg', 'jpeg')):
                    print(HonerableMentions.save_pic_where)
                    save_dir = Input.get_string_input()
                    if save_dir.lower() == "desktop":
                        os.chdir(MySexyVariables.desktop_dir)
                        inverted_clip.save_frame(new_name)
                        print(" Filter Applied")
                    elif save_dir.lower() == "pictures":
                        os.chdir(MySexyVariables.pics_dir)
                        inverted_clip.save_frame(new_name)
                        print(" Filter Applied")
                    else:
                        print(' Not a valid directory.')
                else:
                    print(' New filename must end in:\n .jpeg, .jpg, .png, .webp.')
            else:
                print(' Filename must end in:\n .jpeg, .jpg, .png, .webp.')
        else:
            print(' Not a valid filter.')

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
                main_functions.png_to_jpg()
            elif command == MySexyVariables.calls_list[2]:
                main_functions.webp_to_png()
            elif command == MySexyVariables.calls_list[3]:
                main_functions.get_size()
            elif command == MySexyVariables.calls_list[4]:
                main_functions.resize_image()
            elif command == MySexyVariables.calls_list[5]:
                main_functions.pic_filters()
            elif command == MySexyVariables.calls_list[6]:
                sys.exit()

if __name__ == '__main__':
    print(f" [white]System: {platform.system()}\n Node Name: {platform.node()}\n Release: {platform.release()}[/white]")
    print(f" [white]Version: {platform.version()}\n Machine: {platform.machine()}\n Python version: {platform.python_version()}[/white]")
    print(" [red1]All that we see or seem is but a dream within a dream\n ~ Edgar Allen Poe[/red1]")
    if platform.system() == 'Linux':
        Main.main()
