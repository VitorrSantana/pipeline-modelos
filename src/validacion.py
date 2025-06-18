def validacion_format(text, type_file):

    if len(text) > 3 and type_file in text:
        return True
    else:
        return False
