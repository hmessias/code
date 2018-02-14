newsPassage = """ Bell Canada is alerting customers after hackers illegally
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

def removePunctuation(passage): # Function that removes punctuation
    punctuation = ".", "'", '"', ";", ":", ",", "?"

    # Remove punctation from passage
    for i in punctuation:
        passage = passage.replace(i, "")

    return passage

def createWordList(passage): # Function that converts the sentence into a list

    passage = passage.replace("\n", " ") # Remove end of line characters
    passage = passage.lower() # Change everything to lowercase
    passage = passage.strip() # Strip all extra whitespace from beginning and end"
    passage = passage.split(" ") # Split passage into a list

    return passage

def createUniqueWordList(wordList): # Function that generates unique word list

    uniqueWords = [] # Create an empty list that we can add to
    for word in wordList: # Parse through our list of words
        if word.isalpha() == True: # Checks if the word is alphabetic and not a number
            if word not in uniqueWords: # If the word isn't already in our list of unique words
                uniqueWords.append(word) # Add unique word to our list, and then move onto the next word

    return uniqueWords

newsPassage = removePunctuation(newsPassage) # Remove punctuation using function
wordList = createWordList(newsPassage) # Create list using function
uniqueWords = createUniqueWordList(wordList)

print("Number of words in original passage: " + str(len(wordList)))
print("Number of unique words: " + str(len(uniqueWords)))
print(uniqueWords)
