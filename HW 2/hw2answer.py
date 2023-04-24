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
    SELECT * 
    FROM video_game
    WHERE year = (SELECT max(year)
                  FROM video_game);
	"""

def query2():
	return """
	SELECT genre, count(*) as number_of_games
    FROM video_game
    GROUP BY genre
    HAVING number_of_games = (
        SELECT max(number_of_games) 
        FROM
            (SELECT genre, count(*) as number_of_games
                FROM video_game
                GROUP BY genre) as temp
    );
	"""

def query3():
	return """
	SELECT genre, COUNT(*) as games_in_genre
    FROM video_game
    GROUP BY genre
    HAVING games_in_genre >= (
            SELECT AVG(games_in_genre2)
            FROM 
                (SELECT genre, COUNT(*) as games_in_genre2
                FROM video_game
                GROUP BY genre) as temp
    );
	"""
	
def query4():
	return '''
    SELECT p.platform_name, p.units_sold, p.introductory_price_us, (units_sold * introductory_price_us) as revenue, d.name as developer_name
    FROM platform p JOIN developer d ON p.developer_id = d.id
    WHERE (units_sold * introductory_price_us) = (
        SELECT max(units_sold * introductory_price_us)
        FROM platform
    );
	'''

def query5():
	return '''
    SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as p_man, sum(sales) as total_sales 
    FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1
    WHERE v1.platform_id = p1.platform_id 
    AND v1.publisher_id = d1_1.id 
    AND p1.developer_id = d2_1.id
    AND v1.rank = gs1.game_rank
    GROUP BY rank, v1.name, platform_name, publisher, p_man
    HAVING total_sales = (
        SELECT max(total_sales)
        FROM
            (SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as p_man, sum(sales) as total_sales 
            FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1
            WHERE v1.platform_id = p1.platform_id 
                AND v1.publisher_id = d1_1.id 
                AND p1.developer_id = d2_1.id
                AND v1.rank = gs1.game_rank
            GROUP BY rank, v1.name, platform_name, publisher, p_man) as temp
        WHERE temp.publisher = d1_1.name
    );
	'''

def query6():
	return """
    SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as p_man, sum(sales) as total_sales 
    FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1
    WHERE v1.platform_id = p1.platform_id 
    AND v1.publisher_id = d1_1.id 
    AND p1.developer_id = d2_1.id
    AND v1.rank = gs1.game_rank
    GROUP BY rank, v1.name, platform_name, publisher, p_man
    HAVING total_sales < (
        SELECT AVG(total_sales)
        FROM
            (SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as p_man, sum(sales) as total_sales 
            FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1
            WHERE v1.platform_id = p1.platform_id 
                AND v1.publisher_id = d1_1.id 
                AND p1.developer_id = d2_1.id
                AND v1.rank = gs1.game_rank
            GROUP BY rank, v1.name, platform_name, publisher, p_man) as temp
    );
	"""

def query7():
	return """
    SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as p_man, sum(sales) as NA_total_sales 
        FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1, region r1
        WHERE v1.platform_id = p1.platform_id 
        AND v1.publisher_id = d1_1.id 
        AND p1.developer_id = d2_1.id
        AND v1.rank = gs1.game_rank
        AND r1.id = gs1.region_id
        AND r1.name = 'North America'
        GROUP BY rank, v1.name, platform_name, publisher, p_man
        HAVING NA_total_sales > ( 
            Select avg(NA_total_sales) 
            FROM (
                    SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as   p_man, sum(sales) as NA_total_sales 
                    FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1, region r1
                    WHERE v1.platform_id = p1.platform_id 
                    AND v1.publisher_id = d1_1.id 
                    AND p1.developer_id = d2_1.id
                    AND v1.rank = gs1.game_rank
                    AND r1.id = gs1.region_id
                    AND r1.name = 'North America'
                    GROUP BY rank, v1.name, platform_name, publisher, p_man
                    ) as t1
        );
	"""

def query8():
	return """
    SELECT v1.name 
    FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1
    WHERE v1.platform_id = p1.platform_id 
    AND v1.publisher_id = d1_1.id 
    AND p1.developer_id = d2_1.id
    AND v1.rank = gs1.game_rank
    GROUP BY v1.name
    HAVING sum(sales) < (
        SELECT AVG(total_sales)
        FROM
            (SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as p_man, sum(sales) as total_sales 
            FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1
            WHERE v1.platform_id = p1.platform_id 
                AND v1.publisher_id = d1_1.id 
                AND p1.developer_id = d2_1.id
                AND v1.rank = gs1.game_rank
            GROUP BY rank, v1.name, platform_name, publisher, p_man) as temp
    )
    INTERSECT
    SELECT v1.name 
        FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1, region r1
        WHERE v1.platform_id = p1.platform_id 
        AND v1.publisher_id = d1_1.id 
        AND p1.developer_id = d2_1.id
        AND v1.rank = gs1.game_rank
        AND r1.id = gs1.region_id
        AND r1.name = 'North America'
        GROUP BY v1.name
        HAVING sum(sales) > ( 
            Select avg(NA_total_sales) 
            FROM (
                    SELECT rank, v1.name, platform_name, d1_1.name as publisher, d2_1.name as   p_man, sum(sales) as NA_total_sales 
                    FROM video_game v1, platform p1, developer d1_1, developer d2_1, games_sales gs1, region r1
                    WHERE v1.platform_id = p1.platform_id 
                    AND v1.publisher_id = d1_1.id 
                    AND p1.developer_id = d2_1.id
                    AND v1.rank = gs1.game_rank
                    AND r1.id = gs1.region_id
                    AND r1.name = 'North America'
                    GROUP BY rank, v1.name, platform_name, publisher, p_man
                    ) as t1
        );
	"""

def query9():
	return """
    SELECT rank, v.name, d1.name as publisher, sum(sales) as total_sales, (SELECT sum(sales)
                FROM video_game v_s, developer d1_s, games_sales gs_s
                WHERE v_s.publisher_id = d1_s.id 
                    AND v_s.rank = gs_s.game_rank
                    AND d1_s.name = d1.name) as publisher_sales
    FROM video_game v, developer d1, games_sales gs
    WHERE v.publisher_id = d1.id 
    AND v.rank = gs.game_rank
    GROUP BY rank, v.name, publisher;
	"""

def query10():
	return """
    SELECT t1.name, t1.number_of_games, t2.name, t2.number_of_games
    FROM
        (SELECT d.name, count(distinct rank) as number_of_games
        FROM developer d join video_game v on publisher_id = id
        GROUP BY d.name) as t1
    JOIN
        (SELECT d.name, count(distinct rank) as number_of_games
        FROM developer d join video_game v on publisher_id = id
        GROUP BY d.name) as t2
    ON t1.number_of_games = t2.number_of_games
    AND t1.name < t2.name;
	"""

def query11():
	return """
    SELECT publisher, ifnull(published_games, 0) as published_games, paltform_developer, ifnull(platform_games, 0) as platform_games, 'publish-focused' as type 
    FROM 
    (
    SELECT *
    FROM
    (SELECT d.name as publisher, count(rank) as published_games
        FROM video_game v JOIN developer d ON v.publisher_id = d.id
        GROUP By d.name) as t2
    LEFT OUTER JOIN 
    (SELECT d.name as paltform_developer, count(rank) as platform_games
        FROM platform p natural join video_game v 
            JOIN developer d ON p.developer_id = d.id
        GROUP By d.name) as t1
    ON paltform_developer = publisher
    ) as t3
    WHERE ifnull(published_games, 0) > ifnull(platform_games, 0)
    UNION
    SELECT publisher, ifnull(published_games, 0) as published_games, paltform_developer, ifnull(platform_games, 0) as platform_games, 'platform-focused' as type 
    FROM 
    (
    SELECT *
    FROM
    (SELECT d.name as publisher, count(rank) as published_games
        FROM video_game v JOIN developer d ON v.publisher_id = d.id
        GROUP By d.name) as t2
    LEFT OUTER JOIN 
    (SELECT d.name as paltform_developer, count(rank) as platform_games
        FROM platform p natural join video_game v 
            JOIN developer d ON p.developer_id = d.id
        GROUP By d.name) as t1
    ON paltform_developer = publisher
    ) as t3
    WHERE ifnull(published_games, 0) < ifnull(platform_games, 0)
    UNION
    SELECT publisher, ifnull(published_games, 0) as published_games, paltform_developer, ifnull(platform_games, 0) as platform_games, 'equally-focused' as type 
    FROM 
    (
    SELECT *
    FROM
    (SELECT d.name as publisher, count(rank) as published_games
        FROM video_game v JOIN developer d ON v.publisher_id = d.id
        GROUP By d.name) as t2
    LEFT OUTER JOIN 
    (SELECT d.name as paltform_developer, count(rank) as platform_games
        FROM platform p natural join video_game v 
            JOIN developer d ON p.developer_id = d.id
        GROUP By d.name) as t1
    ON paltform_developer = publisher
    ) as t3
    WHERE ifnull(published_games, 0) = ifnull(platform_games, 0)
	"""

def query12():
	return """
    SELECT * 
    FROM
    (SELECT genre, COUNT(*) as games_in_genre
    FROM video_game
    GROUP BY genre) as t1
    Join
    (SELECT genre, COUNT(*) as games_in_genre
    FROM video_game
    GROUP BY genre) as t2
    ON t1.games_in_genre = t2.games_in_genre AND t1.genre < t2.genre
	"""

def query13():
	return """
    SELECT genre, COUNT(*) as games_in_genre, (
    SELECT AVG(games_in_genre)
    FROM
    (SELECT genre, COUNT(*) as games_in_genre
        FROM video_game
        GROUP BY genre) as t1
    ) as overall_average
    FROM video_game
    GROUP BY genre;
	"""

def query14():
	return """
    SELECT * FROM
    (SELECT genre, sum(sales) as NA_sales
    FROM video_game v join games_sales gs on v.rank = gs.game_rank
        join region r on r.id = gs.region_id
    WHERE  r.name = "North America"    
    GROUP BY genre) as t1
    Natural Join
    (SELECT genre, sum(sales) as EU_sales
    FROM video_game v join games_sales gs on v.rank = gs.game_rank
        join region r on r.id = gs.region_id
    WHERE  r.name = "European Union"    
    GROUP BY genre) as t2
    Natural Join
    (SELECT genre, sum(sales) as JA_sales
    FROM video_game v join games_sales gs on v.rank = gs.game_rank
        join region r on r.id = gs.region_id
    WHERE  r.name = "Japan"    
    GROUP BY genre) as t3
    Natural Join
    (SELECT genre, sum(sales) as Rest_W_sales
    FROM video_game v join games_sales gs on v.rank = gs.game_rank
        join region r on r.id = gs.region_id
    WHERE  r.name = "Rest of the World" 
    GROUP BY genre) as t4
    Natural Join
    (SELECT genre, sum(sales) as total_sales
    FROM video_game v join games_sales gs on v.rank = gs.game_rank
        join region r on r.id = gs.region_id
    GROUP BY genre) as t5;
	"""

def query15():
	return """
    SELECT r.name, genre, sum(sales) as total_sales
    FROM video_game v join games_sales gs on v.rank = gs.game_rank
        join region r on r.id = gs.region_id
    GROUP BY genre, r.name 
    HAVING total_sales = (
    SELECT max(total_sales2)
    FROM 
        (SELECT genre, r2.name, sum(sales) as total_sales2
            FROM video_game v2 join games_sales gs2 on v2.rank = gs2.game_rank
                join region r2 on r2.id = gs2.region_id
            GROUP BY genre, r2.name) as t1 
            WHERE t1.name = r.name
    )
    ORDER BY r.name;
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
