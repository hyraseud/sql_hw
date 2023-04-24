import sys


#TODO: Write your username and answer to each query as a string in the return statements 
# in the functions below. Do not change the function names. 

# Write your queries using multi-line strings and use proper indentation to increase readability

#Make sure to test that python prints out the strings correctly.

#usage: python HW6_Neo4j.py

def username():
	return "username"

def query5():
    return """
            match (user:User)-[:Wrote]-(post_heading:Post)-[:CategorizedAs]-(category:Category)
            where category.name = "Other"
            return user.name as user, post_heading.heading as post_heading, category.name as category
           """ 

def query6():
    return """
           match (user:User)-[:Wrote]-(post_heading:Post)-[:CategorizedAs]-(category:Category)
           where category.name = "Celebration" or category.name = "Travel"
           return user.name as user, post_heading.heading as post_heading, category.name as category
           """ 

def query7():
    return """
           match (user:User)-[a:Rated|Commented]-(post_heading:Post)
           where post_heading.heading = "Trip to Indy"
           return user.name as user, type(a) AS rated_or_commented, post_heading.heading as post_heading
           """ 


def query8():
    return """
            match (u:User)-[:Wrote]->(p:Post)<-[:Rated]-(u2:User), (u2)-[:Follows]->(u)
            return u2.name as user_rated, p.heading as post_heading, u.name as user_posted
           """ 


def query9():
    return """
            match(p:Post)<-[r:Rated]-(u:User)
            with p.heading as post_heading, avg(r.rating) as average
            where average >= 3.5
            return post_heading, average
           """ 


def query10():
    return """
            match(n:Location)-[]-(p:Post)-[]-(c:Category)
            with n.name as location, c.name as category
            return location, category, count(*) as post_count
           """ 


def query11():
    return """
           match(n:Location)-[]-(p:Post)<-[r:Rated]-(u:User), (p)-[:CategorizedAs]-(c:Category)
           with n.name as location, c.name as category, count(c.name) as post_count, r.rating as rating
           where rating = 5 return location, category, count(*) as post_count
           """ 


def query12():
    return """
        match (p2:Post)
        optional match (u:User)-[c:Commented]-(p:Post)
        where p2 = p
        with p2.heading as post_heading, count(c) as commented_count, p2 as p2
        match (p3:Post)
        optional match (u2:User)-[r:Rated]-(p4:Post)
        where p4 = p3 and p4 = p2
        with post_heading, count(r) as rated_count, commented_count
        return post_heading, rated_count, commented_count
           """ 


def query13():
    return """
            match (u:User)-[:Wrote]->(p:Post),(p)-[f:PostedFrom]-(l:Location)
            match (u2:User)-[r:Rated]-(p)
            where l.name = "Chicago" and r.rating = 5
            return u.name as user, count (*) as `5-star_ratings_for_posts_written_by_the_user`
           """ 

#Do not edit below

def main():
	query_options = { 5: query5(), 6: query6(), 7: query7(), 8: query8(), 
		9: query9(), 10: query10(), 11: query11(), 12: query12(), 13: query13()}
	
	if len(sys.argv) == 1:
		if username() == "username":
			print("Make sure to change the username function to return your username.")
			return
		else:
			print(username())
		for query in query_options.values():
			print(query)
	elif len(sys.argv) == 2:
		if sys.argv[1] == "username":
			print(username())
		else:
			print(query_options[int(sys.argv[1])])

	
if __name__ == "__main__":
   main()
