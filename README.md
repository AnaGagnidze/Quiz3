# NASA's API

In this quiz, I usec NASA's API names Mars Rover Photos. This API contains image data gathered by NASA's rovers on mars.

Firstly, I send request to the API (user inputs the desired date they want to see pictures from), afterwards, I check the status code and headers of the response. 
Then work with json file and convert it to python's dictionary to work with it better. (I use json module's loads and dumps functions)

Second part of the code saves the information in json file format using dump function.

Lastly, program connects to the database and creates a table names mars. Mars has three colums: date, rover's name and photo link.
I use for loop to get the desired information from the dictionary and insert it into database. In this for loop I also print out 
date and the photo's link for the user to see. Then the database closes.

I worked in Pycharm and used DB Browser(Sqlite).
