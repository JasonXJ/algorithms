def replace_space(byte_array, true_length):
    """ Inplace replace space in `byte_array`. `byte_array` is supposed to be
    long enough to hold the result string. """
    replace_to = '%20'
    replace_to_ord_list = [ord(x) for x in replace_to]

    space_count = 0
    space_ord = ord(' ')
    for x in byte_array[:true_length]:
        if x == space_ord:
            space_count += 1

    source_index = true_length - 1
    target_index = source_index + space_count * (len(replace_to) - 1)

    while space_count != 0:
        if byte_array[source_index] == space_ord:
            space_count -= 1
            byte_array[target_index - len(replace_to) + 1:target_index+1] = replace_to_ord_list
            source_index -= 1
            target_index -= len(replace_to)
        else:
            byte_array[target_index] = byte_array[source_index]
            source_index -= 1
            target_index -= 1

if __name__ == '__main__':
    a = bytearray(b''); length_a = 0
    b = bytearray(b'hello'); length_b = 5
    c = bytearray(b'hello world  '); length_c = 11
    d = bytearray(b' hello world       '); length_d = 13

    replace_space(a, length_a)
    replace_space(b, length_b)
    replace_space(c, length_c)
    replace_space(d, length_d)

    print(a, b, c, d, sep='\n')
