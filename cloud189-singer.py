#!/usr/bin/env python
import PySimpleGUI as sg
import utils
import checkin
from threading import Thread
import shlex
import config


def Cloud189SignGUI():
    utils.load_setting()
    sg.theme(config.DEFAULT_THEME)
    layout = [
        [sg.Text('Cloud189 Signer', size=(40, 1), font=('Any 15'))],
        [sg.T('账号,多个账号用#号分割:', font=config.default_font), sg.Input(default_text=config.username, size=(40, 1), key='username')],
        [sg.T('密码,多个密码用#号分割:', font=config.default_font), sg.Input(default_text=config.password, size=(40, 1), key='password')],
        [sg.Button('签到', key='Sign')],
        [sg.Output(size=(90, 20), font=config.default_font)],
        [sg.Button('退出', key='Exit', button_color=('white', 'firebrick3'))]
    ]

    window = sg.Window('天翼云签到', layout,
                       text_justification='r',
                       default_element_size=(15, 1),
                       font=('Any 14'))

    while True:
        event, values = window.read()
        if event in ('Exit', None):
            utils.save_setting()
            break           # exit button clicked
        if event == 'Sign':
            window.refresh()
            username = values['username']
            password = values['password']
            err = False
            if username == "":
                err = True
                print("账号不能为空!")

            if password == "":
                err = True
                print("密码不能为空!")
            if not err:
                user_list = username.split("#")
                pass_list = password.split("#")
                if len(user_list) != len(pass_list):
                    print("账号和密码个数不对应!")
                else:
                    config.username = username
                    config.password = password
                    print('开始签到....')
                    try:
                        for i in range(len(user_list)):
                            str_paras = utils.to_command_paras(user_list[i], pass_list[i])
                            thread_download = Thread(target=checkin.main, args=[
                                shlex.split(str_paras)])
                            thread_download.start()
                    except Exception as e:
                        print(e)
    window.close()


if __name__ == '__main__':
    Cloud189SignGUI()