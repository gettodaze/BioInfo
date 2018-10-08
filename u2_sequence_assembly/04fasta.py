def read_sequences_from_fasta_file(filename):
    """Reads all sequence records from the FASTA-formatted file specified by filename
    and returns a list of records.  Each record is represented by a tuple (name, sequence)"""
    sequences = []
    current_record_lines = None
    for line in open(filename):
        if line.startswith(">"):
            if current_record_lines is not None:
                sequences.append(sequence_from_fasta_lines(current_record_lines))
            current_record_lines = []
        current_record_lines.append(line.rstrip())
        
    # Handle the last record in the file
    if current_record_lines is not None:
        sequences.append(sequence_from_fasta_lines(current_record_lines))
    return sequences

def sequence_from_fasta_lines(lines):
    # Strip the beginning '>'
    name = lines[0][1:]
    sequence = ''.join(lines[1:])
    return (name, sequence)
