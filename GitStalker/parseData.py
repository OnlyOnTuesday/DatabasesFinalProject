import subprocess
import fileinput
from pathlib import Path
from GitStalker.models import Commits, User, WorksOn, Repo

"""
TODO: 
extract_data(...) has a problem with carriage returns in the logged data.
My hack to fix this has been to ignore lines that are not the correct length, 
but this does leave some data missing at times.

This takes way too long to run when it's putting all the data in for the first time.
It runs fine when there's little-to-nothing to do, but it took at least 30 minutes 
when it just needed to add commits.  I think there's a faster way to look up the 
references to other table objects that could help.
"""

def parse_database():
    print("START")
    base_path = "/home/user1/OU/Semester5/CS4620/FinalProject/WMs/"
    files = (base_path + "awesome/", base_path + "dwm/", base_path + "i3/",
             base_path + "qtile/", base_path + "spectrwm/", base_path + "stumpwm/",
             base_path + "xmonad/")

    # parseData.pretty_log(files)
    pretty_log(files)
    print("LOGGED")

    base_path = "/home/user1/OU/Semester5/CS4620/FinalProject/Django/"
    files = (base_path + "awesome.txt", base_path + "dwm.txt", base_path + "i3.txt",
             base_path + "qtile.txt", base_path + "spectrwm.txt", base_path + "stumpwm.txt",
             base_path + "xmonad.txt")
    
    # parseData.extract_data(files)
    print("EXTRACTING")
    extract_data(files)
    print("EXTRACTED")

    return


def pretty_log(files_list):
    base_path = "/home/user1/OU/Semester5/CS4620/FinalProject/Django/GitStalker/"
    args = ['bash', base_path + 'log.sh']
    for i in range(0, len(files_list)):
        args.append(files_list[i])

    subprocess.call(args)
    return


# Vals: 0: Commit Hash, 1: Parent Hash, 2: author name, 3: author email, 
# 4: author date, 5: subject, 6: body
def extract_data(files_list):
    for line in fileinput.input(files=files_list):
        print(fileinput.filename())
        print(fileinput.lineno())
        vals = line.split(',')
        if 7 == len(vals):
            print("LENGTH")
            if not is_user_added(vals[3]):
                new_entry = User(authorname = vals[2], authoremail = vals[3])
                new_entry.save()
                print("SAVED 1")
            path = Path('.').parent.absolute().as_posix()
            filename = fileinput.filename()
            filename = filename[len(path) + 1 : len(filename) - 4]
            print("WORKING")
            if not works_on_added(vals[3], filename):
                auth_email = User.objects.get(authoremail = vals[3])
                repo_name = Repo.objects.get(reponame = filename)
                new_entry = WorksOn(authoremail = auth_email, reponame = repo_name)
                new_entry.save()
            if not is_commit_added(vals[0], vals[3]):
                auth_email = User.objects.get(authoremail = vals[3])
                new_entry = Commits(commithash = vals[0],
                                    authoremail = auth_email,
                                    parenthash = vals[1],
                                    datetime = vals[4],
                                    body = vals[6],
                                    subject = vals[5])
                new_entry.save()



def is_user_added(email):
    added = User.objects.filter(authoremail = email)
    if 0 == len(added):
        return False
    else:
        return True
    
def works_on_added(email, repo):
    added = WorksOn.objects.filter(authoremail = email, reponame = repo)
    if 0 == len(added):
        return False
    else:
        return True

def is_commit_added(commith, email):
    added = Commits.objects.filter(authoremail = email, commithash = commith)
    if 0 == len(added):
        return False
    else:
        return True

