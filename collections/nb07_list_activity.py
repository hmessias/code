NEWS_PASSAGE = """ Bell Canada is alerting customers after hackers illegally
accessed the information of fewer than 100,000 customers, the telecom giant
told CBC News.

The breach comes just eight months after 1.9 million customer emails were
stolen from Bell's database by an anonymous hacker.

Bell is Canada's largest telecom company, with over 22 million customers.

The information obtained in the latest breach included details such as names,
email addresses, account user names and numbers, as well as phone numbers.

Bell said there was no indication that credit card, banking or other
information was accessed.

But, it would not say when the breach took place or whether it was related to
a past incident.

"We apologize to our customers and are contacting all those affected," said
Bell spokesperson Marc Choma in an email.

Bell added that it had notified appropriate government agencies including the
Office of the Privacy Commissioner of Canada.

"Bell works closely with law enforcement, government and the broader
technology industry to combat the growth of cybercrimes, and we have
successfully supported law enforcement in past prosecutions of hackers,"
Choma said.

Ongoing investigation Tobi Cohen, a spokesperson for the Office of the
Privacy Commissioner, confirmed in an email that Bell had notified it of the
breach and that it is following up with the company to get more information
and "determine follow up actions."

The RCMP is also investigating.

Chester Wisniewski, an expert at the data security firm Sophos Canada, said
the breach did make customers more likely to be victimized by potential
phishing attacks; as seen in other big breaches like those at LinkedIn and
Ashley Madison.

AshleyMadison security protocols violated privacy laws, watchdog says "When
you see email addresses leaked, that's a really goodthing for spammers and
phishing attacks through email, because they know that if you're in Bell's
database, you likely to have some sort of commercial relationship with Bell,"
he said.

"So, they can send you one of those fake emails saying, 'Hey your cell phone
bill is due, click here to login.'"

Wisniewski added that Bell was under no legal obligation to notify customers
of the breach, because stolen email addresses are not considered personally
identifiable such as a driver's licence or social insurance number.

"A lot of times when companies lose this kind of information, they don't even
tell you," he said. "The good thing about them telling us is to put us on
alert for those types of things now."

A person or group claiming to be behind the attack against Bell in May warned
in an online post that more data would be leaked if Bell did not co-operate."""

def remove_punctuation(passage): #this funcion removes the punctuation
    punctuation = ".", "'", '"', ";", ":", ",", "?"

    for i in punctuation:
        passage = passage.replace(i, " ")

    return passage

def create_list_word(passage): #this function removes the end of lines, lower case the words, strip and split it into a list
    passage = passage.replace("\n", " ") #this will replace the end of a line by an empty space
    passage = passage.lower() #this will set all words with lower case letters
    passage = passage.strip() #this will remove all empty spaces from begining and end
    passage = passage.split(" ") #this will make a list

    return passage

def create_unique_words(word_list): #this function will create a list of just unique words, only one entry for each word from the text
    unique_words = [] #this creates an empty list, that will be appended with unique words over the loop
    for word in word_list: #this loop will check the raw list of words
        if word.isalpha(): #this will check to look just for words, not number, in the raw list
            if word not in unique_words: #this will compare whether the word in the raw list is in the unique list already
                unique_words.append(word) #If the word is not in the unique list, it will include (append) this word to the list

    return unique_words


# Create a function to generate a list of unique words based on 
# a raw word list parameter

    # Create a copy of the raw word list

    # Sort word list copy

    # Create empty word list to hold unique words

    # loop over all of the words in the raw input list copy
        # Convert each word to lower case
        # Append each word to the unique list if
        #   * it isn't already in the list
        #   * it is made up of alphabetic characters
        #   * the only one letter words are 'i' and 'a'

    # sort the unique word list
    # return the sorted unique word list

#Main logic of your code
# Remove all punctuation from the passage
news_passage = remove_punctuation(NEWS_PASSAGE)

# split the news item string into a list of words (or at least thing between spaces)

news_passage_list = create_list_word(news_passage)

# generate a list of unique words based on raw word list using your function above
unique_word_list = create_unique_words(news_passage_list)
# print number of unique words and number of total words
print("The number of unique words are: " + str(len(unique_word_list)))
print("the total number of words are: " + str(len(news_passage_list)))
# print the list of unique words
print(unique_word_list)