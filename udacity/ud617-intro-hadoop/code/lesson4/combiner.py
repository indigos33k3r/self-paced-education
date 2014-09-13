# Mapper

import sys

forummode = 0
usermode = 0

full_line = ""
for line in sys.stdin:
    if line.count("node_type", 0, len(line)) == 1:
        forummode = 1
        usermode = 0
        continue

    if line.count("user_ptr_id", 0, len(line)) == 1:
        forummode = 0
        usermode = 1
        continue

    if forummode == 1:
        full_line += line
        data = full_line.strip().split("\t")
        if len(data) == 19:
            # "author_id"   "clasif"    "id"  "title"  "tagnames"    "node_type"  "parent_id"  "abs_parent_id"  "added_at" "score"
            print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(data[3], "B", data[0], data[1], data[2], data[5], data[6], data[7], data[8], data[9])
            full_line = ""

    elif usermode == 1:
        data = line.strip().split("\t")
        # "id"  "clasif"    "reputation"  "gold"  "silver"  "bronze"
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(data[0], "A", data[1], data[2], data[3], data[4])

    else:
        print 'broken'
        
        
# Reducer

userinfo = None
currentuserid = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if data_mapped[1] == "A":
        # "id"  "clasif"    "reputation"  "gold"  "silver"  "bronze"
        userid, clasif, reputation, gold, silver, bronze = data_mapped
        currentuserid = userid
        userinfo = data_mapped

    elif data_mapped[1] == "B":
        # "author_id"   "clasif"    "id"  "title"  "tagnames"    "node_type"  "parent_id"  "abs_parent_id"  "added_at" "score"
        author_id, clasif, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data_mapped

        # "id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at" "score"  "reputation"  "gold"  "silver"  "bronze"
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, userinfo[2], userinfo[3], userinfo[4], userinfo[5])

    else:
        print "broken"