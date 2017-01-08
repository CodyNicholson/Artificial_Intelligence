#Features And Labels

Instead of giving our program raw data, like the video feed of the self-driving car's camera or the picture of the person you want your program to recognize or the raw music that you usually like to listen to, we extract **features** from the raw data and feed those features to our program

For example, the features we may extract from the music you like to listen to might be the intensity of the song, the tempo, the genre, and the gender of the singer

Then we tell our program that - for example - you *usually* like more intense music at an a fast tempo of the pop genre sung by a male singer

Now that the program knows this, it can begin to recommend you songs that you may like!

***

The computer is able to compare these features by putting them on a **scatterplot**

The scatterplot makes it easy to see the relationship between two variables

If we know the relationship between two variables we can begin to draw conclusions and predict the future outcomes based on the data

***

Now that we know how our program can compare to variables to draw conclusions and make decisions, we can begin to understand how a self-driving car may decide how to drive in the desert

The two features that would be the best to pay attention to in this case are the ruggedness of the terrain, and the steepness of the terrain

***

###Decision Surface

Imagine you have a scatterplot where all the data on the left is labeled one thing, and all the data on the right was labeled another thing

The computer should be able to create something called a **Decision Surface** that divides the data in half (assuming this is possible) so that the computer knows when it gets a new input it can classifiy it based on which side of the decision surface it is on

If the Decision Surface is a line, it is called a Linear Decision Surface
