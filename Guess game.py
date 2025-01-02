import random as rd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.clock import Clock
import time as tm

Window.size = (600, 1000) # a window
Window.clearcolor = "white" # set color white
Window._set_window_pos(1000, 50) # set position of the window on the desktop



# Window._set_window_pos(1200, 40)
# Window.set_system_cursor("arrow")
# Window.borderless = False


class IWH(App):
    def build(self): # building an app
        self.title = "IWH GAME" # setting the title
        my_buttons_color = "#0568FC" # setting overall buttons color variable


        self.left_empty = "D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\left empty.jpg" # a variable with an image
        self.right_empty = "D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\right empty.jpg" # a variable with an image


        self.left_gem = "D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\left gem.jpg" # a variable with an image
        self.right_gem = "D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\right gem.jpg" # a variable with an image

        self.no_gussed_counter = 0 # counters for the game
        self.gussed_counter = 0
        self.game_started = 0 # to check, if the game is already going, to prevent multiple calls for the random_pick funcs

        self.rights_reserved = f"FreeWind Interactive © {tm.gmtime()[0]} All rights reserved" # Companies logo


        main_box_layout = BoxLayout(orientation="vertical") # overall layout, that contains other layouts

        upper_layout = BoxLayout(orientation="horizontal", spacing=2, padding=2, size_hint=(1, 0.2)) # a layout for upper buttons

        middle_layout = BoxLayout(orientation="horizontal", spacing=2, padding=2) # a layout for middle part, consists buttons, for images of hands, that are used in the game

        checkbox_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.2)) # a layout for the checkbox parts

        main_box_layout.add_widget(upper_layout) # add this and the two below layouts into the main layout
        main_box_layout.add_widget(middle_layout)
        main_box_layout.add_widget(checkbox_layout)

        # the button below is for you quessed counter
        self.button_guessed = Button(text="You guessed : " + str(self.gussed_counter),
        font_size=30, color="white", outline_width=2, outline_color="blue", background_color=my_buttons_color,
        font_name="C:\\Windows\\Fonts\\Times")

        self.button_guessed.bind(on_press = self.clear_guessed) # bind the button above to -clear_guessed- func

        # the button below is for you missed counter
        self.button_missed = Button(text="You missed : " + str(self.no_gussed_counter),
        font_size=30, color="white", outline_width=1, outline_color="green", background_color=my_buttons_color,
        font_name="C:\\Windows\\Fonts\\Times")

        self.button_missed.bind(on_press = self.clear_missed) # bind the button above to -clear_missed- func

        # adding these two buttons to the upper layout
        upper_layout.add_widget(self.button_guessed)
        upper_layout.add_widget(self.button_missed)

        self.button_right_hand = Button(background_normal = "D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\right_closed.jpg")

        self.button_left_hand = Button(background_normal="D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\left_closed.jpg")

        middle_layout.add_widget(self.button_right_hand)
        middle_layout.add_widget(self.button_left_hand)

        self.checkbox_auto_restart = CheckBox(color="blue")

        self.label = Label(text= "AUTO RESTART", bold = False, color="black", font_size=30, outline_width=2,
        outline_color="white", disabled_color="grey", font_name="C:\\Windows\\Fonts\\Times")

        checkbox_layout.add_widget(self.checkbox_auto_restart)
        checkbox_layout.add_widget(self.label)

        self.restart_button = Button(text="RESTART", size_hint=(1, 0.2), font_size=45, outline_width=2,
        outline_color="palegreen", color="blue", background_color=my_buttons_color, font_name="C:\\Windows\\Fonts\\Times")

        self.restart_button.bind(on_press = self.restore)

        main_box_layout.add_widget(self.restart_button)

        self.button_left_hand.bind(on_press = self.call_left)
        self.button_right_hand.bind(on_press = self.call_right)

        self.company = Label(text = self.rights_reserved, font_size = 14, color="black", size_hint=(1, 0.050))

        main_box_layout.add_widget(self.company)

        return main_box_layout

    # _______________________________________________________________ *** FUNCTIONS *** _________________________________________________________________
    def clear_guessed(self, v):
        self.gussed_counter = 0
        self.button_guessed.text = "You guessed : " + str(self.gussed_counter)

    def clear_missed(self, v):
        self.no_gussed_counter = 0
        self.button_missed.text = "You no guessed : " + str(self.no_gussed_counter)

    def call_left(self, v):
        if not self.game_started:
            Clock.schedule_once(callback = self.random_pick_left, timeout = 1)
            self.game_started = 1

    def call_right(self, v):
        if not self.game_started:
            Clock.schedule_once(callback = self.random_pick_right, timeout = 1)
            self.game_started = 1

    def random_pick_left(self, v):
        correct_answer = rd.choice(["left", "right"])
        if correct_answer == "left":
            self.button_left_hand.background_normal = self.left_gem
            self.button_right_hand.background_normal = self.right_empty
            self.gussed_counter += 1
            self.button_guessed.text = "You guessed : " + str(self.gussed_counter)
        else:
            self.button_left_hand.background_normal = self.left_empty
            self.button_right_hand.background_normal = self.right_gem
            self.no_gussed_counter += 1
            self.button_missed.text = "You no guessed : " + str(self.no_gussed_counter)
        if not self.checkbox_auto_restart.active:
            pass
        if self.checkbox_auto_restart.active:
            Clock.schedule_once(callback=self.restore, timeout=2)

    def random_pick_right(self, v):
        correct_answer = rd.choice(["left", "right"])
        if correct_answer == "right":
            self.button_left_hand.background_normal = self.left_empty
            self.button_right_hand.background_normal = self.right_gem
            self.gussed_counter += 1
            self.button_guessed.text = "You guessed : " + str(self.gussed_counter)
        else:
            self.button_left_hand.background_normal = self.left_gem
            self.button_right_hand.background_normal = self.right_empty
            self.no_gussed_counter += 1
            self.button_missed.text = "You no guessed : " + str(self.no_gussed_counter)
        if not self.checkbox_auto_restart.active:
            pass
        if self.checkbox_auto_restart.active:
            Clock.schedule_once(callback=self.restore, timeout=2)

    def restore(self, *args):
        self.game_started = 0
        self.button_right_hand.background_normal = "D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\right_closed.jpg"
        self.button_left_hand.background_normal = "D:\\Python\\MyPyCharmProjects\\Guess_game\\edited\\left_closed.jpg"





if __name__ == '__main__':
    IWH().run()



