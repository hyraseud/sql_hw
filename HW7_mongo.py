import sys

#TODO: Write your username and answer to each query as a string in the return statements 
# in the functions below. Do not change the function names. 

# Write your queries using multi-line strings and use proper indentation to increase readability.
# Write mapreduce code as multi-line string. For example:
# 
# def query6():
#     return """
# 
#             var mapFunction1 = function() {
#                ...
#             }
# 
#             var reduceFunction1 = function(a, b) {
#                return ...
#             }
# 
#             db.bills.mapReduce(mapFunction1, reduceFunction1, {
#                ...
#             })
#           """

# Your result should have the attributes in the same order as appeared in the sample answers. 

# Make sure to test that python prints out the strings correctly.

# usage: python hw7.py

def username():
	return "sdua"
    
def query1():
    return """
           db.countries.find({borders:"RWA"}, {_id: 0, "name":"$name.common"})
           """ 

def query2():
    return """
           db.countries.find({area: {$gt: 10000000}}, {_id: 0, "area":"$area", "name":"$name.common"})
           """
            
def query3():
    return """
            db.countries.find({$and: [{"latlng.0": {$gte: -60, $lte: -15}}, {"latlng.1": {$gte: 30, $lte: 50}}]}, {_id: 0, "latlng":"$latlng", "name":"$name.common"})
           """ 

def query4():
    return """
            db.countries.aggregate([{ $unwind : "$area" }, { $group: { _id:"$region", roundedAvg: { $avg : "$area" } } }, {$addFields: {roundedAvg: { $round: ['$roundedAvg', 2]} }} ])
           """

def query5():
    return """
            var map = function(){if(this.region != null){emit(this.region,this.area)}};
            var reduce = function(region,area) {return Array.avg(area);};
            db.countries.mapReduce(map, reduce, {out: "results"})
            db.results.find()
           """ 

def query6():
    return """
           db.countries.aggregate([{$group: {_id : "$demonym", countryWithSameDemonym: {$push: "$name.common"}}}, {$match: {countryWithSameDemonym: "United States"}}, {$unwind: "$countryWithSameDemonym"}, {$project: {_id:0, demonym:"$_id", name: "United States", countryWithSameDemonym: "$countryWithSameDemonym"}}]).pretty()
           """

def query7():
    return """
            db.countries.aggregate([{$unwind: "$borders"}, {$group: {_id : "$borders", borderCioc: {$push: "$cioc"},name: {$push: "$name.common"}}}, { $project: { x: { $zip: { inputs: ["$borderCioc", "$name"] } } } },{ $unwind: "$x" }, {$match: {_id: "RWA"}},{$project: {_id:0, cioc:"$_id", borderCioc: { $first: "$x" }, borderCountryName: { $last: "$x" }}}]).pretty()
           """

def query8():
    return """
            var map = function(){if(this.region != null){emit(this.region,this.landlocked)}};
            var reduce = function(region, landlocked) {return Array.sum(landlocked)};
            db.countries.mapReduce(map, reduce, {out: "results"})
            db.results.find()
           """

def query9():
    return """
            
           """

def query10():
    return """
            db.countries.aggregate([{$project: {array: {$objectToArray: "$languages"}}}, {$unwind: "$array"}, {$group: {_id: {code: "$array.k", language: "$array.v"}, count: {$sum: 1}}}, {$sort: {count:-1}}, {$limit: 5}])
           """

def query11():
    return """
           """

def query12():
    return """
           """                      
#Do not edit below

def main():
	query_options = {1: query1(), 2: query2(), 3: query3(), 4: query4(), 
		5: query5(), 6: query6(), 7: query7(), 8: query8(), 9: query9(), 10: query10(), 11: query11(),
        12: query12()}
	
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
