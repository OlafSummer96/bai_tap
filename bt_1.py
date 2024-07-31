def open_file(file_path: str):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content

def write_to_file(file_path: str, text: str):
    with open(file_path, 'a') as file:
        file.write(text)

def print_file(file_path: str):
    with open(file_path, 'r') as file:
        content = file.read()
    print(content)

# Read the content from the original file
file_path = 'C:/Users/Desktop/Study/Exercise/test.txt'
content = open_file(file_path)

# Write the original content to the result file
result_file_path = 'C:/Users/Desktop/Study/Exercise/test_results_1.txt'
with open(result_file_path, 'w') as file:
    file.writelines(content)

# Append the extra text to the result file
extra_text = """
Can I use these random paragraphs for my project?
Yes! All of the random paragraphs in our generator are free to use for your projects.

Can I contribute random paragraphs?
Yes. We're always interested in improving this generator and one of the best ways to do that is to add new and interesting paragraphs to the generator. If you'd like to contribute some random paragraphs, please contact us.
"""
write_to_file(result_file_path, extra_text)

# Print the content of the result file
print_file(result_file_path)
