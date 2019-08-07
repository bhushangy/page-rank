import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY inbound DESC''')

count = 0
for row in cur :
    if count < 50 : print(row)
    count = count + 1
print(count, 'rows.')
cur.close()


# so output looks like
# (82, 2.5788339653690904, 2.580618446500859, 15, 'https://www.dr-chuck.com/csev-blog/author/drchuck')
# so 82 is basically the number of inbound links to the page given above
# An inbound link is a link coming from another site to your own website. 
# so in the html you see....bigger the circle for a page....that page has more inbound links maning more pages are reaching out to that page...
