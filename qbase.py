# Calculate the average Phred score for each sequence in a FASTQ file

def get_phred_quality_strings(filename):
    """
    Extracts the Phred quality strings from a FASTQ file.

    Args:
        filename (str): The path to the FASTQ file.

    Returns:
        list: A list of Phred quality strings, one for each sequence.
    """
    with open(filename, 'r') as fastq_file:
        all_lines = fastq_file.readlines()
        num_lines = len(all_lines)

        quality_strings = []
        # FASTQ format: each sequence has 4 lines (header, sequence, +, quality)
        # We are interested in the 4th line (index 3) which contains the quality string.
        # We then increment by 4 to get the quality string for the next sequence.
        for i in range(3, num_lines, 4):
            quality_strings.append(all_lines[i].strip())
    return quality_strings

def calculate_average_phred_score(quality_strings):
    """
    Calculates the average Phred score for each quality string.

    Args:
        quality_strings (list): A list of Phred quality strings.

    Returns:
        list: A list of average Phred scores (rounded to the nearest integer),
              where each element corresponds to the average score of a sequence.
    """
    average_scores = []
    for quality_string in quality_strings:
        phred_scores = []
        # Convert each character in the quality string to its Phred score
        for char in quality_string:
            # Phred scores are typically encoded using ASCII values where the score
            # is the ASCII value of the character minus 33 (for Sanger/Illumina 1.8+).
            phred_scores.append(ord(char) - 33)

        # Calculate the average Phred score for the current sequence
        average_score = sum(phred_scores) / len(phred_scores)
        average_scores.append(round(average_score))
    return average_scores

# Example usage:
fastq_file = "data/sample.fastq"
phred_quality_strings = get_phred_quality_strings(fastq_file)
average_phred_scores = calculate_average_phred_score(phred_quality_strings)
print(average_phred_scores)