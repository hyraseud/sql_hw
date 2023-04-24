import sys

# Use this file to write your queries. Submit this file in Brightspace after finishing your homework.

#TODO: Write your username and answer to each query as a string in the return statements in the functions below. 
# Do not change the function names. 

#Your resulting tables should have the attributes in the same order as appeared in the sample answers. 

#Make sure to test that python prints out the strings (your username and SQL queries) correctly.

#usage: python hw1.py or python3 hw1.py
# make sure the program prints out your SQL statements correctly. That means the autograder will read you SQL correctly. Running the Python file will not execute your SQL statements (just prints them).

def username():
	return "YourUsername"
    
def query1():
	return """
    SELECT rank, v.name, year, genre, sales, r.name
	FROM video_game v, games_sales gs, region r
	WHERE v.rank = gs.game_rank AND gs.region_id = r.id
	  AND v.rank <= 3; 
	"""

def query2():
	return """
	SELECT rank, v.name, year, genre, platform_name
	FROM video_game v, platform p
	WHERE v.platform_id = p.platform_id
	  AND v.rank <= 20;
	"""

def query3():
	return """
	SELECT rank, v.name, platform_name, d1.name as game_publisher, d2.name as platform_manufacturer
	FROM video_game v, platform p, developer d1, developer d2
	WHERE v.platform_id = p.platform_id 
	  AND v.publisher_id = d1.id 
	  AND p.developer_id = d2.id
	  AND v.rank <= 20;
	"""
	
def query4():
	return '''
	SELECT rank, v.name, platform_name, d1.name as publisher, d2.name as p_man, sales, r.name as region
FROM video_game v, platform p, developer d1, developer d2, games_sales gs, region r
WHERE v.platform_id = p.platform_id 
  AND v.publisher_id = d1.id 
  AND p.developer_id = d2.id
  AND v.rank = gs.game_rank
  AND gs.region_id = r.id
  AND v.rank <= 3; 
	'''

def query5():
	return '''
	SELECT rank, v.name, platform_name, d1.name as publisher, d2.name as p_man, sum(sales) as total_sales 
FROM video_game v, platform p, developer d1, developer d2, games_sales gs
WHERE v.platform_id = p.platform_id 
  AND v.publisher_id = d1.id 
  AND p.developer_id = d2.id
  AND v.rank = gs.game_rank
  AND v.rank <= 3
GROUP BY rank, v.name, platform_name, publisher, p_man;  
	'''

def query6():
	return """
	SELECT distinct genre
	FROM video_game;
	"""

def query7():
	return """
	SELECT genre, COUNT(*) as games_in_genre
	FROM video_game
	GROUP BY genre;
	"""

def query8():
	return """
	SELECT genre, COUNT(*) as games_in_genre
	FROM video_game
	GROUP BY genre
	HAVING games_in_genre >= 5;
	"""

def query9():
	return """
	SELECT genre, year, COUNT(distinct v.rank) as games_in_genre_year, sum(sales) as total_sales
	FROM video_game v join games_sales gs on v.rank = gs.game_rank
	GROUP BY genre, year
	HAVING games_in_genre_year >= 2;
	"""

def query10():
	return """
	SELECT v1.rank, v1.name, v2.rank, v2.name
	FROM video_game v1, video_game v2 
	WHERE v1.platform_id = v2.platform_id 
	  AND v1.publisher_id = v2.publisher_id
	  AND v1.genre = v2.genre
	  AND v1.year = v2.year
	  AND v1.rank < v2.rank;
	"""

def query11():
	return """
	SELECT r.name, sum(sales) as total_sales
	FROM region r LEFT OUTER JOIN games_sales gs ON r.id = gs.region_id
	GROUP By r.name;
	"""

def query12():
	return """
	SELECT d.name, count(distinct rank) as number_of_games, count(distinct p.platform_id) as number_of_platforms
	FROM developer d left outer join video_game v on publisher_id = id
	     left outer join platform p on d.id = p.developer_id  
	GROUP BY d.name;
	"""

def query13():
	return """
	SELECT d.name, 'games published' as game_platform , count(*) as number_of_games
	FROM developer d join video_game v on publisher_id = id
	GROUP BY d.name
	UNION
	SELECT d.name, 'platforms manufactured' as game_platform , count(*) as number_of_games
	FROM developer d join platform p on developer_id = id
	GROUP BY d.name;
	"""

def query14():
	return """
	SELECT d.name
	FROM developer d join video_game v on d.id = v.publisher_id
	WHERE v.genre = 'Shooter'
	intersect
	SELECT d.name
	FROM developer d join video_game v on d.id = v.publisher_id
	WHERE v.genre = 'Puzzle';
	"""

def query15():
	return """
	SELECT platform_name
	FROM platform p natural join video_game v 
	WHERE v.genre = 'Racing'
	Except
	SELECT platform_name
	FROM platform p natural join video_game v 
	WHERE v.genre = 'Action';
	"""

#Do not edit below

def main():
	query_options = {1: query1(), 2: query2(), 3: query3(), 4: query4(), 5: query5(), 6: query6(), 7: query7(), 8: query8(), 
		9: query9(), 10: query10(), 11: query11(), 12: query12(), 13: query13(), 14: query14(), 15: query15()}
	
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
