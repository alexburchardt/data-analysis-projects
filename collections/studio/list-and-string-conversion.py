proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for separation in strings:
    print(f"Checking list: '{separation}'")
    if "," in separation:
        print("There's a comma in there")
    elif ";" in separation:
        print("There's a semicolon in there")
    elif " " in separation:
        print("There's a space in there")
    else: 
        print("This was a trick question")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
    if ',' in separation:
        items_list=separation.split(',')
        items_list.reverse()
        reversed_string=','.join(items_list)
        print(f"Reversed string: {reversed_string}\n")


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
    elif ';' in separation:
            items_list=separation.split(';')
            items_list.sort()
            reversed_string=','.join(items_list)
            print(f"Alphabetized string: {reversed_string}\n")
       


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
    elif ' ' in separation:
                items_list=separation.split(' ')
                items_list.sort(reverse=True)
                reversed_string=' '.join(items_list)
                print(f"Reverse alphabetized string: {reversed_string}\n")


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
    elif ', ' in separation:
        items_list=separation.split(', ')
        items_list.reverse()
        reversed_string=','.join(items_list)
        print(f"Reversed string: {reversed_string}\n")