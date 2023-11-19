from abc import ABC,abstractmethod
from typing import List, Optional
import string
import random
import nltk

class PasswordGenerator(ABC):
    """Base class for generating passwords.
    """
    @abstractmethod
    def Generate(self):
        """ 
        Subclasses should override this method to generate password.
        """
        pass


class PinGenerator(PasswordGenerator):
    """class to generate Pin Password
    """
    def __init__(self, length: int=8):
        self.length = length

    def Generate(self):
        """function to generate numeric pin password

        :return: Numeric pin password
        :rtype: str
        """
        return "".join([random.choice(string.digits) for _ in range(self.length)])   


class RandomPasswordGenerator(PasswordGenerator):
    """class to generate Random password
    """
    def __init__(self, length : int = 8, include_number : bool = False, include_symbol : bool = False):
        """_summary_

        :param length: length of the random password
        :param include_number: include number in password, defaults to False
        :param include_symbol: include symbol in password, defaults to False
        :type include_symbol: bool, optional
        """
        self.include_number = include_number
        self.include_symbol = include_symbol
        self.length = length

    def Generate(self):
        """generate random password with char_list

        :return: random password 
        :rtype: str
        """
        char_list = string.ascii_lowercase
        if self.include_number:
            char_list += string.digits
        if self.include_symbol:
            char_list += string.punctuation
            
        return "".join([random.choice(char_list) for _ in range(self.length)])    


class MemorablePasswordGenerator(PasswordGenerator):
    """class to generate Meomrable password
    """
    def __init__(
            self,
            num_of_words :int = 4,
            seprator : str = "-", 
            capitalization : bool = False, 
            word_list : Optional[List[str]]= None
            ):
        
        self.num_of_words = num_of_words
        self.seprator = seprator
        self.capitalization = capitalization
        self.word_list = word_list
        
    def Generate(self):
        """fun to generate memorable password with word_list and separator

        :return: memorable password
        :rtype: str
        """
        if self.word_list == None:
            self.word_list = nltk.corpus.words.words()
        password_word = self.seprator.join([random.choice(self.word_list) for _ in range(self.num_of_words)])
        return password_word.upper() if self.capitalization else password_word   


def test_random_password_generator():
    random_gen = RandomPasswordGenerator(length=5, include_number=True, include_symbol=True)
    password = random_gen.Generate()
    print(password)
    assert len(password) == 5



def test_memorable_password_generator():
    memorable_gen = MemorablePasswordGenerator( 
        num_of_words=4,
        seprator="-",
        capitalization=True,
        word_list=nltk.corpus.words.words(),
    )
    password = memorable_gen.Generate()
    print(password)
    assert len(password.split('-')) == 4
    assert all(word[0].isupper() for word in password.split('-'))


def test_pincode_generator():
    pin_gen = PinGenerator(length=4)
    pin = pin_gen.Generate()
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)


def main():
    print("Testing RandomPasswordGenerator:")
    test_random_password_generator()
    print("Testing MemorablePasswordGenerator:")
    test_memorable_password_generator()
    print("Testing PinCodeGenerator:")
    test_pincode_generator()


if __name__ == "__main__":
    main()
  