#Write a set of conditional statements to find whether or not a number is a special number

#Special numbers are defined as numbers less than 100 or greater than  or equal to 300

#That are perfectly divisible by 3,7 or both

#Print out "Divisible by both" if special number divisible by both 3 and 7

#Print out "Divisible by 3" if special number divisible by 3,but not by 7

#Print out "Divisible by 7" if special number divisible by 7,but not by 3

#Print out "Not a special number" otherwise

num=314
if (num < 100 or num >= 300) and (num%3==0 or num%7==0):

    if (num % 3== 0 and num % 7 == 0):

        print("Divisible by both")

    elif (num % 3== 0):

        print("Divisible by 3")

    else:

        print("Divisible by 7")

else:

        print("Not special number")

