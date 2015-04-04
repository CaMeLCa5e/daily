"""
26. wc emulation: reading from file 3-2_example.txt, print the number of lines, words and
characters in the file. Note: when counting characters, include spaces and newlines
as well. Challenge: see if you can get each count without actually using a loop, but by
using len(). Do this without opening the file more than once (hint: read() will read the
file into a string; splitlines() will split a string on the newlines!). Special note: we have
seen anomalies that stem from varying line endings on the Windows and Mac
platforms. If your character count is off by up to 20 characters, don't worry. It just
needs to be within 20.
Expected output:
3-2_example.txt: 20 lines, 270 words, 1435 chars
"""
