speakers_file = open('speakers.txt', 'r')
sym_count = []
for i_line in speakers_file:
    print(i_line, end="")
    sym_count.append(str(len(i_line)))
speakers_file.close()

sym_count_str = "\n".join(sym_count)
counts_file = open("sym_counts.txt",'w')
counts_file.write(sym_count_str)
counts_file.close()