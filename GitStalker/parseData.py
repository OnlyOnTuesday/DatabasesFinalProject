import subprocess
import fileinput
from GitStalker.models import Commits, User, WorksOn

def pretty_log(files_list):
    args = ['bash', './log.sh']
    for i in range(0, len(files_list)):
        args.append(files_list[i])

    subprocess.call(args)
    return


def extract_data(files_list):
    for line in fileinput.input(files=files_list):
        vals = line.split(',')
        if 7 == len(vals):
            if not is_user_added(vals[3]):
                new_entry = User(authorname = vals[2], authoremail = vals[3])
                new_entry.save()
            if not works_on_added(vals[3], fileinput.filename()):
                new_entry = WorksOn(authoremail = vals[3], reponame = fileinput.filename())
                new_entry.save()
            if not is_commit_added(vals[0], vals[3]):
                new_entry = Commits(commithash = vals[0],
                                    authoremail = vals[3],
                                    parenthash = vals[1],
                                    datetime = vals[4],
                                    body = vals[6],
                                    subject = vals[5])
                new_entry.save()
            return


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

            
# import subprocess
# import fileinput
# import sqlite3

"""
TODO: 
extract_data(...) has a problem with carriage returns in the logged data.
My hack to fix this has been to ignore lines that are not the correct length, 
but this does leave some data missing at times.
"""

# def extract_data(files_list):
#     """Takes a file name, opens it, extracts its data, and adds it to the db"""
#     con = sqlite3.connect("wm.db")
#     cur = con.cursor()
    
#     for line in fileinput.input(files=files_list):
#         vals = line.split(",")
#         if 7 == len(vals):
#             if not is_user_added(cur, vals[3]):
#                 cur.execute("insert into USER values (?, ?)", [vals[2], vals[3]])
            
#             if not works_on_added(cur, vals[3], fileinput.filename()):
#                 cur.execute("insert into WORKS_ON values (?, ?)", [vals[3], fileinput.filename()])
            
#             if not is_commit_added(cur, vals[0], vals[3]):
#                 cur.execute("insert into COMMITS values (?, ?, ?, ?, ?, ?)",
#                             [vals[0], vals[3], vals[1], vals[4], vals[6], vals[5]])
            

#     # close the fileinput and database 
#     fileinput.close()
#     con.commit()
#     con.close()
#     return

# def is_user_added(cursor, email):
#     """Check if a user is already in this table"""
#     cursor.execute("select * from user where authoremail = ?", [email])
#     if len(cursor.fetchall()) == 0:
#         return False
#     else:
#         return True

# def works_on_added(cursor, email, repo):
#     """Check if a user is already in this table and associated with a specific repo"""
#     cursor.execute("select * from works_on where authoremail = ? and reponame = ? ", [email, repo])
#     if len(cursor.fetchall()) == 0:
#         return False
#     else:
#         return True

# def is_commit_added(cursor, commit_hash, email):
#     """Check if a commit is already in this table"""
#     cursor.execute("select * from commits where authoremail = ? and commithash = ?", [email, commit_hash])
#     if len(cursor.fetchall()) == 0:
#         return False
#     else:
#         return True
    
