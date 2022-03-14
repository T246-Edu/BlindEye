from subprocess import check_call


def shutdown():
    check_call(['sudo', 'poweroff'])
