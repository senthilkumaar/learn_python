"""
    10. Create a string variable "news" with value below:

    Air travel to become bit costlier as govt announces hike in aviation security fee from July 1

    Question: Using string slicing print the below values:
              Air travel
              July 1
"""
news = "Air travel to become bit costlier as govt announces hike in aviation security fee from July 1"
print(news[:10])
print(news[-6:])

"""

8. Create a string variable 'special_string' and print it. The
   output should be:
"""
text = """Python is an "object-oriented" Programming language"""
print(text)

"""

12. Create a format string with placeholders "{}" and then,
    Make use of string format function to print the error and error code as below:

    Error occurred during data extraction. Error code is: 121
    Error occurred during string manipulation. Error code is: 221

    where,
      "data extraction and 121" is the formatted string in first example
      "string manipulation and 221" is the formatted string in second example
"""
error_text = "Error occurred during {}. Error code is: {}"

print(error_text.format('data extraction', 121))
print(error_text.format('string manipulation', 221))
