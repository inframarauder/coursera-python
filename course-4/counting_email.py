import sqlite3

conn = sqlite3.connect('database/emaildb.sqlite')
curr = conn.cursor()

# initial cleanup of DB and creating the table:
curr.executescript('''
    drop table if exists Counts;
    create table Counts(
        org TEXT,
        count INTEGER
    );
''')

# open file:
fp = open('files/mbox.txt')
for line in fp:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]
    domain = email.split('@')[1]
    org = domain.split('.')[0]

    curr.execute('select count from Counts where org = ?', (org,))
    row = curr.fetchone()
    if row is None:
        curr.execute('insert into Counts (org,count) values (?,1)', (org,))
    else:
        curr.execute(
            'update Counts set count = count + 1 where org = ?', (org,))

conn.commit()

# print the top organizational count:
curr.execute('select org,count from Counts order by count desc')
print(curr.fetchone())

curr.close()
