def replace_spaces(sentence, char):
    return sentence.replace(' ', char)



sentence = "Test  This is a test   Testing "
sentence2 = replace_spaces(sentence, "_")
print(sentence2) # -> Test__This_is_a_test__Testing_