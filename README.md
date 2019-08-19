
# Coding Take-Home Assignment

Name: Cheng Chua
Linkedin: http://linkedin.com/in/chuaccheng
Email: chuaccheng@gmail.com

This program was created as part of a take-home coding exercise.

The main objective of the task was to write a command-line program that finds files which have exactly the same contents, and outputs any duplicates (and their locations) to standard output.

In this case, the script was written specifically for a folder of photos. A client has accidentally merged his photos folder with his partner's. Some of the photos have the same content, but are named differently.  This script looks for any duplicate photographs that have been accidentally merged into this folder. 


Written using Python 2.7.10, on 9 August 2019.

DISCLAIMER: 
While I tailored this script to compare images, I referenced existing solutions that compared file content with MD5 hashing and traversing file directories. The solutions are listed in the References section.


# Installation instructions

 1. Clone or download this repository in Github

 2. Open your choice of command-line software. In coding and testing this, I used Terminal on Macintosh.

 3. Make sure you have Python 2.7.10 installed.

 4. Type in 'python findDuplicateImages.py [foldername]' to run the script on the given folder. An empty folder called "images" is included in this repository.

# Considerations

- With some of the file names or extension changed, I knew that we could not simply compare the string value of the file names anymore. Another method has to be used to scan each image's content, and compare them individually.

- MD5 Hashing was the quickest, and most efficient solution that I could think of, for this exercise. Other solutions that I considered includes comparing file sizes of each file. This assumes that identical images would have identical file sizes, in a small set of images. However, this cannot be generalised for larger sets, since different images might coincidentally have the same file size.

- Currently, this solution would work on a small-to-moderate set of photos. The time complexity of MD5 Hashing is O(n). This can efficiently accommodate sets of 100-1000 photos. For a very large set of photos, such as 1,000,000 photos or more, perhaps another solution might be faster.

- This solution accounts for three-way-merges, with triplicates. As the solution appends each new duplicate found, it is not limited to just two different instances of files with the same content.


# References

While completing this assignment, I referenced a few solutions to comparing file content, and traversing directory trees in os.walk. 

The Python Central post on finding duplicates helped me immensely with this assignment!

[Python Central - Finding Duplicate Files with Python](https://www.pythoncentral.io/finding-duplicate-files-with-python/)
[Python Central - How to Traverse a Directory Tree in Python – Guide to os.walk](https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/)