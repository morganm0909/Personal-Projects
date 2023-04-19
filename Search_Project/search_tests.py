from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    #assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def article_info_test():
    assert article_info(deepcopy(PHOTO), title_to_info) == {'Digital photography': {'author': 'Mintleaf', 'timestamp': 1095727840, 'length': 18093}}
    assert article_info(deepcopy(TRAVEL), title_to_info) == {'Time travel': {'author': 'Thug outlaw69', 'timestamp': 1140826049, 'length': 35170}}
    assert article_info(deepcopy(SOCCER), title_to_info) == {'Spain national beach soccer team': {'author': 'Pegship', 'timestamp': 1233458894, 'length': 1526}, 'Will Johnson (soccer)': {'author': 'Mayumashu', 'timestamp': 1218489712, 'length': 3562}, 'Steven Cohen (soccer)': {'author': 'Scouselad10', 'timestamp': 1237669593, 'length': 2117}}
    
def article_title_len_test():
    assert article_length(2000, deepcopy(SOCCER), title_to_info) == ['Spain national beach soccer team']
    assert article_length(10000, deepcopy(SCHOOL), title_to_info) == ['Edogawa, Tokyo', 'Alex Turner (musician)']
    assert article_length(2500, deepcopy(SOCCER), title_to_info) == ['Spain national beach soccer team', 'Steven Cohen (soccer)']
    
    
def title_timestamp_test():
    assert title_timestamp(deepcopy(TRAVEL), title_to_info) == {'Time travel': 1140826049}
    assert title_timestamp(deepcopy(PHOTO), title_to_info) == {'Digital photography': 1095727840}
    assert title_timestamp(deepcopy(SCHOOL), title_to_info) == {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}
    
def favorite_author_test():
    assert favorite_author('Shakespere', deepcopy(TRAVEL), title_to_info) == False
    assert favorite_author('George Orwell', deepcopy(TRAVEL), title_to_info) == False
    assert favorite_author('Thug outlaw69', deepcopy(TRAVEL), title_to_info) == True
    
def multiple_keywords_test():
    assert multiple_keywords('school', deepcopy(DOG)) == ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']
    assert multiple_keywords('photo', deepcopy(DOG)) == ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', '2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']
    assert multiple_keywords('travel', deepcopy(DOG)) == ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Time travel']
    
def search_test():
    assert search('school') == SCHOOL
    assert search('SChoOl') == SCHOOL
    assert search('dance') == DANCE 
    
def title_to_info_test():
    fake_metadata_one = [['article_one', 'author_one', 12345, 1234, ['random', 'words', 'entered']],
                     ['article_two', 'author_two', 12345, 1234, [['random', 'words', 'entered']]]
    fake_metadata_two = [['Romeo and Juliet', 'Shakespear', 1234567890, 24545, ['romeo', 'juliet', 'thou', 'death', 'love']]
                     
    fake_metadata_three = [['Title', 'Author Name', 123456789, 123, ['these', 'are', 'some', 'keywords']]
    
    expected_one = {'article_one': {'author': 'author_one', 'timestamp': 12345, 'length': 1234}, 'article_two': {'author': 'author_two', 'timestamp': 12345, 'length': 1234}}
    expected_two = {'Romeo and Juliet': {'author': 'Shakespear', 'timestamp': 1234567890, 'length': 24545}, {'Romeo and Juliet': {'author': 'Shakespear', 'timestamp': 1234567890, 'length': 24545}}
    expected_three = {'Title': {'author': 'Author Name', 'timestamp': 123456789, 'length': 123}}
                
    assert title_to_info(deepcopy(fake_metadata_one)) == expected_one
    assert title_to_info(deepcopy(fake_metadata_two)) == expected_two
    assert title_to_info(deepcopy(fake_metadata_three)) == expected_three
    
def keyword_to_titles_test():
    
    fake_metadata_one = [['article_one', 'author_one', 12345, 1234, ['random', 'words', 'entered']],
                     ['article_two', 'author_two', 12345, 1234, [['more', 'words', 'entered']]]
    fake_metadata_two = [['Romeo and Juliet', 'Shakespear', 1234567890, 24545, ['romeo', 'juliet', 'thou', 'death', 'love']], ['Macbeth', 'Shakespear', 987123456, 17121, ['more', 'death', 'thou']]]
                     
    fake_metadata_three = [['Title', 'Author Name', 123456789, 17121, ['these', 'some', 'keywords']],
                     ['Title Two', 'helloworld', 987123456, 834, ['more', 'keywords', 'make', 'sentences']]]
    
    expected_one = {'random': ['article_one'], 'words': ['article_one', 'article_two'], 'entered': ['article_one', 'article_two'], 'more': ['article_two']}
    
    expected_two = {'romeo': ['Romeo and Juliet'], 'juliet': ['Romeo and Juliet'], 'thou': ['Romeo and Juliet', 'Macbeth'] 'death': ['Romeo and Juliet', 'Macbeth'], 'love': ['Romeo and Juliet'], 'more': ['Macbeth']}
    
    expected_three = {'these': ['Title'], 'some': ['Title'], 'keywords': ['Title', 'Title Two'] 'more': ['Title Two'], 'make': ['Title Two'], 'sentences': ['Title Two']}

    assert title_to_info(deepcopy(fake_metadata_one)) == expected_one
    assert title_to_info(deepcopy(fake_metadata_two)) == expected_two
    assert title_to_info(deepcopy(fake_metadata_three)) == expected_three
    
#integration tests
@patch('builtins.input')
def integration_test_one(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 2000

    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat']\n"

    assert output == expected
    
@patch('builtins.input')
def integration_test_two(input_mock):
    keyword = 'dance'
    advanced_option = 2
    advanced_response = 10000

    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Indian classical music'], 'Guide dog']\n"

    assert output == expected
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
     test_example_title_to_info_tests()
     test_example_keyword_to_titles_tests()
     test_example_unit_tests()
     test_example_integration_test()
     article_info_test()
     article_title_len_test()
     title_timestamp_test()
     favorite_author_test()
     multiple_keywords_test()
     search_test()
     title_to_info_test()
     keyword_to_titles_test()
     integration_test_one()
     integration_test_two()
