"""
Longest common subsequence implementation starter
"""
import main


if __name__ == '__main__':
    origin = main.tokenize_big_file('lab_2/data.txt')
    suspicious = main.tokenize_big_file('lab_2/data_2.txt')

    lcs_length = main.find_lcs_length_optimized(origin, suspicious, plagiarism_threshold=0.3)
    print(f"Longest common subsequence consists of {lcs_length} words.")
    actual = main.calculate_plagiarism_score(lcs_length, suspicious)
    print(f"Plagiarism score: {actual:.1f}%")
    print(f"Plagiarism value is {actual}")
    RESULT = actual
    expected = ...

    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Concordance not working'
