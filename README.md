# PiNotes MD

PiNotes is an open source Python based WYSIWYG Markdown editor.  

## Current Features

- Dark / Light Mode
- WYSIWYG Live Interface
- Ablity to create new markdown files
- Ablity to open existing markdown files for modification

## Future Features  

- Enhanced Interface  
- Dropdown list of existing files
- Additional Markdown Feature Support  
- Ability to store files in SQLite3 Database  
- Ability to store files in Cloud for cross platform access  

## Getting Started

User must have Pipenv installed to access virtual environment.  
Change `SECRET_KEY` and `FILE_DIRECTORY` values in the `.env` file alongside other settings if required.

`pipenv shell`  
`python3 app.py`
  
- File name MUST contain the extention `.md`
- To create a new file, enter file name and contents. Click "Submit"
- To open & modify an existing file enter just the name of the file e.g. `test.md`

## Misc

`testing.py` is a live testing version of `app.py` and should not be used!

## Dependencies
- `Flask`
- `Flask-WTF`
- `Flask-MDE`
- `WTForms`
- `PyWebView`
- For Linux Users Only
  - `vext.gi` 

## Project Structure
- `./`
  - Main Python File
  - PipEnv Files
- `./templates` 
  - HTML Templates
- `./static/css`
  - CSS Files
- `./static/js`
  - JavaScript Files
- `./static/img`
  - Image Files