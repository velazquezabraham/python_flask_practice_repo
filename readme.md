#I will be using this to practice git usability and python with flask.
#kill the flask server if "Adress already in service" by using the following bas commands:
	ps -fA | grep python3
	kill -9 <number you want to kill>

#tutorial 3 notes:
#	working with 2 basic HTTP ways to send and receive data using GET/POST
#	Sending info to our service or our clients
#	Get - most common, but insecure. Usually pased through the url bar or use to redirect a link 
#	POST - More secure way,
#TUTORIAL 5 - SESSIONS
#	Sessions- pass information from our back end to from end,
#	temporary, stored on web server, 
#   	there for quick access of info between all of the different pages
#	of website. Load in, use it while user in website, deasapears when
#	they leave.
#	import session
#	create secret key app.secret_key = "whatever"
#	store data in login
#	reference data in user, redirect if key session empty,
#	added a timedelta to set how long our session will last
