## Prerequisites and how to run the project

### Prerequisites
To execute the project, following libraries would be required

- [Tesseract] (https://github.com/tesseract-ocr/tesseract) -  You can download it using ```sudo apt-get install tesseract```. To run the tesseract application on Python, another library needs to be installed using ```pip``` called ```pytesseract```. Simply, ```pip3 install pytesseract```.

- [Pillow] (https://pillow.readthedocs.io/en/5.1.x/) - To download Python's Imaging Library, you can use ```pip3 install pillow```

- [Tkinter] (https://docs.python.org/3/library/tkinter.html) - It a Python binder to the Tk GUI. To view the results of the NER which is viewed as a graph you call install python-tkinter using ```sudo apt-get install python3-tkinter```.

- [Natural Language Toolkit (NLTK)] (http://www.nltk.org/) - To run the Named Entity Recognition, you need to make use of Python's Standard Library for Natural Language Processing. You can install it by simply, ```pip3 install nltk```.
    - You would need to download the standard chunkers, taggers for entity recognition  namely ```punkt```, ```averaged_perceptron_taggers```, ```maxent_ne_chunker``` and ```words```. For that - run a python shell in your terminal and follow the steps below :  
        ``` python
            import nltk
            nltk.download('punkt')
            nltk.download('words')
            nltk.download('maxent_ne_chunker')
            nltk.download('averaged_perceptron_taggers')
        ```
- Stanford NER Library (https://nlp.stanford.edu/software/CRF-NER.shtml#Download) - You can download the 7 class recognizer from the link and move it to the ```/usr/bin``` folder. Please ensure that you have ```java```, ```jre``` and ```jdk``` installed to run this wrapper library.

### Execute and Run
To run the NLTK Standard NER Library, in the terminal, type ```python3 nltk_ner.py -i <path to image here>```.

To run the Stanford NER Tagger, in the terminal type ```python3 stanford_ner.py -i <path to image here>```.

#### As an output, all the will entries of the scanned image is retrieved along with their named entities classified. 
