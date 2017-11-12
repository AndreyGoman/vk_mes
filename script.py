# -*- coding: utf-8 -*-

import vk_api, getpass

def main():
    login = input("Введите логин\n")
    pas = getpass.getpass("Введите пароль\n")

    vk_session = vk_api.VkApi(login,pas)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    
    vk = vk_session.get_api()

    response = vk.friends.get(fields="last_name")


    if response['items']:
        for x in range(0,len(response['items'])-1):
            print(response['items'][x]['last_name'])

    response2 = vk.messages.get()

    if response2['items']:
        for y in range(0, len(response2["items"])-1):
            print(response2['items'][y])

if __name__ == '__main__':
    main()
