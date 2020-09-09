'''


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''

# Look for patterns
# For 1 - 9 there is no pattern
# Same for 10-19
# For 20-29 we have:
# prefix (twenty) + digit (1-9)
# same until 90-99 (note prefix forty, no u)
# For 100-999 we have:
# prefix (1-9) + 'hundred and' + affix (which we calculated earlier)
# 'one thousand' = 11 letters

# code is not optimised for speed but for readability (kind of...)

# one,two,three,four,five,six,seven,eight,nine:
sum_of_digits = 3+3+5+4+4+3+5+5+4
# ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen
sum_of_10_to_19 = 3+6+6+8+8+7+7+9+8+8
# 20-99 prefixes:
# twenty, thirty, forty (!), fifty, sixty, seventy, eighty, ninety
prefixes_of_20_to_99 = 6+6+5+5+5+7+6+6
# therefore:
# 10 times prefixes: thirty, thirty one, thirty two, ... , thirty nine
# 8 times sum_of_digits because we already have 1 through 19
sum_of_1_to_99 = sum_of_digits + sum_of_10_to_19 + 10 * prefixes_of_20_to_99 + 8 * sum_of_digits
# 100-999 prefixes:
# each digit appears 100 times: one hundred, one hundred and one, ... , one hundred and ninety nine
# 'hundred' = 7 letters, occurs 1 time per hundred
# 'hundred and' = 10 letters, occurs 99 times per hundred
prefixes_of_100_to_999 = 100 * sum_of_digits + 9 * (7 + 99 * 10)
# sum of 100-999:
sum_of_100_to_999 = prefixes_of_100_to_999 + 9 * sum_of_1_to_99
# end sum:
# 'one thousand' = 11 letters
end_sum = sum_of_1_to_99 + sum_of_100_to_999 + 11
print(end_sum)