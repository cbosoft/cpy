import subprocess as sp

class ShellError(Exception):
    '''error executing command in shell'''

def runsh(command):

    if isinstance(command, list):
        for subcommand in command:
            runsh(subcommand)
        return

    pr = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    if pr.wait():
        so = pr.stdout.read().decode().split('\n')
        se = pr.stderr.read().decode().split('\n')
        raise ShellError(f'Error in execution of "{command}":\n\n{so}\n\n{se}')
    return
