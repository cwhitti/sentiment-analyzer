#Main funtions
def main():

    #Get the training data
    learn_file = input("Learning data file name?: ")

    #Initialize next task
    run_program = True

    #run the next task
    while run_program == True:

        #Seperate tasks
        print()

        #Introduce the program
        options()
        
        #Ask for the next task
        task = next_task()

        #Word scores
        if task == 1:
            word_score(learn_file)

        #Average scores        
        if task == 2:
            average_score(learn_file)

        #Highest and lowest scoring words
        if task == 3:
            high_low_scores(learn_file)

        #emotions texts
        if task == 4:
            emotion_scores(learn_file)
            
        #Bye felicia
        if task == 5:
        
            run_program = False

def options(): #Gives the user all of their options
    print("What would you like to do?")
    print("1: Get the score of a word")
    print("2: Get the average score of words in a file ")
    print("3: Find the highest / lowest scoring words in a file")
    print("4: Sort the words into positive.txt and negative.txt")
    print("5: Exit the program")

def next_task(): #Gets the next task

    current_task = input("Enter a number 1 - 5: ")

    #See if the input is an integer             
    try:
        current_task = int(current_task)

    #If we get something that isnt an integer, just dont do anything
    except ValueError:
        pass

    ###THIS IS WHAT IS PRODUCED###
    return current_task

#Fixes the file so its all normalized
def fix_file_list(learn_file):

    #initialize list
    file_list = []

    #opel and read the file to a list
    with open(learn_file, 'r') as file:

        words = file.readlines()

    #Normalize everything
    for index in range(len(words)):

        #take out white space
        words[ index ] = words[ index ].strip()

        #make it lowercase
        lower_words = words[ index ].lower()
        
        # initializing punctuations string
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         
        # Removing punctuations in string
        # Using loop + punctuation string
        for letter in lower_words:
            
            if letter in punc:
                
                lower_words = lower_words.replace(letter, "")
                
                words[ index ] = lower_words

###THIS IS WHAT IS PRODUCED### 
    return words
    
def word_score_dict(learn_file):

    #get the reviews
    reviews = fix_file_list(learn_file)

    #initialize the dictionary
    word_score_dict = {}
    
    #initialize the list
    word_score_list = []

    #get the individual reviews
    for review in reviews:

        #split the individual reviews by word
        review_word_list = review.split()

        #loop through all of the items in the word
        for index in range(1,len(review_word_list)):
            
            #if the item isnt in the dictioanry, add it
            if review_word_list[index] not in word_score_dict:

                word_score_dict[review_word_list[index]] = [int(review_word_list[0])]
                
            #if the item is in the dictionry, just extend the score
            else:
            
                word_score_dict[review_word_list[index]].extend([int(review_word_list[0])]) 
                
    return word_score_dict

#gets the average score for each word
def average_word_score(learn_file):

    #initialize the word_scores
    word_scores = word_score_dict(learn_file)

    #make the list
    avg_word_scores = {}

    #Compute the total score
    for key, value in word_scores.items():

        #set the total score for the key
        total_score = 0
        
        #add up the scores for the key
        for index in range(len(value)):

            total_score += value[index]

        #divide the total score by the amount of values for THAT KEY
        average = total_score / (len(value))
        
        #add the average
        avg_word_scores[key] = [average]
        
    return avg_word_scores

#adds in a new score
def correction(learn_file, split_words):

    correction_needed = input("Am I right (yes/no)? ")

    #do we need to correct it?
    if correction_needed == "no":

        #get the average score
        average_scores = word_score_dict(learn_file)

        #Get the correct score
        corrected_score = int(input("What score should this sentence have (0 - 4 where 4 is the most positive)? "))

        #Loop through all of the items in the sentence
        for index in range(len(split_words)):
            
            current_word = split_words[index]
            
            average_scores[current_word].extend([corrected_score])
            
    return correction_needed
               
def word_score(learn_file):#1
    
    #ask for the word
    user_word = input("which word? ")

    #get the average score
    average_score = average_word_score(learn_file)    

    #give the people what they want
    try:
        
        #get the average score for the word
        score_list = average_score[user_word]

        #take it out of the list
        score = score_list[0]

        #round it
        round_score = round(score, 2)

        print(f"score = {round_score}")
        
        #check if positive or negative
        if round_score >= 2:

            print(f"{user_word} is positive")
            
        if round_score <= 2:

            print(f"{user_word} is negative")
            
    # ignore anything that isnt an integer       
    except KeyError:
        pass

def average_score(learn_file): #2

    #get the training scores
    average_score = average_word_score(learn_file)
    
    #get the file we wanna learn from
    new_file = input("file name? ")

    #normalize the input file
    words = fix_file_list(new_file)

    #split the words so we can use them
    for word in words:
        split_words = word.split()
        
    #initialize the total
    score = 0
    
    #get the total scores
    for index in range(len(split_words)):

        current_word = split_words[index]

        current_score = average_score[current_word]

        score += current_score[0]
        
    #GET THE AVERAGE
    new_file_average_score = score / len(split_words)

    #round the average
    rounded_new_file_average_score = round(new_file_average_score,2)
    
    #outputs
    with open(new_file, 'r') as file_2:
        
        print(f'score = {rounded_new_file_average_score}')
        
        print(file_2.read().rstrip())

        #Check the scores, >2 is pos and <2 is neg
        if rounded_new_file_average_score >= 2: 
            print(" is positive")
            
        if rounded_new_file_average_score <= 2:
            print(" is negative")

    #ask if correct
    correction(learn_file, split_words)
           
def high_low_scores(learn_file): #3

    #get the average scores
    average_score = average_word_score(learn_file)

    new_file = input("file name? ")

    words = fix_file_list(new_file)

    #initialize the score tracker
    highest_score = 0

    lowest_score = 4
    
    #split the words so we can use them
    for word in words:
        
        split_words = word.split()

    #Loop through the split words
    for index in range(len(split_words)):

        #get the current word
        current_word = split_words[index]
        
        #get the current score
        current_score = (average_score[current_word][0])

        #check if its the highest
        if current_score >= highest_score:

            highest_word = current_word

            highest_score = current_score

        #check if its the lowest
        if current_score <= lowest_score:

            lowest_word = current_word

            lowest_score = current_score
            
    ##RESULTS##
    print(f"Maximum score is {highest_score} for {highest_word}")
    print(f"Minimum score is {lowest_score} for {lowest_word}")

def emotion_scores(learn_file): #4
    
    #get the average scores
    average_score = average_word_score(learn_file)

    #initialize positive and negative words
    positive_words = []

    negative_words = []

    #loop thorugh the items in the dictionary to sort them in our lists
    for (key, value) in average_score.items():

        #Get the value out of the list
        score = value[0]

        #Check if score is positive, write to positive list
        if score >= 2:

            positive_words.append(key)

        #Check if score is negative, write to negative list
        if score <= 2: 

            negative_words.append(key)

    #Write to positives.txt
    with open("positives.txt", 'w') as p_file:

        for word in positive_words:

            p_file.write(word + "\n")

    #Write to negatives.txt
    with open("negatives.txt", 'w') as n_file:

        for word in negative_words:

            n_file.write(word + "\n")
        
main()
