# qr-code-scrape

Scraping of qr code for testing purposes to [qr_code](https://github.com/iodevs/qr_code) library.
The qr codes are downloaded from [smiley.codes](https://smiley.codes/qrcode) and saved to csv files.

## Usage
Install requirements
```
pip3 install -r requirements.txt
```

and run
```
python3 scrap_qr_code.py
```
> `python3 -V`
>
> `# Python 3.6.7`

## TODO
- [x] downloading and saving is done for one version
- [x] download all version (ECC) for particular function patterns
- [x] download all version (ECC) for format and version information
- [ ] download all version (ECC) for mask patterns