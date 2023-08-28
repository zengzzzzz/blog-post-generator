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

# 博客文章格式转换（json to markdown）

这个脚本自动将 JSON 文件中的博客文章数据转换为适用于基于 Jekyll 的博客的独立 Markdown 文件。它从 JSON 文件中提取博客文章的标题、内容和日期等关键信息，并在 `markdown_files` 目录中生成 Markdown 文件。

## 特点

- 将 JSON 博客文章数据转换为 Markdown 文件。
- 保留博客文章内容中的换行。
- 自动为 Jekyll 生成前置信息。

## 使用方法

1. **前提条件：**

   确保您的系统已安装 Python。

2. **克隆仓库：**

   ```
   bash
   git clone https://github.com/your-username/blog-post-generator.git 
   ```

3. **进入项目目录：**

   ```
   bash
   cd blog-post-generator
   ```

4. **提供博客文章数据：**

   将您的博客文章数据放置在名为 `posts_example.json` 的文件中。JSON 文件应具有以下结构：

   ```
   json
   [
       {
           "Title": "示例博客文章",
           "Body": "这是博客文章的内容...",
           "DateAdded": "2023-08-28T10:00:00"
       },
       // 添加更多博客文章...
   ]
   ```

5. **运行脚本：**

   ```
   bash
   python generate_posts.py
   ```

   这将在 `markdown_files` 目录中为每篇博客文章生成独立的 Markdown 文件。

6. **访问生成的 Markdown 文件：**

   脚本执行完毕后，您将在 `markdown_files` 目录中找到生成的 Markdown 文件。

## 要求

- Python（版本 >= 3.8）

## 许可证

该项目基于 Apache-2.0 许可证。


