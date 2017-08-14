import psycopg2
import datetime

# Commands for postgresql
# pop_art to find popular articles
pop_art = """select A.title, count(*) as views from log L left join articles A
            on substring(L.path,10)=A.slug group by A.title
            order by views desc limit 5 offset 1;"""
# pop_auth to find popular authors
pop_auth = """select A.name, count(*) as veiws from articles R join authors A
            on R.author = A.id join log L  on R.slug = substring(L.path,10)
            group by A.name order by veiws desc;"""
# error_rep to find error report
error_rep = """select * from(select time::timestamp::date,count(*) as all,
            cast(sum(case when status like '404%' then 1 else 0 end)
            as float)*100/cast(count(*) as float) as error from log
            group by time::timestamp::date order by error desc) as subtab
            where error>1.0;"""

# Created a conn object by connecting to database
conn = psycopg2.connect("dbname=news")
# Created a cur object from cursor class
cur = conn.cursor()

# cur execute the command to find popular articles
cur.execute(pop_art)
# cur fetch all result stored it in articles list
articles = cur.fetchall()
# \033[1;36m to make the statement colored
print ("\033[1;36m\nThree most popular articles are:\033[1;m\n")
# A loop to print each result from the articles list
for article in articles:
    print(article[0] + " - " + str(article[1]) + " views")

# cur execute the command to find popular authors
cur.execute(pop_auth)
# cur fetch all result stored it in authors list
authors = cur.fetchall()
# \033[1;36m to make the statement colored
print ("\033[1;36m\nMost popular article authors are:\033[1;m\n")
# A loop to print each result from the authors list
for author in authors:
    print(author[0] + " - " + str(author[1]) + " views")

# cur execute the command to find days error occured more than 1%
cur.execute(error_rep)
# cur fetch all result stored it in errors list
errors = cur.fetchall()
# \033[1;36m to make the statement colored
print ("""\033[1;36m\nList of days that did more than 1% of request lead
       to errors:\033[1;m\n""")
# A loop to print each result from the errors list
for error in errors:
    print(error[0].strftime("%B %d,%Y") + " - " + "%.2f" % (error[2]) +
          "% errors\n")

# cur closed
cur.close()
# conn closed
conn.close()
