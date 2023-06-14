# def strcounter (s):
#     adict = {}
#     for i in s:
#         adict[i] = adict.get(i, 0) + 1
#     for j in adict:
#         print(j, adict[j])


# def strcounter(s):
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sub_sym == sym:
#                 counter += 1
#         print(sym, counter)


def strcounter(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)



strcounter("hjkhk")