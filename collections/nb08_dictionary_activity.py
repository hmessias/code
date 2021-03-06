import pprint

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


def remove_punctuation(passage): #this functuon will remove all the punctuation listed bellow
    
    punctuation = ".", "'", '"', ";", ":", ",", "?"

    for i in punctuation:
        passage = passage.replace(i, " ")

    return passage


def create_list_words(passage): #this function will get a list of words from the text, with no punctuation and lowered case letters

    passage = passage.replace("\n", " ")
    passage = passage.lower()
    passage = passage.strip()
    passage = passage.split(" ")

    return passage

    # split passage into list of words
    # sort word list
def gen_word_freq_dict(passage):

    # create an empty dictionary
    dict_word = {} #this creates an empty dictionary
    word_keys = [] #this creates an empty list, that will holds the number of apperance of a word

    for word in passage: #this will check all the words in the list of words
        if word.isalpha(): #this will check if is a word or a number
            if word not in word_keys: #this will loop over the list to find for unique words
                word_keys.append(word) #this will add only unique words to the list called word_keys

    dict_word = dict.fromkeys(word_keys, 0) #this will create a dictionary that will uses the list of words and the key and assigns a value of 0 to all entries

    
    # loop over each word in the list of raw words
        # convert the word to lower case
        # if word is already in the words dictionary
            # increase the count for that word
            # i.e. increment the dictionary value for that word

        # else if the word is:
        # * made of alphabetical characters and
        # * is longer than a single character or is an "i", or "a"
            # add the word to the dictionary and set its counter to 1
    for word in passage: #this will look over the text
        if word.isalpha(): #this checks if its a word made of alphabetical characters
            dict_word[word] = dict_word[word] + 1 #this will check the word and if appers again will add 1 into its key value in the dictionary

    # return the word:count dictionary
    return dict_word

#def get_key_value(key_value_pair):
    """
    This function returns the value portion of a single dictionary item

    This is a more explicit method than using a lambda when implementing common
    sorting idioms.

    Args:
        key_value_pair: this tuple contains the current key <-> value mapping of the dictionary

    Returns:
        The value stored in the current mapping, i.e. the tuple element in position 1 []
    """

# remove the punctuation from the passage
clean_passage = remove_punctuation(NEWS_PASSAGE) #This will get the text with no punctuation
list_words = create_list_words(clean_passage) #this will get a list of words in the text

# create a dictionary that stores word frequencies
word_freq_dict = gen_word_freq_dict(list_words)

#prompt the user for a word and convert it to lower case
word = input("please, type the word to checked how many times appears in the text: ").lower()
print(" the word " + word + " appers " + str(word_freq_dict[word]) + " times.")
#output how many times that lowercase word appeared in the passage

## Bonus
# create a sorted list from the dictionary using the get_key_value function
# above and the `sorted()` global function
# see https://docs.python.org/3/library/functions.html#sorted and 
# https://docs.python.org/3/howto/sorting.html#sortinghowto
# print the five most frequently used words and how often they were used
