# Headings

Although there are lots of ways to get a heading, the easiset is with the hash (#) symbol.

    # A level one heading
    ## A level two heading
    ### A level three heading
    
# A level one heading
## A level two heading
### A level three heading

#Lists

### Unordered lists can be achieved using a variety of symbols (*, - or +)

    * Item
    * Item
    * Item

* Item
* Item
* Item

### Ordered lists use numbers, but the order is automatically corrected on export

    1. Item 1
    2. Item 2
    3. Item 3
    6. Item 4
    2. Item 5

1. Item 1
2. Item 2
3. Item 3
6. Item 4
2. Item 5


#Code

###If you want to write code you just add a tab (4 space) before each line

    foo = 6
    bar = 4
    foo = foo + bar
    bar = foo - bar
    foo = foo - bar

#Links

Write links like this

[text to display](http://www.example.com)

Images

    Images can be added to your markdown using a similar format to links

![alt text for image](relative/location/of/image.jpg)

    So for instance if my markdown was in a directory, that itself contained a directory called images, where my pictures were stored.

![alt text for image](images/image.jpg)

Exporting

    You'll need to use a command-line application to export markdown to other formats. Pandoc is probably the best one to use.
    Open up PowerShell if you're on windows or Terminal if you're on a *nix system.
    cd into the directory containing your markdown. So if this was my directory structure:

└── projects
    └── writeup
        ├── images
        │   ├── pic1.jpg
        │   ├── pic2.jpg
        │   └── pic3.jpg
        ├── myWriteUp.md
        └── notes.md

cd projects/writeup

    Don't forget you can use the Tab key (-->|) to autocomplete.
    Once you are in the folder containing your markdown file (just type ls to see what's in your folder), you need to run the following command (but obviously use your filename)

pandoc myWriteUp.md -o myWriteUp.html

    You can convert markdown to other formats with pandoc, so the following will work as well.

pandoc myWriteUp.md -o myWriteUp.pdf
pandoc myWriteUp.md -o myWriteUp.docx

