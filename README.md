# About

`gettyt` is a downloader for getty images.

## Features

 - donloads 2048x2048 version
 - removes watermark
 - retains EXIF metadata
 

# Build

```
pip install -r requirements.txt
pyinstaller --onefile gettyt_main.spec
```

# Usage

Pass getty ID

```
gettyt HL7023-001
```

or full url

```
gettyt https://www.gettyimages.com/detail/photo/zeppelin-construction-royalty-free-image/HL7023-001
```

