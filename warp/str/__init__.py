def str_eval(val):
    import distutils.util
    import ast

    def strtobool(val):
        return bool(distutils.util.strtobool(val))

    operations = [ast.literal_eval, strtobool]

    for operation in operations:
        try:
            return_string = operation(val)
            break
        except (ValueError, SyntaxError) as e:
            continue

    else:
        return_string = val
    return return_string