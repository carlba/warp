import subprocess


def check_execute(*args):
    p = subprocess.Popen(args, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()

    if err:
        print err
    return out.rstrip()


def main():
    #print check_execute("ec", "calle")

    subprocess.check_call(["echo","calle"], stdin=None, stdout=None, stderr=None, shell=True)

if __name__ == '__main__':
    main()
