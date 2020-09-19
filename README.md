# intelligent Test

## Setup

### git

- `echo "# itest" >> README.md`
- `git init`
- `git add README.md`
- `git commit -m "first commit"`
- `git branch -M master`
- `git remote add origin https://github.com/id-shiv/itest.git`
- `git push -u origin master`

### Virtual environment  

- `pip install virtualenv`
- `virtualenv venv`
- `source venv/bin/activate`

### Permission for driver file

- `xattr -d com.apple.quarantine src/scraper/ui/drivers/chromedriver-5 `  
