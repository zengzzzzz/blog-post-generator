import os
import json
import re
from datetime import datetime
import urllib.request

# Read JSON file
with open('posts_example.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Create directory if it doesn't exist
if not os.path.exists('markdown_files'):
    os.mkdir('markdown_files')

if not os.path.exists('imgs'):
    os.mkdir('imgs')

# Iterate through each blog post
for post in data:
    title = post['Title']
    content = post['Body']
    date_added = datetime.strptime(post['DateAdded'], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    categories = ''
    tags = 'zengzzzzz-blog'
    title = title.replace('/', '-')

    # Clean HTML tags while retaining line breaks
    content = re.sub(r'<.*?>', '', content)
    content = content.replace('\n', '  \n')  # Markdown line breaks require two trailing spaces
    image_urls = re.findall(r'src="(.*?\.(png|jpg))"', content)  # get img urls

    # Generate img
    if image_urls:
        image_count = 1
        for image_url in image_urls:
            image_name = f"{title}-{image_count}"
            image_path = os.path.join('imgs', image_name)
            urllib.request.urlretrieve(image_url, image_path)
            image_count += 1

    # Generate Markdown content
    markdown_content = f"---\nlayout: post\ntitle:  \"{title}\"\ndate:   {date_added}\ncategories: {categories}\ntags:  {tags}\n---\n\n* content\n{{:toc}}\n\n{content}\n"

    # Write to Markdown file
    markdown_file_path = os.path.join('markdown_files', f'{date_added[:10]}-{title}.md')
    with open(markdown_file_path, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(markdown_content)

print("Markdown file generation complete!")
