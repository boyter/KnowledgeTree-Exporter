import MySQLdb
import os
import shutil

# KnowledgeTree default place to store documents

ktdocument = '/var/www/ktdms/Documents/'

conn = MySQLdb.connect(user='', passwd='',db='', charset="utf8", use_unicode=True)
cursor = conn.cursor()

# global variables FTW

cursor.execute('''select id, parent_id, name from folders;''')
allfolders = cursor.fetchall()

cursor.execute('''select id, folder_id from documents;''')
alldocuments = cursor.fetchall()

cursor.execute('''select document_id, filename, storage_path from document_content_version;''')
document_locations = cursor.fetchall()


# create folder tree which matches whatever the database suggests exists

def create_folder_tree(parent_id, path):
    directories = [x for x in allfolders if x[1] == parent_id]
    for directory in directories:
        d = '.%s/%s/' % (path, directory[2])

        print d
        os.makedirs(d)
        # get all the files that belong in this directory

        for document in [x for x in alldocuments if x[1] == directory[0]]:
            try:
                location = [x for x in document_locations if document[0] == x[0]][0]
                print 'copy %s%s %s%s' % (ktdocument, location[2], d, location[1])
                shutil.copy2('%s%s' % (ktdocument, location[2]), '%s%s' % (d, location[1]))
            except:
                 print 'ERROR exporting - Usually due to a linked document.'

        create_folder_tree(parent_id=directory[0], path='%s/%s' % (path, directory[2]))

create_folder_tree(parent_id=1, path='')
