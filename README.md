# Sorted-character-frequency-histogram

## Estimated time

15-20 minutes

## Level of difficulty

Medium

## Prerequisites

6.1.9.15

## Objectives
- Improve the student's skills in operating with files (reading/writing)
- Using lambdas to change the sort order.

## Scenario

The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

1. The output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
2. The histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

Assuming that the input file contains just one line filled with:
```
cBabAa
```

the expected output should look as follows:
```
a -> 3
b -> 2
c -> 1
```

Tip:
Use a lambda to change the sort order.
