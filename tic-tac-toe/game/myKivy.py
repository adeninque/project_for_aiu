import time
from random import randint
from kivy.app import App

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '620')
Config.set('graphics', 'resizable', 0)

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class TicTacToeApp(App):

    defoult_size = [.9, .9]
    defoult_btn_color = [0.01, 0.69, 0.53, 1]
    x_color = [1, 0, 0, 1]
    o_color = [0, 0, 1, 1]

    mainAL = AnchorLayout(anchor_x = 'center', anchor_y = 'center')

    game_field = []
    player_1 = [Label(text = '', color = [1, 0, 0, 1], font_size = 36), '', 0]
    player_2 = [Label(text = '', color = [1, 1, 1, 1], font_size = 36), '', 0]

    gnv_p2_input_name = TextInput(hint_text = 'Player 2',
        halign = 'center',
        font_size = 48,
        background_color = [1, 1, 1, 1])
    gnv_p1_input_name = TextInput(hint_text = 'Player 1',
        halign = 'center',
        font_size = 48,
        background_color = [1, 1, 1, 1])

    new_game = False
    possible_to_put = True
    tern = 1
    game = 0

    pc_playing = False
    pc_puts = False

    def put_x_o(self):
        if self.game == 0:
            self.player_1[1] = 'X'
            self.player_2[1] = 'O'
            self.player_1[0].color = [1, 0, 0, 1]
            self.player_2[0].color = [1, 1, 1, 1]
        elif self.game == 1:
            self.player_1[1] = 'O'
            self.player_2[1] = 'X'
            self.player_1[0].color = [1, 1, 1, 1]
            self.player_2[0].color = [1, 0, 0, 1]
        print('player 1', self.player_1[1])
        print('player 2', self.player_2[1])
        print('tern', self.tern)
    
# View Part
    def main_menu(self):

        print('main menu called')

        self.mainAL.clear_widgets()

        self.mm_gl = GridLayout(cols = 1, size_hint = [.6, .6], spacing = 5)

        self.mm_gl.add_widget(Label(text = 'Tic Tac Toe',
            font_size = 36))
        self.mm_gl.add_widget(Button(text = '2P Game',
            background_color = self.defoult_btn_color,
            on_press = self.get_name_view,
            background_normal = ''))
        self.mm_gl.add_widget(Button(text = 'Play with PC',
            background_color = self.defoult_btn_color,
            on_press = self.play_with_pc,
            background_normal = ''))

        self.mainAL.add_widget(self.mm_gl)



    def get_name_view(self, instance):
        self.pc_playing = False


        print('get_name_view called')

        self.mainAL.clear_widgets()

        self.gnv_name_input_gl = GridLayout(cols = 1, size_hint = self.defoult_size, spacing = 5)

        self.gnv_name_input_gl.add_widget(self.gnv_p1_input_name)
        self.gnv_name_input_gl.add_widget(self.gnv_p2_input_name)

        self.gnv_name_input_gl.add_widget(Button(text = 'SUBMIT',
        background_color = self.defoult_btn_color, on_press = self.start_game,
        on_release = self.put_names,
        background_normal = '',
        font_size = 36))

        self.mainAL.add_widget(self.gnv_name_input_gl)


    def start_game(self, instance):
        
        self.mainAL.clear_widgets()

        self.sg_x_o_gl = GridLayout(cols = 3, spacing = 5)
        self.sg_names_gl = GridLayout(cols = 2, spacing = 5, size_hint = [1, .1], padding = [20, 20, 20, 20])
        self.sg_wrapper_gl = GridLayout(cols = 1, size_hint = self.defoult_size, spacing = 5)

        defoult_place_color = [1, 1, 1, 8]

        for i in range(3):
            self.game_field.append([Button(text = '',
                background_color = defoult_place_color,
                background_normal = '',
                on_press = self.put_in_place,
                font_size = 46,
                color = [0, 0, 0, 0]) for j in range(3)])
        
        for r in self.game_field:
            for c in r:
                self.sg_x_o_gl.add_widget(c)

        self.sg_names_gl.add_widget(self.player_1[0])
        self.sg_names_gl.add_widget(self.player_2[0])

        self.sg_wrapper_gl.add_widget(self.sg_names_gl)
        self.sg_wrapper_gl.add_widget(self.sg_x_o_gl)

        self.mainAL.add_widget(self.sg_wrapper_gl)

        if self.pc_playing:
            if self.game == 1:
                self.pc_terns()

    def play_with_pc(self, instance):

        self.pc_playing = True

        self.gnv_p1_input_name.text = 'YOU'
        self.gnv_p2_input_name.text = 'PC'

        self.put_names('ins')

        self.start_game('ins')

    
    def game_end(self, winner):

        self.mainAL.clear_widgets()

        gl = GridLayout(cols = 1, size_hint = self.defoult_size, spacing = 5)

        if winner == 'Drew':
            gl.add_widget(Label(text = 'Drew !', font_size = 46))
        else:
            gl.add_widget(Label(text = f'Winner is {winner} !', font_size = 46))

        gl.add_widget(Button(text = 'Play again',
            background_color = self.defoult_btn_color,
            on_press = self.play_again,
            background_normal = '',))
        gl.add_widget(Button(text = 'New game',
            background_color = self.defoult_btn_color,
            on_press = self.start_new_game,
            background_normal = ''))

        self.mainAL.add_widget(gl)

        self.tern = 0
        print('tern by end', self.tern)
    

    def play_again(self, instance):
        
        self.reset_start_game()

        if self.game == 0:
            self.game = 1
            self.put_x_o()
        elif self.game == 1:
            self.game = 0
            self.put_x_o()
        
        self.tern = 1


        self.start_game('a')
    

    def start_new_game(self, instance):
        
        self.reset_start_game()
        self.reset_get_name()
        self.reset_main_menu()
        self.game = 0
        self.tern = 1
        self.pc_playing = False
        self.pc_puts = False
        self.put_x_o()

        self.main_menu()

#----------------------------


#Logic Part
    def put_in_place(self, instance):
        if self.tern >= 9:
            self.game_end('Drew')

        if self.possible_to_put:

            if instance.text == 'X' or instance.text == 'O':
                print('Not possible to put')
            else:
                print('tern :', self.tern)
                if self.game == 0:
                    if self.tern % 2 != 0:
                        instance.text = self.player_1[1]
                        print(f'player puted {self.player_1[1]}')
                        instance.color = self.x_color
                    else:
                        instance.text = self.player_2[1]
                        print(f'player puted {self.player_2[1]}')
                        instance.color = self.o_color
                elif self.game == 1:
                    if self.tern % 2 != 0:
                        instance.text = self.player_2[1]
                        print(f'player puted {self.player_2[1]}')
                        instance.color = self.x_color
                    else:
                        instance.text = self.player_1[1]
                        print(f'player puted {self.player_1[1]}')
                        instance.color = self.o_color
                    
                self.if_wins()

                self.tern += 1

                self.pc_puts = True
        
        if self.pc_playing:
            self.pc_terns()

    def if_wins(self):

        winning = self.winning_check()

        if winning[0]:
            if self.game == 0:
                if self.tern % 2 == 0:
                    winner = self.player_2[0].text
                else:
                    winner = self.player_1[0].text
            else:
                if self.tern % 2 == 0:
                    winner = self.player_1[0].text
                else:
                    winner = self.player_2[0].text
            
            for i in winning[1]:
                self.game_field[i[0]][i[1]].background_color = [0, 0, 1, 1]
            self.game_end(winner)

        print('color change worked')
        if self.game == 0:
            if self.tern % 2 == 0:
                self.player_1[0].color = [1, 0, 0, 1]
                self.player_2[0].color = [1, 1, 1, 1]
            else:
                self.player_1[0].color = [1, 1, 1, 1]
                self.player_2[0].color = [1, 0, 0, 1]
        else:
            if self.tern % 2 == 0:
                self.player_1[0].color = [1, 1, 1, 1]
                self.player_2[0].color = [1, 0, 0, 1]
            else:
                self.player_1[0].color = [1, 0, 0, 1]
                self.player_2[0].color = [1, 1, 1, 1]
        
    def winning_check(self, vX = 'XXX', vO = 'OOO'):

        lens = len(self.game_field)
        sequ = ''
        pos = []

        #hoorizantal check
        for r in range(lens):
            for c in range(lens):
                sequ += self.game_field[r][c].text
                pos.append([r, c])
            if sequ == f'{vX}' or sequ == f'{vO}':
                print('#hoorizantal check +')
                return [True, pos]
            sequ = ''
            pos = []

        #vertical check
        for r in range(lens):
            for c in range(lens):
                sequ += self.game_field[c][r].text
                pos.append([c, r])
            if sequ == f'{vX}' or sequ == f'{vO}':
                print('#vertical check +')
                return [True, pos]
            sequ = ''
            pos = []
        
        #cross \ check
        for i in range(lens):
            sequ += self.game_field[i][i].text
            pos.append([i, i])
        if sequ == f'{vX}' or sequ == f'{vO}':
            print('#cross \\ check +')
            return [True, pos]
        sequ = ''
        pos = []

        #cross / check
        for i in range(lens):
            sequ += self.game_field[i][(lens - 1) - i].text
            pos.append([i, (lens - 1) - i])
        if sequ == f'{vX}' or sequ == f'{vO}':
            print('#cross / check +')
            return [True, pos]
        sequ = ''
        pos = []

        return [False]
        

    def put_names(self, instance):

        self.player_1[0].text = ''
        self.player_1[0].text = ''
        self.player_1[0].text = self.gnv_p1_input_name.text
        self.player_2[0].text = self.gnv_p2_input_name.text

    def pc_terns(self):
        print('PC Terned')
        trying = 0
        while True:
            randR, randC = randint(0, 2), randint(0, 2)
            if self.game_field[randR][randC].text != 'X' and self.game_field[randR][randC].text != 'O':
                self.game_field[randR][randC].text = self.player_2[1]
                if self.player_2[1] == 'X':
                    self.game_field[randR][randC].color = self.x_color
                else:
                    self.game_field[randR][randC].color = self.o_color
                self.if_wins()
                self.tern += 1
                print('tern :', self.tern)
                break
            else:
                trying += 1
                if trying == 9:
                    self.game_end('Drew')
                    break
        time.sleep(randint(3, 9) / 10)
        
#----------------------------
# Resets

    def reset_start_game(self):
        self.game_field = []
        self.sg_x_o_gl.clear_widgets()
        self.sg_names_gl.clear_widgets()
        self.sg_wrapper_gl.clear_widgets()
    
    def reset_get_name(self):
        self.gnv_p1_input_name.text = ''
        self.gnv_p2_input_name.text = ''
        if not(self.pc_playing):
            self.gnv_name_input_gl.clear_widgets()
    
    def reset_main_menu(self):
        self.mm_gl

#----------------------------
#Build Function
    def build(self):
        
        self.put_x_o()

        self.title = 'Tic Tac Toe'

        self.main_menu()

        return self.mainAL
#----------------------------
if __name__ == '__main__':
    TicTacToeApp().run()