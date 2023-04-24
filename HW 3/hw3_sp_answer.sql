DELIMITER //
CREATE PROCEDURE sp1 (IN num_games integer)
    BEGIN
	
    DECLARE done int default 0;
    DECLARE cnt int;
    DECLARE rank1_v int;
    DECLARE name_v varchar(50);
    DECLARE platform_name_v varchar(50);
    DECLARE genre_v varchar(50);
    DECLARE game_publisher_v varchar(50);
    DECLARE total_sales_v float;

    DECLARE gamesList CURSOR FOR 
                            SELECT rank1, v.name, platform_name, genre, d1.name as game_publisher, sum(sales) as total_sales
                            FROM video_game v, platform p, developer d1, games_sales gs
                            WHERE v.platform_id = p.platform_id 
                              AND v.publisher_id = d1.id 
                              AND v.rank1 = gs.game_rank
                            Group By rank1, v.name, platform_name, genre, d1.name 
                            ORDER By total_sales desc;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
	
    Delete from result;

    OPEN gamesList;

	getgames: LOOP
		FETCH gamesList INTO rank1_v, name_v, platform_name_v, genre_v, game_publisher_v, total_sales_v;
		IF done = 1 THEN 
			LEAVE getgames;
		END IF;
        
        SELECT COUNT(*) INTO cnt
        FROM result 
        WHERE platform_name = platform_name_v 
           OR genre = genre_v
           OR game_publisher = game_publisher_v;

        IF cnt = 0 THEN 
			INSERT INTO result values (rank1_v, name_v, platform_name_v, genre_v, game_publisher_v, total_sales_v);
		END IF;

	END LOOP getgames;
	
	CLOSE gamesList;
	
    END //
DELIMITER ; 