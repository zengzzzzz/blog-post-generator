# Blog Post Generator

This script automates the process of converting blog post data from a JSON file into individual Markdown files suitable for a Jekyll-based blog. It extracts key information such as the blog post title, content, and date from the JSON file and generates Markdown files in the `markdown_files` directory.

## Features

- Converts JSON blog post data into Markdown files.
- Retains line breaks in blog post content.
- Automatically generates front matter for Jekyll.

## Usage

1. **Prerequisites:** 

   Make sure you have Python installed on your system.

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/blog-post-generator.git 
   ```

3. **Navigate to the Project Directory:**

   ```bash
   cd blog-post-generator
   ```

4. **Provide Blog Post Data:**

   Place your blog post data in a file named `posts_example.json`. The JSON file should have the following structure:

   ```json
   [
       {
           "Title": "Sample Blog Post",
           "Body": "This is the content of the blog post...",
           "DateAdded": "2023-08-28T10:00:00"
       },
       // Add more blog posts...
   ]
   ```

5. **Run the Script:**

   ```bash
   python generate_posts.py
   ```

   This will generate individual Markdown files for each blog post in the `markdown_files` directory.

6. **Access Generated Markdown Files:** 

   Once the script finishes execution, you will find the generated Markdown files in the `markdown_files` directory.

## Requirements

- Python (version >= 3.8)

## License

This project is licensed under the  Apache-2.0 License. 

