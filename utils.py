import config, os, json


def locate_setting_folder():
    """check local folder and global setting folder for setting.cfg file"""
    # look for previous setting file
    try:
        if 'setting.cfg' in os.listdir(config.current_directory):
            return config.current_directory
    except:
        pass

    # no setting file found will check local folder for writing permission, otherwise will return global sett folder
    try:
        folder = config.current_directory
        with open(os.path.join(folder, 'test'), 'w') as test_file:
            test_file.write('0')
        os.unlink(os.path.join(folder, 'test'))
        return config.current_directory

    except PermissionError:
        log("No enough permission to store setting at local folder:", folder)


config.sett_folder = locate_setting_folder()


def to_command_paras(username, password):
    str_paras = ""
    str_paras += ' -u ' + username
    str_paras += ' -p ' + password
    return str_paras


def load_setting():
    settings = {}
    try:
        log('Load Application setting from', config.sett_folder)
        file = os.path.join(config.sett_folder, 'setting.cfg')
        with open(file, 'r') as f:
            settings = json.load(f)

    except FileNotFoundError:
        log('setting.cfg not found')
    except Exception as e:
        handle_exceptions(e)
    finally:
        if not isinstance(settings, dict):
            settings = {}

        # update config module
        config.__dict__.update(settings)


def save_setting():
    settings = {key: config.__dict__.get(key) for key in config.settings_keys}

    try:
        file = os.path.join(config.sett_folder, 'setting.cfg')
        with open(file, 'w') as f:
            json.dump(settings, f)
            log('setting saved')
    except Exception as e:
        log('save_setting() > error', e)


def handle_exceptions(error):
    if config.TEST_MODE:
        raise error
    else:
        log(error)


def log(*args, start='>> ', end='\n', sep=' '):
    """
    print messages to stdout and log widget in main menu thru main window queue
    :param args: comma separated messages to be printed
    :param start: prefix appended to start of string
    :param end: tail of string
    :param sep: separator used to join text "args"
    :return:
    """

    text = ''
    for arg in args:
        text += str(arg)
        text += sep
    text = text[:-1]  # remove last space, or sep
    text = start + text

    print(text, end=end)
